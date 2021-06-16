import os
import datetime
from menu import title

def insert(con,cur):
    
    while True:
        title()
        sym = input("Enter the stock symbol or press 0 to exit: ")
        if sym == '0':
            os.system('clear')
            break
        else:
            Quantity = int(input('Enter the quantity of the stock: '))
            Price = int(input('Enter the purchase price of the stock: '))
            date_entry = input('Enter purchase date in YYYY-MM-DD format: ')
            year, month, day = map(int, date_entry.split('-'))
            Date = datetime.date(year, month, day)
            cur.execute("INSERT INTO current VALUES (?,?,?,?)", (sym, Quantity, Price, Date))
            con.commit()
            os.system('clear')

# def remove():
#     database_history = 'history.csv'

        