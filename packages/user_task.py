'''
module for managing the queue of tasks
of a user (./logs)
'''

try:

	import os
	import onetimepad as ot
	import pyttsx3
	import speech_recognition as sr
	import packages.user_db as udb

except:

	print('modules for speech recognition and tts not setup\n')
	exit()

class Task:

	#check whether the user has task list
	def check(name):

		try:

			file 	= open('./to-do-list/{}.txt'.format(name), 'r')
			obj 	= file.read()

			if (len(obj) > 0):
				return True

			return False

		except FileNotFoundError: #if user has no task list, create one
			file = open('./to-do-list/{}.txt'.format(name), 'a')

	#show the list of tasks
	def show(name):

		if (Task.check(name) == False): #if task list is empty
			print('No tasks in the to-do list!\n')

		else:

			file 		= open('./to-do-list/{}.txt'.format(name), 'r')
			obj 		= file.read().splitlines()
			password 	= udb.User.crypt_key(name)

			for i in range (len(obj)):

				obj[i] = ot.decrypt(obj[i], password) #decrypt the contents of task
				print('---> ' + str(i+1) + '. ' + obj[i] + '\n') #prints tasks one by one

	#add a task to the list of tasks
	def add(name, task):

		file 		= open('./to-do-list/{}.txt'.format(name), 'a')
		password 	= udb.User.crypt_key(name)
		task 		= ot.encrypt(task, password) #encrypt the content of task
		file.write(task + '\n')
		file.close()

		udb.Logs.add_task(name) #update logs of user
		print('Task was successfully added\n')

	#remove a task from the list of tasks
	def remove(name, number):

		file 		= open('./to-do-list/{}.txt'.format(name), 'r')
		new_file 	= open('./to-do-list/new.txt', 'a')
		obj 		= file.read().splitlines()

		if (int(number) > len(obj)): #if the given number of task is not valid
			print('Task not found\n')

		else:

			for i in range (len(obj)):

				if (i != int(number) - 1):
					new_file.write(obj[i] + '\n')

				elif (i == int(number) - 1):
					pass

			file.close()
			new_file.close()
			os.remove('./to-do-list/{}.txt'.format(name))
			os.rename('./to-do-list/new.txt', './to-do-list/{}.txt'.format(name))

			udb.Logs.delete_task(name, number) #update logs of user
			print('Task was successfully removed\n')

	#update a task in the list of tasks
	def update(name, number, new_task):

		file 		= open('./to-do-list/{}.txt'.format(name), 'r')
		new_file 	= open('./to-do-list/new.txt', 'a')
		obj 		= file.read().splitlines()

		if (int(number) > len(obj)): #if the given number of task is not valid
			print('Task not found\n')

		else:

			for i in range (len(obj)):

				if (i == int(number) - 1):

					password 	= udb.User.crypt_key(name)
					new_task 	= ot.encrypt(new_task, password) #encrypt the contents of task
					obj[i] 		= new_task
					new_file.write(obj[i] + '\n')

				else:
					new_file.write(obj[i] + '\n')

			file.close()
			new_file.close()
			os.remove('./to-do-list/{}.txt'.format(name))
			os.rename('./to-do-list/new.txt', './to-do-list/{}.txt'.format(name))

			udb.Logs.update_task(name, number) #update logs for user
			print('Task was successfully updated\n')

class Speak:	

	#convert text to speech each task in to-do list
	def taskToSpeech(name):

		#setup python text-to-speech
		engine = pyttsx3.init()
		engine.setProperty('rate', 150)

		if (Task.check(name) == False): #if task list is empty

			engine.say('No tasks in the to-do list!')
			engine.runAndWait()

		else:

			file 		= open('./to-do-list/{}.txt'.format(name), 'r')
			obj 		= file.read().splitlines()
			password 	= udb.User.crypt_key(name)

			for i in obj:

				i = ot.decrypt(i, password) #decrypt the task
				engine.say(i)
				engine.runAndWait()

class Speech:

	#add task by speaking
	def speechToTask():

		r = sr.Recognizer()

		with sr.Microphone() as source:

			try:

				audio 		= r.record(source, duration=10)
				converted 	= r.recognize_google(audio)
				converted 	= converted.lower()
				return converted

			except:
				return False

'''
NoterPy
Devansh Singh, 2020
'''