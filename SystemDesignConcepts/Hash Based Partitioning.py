class HashPartitionedTable:
    def __init__(self, num_partitions):
        self.num_partitions = num_partitions
        self.partitions = [[] for _ in range(num_partitions)]  # Create empty lists for each partition

    def get_partition(self, partition_key):
        # Compute hash and map to a partition index
        partition_index = hash(partition_key) % self.num_partitions
        return partition_index

    def insert(self, row):
        # Use the hash-based partitioning logic to insert the row
        partition_key = row['id']  # Use 'id' as the partition key
        partition_index = self.get_partition(partition_key)
        self.partitions[partition_index].append(row)
        print(f"Inserted row with ID {partition_key} into partition {partition_index}")

    def query(self, partition_key):
        # Retrieve data from the correct partition based on partition key
        partition_index = self.get_partition(partition_key)
        for row in self.partitions[partition_index]:
            if row['id'] == partition_key:
                return row
        return None  # If not found

# Example usage of HashPartitionedTable
table = HashPartitionedTable(num_partitions=4)

# Insert rows with different partition keys
table.insert({"id": 101, "name": "Alice", "age": 25})
table.insert({"id": 102, "name": "Bob", "age": 30})
table.insert({"id": 203, "name": "Charlie", "age": 35})
table.insert({"id": 204, "name": "Daisy", "age": 28})

# Query by partition key
result = table.query(102)
print("Query result:", result)

# Check distribution
for i, partition in enumerate(table.partitions):
    print(f"Partition {i}:", partition)

