import random
import matplotlib.pyplot as plt
import time


def merge_sort_recursion(arr):
    if(len(arr) <=1):
        return arr
    
    mid = len(arr) // 2
    left = merge_sort_recursion(arr[:mid])
    right = merge_sort_recursion(arr[mid:])

    return merge(left , right)

def merge(left , right):
    result = []
    i = j = 0

    while(i < len(left) and j < len(right)):
        if(left[i] < right[j]):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

def merge_sort_iterative(arr):
    if len(arr) <= 1:
        return arr
    
    n = len(arr)
    current_size = 1
    
    while current_size < n:
        left = 0
        while left < n:
            mid = min(left + current_size - 1, n - 1)
            right = min(left + 2 * current_size - 1, n - 1)
            
            # Merge the subarrays
            left_arr = arr[left:mid + 1]
            right_arr = arr[mid + 1:right + 1]
            merged = merge(left_arr, right_arr)
            
            
            arr[left:left + len(merged)] = merged
            
            left += 2 * current_size
        
        current_size *= 2
    
    return arr

def quick_sort_iterative(arr):
    if len(arr) <= 1:
        return arr
    
    stack = [(0, len(arr) - 1)]
    
    while stack:
        low, high = stack.pop()
        
        if low >= high:
            continue
            
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        pivot_index = i + 1
        
        stack.append((low, pivot_index - 1))
        stack.append((pivot_index + 1, high))
    
    return arr

