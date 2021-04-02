"""
module for making a database
for a user using MySQL

change the credentials before
using the database
"""

# importing mysql-connector library and set up
try:

	from datetime import datetime
	from tabulate import tabulate
	import random
	import string
	import mysql.connector as mc
	connectMySQL = mc.connect(host='localhost', user='root', password='root') # add specific credentials

except:

	print('module for mysql not setup\n')
	exit()

# cursor object to execute queries
cursor = connectMySQL.cursor(buffered = True)

# making the database for NoterPy if it doesn't exist
cursor.execute('create database IF NOT EXISTS noterpy')
cursor.execute('use noterpy')
cursor.execute('create table IF NOT EXISTS users(name varchar(30), password varchar(30), cryptkey varchar(10))')

class User:

	# generate a cryptkey for encrypting and decrypting a user's content
	def generate_pass():

		password_char 	= string.ascii_letters + string.digits + string.punctuation
		password 		= ''

		for i in range (10):
			password += random.choice(password_char)

		return password

	# show all usernames in database
	def show_all_users():

		cursor.execute('select name from users')
		return cursor.fetchall()

	# check if name exists in user table
	def check(name, password):

		sql = f'select password from users where name = "{name}"'
		cursor.execute(sql)
		result = cursor.fetchone()

		if result == None:
			return False

		elif result[0] == password:
			return True

		elif result[0] != password:
			return "wrong pass"

		return False

	# adding a user to the user table
	def insert(name, password):

		result = User.show_all_users()

		for i in result:

			if i[0] == name:
				return False

		cryptkey 	= User.generate_pass()
		sql 		= f'insert into users values ("{name}", "{password}", "{cryptkey}")' # enter user info into database
		cursor.execute(sql)

		cursor.execute(f'create table IF NOT EXISTS {name}(date varchar(10), log varchar(100), time varchar(10))') # create a table for user logs

		date = datetime.now().strftime("%d/%m/%Y")
		time = datetime.now().strftime("%X")

		cursor.execute(f'insert into {name} values ("{date}", "new user {name} created", "{time}")')
		connectMySQL.commit()
		return True

	# removing a user from the user table
	def remove(name):

		sql = f'delete from users where name="{name}"' # remove user details
		cursor.execute(sql)
		connectMySQL.commit()

		date = datetime.now().strftime("%d/%m/%Y")
		time = datetime.now().strftime("%X")
		cursor.execute(f'insert into {name} values ("{date}", "removed user {name}", "{time}")') # update user logs

		file = open(f'./logs/{name}.txt', 'a')
		cursor.execute(f'select * from {name}')
		result = cursor.fetchall()
		file.write(str(result))
		file.close() # export user logs

		sql = f'drop table {name}' # delete user logs table
		cursor.execute(sql)
		connectMySQL.commit()

	# updating the name of a user
	def update(old_name, new_name):

		result = User.show_all_users()

		for i in result:

			if i[0] == new_name:
				return False
		
		try:

			sql = f'update users set name="{new_name}" where name="{old_name}"' # update the user name in users table
			cursor.execute(sql)

			sql = f'rename table {old_name} to {new_name}' # update user name in user's logs table
			cursor.execute(sql)

			date = datetime.now().strftime("%d/%m/%Y")
			time = datetime.now().strftime("%X")
			cursor.execute(f'insert into {new_name} values ("{date}", "updated username from {old_name} to {new_name}", "{time}")') # update logs for user
			connectMySQL.commit()

		except:
			pass

		return True

	# change password of a user
	def change_password(name, new_password):

		sql = f'update users set password="{new_password}" where name = "{name}"' # change password of a user
		cursor.execute(sql)

		date = datetime.now().strftime("%d/%m/%Y")
		time = datetime.now().strftime("%X")
		cursor.execute(f'insert into {name} values ("{date}", "updated password", "{time}")') # update logs of the user
		connectMySQL.commit()

	# return cryptkey of a user
	def crypt_key(name):

		sql = f'select cryptkey from users where name = "{name}"'
		cursor.execute(sql)
		key = cursor.fetchone()
		return key[0]

	# export the logs of a user for a given date
	def export_logs(name, date):

		sql = f'select * from {name} where date = "{date}"'
		cursor.execute(sql)
		result = cursor.fetchall()
		file_name = date.split('/')
		file_name = '.'.join(file_name)
		file_name = name + '(' + file_name + ')'

		if result is None:
			return False

		else:
			file = open(f'./logs/{file_name}.txt', 'w')
			file.write(tabulate(result, headers = ['Date', 'Log', 'Time'], tablefmt = 'psql'))
			file.close()

# class for maintaining logs of a user
class Logs:

	# log for adding a new note
	def add_note(name, name_of_note):

		date = datetime.now().strftime("%d/%m/%Y")
		time = datetime.now().strftime("%X")
		cursor.execute(f'insert into {name} values ("{date}", "added a new note {name_of_note}", "{time}")')
		connectMySQL.commit()

	# log for updating a note
	def update_note(name, name_of_note):

		date = datetime.now().strftime("%d/%m/%Y")
		time = datetime.now().strftime("%X")
		cursor.execute(f'insert into {name} values ("{date}", "updated note {name_of_note}", "{time}")')
		connectMySQL.commit()

	# log for deleting a note
	def delete_note(name, name_of_note):

		date = datetime.now().strftime("%d/%m/%Y")
		time = datetime.now().strftime("%X")
		cursor.execute(f'insert into {name} values ("{date}", "deleted note {name_of_note}", "{time}")')
		connectMySQL.commit()

	# log for adding a new task
	def add_task(name):

		date = datetime.now().strftime("%d/%m/%Y")
		time = datetime.now().strftime("%X")
		cursor.execute(f'insert into {name} values ("{date}", "added a new task", "{time}")')
		connectMySQL.commit()

	# log for updating a task
	def update_task(name, number):

		date = datetime.now().strftime("%d/%m/%Y")
		time = datetime.now().strftime("%X")
		cursor.execute(f'insert into {name} values ("{date}", "updated task number {number}", "{time}")')
		connectMySQL.commit()

	# log for deleting a task
	def delete_task(name, number):

		date = datetime.now().strftime("%d/%m/%Y")
		time = datetime.now().strftime("%X")
		cursor.execute(f'insert into {name} values ("{date}", "deleted task number {number}", "{time}")')
		connectMySQL.commit()

"""
NoterPy
Devansh Singh, 2020
"""
