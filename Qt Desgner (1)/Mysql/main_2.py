import mysql.connector
from mysql.connector import errorcode
try:
	db_connection = mysql.connector.connect(host='localhost', user='root', password='', database='bruno')
	print("Database connection made!")
except mysql.connector.Error as error:
	if error.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database doesn't exist")
	else:
		print(error)
else:
	db_connection.close()
 
from mysql.connector import (connection)
db_connection = connection.MySQLConnection(
     host='localhost',
     user= 'root',
     password='',
     database='kitton_info'
 )
print("conectado") 
db_connection.close()