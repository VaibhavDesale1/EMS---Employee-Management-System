# delete

from sqlite3 import *

con = None
try:
	con = connect("kc.db")
	print("database created / opened ")
	cursor = con.cursor()
	sql  = "delete from employee where empid='%d' "
	empid = int(input("enter empid to be deleted "))
	cursor.execute(sql % (empid))
	print(cursor.rowcount)
	if cursor.rowcount > 0:
		print("record deleted")
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