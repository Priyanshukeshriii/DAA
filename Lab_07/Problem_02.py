def coin_exchange():
    
    denominations = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    
    try:
       
        amount = int(input("Enter the amount you want to exchange: "))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return

    original_amount = amount
    change_result = {}

   
    for coin in denominations:
        if amount >= coin:
            count = amount // coin  
            amount = amount % coin   
            change_result[coin] = count

    
    print(f"\n--- Exchange for {original_amount} ---")
    if not change_result:
        print("No change needed.")
    else:
        print(f"{'Denomination':<12} | {'Quantity':<8}")
        print("-" * 25)
        total_coins = 0
        for coin, count in change_result.items():
            print(f"{coin:<12} | {count:<8}")
            total_coins += count
        
        print("-" * 25)
        print(f"Total coins/notes used: {total_coins}")

if __name__ == "__main__":
    coin_exchange()