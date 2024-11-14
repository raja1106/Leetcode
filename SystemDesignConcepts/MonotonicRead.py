class MonotonicDistributedSystem:
    def __init__(self):
        self.replicas = {"replica_a": {}, "replica_b": {}, "replica_c": {}}
        self.session_map = {}  # Maps client_id to a specific replica
        self.replica_list = list(self.replicas.keys())
        self.next_replica_index = 0  # Tracks the next replica for round-robin assignment

    def assign_replica(self, client_id):
        # Assign replica to client in a round-robin manner
        assigned_replica = self.replica_list[self.next_replica_index]
        self.session_map[client_id] = assigned_replica
        self.next_replica_index = (self.next_replica_index + 1) % len(self.replica_list)
        print(f"Assigned {client_id} to {assigned_replica}")
        return assigned_replica

    def write(self, client_id, key, value):
        # Assign a replica if the client has not been mapped yet
        if client_id not in self.session_map:
            assigned_replica = self.assign_replica(client_id)
        else:
            assigned_replica = self.session_map[client_id]

        # Write data only to the client's assigned replica
        self.replicas[assigned_replica][key] = value
        print(f"Client {client_id} wrote {key}: {value} to {assigned_replica}")

    def read(self, client_id, key):
        # Read from the same replica that handled the client's write
        assigned_replica = self.session_map.get(client_id, None)
        if assigned_replica:
            return self.replicas[assigned_replica].get(key)
        return None


def test_monotonic_read_your_own_writes():
    system = MonotonicDistributedSystem()

    # Test 1: Client reads its own write
    client_id_1 = "client1"
    system.write(client_id_1, "key1", "value1")
    assert system.read(client_id_1, "key1") == "value1", "Test 1 Failed: Client should read its own write"
    print("Test 1 Passed: Client reads its own write")

    # Test 2: Isolation between clients
    client_id_2 = "client2"
    assert system.read(client_id_2, "key1") is None, "Test 2 Failed: Different client should not see write"
    print("Test 2 Passed: Different client does not see the write")

    # Test 3: Monotonic reads within a single client session
    system.write(client_id_1, "key1", "updated_value1")
    assert system.read(client_id_1, "key1") == "updated_value1", "Test 3 Failed: Client should see the updated write"
    print("Test 3 Passed: Client reads updated write, ensuring monotonic reads")

    # Test 4: Round-robin assignment and RYOW for multiple clients
    client_id_3 = "client3"
    client_id_4 = "client4"
    system.write(client_id_3, "key2", "value2")
    system.write(client_id_4, "key3", "value3")

    assert system.read(client_id_3, "key2") == "value2", "Test 4 Failed: Client 3 should read its own write"
    assert system.read(client_id_4, "key3") == "value3", "Test 4 Failed: Client 4 should read its own write"
    print("Test 4 Passed: Each client reads their own writes with round-robin assignment")


# Run test cases
test_monotonic_read_your_own_writes()
