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

def remove(con,cur):
    title()
    sym = input("Enter the stock symbol to delete or press 0 to exit: ")
    while True:
        if sym == '0':
            os.system('clear')
            break
        else:
            del_list = []

            sellP = int(input("Enter the selling price of the stock: "))
            date_entry = input('Enter selling date in YYYY-MM-DD format: ')
            year, month, day = map(int, date_entry.split('-'))
            Date = datetime.date(year, month, day)

            a = cur.execute("SELECT * FROM current WHERE Symbol='%s'" % sym)
            del_list = a.fetchone()
            if del_list:
                cur.execute("INSERT INTO history VALUES (?,?,?,?,?,?)", (del_list[0], del_list[1], del_list[2], del_list[3], sellP, Date))
                cur.execute("DELETE FROM current WHERE Symbol='%s'" % sym)

                con.commit()
                print("Stock successfully deleted.\n")
            else:
                print("No such symbol found.\n")
            sym = input("Enter the stock symbol to delete or press 0 to exit: ")
    os.system('clear')