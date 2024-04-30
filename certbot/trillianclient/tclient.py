"""Provide functions to establish connection with Trillian Log Server"""
from hashlib import sha256
from certbot.trillianclient import pentry_pb2

def parse_entry_proto(raw_entry:bytes):
    """
    parse an raw encoded entry bytes to the python class
    """
    entry = pentry_pb2.PUFEntry()
    entry.ParseFromString(raw_entry)
    #print("Entry hex", raw_entry.hex())
    # print("In parse_entry_proto, ", entry.caname)
    return entry

def construct_entry_list(raw_entry_list: list):
    """
    parse raw entrie
    """
    decoded_entry_list = []
    for e in raw_entry_list:
        decoded_entry_list.append(parse_entry_proto(e))
    return decoded_entry_list


def verify_cert_and_entry(entry, tbscertbytes: bytes, R: bytes, T: bytes)->bool:
    """
    verify the certificates along with the entries in the entry chain
    """
    z_bytes = entry.caname.encode() + entry.manu.encode() + entry.ts + entry.pufid + entry.comrp
    raw = R + z_bytes + tbscertbytes + T
    tag = sha256(raw).digest()
    # print("In verify_cert_and_entry ", raw.hex(), tag.hex(), entry.tag.hex())
    if entry.tag != tag:
        print("Calculated tag not match")
        return False
    return True
