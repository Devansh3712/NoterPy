#modules for NoterPy
import noter_user as nu
import user_task as ut

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

		else:
			print('Choose a valid option\n')

if flag == True:

	while True:

		print('1. My to-do list')
		print('2. My important dates')
		print('3. Exit')
		print()

		user_prompt = input('Enter your choice: ')
		print()

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

				if user_prompt_list == '1':
					ut.Task.show(name)

				elif user_prompt_list == '2':
					task = input('Enter the task: ')
					ut.Task.add(name, task)

				elif user_prompt_list == '3':
					number = input('Enter task number: ')
					ut.Task.remove(name, number)

				elif user_prompt_list == '4':
					number = input('Enter task number: ')
					task = input('Enter the new task: ')
					ut.Task.update(name, number, task)

				elif user_prompt_list == '5':
					break

				else:
					print('Choose a valid option')

		elif user_prompt == '3':
			print('Thankyou for using NoterPy :)\n')
			break
