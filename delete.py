from pymongo import MongoClient

client = MongoClient('localhost:27017')
db = client.TestDataCollection

def delete():
	try:
		id=input('Enter Id to delete: ')
		db.TestDataDoc.delete_many({"id": id})
		print('\n Data deleted!! \n')
	except ImportError:
		platform_specific_module = None

