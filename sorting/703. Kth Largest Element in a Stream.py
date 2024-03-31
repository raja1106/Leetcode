class KthLargest:

    """
    Problem Description
In this problem, we are asked to design a KthLargest class that can determine the kth largest element in a stream of numbers. Importantly, when we refer to the kth largest element, we mean according to sorted order, not that the element is distinct from the others. The numbers can be repeated in the stream.

The class should be able to handle two types of actions:

Initialization (__init__): When an instance of the class is created, it should be initialized with an integer k and an array of integers nums. The k represents the position of the largest element we are interested in, and nums is the initial stream of numbers.

Adding New Elements (add): The class should provide a method to add a new integer val to the stream. After adding the new integer, this method should return the current kth largest element from the stream.
    """

    def __init__(self, k: int, nums: List[int]):
        # Initialize a min heap to store the k largest elements
        self.min_heap = []
        # Store the size k to know the kth largest value
        self.k = k
        # Add the initial elements to the heap
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # Add the new value to the min heap
        heappush(self.min_heap, val)
        # If the size of the heap exceeds k, remove the smallest element
        if len(self.min_heap) > self.k:
            heappop(self.min_heap)
        # The root of the min heap is the kth largest value
        return self.min_heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

"""
Time and Space Complexity
Time Complexity:

The __init__(self, k: int, nums: List[int]) method has a time complexity of O(n * log(k)) where n is the length of the nums list. This is because for every element in nums, the add operation is called which takes O(log(k)) time due to the heap operation and we perform this n times.

The add(self, val: int) -> int method has a time complexity of O(log(k)). This is because the heappush operation could take up to O(log(k)) time to maintain the heap properties when adding a new element, and similarly heappop operation, which is called only when the heap size exceeds k, takes O(log(k)).
"""