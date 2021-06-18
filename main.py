from stock_calc import calc_profit
from stock_list import insert, remove
from profit import one_stock, all_stock
from menu import title
import os
import sqlite3

if __name__ == '__main__':
    os.system('clear')
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
        print("7. Show Current")
        n = int(input("Enter the number of choice: "))
        print("\n")
        os.system('clear')
        if n == 1:
            calc_profit()
        elif n == 2:
            con = sqlite3.connect('stock_database.db')
            cur = con.cursor()
            insert(con,cur)
            con.close()
        elif n == 3 :
            con = sqlite3.connect('stock_database.db')
            cur = con.cursor()
            remove(con,cur)
            con.close()
        elif n == 4:
            con = sqlite3.connect('stock_database.db')
            cur = con.cursor()
            one_stock(con,cur)
            con.close()
        elif n ==5:
            con = sqlite3.connect('stock_database.db')
            cur = con.cursor()
            all_stock(con,cur)
            con.close()