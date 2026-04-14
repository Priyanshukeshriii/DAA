import random
import matplotlib.pyplot as plt
import copy



def merge_and_count(arr, temp, left, mid, right):
    i = left
    j = mid + 1
    k = left
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    for idx in range(left, right + 1):
        arr[idx] = temp[idx]

    return inv_count


def merge_sort_and_count(arr, temp, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count += merge_sort_and_count(arr, temp, left, mid)
        inv_count += merge_sort_and_count(arr, temp, mid + 1, right)
        inv_count += merge_and_count(arr, temp, left, mid, right)
    return inv_count


def count_inversions(arr):
    temp = [0] * len(arr)
    return merge_sort_and_count(arr, temp, 0, len(arr) - 1)




def insertion_sort(arr):
    swaps = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            swaps += 1
            j -= 1
        arr[j + 1] = key
    return swaps


def selection_sort(arr):
    swaps = 0
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
    return swaps


def quick_sort(arr):
    swaps = 0

    def partition(low, high):
        nonlocal swaps
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        swaps += 1
        return i + 1

    def quick_sort_recursive(low, high):
        if low < high:
            pi = partition(low, high)
            quick_sort_recursive(low, pi - 1)
            quick_sort_recursive(pi + 1, high)

    quick_sort_recursive(0, len(arr) - 1)
    return swaps



sizes = [10,100,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]

inversion_counts = []
insertion_swaps = []
selection_swaps = []
quick_swaps = []

for array_size in sizes:
    arr = [random.randint(1,1000) for _ in range(array_size)]

    inv = count_inversions(copy.copy(arr))
    inversion_counts.append(inv)

    insertion_swaps.append(insertion_sort(copy.copy(arr)))
    selection_swaps.append(selection_sort(copy.copy(arr)))
    quick_swaps.append(quick_sort(copy.copy(arr)))

print("=" * 70)
print(f"{'size':<10}{'Inversions':<15}{'Insertion':<15}{'Selection':<15}{'Quick':<10}")
print("=" * 70)

for i,size  in enumerate (sizes):
    print(f"{size:<6}"
          f"{inversion_counts[i]:<15}"
          f"{insertion_swaps[i]:<15}"
          f"{selection_swaps[i]:<15}"
          f"{quick_swaps[i]:<10}")

print("=" * 70)

plt.figure(figsize=(10, 6))

plt.plot(inversion_counts, label="Actual Inversions", marker='o')
plt.plot(insertion_swaps, label="Insertion Sort Swaps", marker='o')
plt.plot(selection_swaps, label="Selection Sort Swaps", marker='o')
plt.plot(quick_swaps, label="Quick Sort Swaps", marker='o')
plt.yscale('log')
plt.xlabel("Test Case (Random Array)")
plt.ylabel("Number of Swaps / Inversions")
plt.title("Comparison of Inversions vs Sorting Swaps (10 Random Arrays)")
plt.legend()
plt.grid(True)
plt.savefig('compairion of swap_01')
plt.show()


