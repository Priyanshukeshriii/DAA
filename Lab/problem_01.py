import random
import time
import matplotlib.pyplot as plt


def selection_sort(arr):
    comp = 0
    swap = 0
    passes = 0
    n = len(arr)
    
    for i in range(n-1):
        passes += 1
        min_idx = i
        for j in range(i+1, n):
            comp += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swap += 1
    
    return passes, comp, swap


def bubble_sort(arr):
    comp = 0
    swap = 0
    passes = 0
    n = len(arr)
    
    for i in range(n):
        passes += 1
        swapped = False
        for j in range(0, n-i-1):
            comp += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap += 1
                swapped = True
        
      
        if not swapped:
            break
    
    return passes, comp, swap


def insertion_sort(arr):
    comp = 0
    swap = 0
    passes = 0
    n = len(arr)
    
    for i in range(1, n):
        passes += 1
        key = arr[i]
        j = i - 1
        
        while j >= 0:
            comp += 1
            if key < arr[j]:
                arr[j+1] = arr[j]
                swap += 1
                j -= 1
            else:
                break
        
        arr[j+1] = key
    
    return passes, comp, swap


def generate_random_array(size):
    return [random.randint(1, 100) for _ in range(size)]


def run_sorting_experiments():
    
    sizes = [10,100,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
    
    
    results = {
        'selection': {'time': [], 'passes': [], 'comp': [], 'swap': []},
        'bubble': {'time': [], 'passes': [], 'comp': [], 'swap': []},
        'insertion': {'time': [], 'passes': [], 'comp': [], 'swap': []}
    }
    
    print("=" * 80)
    print("SORTING ALGORITHM COMPARISON")
    print("=" * 80)
    
    for i, size in enumerate(sizes):
        print(f"\n{'='*60}")
        print(f"ARRAY {i+1}: Size = {size}")
        print(f"{'='*60}")
        
        
        original_array = generate_random_array(size)
        
        
        arr = original_array.copy()
        start_time = time.time()
        passes, comp, swap = selection_sort(arr)
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        results['selection']['time'].append(elapsed_time)
        results['selection']['passes'].append(passes)
        results['selection']['comp'].append(comp)
        results['selection']['swap'].append(swap)
        
        print(f"\nSelection Sort:")
        print(f"  Time: {elapsed_time:.6f} seconds")
        print(f"  Passes: {passes}")
        print(f"  Comp: {comp}")
        print(f"  Swaps: {swap}")
        
        
        arr = original_array.copy()
        start_time = time.time()
        passes, comp, swap = bubble_sort(arr)
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        results['bubble']['time'].append(elapsed_time)
        results['bubble']['passes'].append(passes)
        results['bubble']['comp'].append(comp)
        results['bubble']['swap'].append(swap)
        
        print(f"\nBubble Sort:")
        print(f"  Time: {elapsed_time:.6f} seconds")
        print(f"  Passes: {passes}")
        print(f"  Comp: {comp}")
        print(f"  Swaps: {swap}")
        
        
        arr = original_array.copy()
        start_time = time.time()
        passes, comp, swap = insertion_sort(arr)
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        results['insertion']['time'].append(elapsed_time)
        results['insertion']['passes'].append(passes)
        results['insertion']['comp'].append(comp)
        results['insertion']['swap'].append(swap)
        
        print(f"\nInsertion Sort:")
        print(f"  Time: {elapsed_time:.6f} seconds")
        print(f"  Passes: {passes}")
        print(f"  Comp: {comp}")
        print(f"  Swaps: {swap}")
    
    return sizes, results

def create_comparison_graphs(sizes, results):
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Sorting Algorithm Comparison', fontsize=16, fontweight='bold')
    
   
    ax1 = axes[0, 0]
    ax1.plot(sizes, results['selection']['time'], 'r-', marker='o', label='Selection Sort')
    ax1.plot(sizes, results['bubble']['time'], 'g-', marker='s', label='Bubble Sort')
    ax1.plot(sizes, results['insertion']['time'], 'b-', marker='^', label='Insertion Sort')
    ax1.set_xlabel('Array Size')
    ax1.set_ylabel('Time (seconds)')
    ax1.set_title('Time Complexity Comparison')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Plot 2: Comp Comparison
    ax2 = axes[0, 1]
    ax2.plot(sizes, results['selection']['comp'], 'r-', marker='o', label='Selection Sort')
    ax2.plot(sizes, results['bubble']['comp'], 'g-', marker='s', label='Bubble Sort')
    ax2.plot(sizes, results['insertion']['comp'], 'b-', marker='^', label='Insertion Sort')
    ax2.set_xlabel('Array Size')
    ax2.set_ylabel('Number of Comp')
    ax2.set_title('Comp Comparison')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # Plot 3: Swaps Comparison
    ax3 = axes[1, 0]
    ax3.plot(sizes, results['selection']['swap'], 'r-', marker='o', label='Selection Sort')
    ax3.plot(sizes, results['bubble']['swap'], 'g-', marker='s', label='Bubble Sort')
    ax3.plot(sizes, results['insertion']['swap'], 'b-', marker='^', label='Insertion Sort')
    ax3.set_xlabel('Array Size')
    ax3.set_ylabel('Number of Swaps')
    ax3.set_yscale('log')
    ax3.set_title('Swaps Comparison')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # Plot 4: Passes Comparison
    ax4 = axes[1, 1]
    ax4.plot(sizes, results['selection']['passes'], 'r-', marker='o', label='Selection Sort')
    ax4.plot(sizes, results['bubble']['passes'], 'g-', marker='s', label='Bubble Sort')
    ax4.plot(sizes, results['insertion']['passes'], 'b-', marker='^', label='Insertion Sort')
    ax4.set_xlabel('Array Size')
    ax4.set_ylabel('Number of Passes')
    ax4.set_title('Passes Comparison')
    ax4.legend()
    ax4.grid(True, alpha=0.3)


    
    plt.tight_layout()
    plt.show()
    


if __name__ == "__main__":
    sizes, results = run_sorting_experiments()
    create_comparison_graphs(sizes, results)
    
  