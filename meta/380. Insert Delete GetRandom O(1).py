from random import choice

class RandomizedSet:
    def __init__(self):
        """
        Initialize the RandomizedSet with an empty dictionary and list.
        """
        self.index_dict = {}  # Mapping of values to their indices in the list
        self.values_list = []  # List to store the values

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns True if the value was successfully inserted, False if it already exists.
        """
        if val in self.index_dict:
            return False  # Value already exists
        self.index_dict[val] = len(self.values_list)  # Map value to its index in the list
        self.values_list.append(val)  # Add value to the list
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns True if the value was successfully removed, False if it does not exist.
        """
        if val not in self.index_dict:
            return False  # Value does not exist
        index_to_remove = self.index_dict[val]  # Get the index of the value to remove
        last_element = self.values_list[-1]  # Get the last element in the list
        self.values_list[index_to_remove] = last_element  # Replace removed element with the last one
        self.index_dict[last_element] = index_to_remove  # Update the index of the last element
        self.values_list.pop()  # Remove the last element
        del self.index_dict[val]  # Delete the value from the dictionary
        return True

    def getRandom(self) -> int:
        """
        Returns a random element from the set.
        Raises an exception if the set is empty.
        """
        if not self.values_list:
            raise IndexError("getRandom() called on empty set")
        return random.choice(self.values_list)  # Randomly select and return a value from the list

# Example usage:
# randomized_set = RandomizedSet()
# param_1 = randomized_set.insert(val)
# param_2 = randomized_set.remove(val)
# param_3 = randomized_set.getRandom()
