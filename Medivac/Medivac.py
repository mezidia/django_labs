import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Hogger",
  database="mydatabase"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS `MYDATABASE`.`CAR` (`ID` INT UNSIGNED NOT NULL AUTO_INCREMENT,`NAME` VARCHAR(45) NOT NULL,PRIMARY KEY (`ID`),UNIQUE INDEX `ID_UNIQUE` (`ID` ASC) VISIBLE)")

sql = "INSERT INTO `MYDATABASE`.`CAR` (`NAME`) VALUES (%s);"
val = ('Full Phylactery')
params = (val,)
mycursor.execute(sql, params)

mydb.commit()

print(mycursor.rowcount, "record inserted.")