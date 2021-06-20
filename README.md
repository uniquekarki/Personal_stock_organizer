# Personal Stock Organizer
This is my personal project to organize my stocks. It allows you to store the details of the stocks you own and also records the stocks that you have sold. This program also allows you to calculate the profit for your individual stocks and total profit from all stocks.

## Requirements:
1. Install sqlite:
```
sudo pacman -S sqlite3
```
2. Install prettytable library:
```
pip install prettytable
```
## How to run:
1. First run _db_init.py_ file to create a database _"stock_database.db"_
2. Run _main.py_ file to use the system.

## Notes:
This program was written in linux operating system so there are a few commands written for this OS specifically.<br>


In places where screen clear command is written use:
```
os.system('cls')
```
instead of:
```
os.system('clear')
```
for Windows operating system.