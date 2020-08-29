import mysql.connector
from mysql.connector.errors import Error
Db_name="projectdb"

try:
	mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="",
	database=Db_name
	)
except mysql.connector.Error as e:
	if e.errno==1049:
		mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd=""
		)
		mycursor = mydb.cursor()
		mycursor.execute("CREATE DATABASE {}".format(Db_name))
		mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="",
		database=Db_name
		)
		mycursor=mydb.cursor()
		#mycursor.execute("ALTER DATABASE {} CHARACTER SET 'utf8' COLLATE 'utf8_general_ci'".format(Db_name))
		f=open("projectdb.sql","r")
		for line in f:
			print("printed"+line)
			mycursor.execute(line)
		#mycursor.execute(db_sql2,multi=True)

	else:
		raise e





