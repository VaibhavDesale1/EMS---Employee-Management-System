# create table in database
#create table employee(name varchar(25), fname varchar(30), age varchar(10), dob varchar(20), address varchar(50), phone varchar(20), email varchar(30), education varchar(15), post varchar(15), aadhar varchar(20), emp_id varchar(10));
#sql = "create table employee(empid int primary key, name text, age int )"


from sqlite3 import *

con = None
try:
	con = connect("kc.db")
	print("database created / open ")
	cursor = con.cursor()
	sql = "create table employee(empid int primary key, name varchar(25), fname varchar(30), age varchar(10), dob varchar(20), address varchar(50), phone varchar(20), emailid varchar(30), education varchar(15), post varchar(15), aadharno varchar(20));"

	cursor.execute(sql)
	print("table created")
except Exception as e:
	print("issue ", e)
finally:
	if con is not None:
		con.close()
		print("closed")