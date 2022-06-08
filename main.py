from stock_calc import calc_profit
from stock_list import insert, remove
from profit import one_stock, all_stock
from display import disp_current,disp_history
from menu import title
import os
import sqlite3

if __name__ == '__main__':
    os.system('clear')
    n = None
    con = sqlite3.connect('stock_database.db')
    cur = con.cursor()
    while(n != 0):
        title()
        print("Choose from the following:")
        print("0. Exit")
        print("1. Stock Calculator")
        print("2. Add a stock to your list")
        print("3. Remove the stock from your list")
        print("4. Calculate your profit for a particular stock")
        print("5. Calculate your total profit for today")
        print("6. Show Current")
        print("7. Show History")
        n = int(input("Enter the number of choice: "))
        print("\n")
        os.system('clear')
        if n == 1:
            calc_profit()
        elif n == 2:
            insert(con,cur)
        elif n == 3 :
            remove(con,cur)
        elif n == 4:
            one_stock(con,cur)
        elif n ==5:
            all_stock(con,cur)
        elif n == 6:
            disp_current(con,cur)
        elif n == 7:
            disp_history(con,cur)
    con.close()