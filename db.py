import mysql.connector

cnx = mysql.connector.connect(user='root', password='Jayanth123',database = 'todo')

cur = cnx.cursor()

query = ("SELECT name,emailId FROM alpha")

cur.execute(query)

for(name , emailId) in cur:
    print("{}'s email Id is {}".format(name,emailId))

cur.close()
cnx.close()