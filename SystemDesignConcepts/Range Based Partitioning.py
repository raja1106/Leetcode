from datetime import datetime
from typing import List, Dict


# Partition class to hold data for a specific range
class Partition:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.data = []  # List to hold rows of data within this partition's range

    def insert(self, row):
        # Add row to partition
        self.data.append(row)

    def query(self, start, end):
        # Filter rows within the query range
        return [row for row in self.data if start <= row['date'] < end]

    def __repr__(self):
        return f"Partition({self.start} to {self.end}) with {len(self.data)} rows"


# PartitionedTable class to manage multiple partitions based on ranges
class PartitionedTable:
    def __init__(self):
        self.partitions = []

    def create_partition(self, start, end):
        # Create a new partition for a given range and add to the list of partitions
        partition = Partition(start, end)
        self.partitions.append(partition)

    def insert(self, row):
        # Route the row to the correct partition based on the 'date' key
        for partition in self.partitions:
            if partition.start <= row['date'] < partition.end:
                partition.insert(row)
                return
        print("No partition found for date:", row['date'])

    def query(self, start, end):
        # Query only the relevant partitions based on the given date range
        results = []
        for partition in self.partitions:
            if partition.start < end and partition.end > start:
                results.extend(partition.query(start, end))
        return results


# Example Usage of Range-Based Partitioning
# Initialize PartitionedTable
table = PartitionedTable()

# Create partitions for January, February, and March 2024
table.create_partition(datetime(2024, 1, 1), datetime(2024, 2, 1))
table.create_partition(datetime(2024, 2, 1), datetime(2024, 3, 1))
table.create_partition(datetime(2024, 3, 1), datetime(2024, 4, 1))

# Insert data rows with 'date' as partition key
table.insert({"id": 1, "product": "A", "amount": 150, "date": datetime(2024, 1, 15)})
table.insert({"id": 2, "product": "B", "amount": 200, "date": datetime(2024, 2, 20)})
table.insert({"id": 3, "product": "C", "amount": 300, "date": datetime(2024, 3, 10)})

# Query data within a specific date range
results = table.query(datetime(2024, 2, 1), datetime(2024, 3, 1))
print("Query Results for February 2024:")
for row in results:
    print(row)

# Print partitions to visualize data distribution
for partition in table.partitions:
    print(partition)
