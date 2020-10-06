'''
module for maintaining user's name
'''

try:
	import os
	import user_db as udb 
except:
	print('Required modules not installed\n')
	exit()

class User:

	#check if the user exists
	def check(name):

		file = open('user.txt','r')
		obj = file.read().split()
		if name in obj:
			return True #user exists
		return False #user doesn't exist

	#create a new user
	def new(name):

		file = open('user.txt', 'a')
		obj = name + '\n'
		file.write(obj)
		file.close()
		udb.User.insert(name) #insert name of user into database
		try:
			os.system(f'cmd /c "cd notes & mkdir {name}"') #create notes folder for user
			file = open('./to-do-list/{}.txt'.format(name), 'a') #create to-do list for user
			file.close()
		except:
			pass

	#delete a user
	def delete(name):

		file = open('user.txt', 'r')
		new_file = open('new.txt', 'a')
		obj = file.read().split()

		if User.check(name) == False:
			print('User not found\n')

		else:
			for i in obj:
				if i != name:
					new_file.write(i)
			new_file.close()
			file.close()
			os.remove('user.txt')
			os.rename('new.txt','user.txt')

			try:
				os.remove(f'./notes/{name}') #remove notes of user
				os.remove(f'./to-do-list/{name}.txt') #remove to-do list of user
			except:
				pass
			udb.User.remove(name) #remove user from database
			print('User removed successfully\n')

	#update a user's name
	def update(old_name, new_name):
		
		file = open('user.txt', 'r')
		new_file = open('new.txt', 'a')
		obj = file.read().split()

		if User.check(old_name) == False:
			print('User not found\n')

		else:
			for i in obj:
				if i == old_name:
					i = new_name
					new_file.write(i)
				else:
					new_file.write(i)
			new_file.close()
			file.close()
			os.remove('user.txt')
			os.rename('new.txt','user.txt')
			try:
				os.rename(f'./notes/{old_name}', f'./notes/{new_name}') #update the name of notes folder
				os.rename(f'./to-do-list/{old_name}.txt', f'./to-do-list/{new_file}.txt') #update the name of to-do list 
			except:
				pass
			udb.User.update(old_name, new_name) #update name in database
			print('User name changed successfully\n')

'''
made by Devansh Singh, 2020
GitHub: Devansh3712
'''