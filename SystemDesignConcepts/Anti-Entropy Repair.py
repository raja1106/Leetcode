import hashlib
class MerkleTreeNode:
    def __init__(self, hash_val=None, left=None, right=None):
        self.hash_val = hash_val
        self.left = left
        self.right = right


class MerkleTree:
    def __init__(self, data_blocks):
        self.root = self.build_tree(data_blocks)

    def hash(self, data):
        return hashlib.sha256(data.encode()).hexdigest()

    def build_tree(self, data_blocks):
        # Create leaf nodes
        leaf_nodes = [MerkleTreeNode(hash_val=self.hash(data)) for data in data_blocks]

        # Build tree from leaves to root
        while len(leaf_nodes) > 1:
            new_level = []
            for i in range(0, len(leaf_nodes), 2):
                left = leaf_nodes[i]
                right = leaf_nodes[i + 1] if i + 1 < len(leaf_nodes) else left
                combined_hash = self.hash(left.hash_val + right.hash_val)
                parent = MerkleTreeNode(hash_val=combined_hash, left=left, right=right)
                new_level.append(parent)
            leaf_nodes = new_level
        return leaf_nodes[0]  # Root node

    def get_root_hash(self):
        return self.root.hash_val if self.root else None


def perform_anti_entropy(replica_a_data, replica_b_data):
    # Step 1: Build Merkle Trees for each replica
    tree_a = MerkleTree(replica_a_data)
    tree_b = MerkleTree(replica_b_data)

    # Step 2: Compare the root hashes
    if tree_a.get_root_hash() == tree_b.get_root_hash():
        print("Replicas are consistent.")
        return
    else:
        print("Inconsistencies detected, synchronizing replicas...")
        # Traverse down the trees to find and repair differences
        sync_data(tree_a.root, tree_b.root)


def sync_data(node_a, node_b):
    # Traverse nodes until differences are found at the leaf level
    if node_a.hash_val != node_b.hash_val:
        if node_a.left and node_b.left:
            sync_data(node_a.left, node_b.left)
            sync_data(node_a.right, node_b.right)
        else:
            print(f"Repairing data block: {node_a.hash_val} -> {node_b.hash_val}")
            # Code to replace outdated data with the correct data would go here


# Test Case
replica_a = ["block1_data", "block2_data", "outdated_block3"]
replica_b = ["block1_data", "block2_data", "updated_block3"]  # Replica B has updated data

perform_anti_entropy(replica_a, replica_b)
