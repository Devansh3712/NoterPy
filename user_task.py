'''
module for managing the queue of tasks
of a user,  user file saved in 
to-do-list folder
'''

import os

class Task:

	#check whether the user has task list
	def check(name):

		try:
			file = open('./to-do-list/{}.txt'.format(name), 'r')

		except FileNotFoundError: #if user has no task list, create one
			file = open('./to-do-list/{}.txt'.format(name), 'a')

		obj = file.read()

		if len(obj)>0:
			return True

		return False

	#show the list of tasks
	def show(name):

		if Task.check(name) == False: #if task list is empty
			print('No tasks in the to-do list!\n')

		else:
			file = open('./to-do-list/{}.txt'.format(name), 'r')
			obj = file.read().splitlines()
			for i in range (len(obj)):
				print('---> ' + str(i+1) + '. ' + obj[i] + '\n') #prints tasks one by one

	#add a task to the list of tasks
	def add(name, task):

		file = open('./to-do-list/{}.txt'.format(name), 'a')
		file.write(task+'\n')
		file.close()
		print('Task was successfully added\n')

	#remove a task from the list of tasks
	def remove(name, number):

		file = open('./to-do-list/{}.txt'.format(name), 'a')
		new_file = open('./to-do-list/new.txt', 'a')
		obj = file.read().splitlines()

		if number > len(obj): #if the given number of task is not valid
			print('Task not found\n')

		else:
			for i in range (len(obj)):
				if i != number - 1:
					new_file.write(obj[i]+'\n')
			file.close()
			new_file.close()
			os.remove('./to-do-list/{}.txt'.format(name))
			os.rename('./to-do-list/new.txt', './to-do-list/{}.txt'.format(name))
			print('Task was successfully removed\n')

	#update a task in the list of tasks
	def update(name, number, new_task):

		file = open('./to-do-list/{}.txt'.format(name), 'a')
		new_file = open('./to-do-list/new.txt', 'a')
		obj = file.read().splitlines()

		if number > len(obj): #if the given number of task is not valid
			print('Task not found\n')

		else:
			for i in range (len(obj)):
				if i == number - 1:
					obj[i] = new_task
					new_file.write(obj[i]+'\n')
				else:
					new_file.write(obj[i]+'\n')
			file.close()
			new_file.close()
			os.remove('./to-do-list/{}.txt'.format(name))
			os.rename('./to-do-list/new.txt', './to-do-list/{}.txt'.format(name))
			print('Task was successfully updated\n')

'''
made by Devansh Singh, 2020
GitHub: Devansh3712
'''