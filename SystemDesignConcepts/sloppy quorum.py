from collections import defaultdict
import threading
import time
from typing import List

class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.store = {}  # Key-value store
        self.hints = defaultdict(list)  # Temporary storage for hinted handoff data

    def write(self, key, value):
        self.store[key] = value
        print(f"Node {self.node_id} wrote {key}: {value}")

    def read(self, key):
        return self.store.get(key, None)

    def receive_hint(self, key, value):
        # Temporarily store the data as a "hint" for eventual handoff
        self.hints[key].append(value)
        print(f"Node {self.node_id} received hinted handoff data for {key}: {value}")

    def apply_hints(self, correct_nodes):
        # Forward hinted data to the correct primary nodes when they are back online
        for key, values in self.hints.items():
            for value in values:
                for correct_node in correct_nodes:
                    print(f"Node {self.node_id} applying hinted handoff for {key} to Node {correct_node.node_id}")
                    correct_node.write(key, value)
            self.hints[key] = []  # Clear hints after they are applied

class RiakCluster:
    def __init__(self, nodes: List[Node], replication_factor: int, write_quorum: int, read_quorum: int):
        self.nodes = nodes
        self.replication_factor = replication_factor
        self.write_quorum = write_quorum
        self.read_quorum = read_quorum
        self.key_node_map = {}  # Mapping from key to primary nodes

    def get_primary_nodes(self, key):
        # Determine the primary nodes for each key based on the replication factor
        if key not in self.key_node_map:
            primary_nodes = self.nodes[:self.replication_factor]  # Simple mapping for primary nodes
            self.key_node_map[key] = primary_nodes
        return self.key_node_map[key]

    def write(self, key, value):
        primary_nodes = self.get_primary_nodes(key)
        successful_writes = 0
        alternative_nodes = []

        # Try to write to primary nodes
        for node in primary_nodes:
            try:
                node.write(key, value)
                successful_writes += 1
            except Exception as e:
                # If a primary node is unavailable, add it to alternative nodes for hinted handoff
                print(f"Primary node {node.node_id} is unavailable for {key}")
                alternative_nodes.append(node)

        # Use alternative nodes if needed to meet the write quorum
        if successful_writes < self.write_quorum:
            for alt_node in self.nodes:
                if alt_node not in primary_nodes:
                    alt_node.receive_hint(key, value)  # Store data as a hint
                    successful_writes += 1
                    if successful_writes >= self.write_quorum:
                        break
            if successful_writes < self.write_quorum:
                print("Failed to meet the write quorum.")
        else:
            print("Write quorum met successfully.")

    def read(self, key):
        primary_nodes = self.get_primary_nodes(key)
        successful_reads = 0
        data = None

        # Attempt to read from primary nodes
        for node in primary_nodes:
            result = node.read(key)
            if result is not None:
                data = result
                successful_reads += 1
            if successful_reads >= self.read_quorum:
                return data

        # If quorum not met, return None (Riak would trigger further repairs in the background)
        print("Failed to meet the read quorum.")
        return None

# Testing the Riak-inspired Cluster with Sloppy Quorum
nodes = [Node(i) for i in range(5)]
cluster = RiakCluster(nodes, replication_factor=3, write_quorum=2, read_quorum=2)

# Writing data with Sloppy Quorum and Hinted Handoff
cluster.write("key1", "value1")

# Simulate node recovery and hinted handoff application
for node in nodes:
    primary_nodes = cluster.get_primary_nodes("key1")
    node.apply_hints(primary_nodes)
