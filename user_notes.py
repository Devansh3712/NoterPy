'''
module for maintaining notes of
a user, saved in directory notes
'''

try:
	import os
	import pyttsx3
	import speech_recognition as sr
except:
	print('Required modules not installed\n')
	exit()

class Notes:

	#check whether a folder of notes for a user exists
	def checkFolder(name):
		return os.path.isdir('./notes/{}'.format(name))


	#show the list of notes of user
	def showList(name):

		#if there is no folder, create one
		if Notes.checkFolder(name) == False:
			os.system(f'cmd /c "cd notes & mkdir {name}"')
			print('You have no notes!\n')

		#if folder is empty
		elif os.listdir('./notes/{}'.format(name)) == []:
			print('You have no notes!\n')

		else:
			obj = os.listdir('./notes/{}'.format(name))
			for i in range (len(obj)):
				print('---> ' + str(i+1) + " " + obj[i][:-3])

	#show the contents of a note
	def show(name, name_of_note):

		#if there is no folder, create one
		if os.path.isfile('./notes/{}/{}.txt'.format(name, name_of_note)) == False:
			print('Note not found\n')

		#if folder is empty
		elif os.listdir('./notes/{}'.format(name)) == []:
			print('You have no notes!\n')

		else:
			file = open('./notes/{}/{}.txt'.format(name, name_of_note), 'r')
			print(file.read())

	#add a new note
	def add(name, name_of_note, content):

		#if there is no folder, create one
		if Notes.checkFolder(name) == False:
			os.system(f'cmd /c "cd notes & mkdir {name}"')
		
		file = open('./notes/{}/{}.txt'.format(name, name_of_note), 'a')
		file.write(content+'\n')
		file.close()
		print('Note made succesfully\n')

	#remove a note
	def remove(name, name_of_note):

		#if there is no folder, create one
		if os.path.isfile('./notes/{}/{}.txt'.format(name, name_of_note)) == False:
			print('Note not found\n')

		#if the folder is empty
		elif os.listdir('./notes/{}'.format(name)) == []:
			print('You have no notes\n')

		else:
			os.remove('./notes/{}/{}.txt'.format(name, name_of_note))	#delete the file
			print('Note removed succesfully\n')

	#update a note (previous data deletes)
	def update(name, name_of_note, content):

		#if there is no folder, create one
		if os.path.isfile('./notes/{}/{}.txt'.format(name, name_of_note)) == False:
			print('Note not found\n')

		#if the folder is empty
		elif os.listdir('./notes/{}'.format(name)) == []:
			print('You have no notes\n')

		else:
			file = open('./notes/{}/{}.txt'.format(name, name_of_note), 'w')
			file.write(content+'\n')
			file.close()
			print('Note updated succesully\n')

class Speak:

	#convert text to speech a note of user
	def noteToSpeech(name, name_of_note):

		#setup python text-to-speech
		engine = pyttsx3.init()
		engine.setProperty('rate', 150)

		if os.path.isfile('./notes/{}/{}.txt'.format(name, name_of_note)) == False: #if task list is empty
			engine.say('Note not found!')
			engine.runAndWait()

		else:
			file = open('./notes/{}/{}.txt'.format(name, name_of_note), 'r')
			obj = file.read()
			engine.say(obj)
			engine.runAndWait()

class Speech:

	#add note by speaking
	def speechToNote():

		#setup python speech-to-text
		r = sr.Recognizer()

		try:
			with sr.Microphone() as source:
				audio = r.record(source, duration=30)
				converted = r.recognize_google(audio)
				converted = converted.lower()
				return converted

		except:
			return False
			pass

'''
made by Devansh Singh, 2020
GitHub: Devansh3712
'''