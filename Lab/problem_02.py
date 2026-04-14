import matplotlib.pyplot as plt
import random
import time


def merge(arr, st, end, mid, size):
    i = st
    j = mid + 1
    temp = [0] * (end - st + 1)
    index = 0

    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            temp[index] = arr[i]
            i += 1
        else:
            temp[index] = arr[j]
            j += 1
        index += 1

    while i <= mid:
        temp[index] = arr[i]
        i += 1
        index += 1

    while j <= end:
        temp[index] = arr[j]
        j += 1
        index += 1

    for i in range(index):
        arr[i + st] = temp[i]


def merge_sort(arr, st, end, size):
    if st < end:
        mid = st + (end - st) // 2
        merge_sort(arr, st, mid, size)
        merge_sort(arr, mid + 1, end, size)
        merge(arr, st, end, mid, size)




def partition(arr, left, right, loc, n):
    global comparisons
    while left < right:
        comparisons += 1
        
        if loc == left:
            if arr[loc] > arr[right]:
                arr[loc], arr[right] = arr[right], arr[loc]
                loc = right
                left += 1
            else:
                right -= 1
        elif loc == right:
            if arr[loc] < arr[left]:
                arr[loc], arr[left] = arr[left], arr[loc]
                loc = left
                right -= 1
            else:
                left += 1
    return loc

def quick_sort(arr, left, right, n):
    if left < right:
        loc = partition(arr, left, right, left, n)        
        quick_sort(arr, left, loc - 1, n)
        quick_sort(arr, loc + 1, right, n)





def generate_array(size):
    return [random.randint(1, 1000) for _ in range(size)]

def sorting():
    sizes = [10,100,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000]
    result = {
        'quick_sort' :[],
        'merge_sort' :[],
        'iteraative_merge_sort': [],
        'iteraative_quick_sort': []
    }

    for i , size in enumerate(sizes) :
        orignal_array = generate_array(size)
        arr = orignal_array.copy()
        time_start = time.time()
        merge_sort(arr,0,size - 1,size)
        time_end = time.time()
        time_taken = time_end - time_end

        arr = orignal_array.copy()
        time_start = time.time()
        quick_sort(arr,0,size - 1,size)
        time_end = time.time()
        time_taken = time_end - time_end
        
        arr = orignal_array.copy()
        time_start = time.time()
        merge_sort(arr,0,size - 1,size)
        time_end = time.time()
        time_taken = time_end - time_end

        arr = orignal_array.copy()
        time_start = time.time()
        merge_sort(arr,0,size - 1,size)
        time_end = time.time()
        time_taken = time_end - time_end

