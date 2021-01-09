'''
module for maintaining user's name
and other settings
'''

import os
import packages.user_db as udb 
import shutil

class User:

	#check if the user exists
	def check(name, password):

		if udb.User.check(name, password) == True:
			return True
		
		elif udb.User.check(name, password) == "wrong pass":
			return "Wrong Password"

		return False

	#create a new user
	def new(name, password):

		if udb.User.insert(name, password) == False: #check if the same name exists in database
			return False
		
		else: #if it is a unique username

			try:
				os.system(f'cmd /c "cd notes & mkdir {name}"') #create notes folder for user
				file = open('./to-do-list/{}.txt'.format(name), 'a') #create to-do list for user
				file.close()
			except:
				pass
			return True

	#delete a user
	def delete(name, password):

		if User.check(name, password) == False:
			print('User not found\n')

		elif User.check(name, password) == "Wrong Password":
			print("Wrong Password\n")

		else:

			try:
				shutil.rmtree(f'./notes/{name}') #remove notes of user
				os.remove(f'./to-do-list/{name}.txt') #remove to-do list of user
			except:
				pass
			udb.User.remove(name) #remove user from database
			print('User removed successfully\nTerminating Program\n')
			exit()

	#update a user's name
	def update(old_name, new_name, password):

		if User.check(old_name, password) == False:
			print('User not found\n')

		elif User.check(old_name, password) == "Wrong Password":
			print("Wrong Password\n")

		else:
			
			if udb.User.update(old_name, new_name) == False: #check whether same name exists in database
				return False

			else: #if it is a unique username
				try:
					os.rename(f'./notes/{old_name}', f'./notes/{new_name}') #update the name of notes folder
					os.rename(f'./to-do-list/{old_name}.txt', f'./to-do-list/{new_name}.txt') #update the name of to-do list 
				except:
					pass
				return True

	def change_pass(name, old_password, new_password):

		if User.check(name, old_password) == False:
			print('User not found\n')

		elif User.check(name, old_password) == "Wrong Password":
			print("Wrong Password\n")

		else:
			udb.User.change_password(name, new_password) #Change the User's password in database
			print('Password changed succesfully\n')

'''
made by Devansh Singh, 2020
GitHub: Devansh3712
'''