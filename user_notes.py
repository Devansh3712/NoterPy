'''
module for maintaining notes of
a user, saved in directory notes
'''

import os

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
		if Notes.checkFolder(name) == False:
			os.system(f'cmd /c "cd notes & mkdir {name}"')
			print('You have no notes!\n')

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
		if Notes.checkFolder(name) == False:
			os.system(f'cmd /c "cd notes & mkdir {name}"')
			print('You have no notes!\n')

		#if the folder is empty
		elif os.listdir('./notes/{}'.format(name)) == []:
			print('You have no notes!\n')

		else:
			os.remove('./notes/{}/{}.txt'.format(name, name_of_note))	#delete the file
			print('Note removed succesfully\n')

	#update a note (previous data deletes)
	def update(name, name_of_note, content):

		#if there is no folder, create one
		if Notes.checkFolder(name) == False:
			os.system(f'cmd /c "cd notes & mkdir {name}"')
			print('You have no notes!\n')

		#if the folder is empty
		elif os.listdir('./notes/{}'.format(name)) == []:
			print('You have no notes!\n')

		else:
			file = open('./notes/{}/{}.txt'.format(name, name_of_note), 'w')
			file.write(content+'\n')
			file.close()
			print('Note updated succesully\n')

'''
made by Devansh Singh, 2020
GitHub: Devansh3712
'''