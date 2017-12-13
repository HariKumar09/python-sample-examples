import sqlite3

sqlite_file = 'my_first_db.sqlite'    # name of the sqlite database file
table_name1 = 'my_table_1'	# name of the table to be created
table_name2 = 'my_table_2'	# name of the table to be created
new_field = 'my_1st_column' # name of the column
field_type = 'INTEGER'  # column data type

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# Creating a new SQLite table with 1 column
c.execute('CREATE TABLE Coffees
  (id INTEGER PRIMARY KEY,
   coffee_name TEXT NOT NULL,
   price REAL NOT NULL)')

# Creating a second table with 1 column and set it as PRIMARY KEY
# note that PRIMARY KEY column must consist of unique values!
c.execute('INSERT INTO Coffees VALUES (null, 'Colombian', 7.99)')

data = [(INSERT INTO coffees VALUES (null, 'French_Roast', 8.99);
INSERT INTO coffees VALUES (null, 'Espresso', 9.99);
INSERT INTO coffees VALUES (null, 'Colombian_Decaf', 8.99);
INSERT INTO coffees VALUES (null, 'French_Roast_Decaf', 9.99);
]

c.executemany('INSERT INTO Coffees VALUES (?, ?)', data)
# Committing changes and closing the connection to the database file
conn.commit()
conn.close()
