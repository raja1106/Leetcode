class Replica: #a replica-level version vector is implemented here
    def __init__(self, replica_id):
        self.data = {}  # Holds key-value data
        self.version_vector = {"A": 0, "B": 0, "C": 0}  # Tracks causality by replica
        self.replica_id = replica_id
        self.buffered_updates = []  # Buffer for updates with unmet dependencies

    def local_write(self, key, value):
        self.data[key] = value
        self.version_vector[self.replica_id] += 1
        print(f"{self.replica_id} local write: {key} = {value}")
        print(f"{self.replica_id} version vector after write: {self.version_vector}")

    def receive_update(self, key, value, incoming_vector):
        if self.is_causally_ready(incoming_vector):
            self.data[key] = value
            self.update_version_vector(incoming_vector)
            print(f"{self.replica_id} received update: {key} = {value}")
            print(f"{self.replica_id} version vector after update: {self.version_vector}")
            self.process_buffered_updates()
        else:
            self.buffer_update(key, value, incoming_vector)

    def is_causally_ready(self, incoming_vector):
        for replica, version in incoming_vector.items():
            if version > self.version_vector.get(replica, 0):
                return False
        return True

    def update_version_vector(self, incoming_vector):
        for replica, version in incoming_vector.items():
            self.version_vector[replica] = max(self.version_vector.get(replica, 0), version)

    def buffer_update(self, key, value, incoming_vector):
        self.buffered_updates.append((key, value, incoming_vector))
        print(f"{self.replica_id} buffered update: {key} = {value} with vector {incoming_vector}")

    def process_buffered_updates(self):
        still_buffered = []
        for key, value, vector in self.buffered_updates:
            if self.is_causally_ready(vector):
                self.data[key] = value
                self.update_version_vector(vector)
                print(f"{self.replica_id} processed buffered update: {key} = {value}")
                print(f"{self.replica_id} version vector after processing buffer: {self.version_vector}")
            else:
                still_buffered.append((key, value, vector))
        self.buffered_updates = still_buffered


# Test code with debugging

replica_a = Replica(replica_id="A")
replica_b = Replica(replica_id="B")
replica_c = Replica(replica_id="C")

def test_causal_consistency():
    print("\n--- Test Start ---\n")

    print("\nStep 1: Replica A writes 'key1': 'valueA'")
    replica_a.local_write("key1", "valueA")

    print("\nStep 2: Replica B receives update from A")
    replica_b.receive_update("key1", "valueA", replica_a.version_vector)

    print("\nStep 3: Replica B writes 'key2': 'valueB'")
    replica_b.local_write("key2", "valueB")

    print("\nStep 4: Replica A receives update from B")
    replica_a.receive_update("key2", "valueB", replica_b.version_vector)
    print("\nStep 4: Replica C receives update from B")
    replica_c.receive_update("key2", "valueB", replica_b.version_vector)

    print("\nStep 5: Replica C receives update from A")
    replica_c.receive_update("key1", "valueA", replica_a.version_vector)

    print("\n--- Final State Check ---")
    print("Replica A data:", replica_a.data)
    print("Replica A version vector:", replica_a.version_vector)
    print("Replica B data:", replica_b.data)
    print("Replica B version vector:", replica_b.version_vector)
    print("Replica C data:", replica_c.data)
    print("Replica C version vector:", replica_c.version_vector)

    assert replica_a.data == {"key1": "valueA", "key2": "valueB"}, "Replica A data mismatch"
    assert replica_b.data == {"key1": "valueA", "key2": "valueB"}, "Replica B data mismatch"
    assert replica_c.data == {"key1": "valueA", "key2": "valueB"}, "Replica C data mismatch"
    print("\nCausal Consistency Test Passed.")


# Run the test
test_causal_consistency()

# ----------------Record-Level Version Vector --------------------- #

class Replica:
    def __init__(self, replica_id):
        self.data = {}  # Stores each record's data
        self.record_version_vectors = {}  # Tracks version vectors for each record
        self.replica_id = replica_id
        self.buffered_updates = []  # Buffer for updates with unmet dependencies

    def local_write(self, key, value):
        self.data[key] = value

        # Initialize version vector for this record if it doesn't exist
        if key not in self.record_version_vectors:
            self.record_version_vectors[key] = {"A": 0, "B": 0, "C": 0}

        # Increment this replica's counter for the specific record's version vector
        self.record_version_vectors[key][self.replica_id] += 1
        print(f"{self.replica_id} local write: {key} = {value}")
        print(f"{self.replica_id} record-level version vector for {key}: {self.record_version_vectors[key]}")

    def receive_update(self, key, value, incoming_vector):
        # Check if all causal dependencies for the record are met
        if self.is_causally_ready(key, incoming_vector):
            self.data[key] = value
            # Merge the version vectors for this record
            self.update_version_vector(key, incoming_vector)
            print(f"{self.replica_id} received update: {key} = {value}")
            print(f"{self.replica_id} record-level version vector after update for {key}: {self.record_version_vectors[key]}")
            # Process any buffered updates that might now be ready
            self.process_buffered_updates()
        else:
            # Buffer this update until dependencies are met
            self.buffer_update(key, value, incoming_vector)

    def is_causally_ready(self, key, incoming_vector):
        # Check if the incoming update's version vector is <= current version vector for this record
        if key not in self.record_version_vectors:
            return False

        for replica, version in incoming_vector.items():
            if version > self.record_version_vectors[key].get(replica, 0):
                return False
        return True

    def update_version_vector(self, key, incoming_vector):
        # Merge version vectors for the specific record by taking the max version per replica
        for replica, version in incoming_vector.items():
            self.record_version_vectors[key][replica] = max(self.record_version_vectors[key].get(replica, 0), version)

    def buffer_update(self, key, value, incoming_vector):
        # Add the update to the buffer with its causality metadata
        self.buffered_updates.append((key, value, incoming_vector))
        print(f"{self.replica_id} buffered update: {key} = {value} with vector {incoming_vector}")

    def process_buffered_updates(self):
        # Process buffered updates to see if any are now causally ready
        still_buffered = []
        for key, value, vector in self.buffered_updates:
            if self.is_causally_ready(key, vector):
                # Apply the buffered update
                self.data[key] = value
                self.update_version_vector(key, vector)
                print(f"{self.replica_id} processed buffered update: {key} = {value}")
                print(f"{self.replica_id} record-level version vector after processing buffer for {key}: {self.record_version_vectors[key]}")
            else:
                # Keep updates that are still not ready
                still_buffered.append((key, value, vector))
        # Update the buffer with only the updates that are still pending
        self.buffered_updates = still_buffered
