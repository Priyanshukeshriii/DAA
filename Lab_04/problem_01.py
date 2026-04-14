import random

def counting_sort1(arr, count):
    freq_arr = [0]* 10
    result = [0]* len(arr)

    for i in range( len(arr)):
        digit = ((arr[i]) // count) % 10
        freq_arr[digit] += 1
    for i in range (1, len(freq_arr)):
        freq_arr[i] += freq_arr[i-1]
    for i in range(len(arr)-1, -1 , -1):
        digit = (arr[i] // count) %10
        result[freq_arr[digit]-1] = arr[i]
        freq_arr[digit] -= 1

    
    return result




def radix_sort(arr):
    if len(arr) <= 1:
        return
    print('='*100)
    print("Origanl Array : ", arr)
    size_of_array = len(arr)
    result = arr.copy()
    
    itr = max(arr)
    count = 1
    while itr > 0:
        print('-'*100)
        print("Input array : " ,result)
        result = counting_sort1(result , count)
        itr = itr//10
        count*=10
        print("Auxilarry array: ", result)
    print(result)
    return result
    

def bucket_sort(arr):
    size = len(arr)
    buckets = [[] for _ in range(size)]


    for num in arr:
        Index = int(num * size)
        buckets[Index].append(num)
    
    for i in range(size):
        print(f"bucket {i} : ", buckets[i])
        buckets[i].sort()
        print(f"bucket {i} After sort : ",buckets[i])
    
    result = []
    for bucket in buckets:
        result.extend(buckets)

    return result


arr = [random.randint(1, 1000) for _ in range (10)]
radix_sort(arr)
arr1 = [random.random() for _  in range(10)]
bucket_sort(arr1)


