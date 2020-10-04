'''
module for maintaining user's name
'''

import os

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

	#delete a user
	def delete(name):
		file = open('user.txt', 'r')
		new_file = open('new.txt', 'a')
		obj = file.read().split()
		for i in obj:
			if i != name:
				new_file.write(i)
		new_file.close()
		file.close()
		os.remove('user.txt')
		os.rename('new.txt','user.txt')

	#update a user's name
	def update(old_name, new_name):
		file = open('user.txt', 'r')
		new_file = open('new.txt', 'a')
		obj = file.read().split()
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