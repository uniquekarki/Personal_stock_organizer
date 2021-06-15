import sqlite3
con = sqlite3.connect('stock_database.db')

cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE current
               (
                   Symbol varchar(255),
                   Quantity int,
                   Price int,
                   Date date
               )''')

cur.execute('''CREATE TABLE history
               (
                   Symbol varchar(255),
                   Quantity int,
                   BuyPrice int,
                   BuyDate date,
                   SellPrice int,
                   SellDate date
               )''')

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()