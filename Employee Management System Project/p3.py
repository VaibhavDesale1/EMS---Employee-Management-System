# inserting record in table (insert static data) --> data will be decided by the programmer
#create table employee(emp_id varchar(10), name varchar(25), fname varchar(30), age varchar(10), dob varchar(20), address varchar(50), phone varchar(20), email varchar(30), education varchar(15), post varchar(15), aadhar varchar(20));
#"create table employee(empid int primary key, name varchar(25), fname varchar(30), age varchar(10), dob varchar(20), address varchar(50), phone varchar(20), emailid varchar(30), education varchar(15), post varchar(15), aadharno varchar(20));"

from sqlite3 import *

con = None
try:
	con = connect("kc.db")
	print("database created / opened ")
	cursor = con.cursor()
	sql = "insert into employee values(10, 'sumit', 'ramesh', 20, '19-06-2001', 'mumbai', '1234567890', 'sumit@gmail.com', 'Btech', 'clerk', '123345678901234');"
	cursor.execute(sql)
	print("record created")
	con.commit()		# database me save krna 
except Exception as e:
	print("issue ", e)
	con.rollback()		# save nahi krna / nahi kiya to bhi chalta hai
finally:
	if con is not None:
		con.close()
		print("closed")