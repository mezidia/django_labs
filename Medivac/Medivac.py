import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Hogger",
  database="mydatabase"
)

mycursor = mydb.cursor()

# sql = "INSERT INTO `MYDATABASE`.`CAR` (`NAME`) VALUES (%s);"
# val = ('Full Phylactery')

sql = "INSERT INTO `MYDATABASE`.`ROUTES`(`NAME`,`PLACE_FROM`,`PLACE_TO`,`PRICE`,`TIME`,`CAR`) VALUES (%s,%s,%s,%s,%s,%s);"
id = mycursor.execute("SELECT ID FROM MYDATABASE.CAR WHERE ID = 2")
rows = mycursor.fetchone()
val = ('FOURTH GOLD EXPRESS ROUTE','HANAMURA TEMPLE','BRAXIS HOLDOUT',400,'2021-09-21 13:25:00',rows[0])
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")