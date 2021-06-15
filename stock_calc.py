import os
from menu import title

def calc_profit():
    n = None
    while (n != 0):
        title()
        print("Price calc")
        print("Choose from the following:")
        print("0. Exit")
        print("1. For Calculating buy amount")
        print("2. For Calculating sell amount")
        n = int(input("Enter the number of choice: "))
        print("\n")
        os.system('clear')
        if n ==1:
            quantity = int(input("Enter the quantity of shares: "))
            purchase = int(input("Enter the purchase price of your share: "))
            print("Your total purchase amount is ----> Rs.",purchase,"\n")
        elif n ==2:
            quantity = int(input("Enter the quantity of shares: "))
            purchase = int(input("Enter the purchase price of your share: "))
            sell = int(input("Enter the selling price of your share: "))
            print("Your profit/loss is ----> Rs.", quantity*(sell - purchase),"\n")