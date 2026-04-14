import random

def count_sort(arr):
    size_aux = (max(arr) + 1)
    aux = [0]*   size_aux
    result = [0] * (len(arr))
    for i in range(len(arr)):
        aux[arr[i]] += 1
    
    for j in range(1,size_aux):
        aux[j] += aux[j-1]
    
    for k in range(len(arr)-1, -1,-1):
        result[aux[arr[k]]-1] = arr[k]
        aux[arr[k]] -= 1
        print("=" * 25 + f" After {len(arr)-k} pass " + "=" * 25)
        print("input: ",arr) 
        print("auxiliary: ",aux)
        print("output: ",result)
    
    return result

array = [random.randint(0, 9) for _ in range(10)]
print(count_sort(array))