def quick_sort_recursion(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort_recursion(left) + middle + quick_sort_recursion(right)


def binary_search_recursion(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursion(arr, target, low, mid - 1)
    else:
        return binary_search_recursion(arr, target, mid + 1, high)


def binary_search_iterative(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1


def generate_random_array(size):
    return [random.randint(1, 10000000) for _ in range(size)]


def test_sorting_algorithms():
    """Test and compare sorting algorithms"""
    print("=" * 80)
    print("SORTING ALGORITHMS COMPARISON")
    print("=" * 80)
    
    
    sizes = [10,100, 1000, 10000, 50000, 100000, 200000, 300000, 400000, 500000, 600000]
    # sizes = [10,100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000]
    results = []
    
    for size in sizes:
        
        arr = generate_random_array(size)
        
        
        sorted_arr = sorted(arr)
        
       
        arr1 = arr.copy()
        start = time.time()
        result1 = quick_sort_recursion(arr1)
        qs_rec_time = time.time() - start
        
       
        arr2 = arr.copy()
        start = time.time()
        result2 = quick_sort_iterative(arr2)
        qs_itr_time = time.time() - start
        
        
        arr3 = arr.copy()
        start = time.time()
        result3 = merge_sort_recursion(arr3)
        ms_rec_time = time.time() - start
        
        
        arr4 = arr.copy()
        start = time.time()
        result4 = merge_sort_iterative(arr4)
        ms_itr_time = time.time() - start
        
        
        
        results.append({
            'Size': size,
            'QS Recursive': qs_rec_time,
            'QS Iterative': qs_itr_time,
            'MS Recursive': ms_rec_time,
            'MS Iterative': ms_itr_time
        })
        
        print(f"Size {size:10d}: QS_Rec={qs_rec_time:.6f}s, QS_Itr={qs_itr_time:.6f}s, "
              f"MS_Rec={ms_rec_time:.6f}s, MS_Itr={ms_itr_time:.6f}s")
    
    return results, sizes



def test_searching_algorithms():
    
    print("\n" + "=" * 80)
    print("SEARCHING ALGORITHMS COMPARISON")
    print("=" * 80)
    
    # sizes = [10,100, 1000, 10000, 50000, 100000, 200000, 300000, 400000, 500000, 600000]
    
    sizes = [10,100, 1000, 10000, 100000, 1000000]
    
    results = []
    
    for size in sizes:
        
        arr = generate_random_array(size)
        arr.sort()
        
        
        target = random.randint(1, 1000000)
        
        
        start = time.time()
        idx1 = binary_search_recursion(arr, target)
        bs_rec_time = time.time() - start
        
        
        start = time.time()
        idx2 = binary_search_iterative(arr, target)
        bs_itr_time = time.time() - start
        
        
        assert idx1 == idx2, f"Binary Search implementations give different results: {idx1} vs {idx2}"
        
       

        
        results.append({
            'Size': size,
            'BS Recursive': bs_rec_time,
            'BS Iterative': bs_itr_time,
            
        })
        
        print(f"Size {size:7d}: BS_Rec={bs_rec_time:.8f}s, BS_Itr={bs_itr_time:.8f}s")
    
    return results, sizes


def plot_results(sorting_results, searching_results, sorting_sizes, searching_sizes):
    """Create visual plots of the results"""
  
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
   
    ax1 = axes[0, 0]
    ax1.plot(sorting_sizes, [r['QS Recursive'] for r in sorting_results], 
             'bo-', label='Quick Sort Recursive', linewidth=2)
    ax1.plot(sorting_sizes, [r['QS Iterative'] for r in sorting_results], 
             'ro-', label='Quick Sort Iterative', linewidth=2)
    ax1.plot(sorting_sizes, [r['MS Recursive'] for r in sorting_results], 
             'go-', label='Merge Sort Recursive', linewidth=2)
    ax1.plot(sorting_sizes, [r['MS Iterative'] for r in sorting_results], 
             'mo-', label='Merge Sort Iterative', linewidth=2)
    ax1.set_xlabel('Array Size')
    ax1.set_ylabel('Time (seconds)')
    ax1.set_title('Sorting Algorithms Performance Comparison')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.set_xscale('log')
    ax1.set_yscale('log')
    
 
    ax2 = axes[0, 1]
    ax2.plot(sorting_sizes, [r['QS Recursive'] for r in sorting_results], 
             'bo-', label='Recursive', linewidth=2)
    ax2.plot(sorting_sizes, [r['QS Iterative'] for r in sorting_results], 
             'ro-', label='Iterative', linewidth=2)
    ax2.set_xlabel('Array Size')
    ax2.set_ylabel('Time (seconds)')
    ax2.set_title('Quick Sort: Recursive vs Iterative')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    ax2.set_xscale('log')
    ax2.set_yscale('log')
    
  
    ax3 = axes[1, 0]
    ax3.plot(sorting_sizes, [r['MS Recursive'] for r in sorting_results], 
             'go-', label='Recursive', linewidth=2)
    ax3.plot(sorting_sizes, [r['MS Iterative'] for r in sorting_results], 
             'mo-', label='Iterative', linewidth=2)
    ax3.set_xlabel('Array Size')
    ax3.set_ylabel('Time (seconds)')
    ax3.set_title('Merge Sort: Recursive vs Iterative')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    ax3.set_xscale('log')
    ax3.set_yscale('log')
    
   
    ax4 = axes[1, 1]
    ax4.plot(searching_sizes, [r['BS Recursive'] for r in searching_results], 
             'bo-', label='Recursive', linewidth=2)
    ax4.plot(searching_sizes, [r['BS Iterative'] for r in searching_results], 
             'ro-', label='Iterative', linewidth=2)
    ax4.set_xlabel('Array Size')
    ax4.set_ylabel('Time (miroseconds)')
    ax4.set_title('Binary Search: Recursive vs Iterative')
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    ax4.set_xscale('log')
    
    plt.tight_layout()
    plt.savefig('algorithm_comparison.png', dpi=150, bbox_inches='tight')
    plt.show()

def main():
    """Main function to run all tests"""
    print("Algorithm Comparison Program")
    print("Generating random arrays and testing algorithms...\n")
    
    sorting_results, sorting_sizes = test_sorting_algorithms()
    searching_results, searching_sizes = test_searching_algorithms()

    plot_results(sorting_results, searching_results, sorting_sizes, searching_sizes)
        

if __name__ == "__main__":
    random.seed(42)
    main()