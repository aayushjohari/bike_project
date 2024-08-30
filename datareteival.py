import mysql.connector as mc
conn=mc.connect(host ='localhost' , user = 'root' , password = 'Aayush2211', database = "bikeprediction")

cur=conn.cursor()
query="select*from bikedetails"

cur.execute(query)
for record in cur.fetchall():
    print(record)

cur.close()
cur.close()