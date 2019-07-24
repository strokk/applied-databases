# Guilherme Paes - Python program for project

#importing necessary libraries
import pymysql
import pymongo

#connecting python with mysql via pymysql (you might need to change the password)
conn = pymysql.connect(host="localhost", user="root", password="100956", database="world", cursorclass=pymysql.cursors.DictCursor)

#connecting python with mongo via pymongo
myclient = pymongo.MongoClient()

#main function
def main():

	display_menu()

	while True:
		choice = input("Enter choice: ")
		if (choice == "1"):
			get_cities()
			print()
			display_menu()
		elif (choice == "2"):
			city_pop()
			print()
			display_menu()
		elif (choice == "3"):
			add_city()
			print()
			display_menu()
		elif (choice == "4"):
			find_car()
			print()
			display_menu()
		elif (choice == "5"):
			add_car()
			display_menu()
		elif (choice == "6"):
			country_name()
			print()
			display_menu()
		elif (choice == "7"):
			country_pop()
			print()
			display_menu()
		elif (choice == "x"):
			break;
		else:
			display_menu()
			

# ==== QUESTION 01 ====			
#function to show cities
def get_cities():
    sql = "SELECT * FROM city limit 15"

    with conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        subjects = cursor.fetchall()
        for s in subjects:
            print(s["Name"], "|", s["CountryCode"], "|", s["District"])


# ==== QUESTION 02 ====	
#function for city by population
def city_pop():
	
	print("Cities by Population")
	print("-" * 20)

	inpt = input("Enter >, < or =: ")
	popul = int(input("Enter Population: "))
	
	#if statements to make action depending on what user chooses
	if (inpt == ">"):
		query = "SELECT * from city WHERE Population > %s"
		
		with conn:
			cursor = conn.cursor()
			cursor.execute (query, popul)
			subjects = cursor.fetchall()
			
			for s in subjects:
				print(s["Name"], "|", s["CountryCode"], "|", s["District"], "|", s["Population"])
	elif (inpt == "<"):
		query2 = "SELECT * from city WHERE Population < %s"
		
		with conn:
			cursor = conn.cursor()
			cursor.execute (query2, popul)
			subjects = cursor.fetchall()
			
			for s in subjects:
				print(s["Name"], "|", s["CountryCode"], "|", s["District"], "|", s["Population"])
	elif (inpt == "="):
		query3 = "SELECT * from city WHERE Population = %s"
		
		with conn:
			cursor = conn.cursor()
			cursor.execute (query3, popul)
			subjects = cursor.fetchall()
			
			for s in subjects:
				print(s["Name"], "|", s["CountryCode"], "|", s["District"], "|", s["Population"])
	else:
		display_menu()


# ==== QUESTION 03 ====		
#function to add a new city
def add_city():
    ins = "INSERT INTO city (Name, CountryCode, District, Population) VALUES (%s, %s, %s, %s)"

    print("Add new city")
    print("-" * 12)
    Name = input("Enter city name: ")
    CountryCode = input("Country Code: ")
    District = input("District: ")
    Population = int(input("Population: "))

    try:
        with conn:
	        cursor = conn.cursor()
	        cursor.execute (ins, (Name, CountryCode, District, Population))
	        conn.commit()
	#creating exceptions for error messages
    except pymysql.err.IntegrityError as e:
        print("***ERROR***: CountryCode ", CountryCode, "does not exist")
    except Exception as e:
        print("Error: ", e)


# ==== QUESTION 04 ====	
#Function to show cars by engine size
def find_car():
	print("Show cars by Engine Size")
	print("-" * 24)
	
	engine = float(input("Engine Size: "))
	query = {"car.engineSize":engine}

	mydb = myclient["project"]
	docs = mydb["docs"]
	cars = docs.find(query)
	
	#printing the cars by engine size
	for c in cars:
		print(c["_id"], "|", c["car"]["reg"], "|", c["car"]["engineSize"], "|", c["addresses"])
				


# ==== QUESTION 05 ====	
#function to add a new car to mongo collection
def add_car():
	print("Add new car")
	print("-" * 16)
	
	ids = int(input("_ids: "))
	reg = input("reg: ")
	eng = float(input("Engine Size: "))
	ins = {"_id":ids, "car":{"reg":reg, "engineSize": eng}}
	mydb = myclient["project"]
	docs = mydb["docs"]
	car = docs.insert(ins)
	
	#printing the newly added doccument
	query = {"_id":ids, "car.reg":reg, "car.engineSize":eng}
	show = docs.find(query)
	for i in show:
		print(i["_id"], "|", i["car"]["reg"], "|", i["car"]["engineSize"])


# ==== QUESTION 06 ====
#function to show country inputed by user
def country_name():
	
	query = "SELECT * from country WHERE Name LIKE %s"

	Country = input("Enter country name: ")
	
	with conn:
		cursor = conn.cursor()
		cursor.execute (query, ("%"+Country+"%"))
		subjects = cursor.fetchall()
		
		for s in subjects:
			print(s["Name"], "|", s["Continent"], "|", s["Population"], "|", s["HeadOfState"])
		
		
# ==== QUESTION 07 ====			
#function to show for country by population
def country_pop():
	
	print("Countries by Population")
	print("-" * 23)
	inpt = input("Enter >, < or =: ")
	popul = int(input("Enter Population: "))
	
	#if statements to make action depending on what user chooses
	if (inpt == ">"):
		query = "SELECT * from country WHERE Population > %s"
		
		with conn:
			cursor = conn.cursor()
			cursor.execute (query, popul)
			subjects = cursor.fetchall()
			
			for s in subjects:
				print(s["Code"], "|", s["Name"], "|", s["Continent"], "|", s["Population"])
	elif (inpt == "<"):
		query2 = "SELECT * from country WHERE Population < %s"
		
		with conn:
			cursor = conn.cursor()
			cursor.execute (query2, popul)
			subjects = cursor.fetchall()
			
			for s in subjects:
				print(s["Code"], "|", s["Name"], "|", s["Continent"], "|", s["Population"])
	elif (inpt == "="):
		query3 = "SELECT * from country WHERE Population = %s"
		
		with conn:
			cursor = conn.cursor()
			cursor.execute (query3, popul)
			subjects = cursor.fetchall()
			
			for s in subjects:
				print(s["Code"], "|", s["Name"], "|", s["Continent"], "|", s["Population"])
	else:
		display_menu()


# =====================

#function to display the main menu
def display_menu():
    print("World DB")
    print("-" * 8)
    print("")
    print("MENU")
    print("=" * 4)
    print("1 - View 15 Cities")
    print("2 - View Cities by population")
    print("3 - Add New City")
    print("4 - Find Car by Engine Size")
    print("5 - Add New Car")
    print("6 - View Countries by name")
    print("7 - View Countries by population")
    print("x - Exit application")

if __name__ == "__main__":
	# execute only if run as a script
	main()
