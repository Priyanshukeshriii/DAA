import random
import time
import matplotlib.pyplot as plt


def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j][0] > key[0]:  # sort based on digit
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def radix_sort_insertion(arr):
    a = arr.copy()
    if not a:
        return a

    max_num = max(a)
    exp = 1 

    while max_num // exp > 0:
        
        digit_list = [( (num // exp) % 10, num) for num in a]
        sorted_digit_list = insertion_sort(digit_list)
        a = [num for digit, num in sorted_digit_list]
        exp *= 10

    return a


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


def bucket_sort_quick(arr):
    size = len(arr)
    buckets = [[] for _ in range(size)]

    # distribute numbers into buckets
    for num in arr:
        index = min(int(num * size), size - 1)
        buckets[index].append(num)

    # sort each bucket using quicksort
    for i in range(size):
        if buckets[i]:
            buckets[i] = quicksort(buckets[i])

    # merge all buckets
    result = []
    for bucket in buckets:
        result.extend(bucket)
    return result


array_sizes = [10, 100, 1000,10000,100000]
radix_arrays = [ [random.randint(0, 10000) for _ in range(size)] for size in array_sizes]
insertion_arrays = [arr.copy() for arr in radix_arrays]  # same integers
bucket_arrays = [ [random.random() for _ in range(size)] for size in array_sizes]  # floats for bucket sort


radix_times = []
bucket_times = []

for i in range(len(array_sizes)):
    # Radix sort with insertion
    start = time.time()
    radix_sort_insertion(radix_arrays[i])
    end = time.time()
    radix_times.append(end - start)

    # Bucket sort with quicksort
    start = time.time()
    bucket_sort_quick(bucket_arrays[i])
    end = time.time()
    bucket_times.append(end - start)


plt.figure(figsize=(10,6))
plt.plot(array_sizes, radix_times, 'o-', label="Radix Sort (with Insertion Sort)")
plt.plot(array_sizes, bucket_times, 's-', label="Bucket Sort (with Quicksort)")
# plt.xscale('log')
# plt.yscale('log')
plt.xlabel("Array Size (log scale)")
plt.ylabel("Time (seconds, log scale)")
plt.title("Radix Sort vs Bucket Sort Performance")
plt.legend()
plt.grid(True, which="both", ls="--")
plt.savefig('Time comparision for bucket and Radix sort')
plt.show()