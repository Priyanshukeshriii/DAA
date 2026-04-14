import random
import time
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

# ==================== SORTING ALGORITHMS ====================

# Quick Sort - Recursive
def quick_sort_recursive(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort_recursive(left) + middle + quick_sort_recursive(right)

# Quick Sort - Iterative
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

# Merge Sort - Recursive
def merge_sort_recursive(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort_recursive(arr[:mid])
    right = merge_sort_recursive(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Merge Sort - Iterative
def merge_sort_iterative(arr):
    if len(arr) <= 1:
        return arr
    
    # Create subarrays of size 1, 2, 4, 8, ...
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
            
            # Copy merged array back
            arr[left:left + len(merged)] = merged
            
            left += 2 * current_size
        
        current_size *= 2
    
    return arr

# ==================== SEARCHING ALGORITHMS ====================

# Binary Search - Recursive
def binary_search_recursive(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, high)

# Binary Search - Iterative
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

# ==================== TESTING AND COMPARISON ====================

def generate_random_array(size):
    """Generate random array of given size"""
    return [random.randint(1, 1000000) for _ in range(size)]

def test_sorting_algorithms():
    """Test and compare sorting algorithms"""
    print("=" * 80)
    print("SORTING ALGORITHMS COMPARISON")
    print("=" * 80)
    
    # Generate array sizes in increasing order
    sizes = [10, 100, 1000, 5000, 10000, 20000, 30000, 40000, 50000, 60000]
    
    results = []
    
    for size in sizes:
        # Generate random array
        arr = generate_random_array(size)
        
        # Get reference sorted array
        sorted_arr = sorted(arr)
        
        # Test Quick Sort Recursive
        arr1 = arr.copy()
        start = time.time()
        result1 = quick_sort_recursive(arr1)
        qs_rec_time = time.time() - start
        
        # Test Quick Sort Iterative
        arr2 = arr.copy()
        start = time.time()
        result2 = quick_sort_iterative(arr2)
        qs_itr_time = time.time() - start
        
        # Test Merge Sort Recursive
        arr3 = arr.copy()
        start = time.time()
        result3 = merge_sort_recursive(arr3)
        ms_rec_time = time.time() - start
        
        # Test Merge Sort Iterative
        arr4 = arr.copy()
        start = time.time()
        result4 = merge_sort_iterative(arr4)
        ms_itr_time = time.time() - start
        
        # Verify all produce same result
        # Note: result1 is a new list from recursive quick sort
        # result2, result3, result4 are the modified original lists
        assert result1 == sorted_arr, "Quick Sort Recursive failed"
        assert arr2 == sorted_arr, "Quick Sort Iterative failed"
        assert arr3 == sorted_arr, "Merge Sort Recursive failed"
        assert arr4 == sorted_arr, "Merge Sort Iterative failed"
        
        results.append({
            'Size': size,
            'QS Recursive': qs_rec_time,
            'QS Iterative': qs_itr_time,
            'MS Recursive': ms_rec_time,
            'MS Iterative': ms_itr_time
        })
        
        print(f"Size {size:6d}: QS_Rec={qs_rec_time:.6f}s, QS_Itr={qs_itr_time:.6f}s, "
              f"MS_Rec={ms_rec_time:.6f}s, MS_Itr={ms_itr_time:.6f}s")
    
    return results, sizes

def test_searching_algorithms():
    """Test and compare searching algorithms"""
    print("\n" + "=" * 80)
    print("SEARCHING ALGORITHMS COMPARISON")
    print("=" * 80)
    
    # Generate array sizes
    sizes = [100, 1000, 10000, 50000, 100000, 200000, 300000, 400000, 500000, 600000]
    
    results = []
    
    for size in sizes:
        # Generate random sorted array
        arr = generate_random_array(size)
        arr.sort()
        
        # Generate random target (may or may not be in array)
        target = random.randint(1, 1000000)
        
        # Test Binary Search Recursive
        start = time.time()
        idx1 = binary_search_recursive(arr, target)
        bs_rec_time = time.time() - start
        
        # Test Binary Search Iterative
        start = time.time()
        idx2 = binary_search_iterative(arr, target)
        bs_itr_time = time.time() - start
        
        # Verify both give same result
        assert idx1 == idx2, f"Binary Search implementations give different results: {idx1} vs {idx2}"
        
        # Also test with target known to be in array
        if arr:  # if array is not empty
            known_target = random.choice(arr)
            start = time.time()
            binary_search_recursive(arr, known_target)
            bs_rec_found_time = time.time() - start
            
            start = time.time()
            binary_search_iterative(arr, known_target)
            bs_itr_found_time = time.time() - start
        else:
            bs_rec_found_time = bs_itr_found_time = 0
        
        results.append({
            'Size': size,
            'BS Recursive': bs_rec_time,
            'BS Iterative': bs_itr_time,
            'BS Rec (Found)': bs_rec_found_time,
            'BS Itr (Found)': bs_itr_found_time
        })
        
        print(f"Size {size:7d}: BS_Rec={bs_rec_time:.8f}s, BS_Itr={bs_itr_time:.8f}s, "
              f"Found_Rec={bs_rec_found_time:.8f}s, Found_Itr={bs_itr_found_time:.8f}s")
    
    return results, sizes

def display_results_table(sorting_results, searching_results):
    """Display results in tabular format"""
    
    print("\n" + "=" * 80)
    print("SORTING RESULTS TABLE")
    print("=" * 80)
    
    # Prepare sorting data for table
    sorting_table = []
    headers = ["Array Size", "QS Recursive (s)", "QS Iterative (s)", 
               "MS Recursive (s)", "MS Iterative (s)"]
    
    for result in sorting_results:
        sorting_table.append([
            result['Size'],
            f"{result['QS Recursive']:.6f}",
            f"{result['QS Iterative']:.6f}",
            f"{result['MS Recursive']:.6f}",
            f"{result['MS Iterative']:.6f}"
        ])
    
    print(tabulate(sorting_table, headers=headers, tablefmt="grid"))
    
    print("\n" + "=" * 80)
    print("SEARCHING RESULTS TABLE")
    print("=" * 80)
    
    # Prepare searching data for table
    searching_table = []
    headers = ["Array Size", "BS Recursive (s)", "BS Iterative (s)", 
               "BS Rec Found (s)", "BS Itr Found (s)"]
    
    for result in searching_results:
        searching_table.append([
            result['Size'],
            f"{result['BS Recursive']:.8f}",
            f"{result['BS Iterative']:.8f}",
            f"{result['BS Rec (Found)']:.8f}",
            f"{result['BS Itr (Found)']:.8f}"
        ])
    
    print(tabulate(searching_table, headers=headers, tablefmt="grid"))

def plot_results(sorting_results, searching_results, sorting_sizes, searching_sizes):
    """Create visual plots of the results"""
    
    # Create figure with 2 subplots
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # Plot 1: Sorting Algorithms Comparison
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
    
    # Plot 2: Quick Sort Recursive vs Iterative
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
    
    # Plot 3: Merge Sort Recursive vs Iterative
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
    
    # Plot 4: Binary Search Comparison
    ax4 = axes[1, 1]
    ax4.plot(searching_sizes, [r['BS Recursive'] for r in searching_results], 
             'bo-', label='Recursive', linewidth=2)
    ax4.plot(searching_sizes, [r['BS Iterative'] for r in searching_results], 
             'ro-', label='Iterative', linewidth=2)
    ax4.set_xlabel('Array Size')
    ax4.set_ylabel('Time (seconds)')
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
    
    try:
        # Test sorting algorithms
        sorting_results, sorting_sizes = test_sorting_algorithms()
        
        # Test searching algorithms
        searching_results, searching_sizes = test_searching_algorithms()
        
        # Display results in tables
        display_results_table(sorting_results, searching_results)
        
        # Plot results
        plot_results(sorting_results, searching_results, sorting_sizes, searching_sizes)
        
        print("\n" + "=" * 80)
        print("SUMMARY OBSERVATIONS:")
        print("=" * 80)
        print("1. SORTING ALGORITHMS:")
        print("   - Both Quick Sort and Merge Sort have O(n log n) average time complexity")
        print("   - Quick Sort is generally faster for random data due to better cache performance")
        print("   - Merge Sort has consistent O(n log n) performance but uses more memory")
        print("   - Recursive vs Iterative: Usually similar performance, but iterative avoids recursion limits")
        
        print("\n2. SEARCHING ALGORITHMS:")
        print("   - Binary Search has O(log n) time complexity for sorted arrays")
        print("   - Iterative version is usually slightly faster and uses less memory")
        print("   - Recursive version is more elegant but has recursion depth limits")
        
        print("\n3. PRACTICAL NOTES:")
        print("   - For large arrays, iterative methods avoid recursion depth limits")
        print("   - Quick Sort can degrade to O(n²) for certain inputs (not random)")
        print("   - Merge Sort is stable and predictable")
        print("   - Binary Search requires sorted array as precondition")
        
    except Exception as e:
        print(f"Error during execution: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    # Set random seed for reproducibility
    random.seed(42)
    main()