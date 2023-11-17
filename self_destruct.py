import mysql.connector
import time

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456789'
)
print("DANGER!!! By proceeding with this script, your database will be completely deleted and you can't retrieve the contents back! DANGER!!!")
confrm = input("Do you wish to continue? (Y/N): ")
if confrm == 'y' or confrm == 'Y':
    cursor = db.cursor()
    print("DELETING DATABASE...")
    time.sleep(3)
    cursor.execute("DROP DATABASE SEARCH_ENGINE")
    print("Self Destruction Successful")
else:
    print("Operation Aborted!!")
