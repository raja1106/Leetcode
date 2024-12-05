import redis


class DistributedLockWithFencing:
    """
    A distributed lock implementation with fencing tokens using Redis.
    """

    def __init__(self, redis_client, lock_key):
        self.redis_client = redis_client
        self.lock_key = lock_key

    def acquire_lock(self, client_id):
        """
        Acquires a distributed lock and returns a fencing token.
        """
        # Atomic operation to set lock and generate token
        token = self.redis_client.incr(self.lock_key)
        print(f"Lock acquired by {client_id} with token {token}")
        return token

    def release_lock(self, client_id):
        """
        Releases the lock if the client holds it.
        """
        current_holder = self.redis_client.get(f"{self.lock_key}:holder")
        if current_holder and current_holder.decode() == client_id:
            self.redis_client.delete(f"{self.lock_key}:holder")
            print(f"Lock released by {client_id}")
        else:
            print(f"Lock release failed for {client_id}: Not the lock holder")


class ResourceManager:
    """
    A resource manager that validates fencing tokens to prevent stale clients from acting.
    """

    def __init__(self):
        self.latest_token = 0  # Stores the highest valid fencing token

    def validate_and_process(self, token, client_id, action):
        """
        Validates the fencing token and processes the action if valid.
        """
        if token >= self.latest_token:
            self.latest_token = token
            print(f"Action '{action}' by {client_id} processed with token {token}")
        else:
            print(f"Action '{action}' by {client_id} rejected (stale token: {token})")


if __name__ == "__main__":
    # Connect to Redis
    redis_client = redis.StrictRedis(host="localhost", port=6379, db=0)

    # Create lock and resource manager
    lock = DistributedLockWithFencing(redis_client, "resource_lock")
    resource = ResourceManager()

    # Simulate clients acquiring locks and processing actions
    token1 = lock.acquire_lock("Client1")
    resource.validate_and_process(token1, "Client1", "update")

    token2 = lock.acquire_lock("Client2")
    resource.validate_and_process(token2, "Client2", "update")

    # Stale client retrying
    resource.validate_and_process(token1, "Client1", "update")  # Rejected
