# insert dynamic data --> data will be decided by the user

from sqlite3 import *

con = None
try:
	con = connect("kc.db")
	print("database created / open ")
	cursor = con.cursor()
	sql  = "insert into employee values('%d', '%s', '%s', '%d', '%s', '%s', '%d', '%s', '%s', '%s', '%d')"
	empid = int(input("Enter empid "))
	name = input("Enter name ")
	fname = input("Enter Father's name ")
	age = int(input("Enter age "))
	dob = input("Enter Date of Birth ")
	address = input("Enter address ")
	phone = int(input("Enter phone no "))
	emailid = input("Enter emailid ")
	education = input("Enter education ")
	post = input("Enter post ")
	aadharno = int(input("Enter aadharno "))

	cursor.execute(sql % (empid, name, fname, age, dob, address, phone, emailid, education, post, aadharno))
	print("record added")
	con.commit()
	
except Exception as e:
	print("issue ", e)
	con.rollback()	

finally:
	if con is not None:
		con.close()
		print("closed")