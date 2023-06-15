# # Create database
import mysql.connector
# importing databse
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase")