import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()   

DB_HOST = os.getenv('DB_HOST') 
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_DATABASE = os.getenv('DB_DATABASE')

db_config = {
    'host': DB_HOST,
    'user': DB_USER,
    'password': DB_PASSWORD,
    'database': DB_DATABASE
}

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

fetch_responses_query = '''
    SELECT * FROM response;
'''
cursor.execute(fetch_responses_query) 

responses = cursor.fetchall()  

cursor.close()
conn.close()

def fetch_responses():
    return responses