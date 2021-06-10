from profit_calc import calc_profit

if __name__ == '__main__':
    quantity = int(input("Enter the quantity of shares: "))
    purchase = int(input("Enter the purchase price of your share: "))
    sell = int(input("Enter the selling price of your share: "))
    print("Your profit/loss is: Rs.", calc_profit(quantity,purchase,sell))