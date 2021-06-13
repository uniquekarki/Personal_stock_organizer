def calc_profit():
    n = None
    while (n != 0):
        print("Choose from the following:")
        print("0. Exit")
        print("1. For Calculating buy amount")
        print("2. For Calculating sell amount")
        n = int(input("Enter the number of choice: "))
        print("\n")
        if n ==2:
            quantity = int(input("Enter the quantity of shares: "))
            purchase = int(input("Enter the purchase price of your share: "))
            sell = int(input("Enter the selling price of your share: "))
            print("Your profit/loss is ----> Rs.", quantity*(sell - purchase),"\n")
    return None