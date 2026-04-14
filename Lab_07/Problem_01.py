import random

def fractional_knapsack():

    try:
        n = int(input("Enter the number of items: "))
        capacity = float(input("Enter the total capacity of the knapsack: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    items = []
    print("\n--- Generated Items ---")
    print(f"{'Item':<8} | {'Profit':<8} | {'Weight':<8} | {'Ratio':<8}")
    print("-" * 45)
    
    for i in range(n):
        profit = random.randint(10, 100)
        weight = random.randint(5, 100)
        ratio = profit / weight
        items.append({
            'id': i + 1,
            'profit': profit,
            'weight': weight,
            'ratio': ratio
        })
        print(f"Item {i+1:<3} | {profit:<8} | {weight:<8} | {ratio:.2f}")


    items.sort(key=lambda x: x['ratio'], reverse=True)

    total_profit = 0.0
    selected_items = []

    for item in items:
        if capacity == 0:
            break
            
        if item['weight'] <= capacity:
            capacity -= item['weight']
            total_profit += item['profit']
            selected_items.append((item['id'], item['weight'], "100%"))
        else:

            fraction = capacity / item['weight']
            total_profit += item['profit'] * fraction
            selected_items.append((item['id'], capacity, f"{fraction*100:.1f}%"))
            capacity = 0


    print("\n--- Final Selection ---")
    print(f"{'Item ID':<8} | {'Weight Taken':<12} | {'Portion'}")
    for id, w, p in selected_items:
        print(f"{id:<8} | {w:<12.2f} | {p}")

    print("-" * 45)
    print(f"Maximum Profit Achieved: {total_profit:.2f}")

if __name__ == "__main__":
    fractional_knapsack()