import random
import time 
import matplotlib.pyplot as plt

def bruteForce(arr):
    max_sum = 0
    for i in range(len(arr)):
        current_sum = arr[i]
        for k in range(i+1,len(arr)):
            current_sum += arr[k]
        max_sum = max(current_sum,max_sum)
    return max_sum


# Algorithm MaxSum(p, q)
# if p == q then return max(A[p], 0)
# m = (p+q)/2
# maxL = MaxSum(p,m)
# maxR = MaxSum(m+1, q)
# compute maxMidL
# compute maxMidR
# maxMid = maxMidL + maxMidR

# return max(maxL, maxR, maxMid)


def divide_conquer(arr, p=0, q=None):
    if q is None:
        q = len(arr) - 1
    if p == q :
        return max(arr[p],0)
    
    mid = (p+q)//2
    maxL = divide_conquer(arr,p,mid)
    maxr = divide_conquer(arr,mid+1,q)
    
    left_sum = float('-inf')
    temp = 0
    for i in range (p , mid+1):
        temp += arr[i]
        left_sum = max(left_sum, temp)

    right_sum =float('-inf')
    temp = 0
    for i in range (q, mid, -1):
        temp += arr[i]
        right_sum = max(right_sum, temp)

    # maxMid = max((left_sum + right_sum),left_sum,right_sum)
    maxMid = (left_sum + right_sum)
    print(left_sum , maxMid, right_sum)
    return max(maxL,maxr,maxMid)
            
# result={
#     'BruteForce' :[],
#     'Divide_conquer' : []
# }


# sizes = [10**i for i in range(1,5)]


# for n in sizes:
#     arr = [random.randint(-10000, 10000) for _ in range(n)]
#     arr1 = arr.copy()
#     arr2 = arr.copy()

#     st_time = time.time()
#     divide_conquer(arr2)
#     result['Divide_conquer'].append(time.time() - st_time)

#     st_time = time.time()
#     bruteForce(arr1)
#     result['BruteForce'].append(time.time() - st_time)


# plt.figure(figsize=(10, 6))
# plt.plot(sizes, result['Divide_conquer'], marker='o', label='Divide & Conquer O(n log n)')
# plt.plot(sizes, result['BruteForce'], marker='s', label='BruteForce O(n^2)')
# plt.xscale('log')
# plt.yscale('log')
# plt.xlabel("Array Size")
# plt.ylabel("Time (seconds)")
# plt.title("Time Complexity Comparison")
# plt.legend()
# plt.savefig('Maximum sum Time comparision2')
# plt.show()

arr = [-2,-3,-5,8,10,20,-50]
print(divide_conquer(arr))