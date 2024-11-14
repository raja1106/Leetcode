from datetime import datetime
from typing import List, Tuple


class Replica:
    def __init__(self, data: str, timestamp: datetime):
        self.data = data
        self.timestamp = timestamp

    def update_data(self, new_data: str, new_timestamp: datetime):
        self.data = new_data
        self.timestamp = new_timestamp


def read_repair(replicas: List[Replica]) -> str:
    # Step 1: Identify the most recent data across replicas
    latest_replica = max(replicas, key=lambda r: r.timestamp)

    # Step 2: Check if all replicas have consistent data
    inconsistent_replicas = [r for r in replicas if r.data != latest_replica.data]

    if inconsistent_replicas:
        # Step 3: Repair inconsistent replicas
        for replica in inconsistent_replicas:
            replica.update_data(latest_replica.data, latest_replica.timestamp)

    # Step 4: Return the most recent, consistent data
    return latest_replica.data


# Test Case
replicas = [
    Replica(data="v1", timestamp=datetime(2023, 10, 1)),
    Replica(data="v2", timestamp=datetime(2023, 11, 1)),  # latest
    Replica(data="v1", timestamp=datetime(2023, 10, 1)),
]

correct_data = read_repair(replicas)
print(f"Correct data after read repair: {correct_data}")
# Verifying replicas are repaired
for i, replica in enumerate(replicas):
    print(f"Replica {i + 1} data: {replica.data}, timestamp: {replica.timestamp}")