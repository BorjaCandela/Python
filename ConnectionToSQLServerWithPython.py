###########################################
###########################################
###                                     ###
###        Borja Candela Salinas        ###
###             Free to use             ###
###                                     ###
###########################################
###########################################

# I think i dont forget an import 
import pyodbc
import os

# Use these variables instead hardcoding 
server = 'IPAddr'
port = '1433'
database = 'DataBaseName' 
username = 'user' 
password = 'pass' 
driverLnx = '{FreeTDS}'
driverWin = '{SQL Server}'


# LINUX CLIENT
#cnxn = pyodbc.connect('DRIVER={FreeTDS};'
# WINDOWS CLIENT
#cnxn = pyodbc.connect('DRIVER={SQL Server};'
			'SERVER=IPAddr;'
			'PORT=1433;'
			'DATABASE=DataBaseName;'
			'UID=user;'
			'PWD=pass') 
            

cursor = cnxn.cursor()

cursor.execute("SELECT * FROM [Database].[dbo].[Table]") # NOTE: This SQL syntax is for SQL Server
for row in cursor.fetchall(): 
    print row
cursor.execute("DELETE FROM [Database].[dbo].[Table]") # NOTE: This SQL syntax is for SQL Server

cnxn.commit() # Without this line, the changes are nor applied in the server

