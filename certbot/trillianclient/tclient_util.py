"""Provide tool functions to interact with Trillian Log Server"""
from typing import List

import grpc
from certbot.trillianclient import trillian_log_api_pb2
from certbot.trillianclient import trillian_log_api_pb2_grpc

TRILLIANADDR = "localhost:50054"
TREEID : int = 8438661973015862380
BASEINDEX : int = 121

class TrillianClient:
    """
    Client Class to communicate with Trillian Server for Certbot
    """
    client : trillian_log_api_pb2_grpc.TrillianLogStub

    def __init__(self, addr=TRILLIANADDR):
        """
        connect to a existing trillian server
        """
        #print("Will try to greet world ...")
        channel = grpc.insecure_channel(addr)
        self.client = trillian_log_api_pb2_grpc.TrillianLogStub(channel=channel)

    def get_single_entry(self, index, tree_size)->bytes:
        """
        retrieve single PUF invocation entry from the log server
        """
        req = trillian_log_api_pb2.GetEntryAndProofRequest(
            log_id=TREEID,
            leaf_index=index,
            tree_size=tree_size,
        )
        resp : trillian_log_api_pb2.GetEntryAndProofResponse = self.client.GetEntryAndProof(req) # type claim
        entry_bytes : bytes = resp.leaf.leaf_value
        if len(entry_bytes) == 0:
            print("Empty entry content")
        return entry_bytes
       
    def get_entry_list(self, base=BASEINDEX, tsize=BASEINDEX+4)->List[bytes]:
        """
        retrieve single entry and form the entry chain for verification
        """
        entry_list = []
        entry_chain_len = 4
        for i in range(entry_chain_len):
            entry = self.get_single_entry(base + i, tsize) # leaf index calculation
            entry_list.append(entry)
        return entry_list
    