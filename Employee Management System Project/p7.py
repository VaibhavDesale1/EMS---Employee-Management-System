# update

from sqlite3 import *

con = None
try:
	con = connect("kc.db")
	print("database created / opened ")
	cursor = con.cursor()
	sql  = "update employee set name='%s', fname='%s', age='%d', dob='%s', address='%s', phone='%d', emailid='%s', education='%s', post='%s', aadharno='%d' where empid='%d' "
	empid = int(input("enter empid "))
	name = input("enter new name ")
	fname = input("Enter Father's name ")
	age = int(input("Enter age "))
	dob = input("Enter Date of Birth ")
	address = input("Enter address ")
	phone = int(input("Enter phone no "))
	emailid = input("Enter emailid ")
	education = input("Enter education ")
	post = input("Enter post ")
	aadharno = int(input("Enter aadharno "))
	cursor.execute(sql % (name, fname, age, dob, address, phone, emailid, education, post, aadharno, empid))
	if cursor.rowcount > 0: 
		print("record updated")
		con.commit()
	else:
		print("record does not exists ")

except Exception as e:
	print("issue ", e)
	con.rollback()	

finally:
	if con is not None:
		con.close()
		print("closed")