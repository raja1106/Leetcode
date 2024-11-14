import threading
from datetime import datetime
from typing import List, Tuple


class Replica:
    def __init__(self, data: str, timestamp: datetime):
        self.data = data
        self.timestamp = timestamp

    def update_data(self, new_data: str, new_timestamp: datetime):
        self.data = new_data
        self.timestamp = new_timestamp


def async_read_repair(replicas: List[Replica], latest_data: str, latest_timestamp: datetime):
    """ Asynchronously repair stale replicas """
    for replica in replicas:
        if replica.data != latest_data:
            print(f"Repairing replica with outdated data: {replica.data}")
            replica.update_data(latest_data, latest_timestamp)
    print("Async read repair complete.")


def read_with_repair(replicas: List[Replica], required_reads: int) -> str:
    # Step 1: Select "R" nodes for quorum read based on consistency level
    read_replicas = replicas[:required_reads]

    # Step 2: Identify the latest data across read replicas
    latest_replica = max(read_replicas, key=lambda r: r.timestamp)

    # Step 3: Detect any inconsistent replicas
    inconsistent_replicas = [r for r in read_replicas if r.data != latest_replica.data]

    if inconsistent_replicas:
        # Trigger asynchronous read repair to update stale replicas
        print("Inconsistent data detected, initiating async read repair...")
        repair_thread = threading.Thread(target=async_read_repair,
                                         args=(inconsistent_replicas, latest_replica.data, latest_replica.timestamp))
        repair_thread.start()

    # Step 4: Return the latest data to the client
    return latest_replica.data


# Test Case
replicas = [
    Replica(data="v1", timestamp=datetime(2023, 10, 1)),
    Replica(data="v2", timestamp=datetime(2023, 11, 1)),  # latest data
    Replica(data="v1", timestamp=datetime(2023, 10, 1)),
]

# Assuming "R" = 2 for a quorum read (2 out of 3 replicas)
required_reads = 2
correct_data = read_with_repair(replicas, required_reads)
print(f"Data returned to client: {correct_data}")

# Verification
for i, replica in enumerate(replicas):
    print(f"Replica {i + 1} data: {replica.data}, timestamp: {replica.timestamp}")
