"""Provide some util functions for Armored Core functions"""
from typing import List
from cryptography import x509
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey

from certbot import errors

#class AcoreCertHandler:

PUF_LENGTH = 32
RSA_2048_SIZE = 256

def bytes_xor(a: bytes, b: bytes) ->bytes:
    """
    XOR two byte array
    """
    if len(a) != len(b):
        return
    c = []
    for x, y in zip(a, b):
        c.append(x ^ y)
    return bytes(c)


def read_certs_from_path(cert_path: str, domain: str) -> bytes:
    """
    Read raw certs from the given path.

    :param cert_path: file path that storing the letsencrypt certs
    :type cert_path: `str`

    :returns: value for `sys.exit` about the exit status of Certbot
    :rtype: `str`
    """
    domain_cert_path = cert_path + "/live/" + domain
    #print("In read_cert_from_path", domain_cert_path)

    try:
        with open(domain_cert_path + "/cert.pem", "rb") as raw:
            domain_raw = raw.read()
        with open(domain_cert_path + "/chain.pem", "rb") as raw:
            chain_raw = raw.read()
        with open(domain_cert_path + "/fullchain.pem", "rb") as raw:
            fullchain_raw = raw.read()
        if (domain_raw + chain_raw) != fullchain_raw:
            error_str = "fullchain does not match cert + chain!"
            raise errors.Error(error_str)
        # Dangerous operation, just for PoC
        with open(domain_cert_path + "/roots.pem", "rb") as raw:
            root_raw = raw.read()
    except IOError as e:
        error_str = f"reading one of cert, chain, or fullchain has failed: {0}".format(e)
        raise errors.Error(error_str)
    return fullchain_raw + root_raw


def parse_pem_certs(cert_raw:bytes)->List[x509.Certificate]:
    """
    Convert raw cert bytes to the X509 structured object

    :param cert_raw: raw cert bytes read from the file path
    :type cert_raw: `str`

    :returns: X509v3 certificate object
    :rtype: x509.Certificate
    """
    real_certs = x509.load_pem_x509_certificates(cert_raw)
    real_certs.reverse()
    return real_certs

def recover_pufproof_from_key(pubkey : any)->bytes:
    """
    Convert a given cryptographically wrapped pubkey into the PUF-based proof bytes
    
    :param pubkey: extracted raw pubkey from the certificates.
    :type pubkey: any (only support RSAPublicKey for now)

    :returns: pub_puf_proof PUF-based proof
    :rtype: pub_puf_proof bytes
    """
    pub_puf_proof = b''
    if isinstance(pubkey, RSAPublicKey):
        #print("The type of the pubkey is RSA")
        rsa_size, proof_size = RSA_2048_SIZE, PUF_LENGTH
        proof_bytes = pubkey.public_numbers().n.to_bytes(rsa_size)
        pub_puf_proof = proof_bytes[:proof_size]
        #print("pub_puf_proof", pub_puf_proof.hex())
    #else:
        #print("Do not support this type of pubkey convering: ", type(pubkey))
    return pub_puf_proof
