import pandas as pd
import os

def insert():
    database_current = 'current.csv'
    
    if not os.path.isfile(database_current):
        df = pd.DataFrame(columns=['Symbol','Quantity','Price'])
        print('Creating Database For Your Stocks')
    else:
        df = pd.read_csv(database_current)
    
    data = {}
    while True:
        sym = input("Enter the stock symbol or press 0 to exit: ")
        if sym == '0':
            break
        else:
            data['Symbol'] = sym
            data['Quantity'] = int(input('Enter the quantity of the stock: '))
            data['Price'] = int(input('Enter the purchase price of the stock: '))
            df = df.append(data, ignore_index = True)
            df.to_csv(database_current, index = False)

def remove():
    database_history = 'history.csv'

        