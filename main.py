from profit_calc import calc_profit

if __name__ == '__main__':
    n = None
    print("\n")
    print("----------------WELCOME TO YOUR PERSONAL STOCK ASSISTANT----------------")
    print("\n")
    while(n != 0):
        print("Choose from the following:")
        print("0. Exit")
        print("1. Stock Calculator")
        print("2. Add a stock to your list")
        print("3. Remove the stock from your list")
        print("4. Calculate your profit for a particular stock")
        print("5. Calculate your total profit for today")
        print("6. Show history")
        n = int(input("Enter the number of choice: "))
        print("\n")
        if n == 1:
            calc_profit()