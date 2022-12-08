import mysql.connector

def main():
	try:
		mydb = mysql.connector.connect(
			host = "localhost",
			user = "josh",
			password = "password",
			database = "biblioteca"
		)

		print(mydb)

		cursor = mydb.cursor()

		cursor.execute("SELECT Titolo FROM libri;")

		print(cursor)

		for x in cursor:
			print(x)


	except Exception as e:
		print(e)

	finally:
		print("EOP")

if __name__ == "__main__":
    main()
