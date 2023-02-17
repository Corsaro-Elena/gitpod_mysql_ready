
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Mammiferi (Nome_Proprio ,Razza  ,Peso ,Eta ) VALUES (%s, %s, %s, %s)"
val = [
  ('Peter', 'scimmia', 9 , 10),
  ('Amy', 'cane', 10 , 11),
  ('Hannah', 'delfino', 2 , 9),
  ('Michael', 'panda', 200 , 3),
  ('Sandy', 'pitone', 6 , 4)
]

mycursor.executemany(sql, val)

mydb.commit()

