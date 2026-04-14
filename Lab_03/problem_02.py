import random
import matplotlib.pyplot as plt
import time

def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key

def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

def selection_sort(arr):
    a = arr.copy()
    for i in range(len(a)):
        min_idx = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]

def counting_sort(arr):
    if len(arr) == 0:
        return

    size_aux = max(arr) + 1
    aux = [0] * size_aux
    result = [0] * len(arr)

    for num in arr:
        aux[num] += 1

    for i in range(1, size_aux):
        aux[i] += aux[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        result[aux[arr[i]] - 1] = arr[i]
        aux[arr[i]] -= 1

    for i in range(len(arr)):
        arr[i] = result[i]


sizes = [10,50, 100,200,300,400,500,600,700,800,900, 1000, 2000,3000,4000,5000]

insertion_times = []
bubble_times = []
selection_times = []
counting_times = []

for size in sizes:
    arr = [random.randint(0, 1000) for _ in range(size)]

    arr_copy = arr.copy()
    start = time.perf_counter()
    insertion_sort(arr_copy)
    insertion_times.append(time.perf_counter() - start)

    arr_copy = arr.copy()
    start = time.perf_counter()
    bubble_sort(arr_copy)
    bubble_times.append(time.perf_counter() - start)

    arr_copy = arr.copy()
    start = time.perf_counter()
    selection_sort(arr_copy)
    selection_times.append(time.perf_counter() - start)

    arr_copy = arr.copy()
    start = time.perf_counter()
    counting_sort(arr_copy)
    counting_times.append(time.perf_counter() - start)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(sizes, insertion_times, label="Insertion Sort")
plt.plot(sizes, bubble_times, label="Bubble Sort")
plt.plot(sizes, selection_times, label="Selection Sort")
plt.plot(sizes, counting_times, label="Counting Sort")

plt.xlabel("Array Size")
plt.ylabel("Time (seconds)")
plt.title("Sorting Algorithm Time Comparison")
plt.legend()
plt.grid(True)
plt.show()
plt.savefig("time comarision")
print("completed")