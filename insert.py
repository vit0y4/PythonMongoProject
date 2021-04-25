from pymongo import MongoClient

client = MongoClient('localhost:27017')
db = client.TestDataCollection

def insert():
	try:
		id=input('Enter Id: ')
		name=input('Enter Name: ')
		age=input('Enter Age: ')
		country=input('Enter Country: ')
		db.TestDataDoc.insert_one(
		{
			"id": id,
			"name": name,
			"age": age,
			"country": country
		})
		print('Data Inserted!!')
	except ImportError:
		platform_specific_module = None
