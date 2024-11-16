import hashlib
import bisect

class ConsistentHashing:
    def __init__(self, num_replicas=3):
        self.num_replicas = num_replicas  # Number of virtual nodes per physical node
        self.ring = {}  # Hash ring: Maps hash value -> node
        self.sorted_keys = []  # Sorted list of hash values (positions on the ring)
        self.data_store = {}  # Simulated data store for each node

    def _hash(self, key):
        """Generate a consistent hash for a given key."""
        return int(hashlib.sha256(key.encode()).hexdigest(), 16)

    def add_node(self, node):
        """Add a physical node and its virtual nodes to the hash ring."""
        self.data_store[node] = {}  # Initialize data store for the node
        for i in range(self.num_replicas):
            # Create virtual nodes by appending replica index
            virtual_node_key = f"{node}:{i}"
            hash_value = self._hash(virtual_node_key)
            self.ring[hash_value] = node
            bisect.insort(self.sorted_keys, hash_value)
        print(f"Added node {node} with {self.num_replicas} virtual nodes.")

    def remove_node(self, node):
        """Remove a physical node and its virtual nodes from the hash ring."""
        for i in range(self.num_replicas):
            virtual_node_key = f"{node}:{i}"
            hash_value = self._hash(virtual_node_key)
            del self.ring[hash_value]
            self.sorted_keys.remove(hash_value)
        del self.data_store[node]
        print(f"Removed node {node} and its virtual nodes.")

    def get_node(self, key):
        """Get the node responsible for storing a given key."""
        hash_value = self._hash(key)
        # Find the first hash value >= hash_value in the sorted_keys list
        index = bisect.bisect(self.sorted_keys, hash_value) % len(self.sorted_keys)
        responsible_hash = self.sorted_keys[index]
        return self.ring[responsible_hash]

    def add_data(self, key, value):
        """Add data to the appropriate node."""
        node = self.get_node(key)
        self.data_store[node][key] = value
        print(f"Added key '{key}' with value '{value}' to node '{node}'.")

    def retrieve_data(self, key):
        """Retrieve data from the appropriate node."""
        node = self.get_node(key)
        if key in self.data_store[node]:
            return self.data_store[node][key]
        else:
            print(f"Key '{key}' not found in node '{node}'.")
            return None

# Example Usage
if __name__ == "__main__":
    ch = ConsistentHashing(num_replicas=3)

    # Add nodes to the hash ring
    ch.add_node("NodeA")
    ch.add_node("NodeB")
    ch.add_node("NodeC")

    # Add data to the consistent hash ring
    ch.add_data("key1", "value1")
    ch.add_data("key2", "value2")
    ch.add_data("key3", "value3")

    # Retrieve data from the consistent hash ring
    print("Retrieved:", ch.retrieve_data("key1"))  # Should return "value1"
    print("Retrieved:", ch.retrieve_data("key2"))  # Should return "value2"
    print("Retrieved:", ch.retrieve_data("key3"))  # Should return "value3"

    # Remove a node and test retrieval
    ch.remove_node("NodeB")
    print("Retrieved after NodeB removal:", ch.retrieve_data("key2"))
