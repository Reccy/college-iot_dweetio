import sqlite3

c = sqlite3.connect('iot_assignment_one.db')

for row in c.execute('''SELECT * FROM pi_data'''):
	print row