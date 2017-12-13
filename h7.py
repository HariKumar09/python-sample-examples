from peewee import *
from playhouse.pool import PooledSqliteExtDatabase
import sqlite3
from sqlite3 import Error
conn = sqlite3.connect('harikumar1.db')


c = conn.cursor()

c.execute('''CREATE TABLE OverlayIcon5
(name, path, status)''')

c.execute("INSERT INTO OverlayIcon5 VALUES ('name1', '/home/harikumar/Desktop', 'syncing')")


# Larger example that inserts many records at a time
purchases = [('name2', '/home/harikumar/Desktop', 'syncerror'),
('name3', '/home/harikumar/Desktop', 'syncerror'),
('name4', '/home/harikumar/Desktop', 'syncdone'),
('name5', '/home/harikumar/Desktop', 'syncdone'),
]

c.executemany('INSERT INTO OverlayIcon5 VALUES (?, ?, ?)', purchases)

conn.commit()

conn.close()



db = PooledSqliteExtDatabase('harikumar1.db')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    path = CharField()
    status = CharField()


User.create_table(True)
# User.insert(path="/home/harikumar/Desktop",
#     status="syncerror").execute()

# k = User.get(User.status == "syncerror").path
# print k


for path in User.select().where(User.status == 'syncerror'):
    print path.path
