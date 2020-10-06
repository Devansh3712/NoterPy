'''
module for saving everything
using MySQL for a user

change the credentials before
using
'''

#importing mysql-connector library and set up
try:
	import mysql.connector as mc
	connectMySQL = mc.connect(host='localhost', user='root', password='root')
except:
	print('Required modules not installed\n')
	exit()

#cursor object to execute queries
cursor = connectMySQL.cursor()

#making the database for NoterPy if it doesn't exist
cursor.execute('create database IF NOT EXISTS noterpy')
cursor.execute('use noterpy')

class User:

	#check if name exists in user table
	def check(name):
		name = name.lower()
		sql = 'select * from users'
		cursor.execute(sql)
		result = cursor.fetchall()
		if name in result:
			return True
		return False

	#adding a user to the user table
	def insert(name):
		name = name.lower()
		cursor.execute('create table IF NOT EXISTS users(name varchar(30))')
		sql = f'insert into users values ("{name}")'
		cursor.execute(sql)
		connectMySQL.commit()

	#removing a user from the user table
	def remove(name):

		if check(name) == False:
			return False

		else:
			name = name.lower()
			sql = f'delete from users where name="{name}"'
			cursor.execute(sql)
			connectMySQL.commit()
			return True

	#updating the name of a user
	def update(old_name, new_name):

		if check(name) == False:
			return False

		else:
			name = name.lower()
			sql = f'update users set name="{new_name}" where name="{old_name}"'
			cursor.execute(sql)
			connectMySQL.commit()
			return True

class Task:

	#check if a table of to-do list for user exists
	def check(name):
		name = name.lower()
		sql = f'show tables'
		cursor.execute(sql)
		result = cursor.fetchall()
		if name in result[0]:
			return True
		return False

	#add a task to the to-do list
	def add(name, task):
		name = name.lower()
		cursor.execute(f'create table IF NOT EXISTS {name}(task varchar(21844))')
		sql = f'insert into {name} values ("{task}")'
		cursor.execute(sql)
		connectMySQL.commit()

	#remove a task from the to-do list
	def remove(name, task):

		if Task.check(name) == False:
			name = name.lower()
			cursor.execute(f'create table {name}(task varchar(21844))')
			return False

		else:
			name = name.lower()
			sql = f'delete from {name} where task="{task}"'
			cursor.execute(sql)
			connectMySQL.commit()
			return True

	#update a task in the to-do list
	def update(name, task, new_task):

		if Task.check(name) == False:
			name = name.lower()
			cursor.execute(f'create table {name}(task varchar(21844))')
			return False

		else:
			name = name.lower()
			sql = f'update {name} set task="{new_task}" where task="{task}"'
			cursor.execute(sql)
			connectMySQL.commit()
			return True


'''
made by Devansh Singh, 2020
GitHub: Devansh3712
'''