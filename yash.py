import sqlite3
from sqlite3 import Error
conn = sqlite3.connect('stock.db')

c = conn.cursor()
# Create table
# c.execute('''CREATE TABLE Stocks2
#               (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
c.execute("INSERT INTO Stocks2 VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

symbol = 'RHAT'
c.execute("SELECT * FROM Stocks2 WHERE symbol = '%s'" % symbol)

# Do this instead
t = ('RHAT',)
c.execute('SELECT * FROM Stocks2 WHERE symbol=?', t)
# print c.fetchone()

# Larger example that inserts many records at a time
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
             ('2006-09-09', 'SELL', 'MSFT', 900, 54.00)
            ]
c.executemany('INSERT INTO Stocks2 VALUES (?,?,?,?,?)', purchases)

c.execute("ALTER TABLE Stocks2 ADD COLUMN name text")

conn.commit()

conn.close()
