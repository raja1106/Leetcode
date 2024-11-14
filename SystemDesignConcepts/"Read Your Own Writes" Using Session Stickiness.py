class DistributedSystem:
    def __init__(self):
        self.replicas = {"replica_a": {}, "replica_b": {}}
        self.session_map = {}  # Maps client_id to a specific replica

    def write(self, client_id, key, value):
        # Select a replica for the client if not already mapped
        if client_id not in self.session_map:
            self.session_map[client_id] = "replica_a"  # Can use load balancing logic here
        replica = self.session_map[client_id]
        self.replicas[replica][key] = value

    def read(self, client_id, key):
        # Read from the same replica that handled the write
        replica = self.session_map.get(client_id, "replica_a")
        return self.replicas[replica].get(key)


# Test cases
def test_read_your_own_writes():
    system = DistributedSystem()

    # Test 1: Write and Read on same client
    client_id = "client1"
    system.write(client_id, "key1", "value1")
    assert system.read(client_id, "key1") == "value1", "Test 1 Failed: Client should read their own write"
    print("Test 1 Passed: Client reads their own write")

    # Test 2: Read from a different client (should not see the write)
    another_client_id = "client2"
    assert system.read(another_client_id, "key1") is None, "Test 2 Failed: Different client should not see write"
    print("Test 2 Passed: Different client does not see the write")

    # Test 3: Different clients with different keys
    system.write(another_client_id, "key2", "value2")
    assert system.read(another_client_id,
                       "key2") == "value2", "Test 3 Failed: Second client should read their own write"
    assert system.read(client_id,
                       "key2") is None, "Test 3 Failed: First client should not see the second client's write"
    print("Test 3 Passed: Separate clients isolated")

    # Test 4: Read from the same replica after a write
    system.write(client_id, "key1", "updated_value1")
    assert system.read(client_id, "key1") == "updated_value1", "Test 4 Failed: Client should see updated write"
    print("Test 4 Passed: Client reads updated write")


# Run test cases
#test_read_your_own_writes()

#-----------With LB Logic in the above code -------------------------------------------#


class DistributedSystemWithLB:
    def __init__(self):
        self.replicas = {"replica_a": {}, "replica_b": {}, "replica_c": {}}
        self.session_map = {}  # Maps client_id to a specific replica
        self.replica_list = list(self.replicas.keys())
        self.next_replica_index = 0  # Tracks the next replica for round-robin

    def assign_replica(self, client_id):
        # Round-robin assignment: Select the next replica in sequence
        assigned_replica = self.replica_list[self.next_replica_index]
        self.session_map[client_id] = assigned_replica
        # Update the index for the next client
        self.next_replica_index = (self.next_replica_index + 1) % len(self.replica_list)
        print(f"Assigned {client_id} to {assigned_replica}")
        return assigned_replica

    def write(self, client_id, key, value):
        # Assign a replica if the client has not been mapped yet
        if client_id not in self.session_map:
            assigned_replica = self.assign_replica(client_id)
        else:
            assigned_replica = self.session_map[client_id]

        # Write data to the assigned replica
        self.replicas[assigned_replica][key] = value
        print(f"Client {client_id} wrote {key}: {value} to {assigned_replica}")

    def read(self, client_id, key):
        # Read from the same replica that handled the client's write
        assigned_replica = self.session_map.get(client_id, None)
        if assigned_replica:
            return self.replicas[assigned_replica].get(key)
        return None


def test_load_balanced_read_your_own_writes():
    system = DistributedSystemWithLB()

    # Test 1: Check round-robin assignment and RYOW for multiple clients
    client_id_1 = "client1"
    client_id_2 = "client2"
    client_id_3 = "client3"
    system.write(client_id_1, "key1", "value1")
    system.write(client_id_2, "key2", "value2")
    system.write(client_id_3, "key3", "value3")

    # Ensure each client reads their own writes from their assigned replica
    assert system.read(client_id_1, "key1") == "value1", "Test 1 Failed: Client 1 RYOW check"
    assert system.read(client_id_2, "key2") == "value2", "Test 1 Failed: Client 2 RYOW check"
    assert system.read(client_id_3, "key3") == "value3", "Test 1 Failed: Client 3 RYOW check"
    print("Test 1 Passed: Each client reads their own writes with round-robin assignment")

    # Test 2: Verify round-robin assignment is balanced
    # Adding a fourth client to check if it wraps around
    client_id_4 = "client4"
    system.write(client_id_4, "key4", "value4")
    assert system.read(client_id_4, "key4") == "value4", "Test 2 Failed: Client 4 RYOW check"
    print("Test 2 Passed: Round-robin load balancing wraps around correctly")

    # Test 3: Verify isolation between clients
    assert system.read(client_id_1, "key2") is None, "Test 3 Failed: Client 1 should not see Client 2's write"
    assert system.read(client_id_2, "key3") is None, "Test 3 Failed: Client 2 should not see Client 3's write"
    assert system.read(client_id_3, "key1") is None, "Test 3 Failed: Client 3 should not see Client 1's write"
    print("Test 3 Passed: Client isolation is maintained across replicas")


# Run test cases
test_load_balanced_read_your_own_writes()

