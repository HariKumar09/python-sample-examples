
import sqlite3
conn = sqlite3.connect('hari.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE OverlayIcon4
(path, status)''')

 
# Larger example that inserts many records at a time
data = [('/home/harikumar/Desktop', 'syncing'),
('/home/harikumar/Desktop', 'syncerror'),
('/home/harikumar/Desktop', 'syncerror'),
('/home/harikumar/Desktop', 'syncdone'),
('/home/harikumar/Desktop', 'syncdone')
]
c.executemany('INSERT INTO OverlayIcon4 VALUES (?, ?)', data)

# # Insert a row of data
# c.execute("INSERT INTO OverlayIcon3 VALUES ('/home/harikumar/Desktop', 'syncing'),
# ('/home/harikumar/Desktop', 'syncerror'),
# ('/home/harikumar/Desktop', 'syncerror'),
# ('/home/harikumar/Desktop', 'syncdone'),
# ('/home/harikumar/Desktop', 'syncdone')")

conn.commit()

conn.close()
