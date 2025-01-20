def bucket_sort(arr, bucket_size=5):
    if len(arr) == 0:
        return arr

    # Find the range of the input array
    min_val, max_val = min(arr), max(arr)

    # Number of buckets
    bucket_count = (max_val - min_val) // bucket_size + 1
    buckets = [[] for _ in range(bucket_count)]

    # Distribute elements into buckets
    for num in arr:
        index = (num - min_val) // bucket_size
        buckets[index].append(num)

    # Sort individual buckets and concatenate results
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))  # Using built-in sorting for simplicity

    return sorted_arr


# Example Usage
arr = [42, 32, 33, 52, 37, 47, 51]
print(bucket_sort(arr))  # Output: [32, 33, 37, 42, 47, 51, 52]
