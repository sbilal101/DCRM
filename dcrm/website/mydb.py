# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python
import mysql.connector

dataBase = mysql.connector.connect(
     host = 'localhost',
     user = 'root',
     passwd = 'Pass@1234',
)

# prepare a cursor object

cursorObject = dataBase.cursor()

#create database
cursorObject.execute(" CREATE DATABASE db_dcrm")

print("ALL DONE")