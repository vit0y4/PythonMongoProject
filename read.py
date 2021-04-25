from pymongo import MongoClient

client = MongoClient('localhost:27017')
db = client.TestDataCollection

def read():
	try:
		datacol = db.TestDataDoc.find()
		print('\n All data charged \n')
		for data in datacol:
			print(data)
	except ImportError:
		platform_specific_module = None
