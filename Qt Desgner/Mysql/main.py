import mysql.connector
from mysql.connector import Error
import pandas as pd

def create_server_connector(local, usuario, senha):
    connection = None
    try:
        connection=mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = ""
        )
        print("Mysql database conctado com sucesso!")
    except Error as err:
        print(f"Error:'{err}'")
        return connection
    
    
    
    def create_database(connection, query):
        cursor= connection.cursor()

            
        