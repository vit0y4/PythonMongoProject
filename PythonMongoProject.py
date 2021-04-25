import insert 
import read 
import update 
import delete 

class Programa:
	def __init__(self):
		self.dato=1

	def menu(self):
		while self.dato:
			print('\nSelect: ')
			print('\n 1 to Insert ')
			print('\n 2 to Update ')
			print('\n 3 to Read ')
			print('\n 4 to Delete ')
			selection = input('\nChoose your option: ')
			if selection=='1':
				insert.insert()
			elif selection=='2':
				update.update()
			elif selection=='3':
				read.read()
			elif selection=='4':
				delete.delete()
			else:
				print('\n INVALID SELECTION \n')
persona1= Programa()
persona1.menu()

