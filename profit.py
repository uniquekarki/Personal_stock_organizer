import os
from menu import title

def one_stock(con,cur):
    title()
    sym = input("Enter the stock symbol or press 0 to exit: ")
    while True:
        if sym == '0':
            os.system('clear')
            break
        else:
            a = cur.execute("SELECT Quantity,Price FROM current WHERE Symbol='%s'" % sym).fetchone()
            if a:
                currentP = int(input(f"Enter the current value of {sym}: "))
                print(f"Profit per stock for {sym} ----> {currentP - a[1]}")
                print(f"Total profit for {sym} ----> {(currentP - a[1])*a[0]}\n")
            else:
                print("No such symbol found.\n")
        sym = input("Enter the stock symbol or press 0 to exit: ")

def all_stock(con,cur):
    # '''
    #     1. Press 0 to exit
    #     2. Current list = [a,b,c,d,e,...]
    #     3. loop:
    #             current list ko current price?
    #     4. Total profit as of today ----> Rs. xyz
    # '''
    title()
    curVal = []
    iniSym = cur.execute("SELECT Symbol FROM current").fetchall()
    iniSym_Price_quant = cur.execute("SELECT Symbol,Quantity,Price FROM current").fetchall()
    # print("The stocks you have are:\n")
    # iniPrice = cur.execute("SELECT Price FROM current").fetchall()
    # for i,sym in enumerate(iniSym):
    #     print(i+1,sym[0])
    for i,sym in enumerate(iniSym):
        temp = int(input(f"Enter the current price of {sym[0]}: "))
        curVal.append(temp)
    profits = []
    print("\nSYMBOL, QUANTITY, PRICE, CURRENT_VALUE, PROFIT")
    for i, (sym, quantity,price) in enumerate(iniSym_Price_quant):
        sp = (curVal[i] - price)*quantity
        profits.append(sp)
        print(sym, quantity, price, curVal[i], sp)
    print("The total profit is ----> Rs.",sum(profits))
    _ = input("Press enter to continue...")
    os.system('clear')