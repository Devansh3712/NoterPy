'''
module for making a database
for a user using MySQL

change the credentials before
using the database
'''

#importing mysql-connector library and set up
try:
	import mysql.connector as mc
	connectMySQL = mc.connect(host='localhost', user='root', password='root') #add specific credentials
except:
	print('module for mysql not setup\n')
	exit()

#cursor object to execute queries
cursor = connectMySQL.cursor(buffered = True)

#making the database for NoterPy if it doesn't exist
cursor.execute('create database IF NOT EXISTS noterpy')
cursor.execute('use noterpy')
cursor.execute('create table IF NOT EXISTS users(name varchar(30), password varchar(30))')

class User:

	#check if name exists in user table
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

	#adding a user to the user table
	def insert(name, password):

		cursor.execute('select name from users')
		result = cursor.fetchall()
		for i in result:
			if i[0] == name:
				return False

		cursor.execute('create table IF NOT EXISTS users(name varchar(30), password varchar(30))')
		sql = f'insert into users values ("{name}", "{password}")'
		cursor.execute(sql)
		connectMySQL.commit()
		return True

	#removing a user from the user table
	def remove(name):

		sql = f'delete from users where name="{name}"'
		cursor.execute(sql)
		connectMySQL.commit()

	#updating the name of a user
	def update(old_name, new_name):

		cursor.execute('select name from users')
		result = cursor.fetchall()
		for i in result:
			if i[0] == new_name:
				return False
		
		sql = f'update users set name="{new_name}" where name="{old_name}"'
		cursor.execute(sql)
		connectMySQL.commit()
		return True

	def change_password(name, new_password):

		sql = f'update users set password="{new_password}" where name = "{name}"'
		cursor.execute(sql)
		connectMySQL.commit()

class Task:

	#check if a table of to-do list for user exists
	def check(name):
		sql = f'show tables'
		cursor.execute(sql)
		result = cursor.fetchall()
		if name in result[0]:
			return True
		return False

	#add a task to the to-do list
	def add(name, task):
		cursor.execute(f'create table IF NOT EXISTS {name}(task varchar(21844))')
		sql = f'insert into {name} values ("{task}")'
		cursor.execute(sql)
		connectMySQL.commit()

	#remove a task from the to-do list
	def remove(name, task):

		if Task.check(name) == False:
			cursor.execute(f'create table {name}(task varchar(21844))')
			return False

		else:
			sql = f'delete from {name} where task="{task}"'
			cursor.execute(sql)
			connectMySQL.commit()
			return True

	#update a task in the to-do list
	def update(name, task, new_task):

		if Task.check(name) == False:
			cursor.execute(f'create table {name}(task varchar(21844))')
			return False

		else:
			sql = f'update {name} set task="{new_task}" where task="{task}"'
			cursor.execute(sql)
			connectMySQL.commit()
			return True


'''
made by Devansh Singh, 2020
GitHub: Devansh3712
'''