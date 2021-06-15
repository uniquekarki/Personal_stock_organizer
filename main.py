from stock_calc import calc_profit
from menu import title
import os

if __name__ == '__main__':
    n = None
    while(n != 0):
        title()
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
        os.system('clear')
        if n == 1:
            calc_profit()