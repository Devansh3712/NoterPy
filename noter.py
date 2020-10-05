#modules for NoterPy
import noter_user as nu
import user_task as ut
import user_notes as un

#extra libraries
import time
import datetime

#ascii art for program
ASCII = '''
  _   _       _            _____       
 | \ | |     | |          |  __ \      
 |  \| | ___ | |_ ___ _ __| |__) |   _ 
 | . ` |/ _ \| __/ _ \ '__|  ___/ | | |
 | |\  | (_) | ||  __/ |  | |   | |_| |
 |_| \_|\___/ \__\___|_|  |_|    \__, |
                                  __/ |
                                 |___/ 
'''

print(ASCII)
time.sleep(1)

#print the current day and date
current_date = datetime.datetime.now()
print(current_date.strftime("%A, %d %B %Y"))
print()

flag = False
name = ''

while True:

	username = input('Enter name: ')
	print()

	#if user exists in user.txt
	if nu.User.check(username) == True:
		print(f'Hello, {username}\nHope you\'re having a nice day!\n')
		flag = True
		name = username
		break

	#if user doesn't exist in user.txt
	else:
		user_prompt = input('Name not found in record, new user? Y/N: ')
		print()

		#add new user
		if user_prompt.lower() == 'y':
			nu.User.new(username)
			print(f'Welcome, {username}\n')
			flag = True
			name = username
			break

		#terminate the program
		elif user_prompt.lower() == 'n':
			print('Thankyou for using NoterPy :)\n')
			break

		#if any other option is given as input
		else:
			print('Choose a valid option\n')

#if flag is false, program terminates
if flag == True:

	while True:

		#contents of program
		print('1. My to-do list')
		print('2. My important dates')
		print('3. My notes')
		print('4. Exit')
		print()

		#input of user's choice
		user_prompt = input('Enter your choice: ')
		print()

		#to-do list
		if user_prompt == '1':

			while True:

				print('1. Show to-do list')
				print('2. Add a task')
				print('3. Remove a task')
				print('4. Update a task')
				print('5. Return to main menu')
				print()

				user_prompt_list = input('Enter your choice: ')
				print()

				#show the tasks in the list
				if user_prompt_list == '1':
					ut.Task.show(name)

				#add a task in the list
				elif user_prompt_list == '2':
					task = input('Enter the task: ')
					ut.Task.add(name, task)

				#remove a task from the list
				elif user_prompt_list == '3':
					number = input('Enter task number: ')
					ut.Task.remove(name, number)

				#update a task in the list
				elif user_prompt_list == '4':
					number = input('Enter task number: ')
					task = input('Enter the new task: ')
					ut.Task.update(name, number, task)

				#exit the to-do list loop, return to main menu
				elif user_prompt_list == '5':
					break

				#if any other option is chosen
				else:
					print('Choose a valid option')

				print()

		#notes
		elif user_prompt == '3':

			while True:

				print('1. Show list of notes')
				print('2. Show a note')
				print('3. Add a note')
				print('4. Remove a note')
				print('5. Update a note')
				print('6. Return to main menu')
				print()

				user_prompt_list = input('Enter your choice: ')
				print()

				#show all notes of a user
				if user_prompt_list == '1':
					un.Notes.showList(name)

				#show contents of a selected note
				elif user_prompt_list == '2':
					name_of_note = input('Enter name of note: ')
					un.Notes.show(name, name_of_note)

				#add a note for the user
				elif user_prompt_list == '3':
					name_of_note = input('Enter name of note: ')
					content = input('Enter content: ')
					un.Notes.add(name, name_of_note, content)

				#delete a note of a user
				elif user_prompt_list == '4':
					name_of_note = input('Enter name of note: ')
					un.Notes.remove(name, name_of_note)

				#update a note of a user					
				elif user_prompt_list == '5':
					name_of_note = input('Enter name of note: ')
					content = input('Enter content to be updated: ')
					un.Notes.update(name, name_of_note, content)

				#exit the note loop, return to main menu
				elif user_prompt_list == '6':
					break

				#if any other option is chosen
				else:
					print('Choose a valid option\n')

				print()

		#exit the program
		elif user_prompt == '4':
			print('Thankyou for using NoterPy :)\n')
			break

		#if any other option is chosen
		else:
			print('Choose a valid option\n')