# view record (select) --> fetchall() --> ek saath record

from sqlite3 import *

con = None
try:
	con = connect("kc.db")
	print("database created / open ")
	cursor = con.cursor()
	sql = "select * from employee"
	cursor.execute(sql)
	data = cursor.fetchall()	# list of tuples 		[(rno,name, marks) (...) () ]
	print(data)
	
	for d in data:
		print("empid = ", d[0], 'name = ', d[1], 'fname = ', d[2], 'age = ', d[3], 'dob = ', d[4], 'address = ', d[5], 'phone = ', d[6], 'emailid = ', d[7], 'education = ', d[8], 'post = ', d[9], 'aadharno = ', d[10])
except Exception as e:
	print("issue ", e)
	
finally:
	if con is not None:
		con.close()
		print("closed")