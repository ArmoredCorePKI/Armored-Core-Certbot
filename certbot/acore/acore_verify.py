"""Provide verification functions for Armored Core functions"""
from typing import List
from typing import Tuple
from hashlib import sha256
from cryptography import x509
from cryptography.x509.oid import ExtensionOID

from certbot.acore import acore_utils
from certbot.trillianclient import tclient
from certbot.trillianclient import pentry_pb2


def resolve_response_sig(cert, rlast, hlast, loc)-> Tuple[bytes, bytes]:
    """
    Calculate R and H used in the sig field of the certificate

    :param cert: certificate to verify, 
    :type cert: x509.Certificate

    :returns
    :rtype:
    """
    ts = bytearray(4)
    raw_input = ts + cert.tbs_certificate_bytes + cert.issuer.rfc4514_string().encode()
    hc = sha256(raw_input).digest()
    # print("hc", hc)
    hmask = b""
    if loc == 0 :
        hmask = hc
    else:
        hmask = sha256(rlast + cert.tbs_certificate_bytes + hlast).digest()
    r = acore_utils.bytes_xor(cert.signature, hmask)

    return (r, hmask)

def verify_pub_proof(cert: x509.Certificate, entry: pentry_pb2.PUFEntry, pi_proof: bytes)->bool:
    """
    Verify the Public Proof (equal to the issuer's public key)

    :param cert: certificate to verify, 
    :type cert: x509.Certificate

    :param pi_proof: the Public PUF accumulation proof in the issuer's certificate
    :type pi_proof: bytes

    :returns ret: the validation result
    :rtype ret: boolean
    """
    ext = cert.extensions.get_extension_for_oid(ExtensionOID.SUBJECT_KEY_IDENTIFIER)
    rp = ext.value.public_bytes()[2:] # the first two bytes is ignored
    crp = entry.comrp
    #print("rp", rp.hex(), crp.hex(), pi_proof.hex())
    return acore_utils.bytes_xor(crp, rp) == pi_proof

def verify_all(cert_list: List[bytes], entry_list: List[bytes]) -> bool:
    """ Verifies that fullchain (including the root certs).

    :param cert_list: certificates to verify
    :type cert_list: a list of all certificates

    :param entry_list: PUF entries to verify
    :type entry_list: a list of all PUF entries

    :returns ret: the validation result
    :rtype ret: boolean
    """
    # one root CA, two intermediate CA and one domain
    assert len(cert_list) == 4 & len(entry_list) == 4
    rlast, hlast, pi_last = b'', b'', b''
    tlast = b''
    for i, (cert, entry) in enumerate(zip(cert_list, entry_list)):
        #print(cert.issuer.rfc4514_string())
        #print(entry.caname)
        sigs = resolve_response_sig(cert, rlast, hlast, i)
        # print("Resolving R, h: ", sigs[0].hex(), sigs[1].hex())
        rlast, hlast = sigs[0], sigs[1]
        # verify cert and entry
        if not tclient.verify_cert_and_entry(entry, cert.tbs_certificate_bytes, rlast, tlast):
            print("Verify Certificates and Entries Failed.")
            return False

        # verify the RP and cRP
        if i != 0 and not verify_pub_proof(cert, entry, pi_last):
            print("Verify Public PUF-based Proof Failed.")
            return False
        pi_last = acore_utils.recover_pufproof_from_key(cert.public_key())
        tlast = entry.tag
    return True
