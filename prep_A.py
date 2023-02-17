import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE Animali")


import mysql.connector

mydb = mysql.connector.connect(
 host="localhost",
  user="root",
  password="",
  database="Animali"
)


mycursor = mydb.cursor()


mycursor.execute("CREATE TABLE Mammiferi (Id INT AUTO_INCREMENT PRIMARY KEY, Nome_Proprio VARCHAR(200) ,Razza VARCHAR(200) ,Peso INT ,Eta INT)")

