###    database create and table create

import mysql.connector as mc
conn=mc.connect(host ='localhost' , user = 'root' , password = 'Aayush2211', database = "bikeprediction")

if(conn.is_connected()):
    print('connection established')
else:
    print('unable to connect')


# import sqlite3
# conn = sqlite3.connect('bikedata.db)


query_to_create_table = """
CREATE TABLE bike_details (
        brand varchar(50),
        Kms_Driven int,
        owner int,
        age int,
        power int,
        PREDICTION INT
        );
"""

cur = conn.cursor()
cur.execute(query_to_create_table)
print("database created")
cur.close()
conn.close()