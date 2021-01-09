'''
main noterpy program
'''

try:
	#modules for NoterPy
	import packages.noter_user as nu
	import packages.user_task as ut
	import packages.user_notes as un
	import packages.user_db as udb

	#extra libraries
	import time
	import datetime
	import getpass

except:
	print('Required modules not installed, terminating\n')
	exit()

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

main_menu = '''
+-------------------+
|Main Menu          |
+-------------------+
|1. My to-do list   |
|2. My notes        |
|3. Settings        |
|4. About           |
|5. Exit            |
+-------------------+
'''

task_menu = '''
+---------------------------+
|To-do List                 |
+---------------------------+
|1. Show to-do list         |
|2. Add a task              |
|3. Add a task by speaking  |
|4. Remove a task           |
|5. Update a task           |
|6. Speak the to-do list    |
|7. Return to main menu     |
+---------------------------+
'''

note_menu = '''
+---------------------------+
|Notes                      |
+---------------------------+
|1. Show list of notes      |
|2. Show a note             |
|3. Add a note              |
|4. Add a note by speaking  |
|5. Remove a note           |
|6. Update a note           |
|7. Speak a note            |
|8. Return to main menu     |
+---------------------------+
'''

settings_menu = '''
+-------------------------+
|Settings                 |
+-------------------------+
|1. Change user name      |
|2. Change user password  |
|3. Remove user           |
|4. Export logs           |
|5. Return to main menu   |
+-------------------------+
'''

info = '''
+-------------------------------------------------------------------------------+
|About                                                                          |
+-------------------------------------------------------------------------------+
|NoterPy is a tasks and notes management program, made using Python and MySQL.  |
|It is an open-sourced project, available on GitHub. It is a secure system      |
|for maintaining information as it generates a unique key for each user,        |
|which is used to encrypt and decrypt information stored by them in the         |
|database.                                                                      |
|                                                                               |
|NoterPy uses self-made and external modules, along with MySQL database for     |
|storing user credentials and their logs. Contributions can be made to the      |
|project by visiting the official GitHub page for NoterPy.                      |
|                                                                               |
|Visit: https://github.com/Devansh3712/NoterPy                                  |
+-------------------------------------------------------------------------------+
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
	password = getpass.getpass(prompt = 'Password: ')
	print()

	#if user exists in database
	if nu.User.check(username, password) == True:
		print(f'Hello, {username}\nHope you\'re having a nice day!\n')
		flag = True
		name = username
		break

	#if user's password is wrong
	elif nu.User.check(username, password) == "wrong pass":
		user_prompt = input("Wrong password, terminating program\n")
		break

	#if user doesn't exist in user.txt
	else:
		user_prompt = input('Name not found in record, new user? Y/N: ')
		print()

		#add new user
		if user_prompt.lower() == 'y':
			if nu.User.new(username, password) == False:
				print('Username already exists, try another name\n')
			else:
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
		print(main_menu)
		print()

		#input of user's choice
		user_prompt = input('Enter your choice: ')
		print()

		#to-do list
		if user_prompt == '1':

			while True:

				print(task_menu)
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

				#add task to list by speaking
				elif user_prompt_list == '3':
					print('The next 10 seconds audio will be taken in as input\n')
					task = ut.Speech.speechToTask()

					if task != False:
						print('Did you say: ' + task + '?' + '\n')
						user_input = input('Y/N: ')

						if user_input.lower() == 'y':
							ut.Task.add(name, task)

						else:
							print('Returning back to main menu\n')
							break

					else:
						print('No audio found\n')

				#remove a task from the list
				elif user_prompt_list == '4':
					number = input('Enter task number: ')
					ut.Task.remove(name, number)

				#update a task in the list
				elif user_prompt_list == '5':
					number = input('Enter task number: ')
					task = input('Enter the new task: ')
					ut.Task.update(name, number, task)

				#text-to-speech output for to-do list
				elif user_prompt_list == '6':
					ut.Speak.taskToSpeech(name)

				#exit the to-do list loop, return to main menu
				elif user_prompt_list == '7':
					break

				#if any other option is chosen
				else:
					print('Choose a valid option')

				print()

		#notes
		elif user_prompt == '2':

			while True:

				print(note_menu)
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

				#add a note for user by speaking
				elif user_prompt_list == '4':
					name_of_note = input('Enter name of note: ')
					print('The next 30 seconds will be taken in as input\n')
					content = un.Speech.speechToNote()

					if content != False:
						print('Did you say: ' + content + '?' + '\n')
						user_input = input('Y/N: ')

						if user_input.lower() == 'y':
							un.Notes.add(name, name_of_note, content)

						else:
							print('Returning back to main menu\n')
							break

					else:
						print('No audio found\n')

				#delete a note of a user
				elif user_prompt_list == '5':
					name_of_note = input('Enter name of note: ')
					un.Notes.remove(name, name_of_note)

				#update a note of a user					
				elif user_prompt_list == '6':
					name_of_note = input('Enter name of note: ')
					content = input('Enter content to be updated: ')
					un.Notes.update(name, name_of_note, content)

				elif user_prompt_list == '7':
					name_of_note = input('Enter name of note: ')
					un.Speak.noteToSpeech(name, name_of_note)

				#exit the note loop, return to main menu
				elif user_prompt_list == '8':
					break

				#if any other option is chosen
				else:
					print('Choose a valid option\n')

				print()

		#user settings
		elif user_prompt == '3':

			while True:

				print(settings_menu)
				print()

				user_prompt_list = input('Enter your choice: ')
				print()

				#update name of user
				if user_prompt_list == '1':
					new_name = input('Enter the new name of user: ')
					password = getpass.getpass(prompt = "Password: ")
					if nu.User.update(name, new_name, password) == False:
						print('Username already exists, try another name\n')
					else:
						print('User name changed successfully\n')

				elif user_prompt_list == '2':
					password = getpass.getpass(prompt = "Current Password: ")
					new_password = getpass.getpass(prompt = "New Password: ")
					nu.User.change_pass(name, password, new_password)

				#delete all data of user
				elif user_prompt_list == '3':
					con = input('All user data will be deleted. Do you want to continue? Y/N: ')

					if con.lower() == 'y':
						password = getpass.getpass(prompt = "Password: ")
						nu.User.delete(name, password)

					elif con.lower() == 'n':
						print('Returning to main menu')
						break

					else:
						print('Choose a valid option\n')

				#export logs of a user
				elif user_prompt_list == '4':
					
					date = input('Date for logs (DD/MM/YYYY): ')
					
					if udb.User.export_logs(name, date) == False:
						print(f'No logs available for {date}\n')
					else:
						print(f'Logs for date {date} exported succesfully into logs directory\n')

				#exit the settings loop, return to main menu
				elif user_prompt_list == '5':
					break

				#if any other option is chosen
				else:
					print('Choose a valid option\n')

				print()

		elif user_prompt == '4':
			print(info)
			print()

		#exit the program
		elif user_prompt == '5':
			print('Thankyou for using NoterPy :)\n')
			break

		#if any other option is chosen
		else:
			print('Choose a valid option\n')

'''
made by Devansh Singh, 2020
GitHub: Devansh3712
'''
