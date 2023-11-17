import mysql.connector
import time

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='SidharthPriya'
)
print("Database configuration in progress...")
time.sleep(3)
cursor = db.cursor()
cursor.execute("CREATE DATABASE SEARCH_ENGINE")
cursor.execute("USE SEARCH_ENGINE")
cursor.execute("CREATE TABLE search_results(id INT AUTO_INCREMENT PRIMARY KEY, keyword VARCHAR(255), result_text TEXT)")

print("Server Configured Successfully..")
