from pymongo import MongoClient

client = MongoClient('localhost:27017')
db = client.TestDataCollection
def update():
	try:
		id=input('Enter Id to search: ')
		name=input('Enter Name to update: ')
		age=input('Enter Age to Update: ')
		country=input('Enter Country to update: ')
		db.TestDataDoc.update_one(
		{	"id": id},
		{
			"$set": {
				"name": name,
				"age": age,
				"country": country
				}
		})
		print('Data Updated!!')
	except ImportError:
		platform_specific_module = None
