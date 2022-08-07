# Employee Management Project Project

from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import requests
import bs4
import tkinter

splash = Tk()
splash.after(1000, splash.destroy)
splash.wm_attributes('-fullscreen', 'true')
msg = Label(splash, text="Employee \nManagement System \nby \nVaibhav Desale \n:-)", font=('Calibri', 100, 'bold'), fg='red')
msg.pack()
splash.mainloop()

def f1():
	add_window.deiconify()
	main_window.withdraw()

def f2():
	main_window.deiconify()
	add_window.withdraw()

def f3():
	view_window.deiconify()
	main_window.withdraw()
	view_window_st_data.delete(1.0, END)
	info = ""
	con = None
	try:
		con = connect('kc.db')
		cursor = con.cursor()
		sql = "select * from employee"
		cursor.execute(sql)
		data = cursor.fetchall()
		for d in data:
			info = info + " empid = " + str(d[0])+ "\n name = " + str(d[1])+ "\n fname = " + str(d[2])+ "\n age = " + str(d[3])+ "\n dob = " + str(d[4])+ "\n address = " + str(d[5])+ "\n phone = " + str(d[6])+ "\n emailid = " + str(d[7])+ "\n education = " + str(d[8])+ "\n post = " + str(d[9])+ "\n aadharno = " + str(d[10]) + "\n" + '*' * 40 + "\n"
		view_window_st_data.insert(INSERT, info)
	except Exception as e:
		showerror('Failure', e)
	finally:
		if con is not None:
			con.close()

def f4():
	main_window.deiconify()
	view_window.withdraw()


def f5():
	con = None

	if int(add_window_ent_age.get()) < 0 or int(add_window_ent_age.get()) > 100:
		showerror("Error ", 'Invalid age' )
	else:
		try:
			con = connect('kc.db')
			cursor = con.cursor()
			sql  = "insert into employee values('%d', '%s', '%s', '%d', '%s', '%s', '%d', '%s', '%s', '%s', '%d')"
			empid = int(add_window_ent_empid.get())
			name = add_window_ent_name.get()
			fname = add_window_ent_fname.get()
			age = int(add_window_ent_age.get())
			dob = add_window_ent_dob.get()
			address = add_window_ent_address.get()
			phone = int(add_window_ent_phone.get())
			emailid = add_window_ent_emailid.get()
			education = add_window_ent_education.get()
			post = add_window_ent_post.get()
			aadharno = int(add_window_ent_aadharno.get())
			cursor.execute(sql % (empid, name, fname, age, dob, address, phone, emailid, education, post, aadharno))
			con.commit()
			showinfo('Success', 'record added')

		except Exception as e:
			showerror('Failure', e)
		finally:
			if con is not None:
				con.close()

def f6():
	try:
		wa = "https://www.brainyquote.com/quote_of_the_day"
		res = requests.get(wa)
		data = bs4.BeautifulSoup(res.text, 'html.parser')
		info = data.find('img', {'class':'p-qotd'})
		msg = info['alt']
		showinfo("The Quote of the day is ", str(msg))
	except Exception as e:
		showerror("issue ", e)


def f7():
	update_window.deiconify()
	main_window.withdraw()

def f8():
	delete_window.deiconify()
	main_window.withdraw()

def f9():
	con = None
	con = None
	if int(update_window_ent_age.get()) < 0 or int(update_window_ent_age.get()) > 100:
		showerror("Error ", 'Invalid age' )
	else:
		try:
			con = connect("kc.db")
			cursor = con.cursor()
			sql  = "update employee set name='%s', fname='%s', age='%d', dob='%s', address='%s', phone='%d', emailid='%s', education='%s', post='%s', aadharno='%d' where empid='%d' "
			empid = int(update_window_ent_empid.get())
			name = update_window_ent_name.get()
			fname = update_window_ent_fname.get()
			age = int(update_window_ent_age.get())
			dob = update_window_ent_dob.get()
			address = update_window_ent_address.get()
			phone = int(update_window_ent_phone.get())
			emailid = update_window_ent_emailid.get()
			education = update_window_ent_education.get()
			post = update_window_ent_post.get()
			aadharno = int(update_window_ent_aadharno.get())
			cursor.execute(sql % (name, fname, age, dob, address, phone, emailid, education, post, aadharno, empid))
			if cursor.rowcount > 0: 
				showinfo('Success', 'record updated')
				con.commit()
			else:
				showerror('Success', 'record does not exists')

		except Exception as e:
			showerror('Failure', e)
		finally:
			if con is not None:
				con.close()

def f10():
	con = None
	try:
		con = connect("kc.db")
		cursor = con.cursor()
		sql  = "delete from employee where empid='%d' "
		delete_window_ent_empid.focus()
		empid = int(delete_window_ent_empid.get())
		cursor.execute(sql % (empid))
		if cursor.rowcount > 0:
			showinfo('Success', 'record deleted')
			con.commit()
			delete_window_ent_empid.focus()
			delete_window_ent_empid.delete(0, END)
		else:
			showerror('Success', 'record does not exists')
			delete_window_ent_empid.focus()
			delete_window_ent_empid.delete(0, END)	

	except Exception as e:
		showerror('Failure', e)
	finally:
		if con is not None:
			con.close()
def f11():
	main_window.deiconify()
	update_window.withdraw()

def f12():
	main_window.deiconify()
	delete_window.withdraw()

main_window = Tk()
main_window.title("E. M. S.")
main_window.geometry("500x500+400+100")

main_window_btn_add = Button(main_window, text="Add", font=('Arial', 20, 'bold'), width=10, command=f1)
main_window_btn_view = Button(main_window, text="View", font=('Arial', 20, 'bold'), width=10, command=f3)
main_window_btn_update = Button(main_window, text="Update", font=('Arial', 20, 'bold'), width=10, command=f7)
main_window_btn_delete = Button(main_window, text="Delete", font=('Arial', 20, 'bold'), width=10, command=f8)
main_window_btn_qotd = Button(main_window, text="QOTD:", font=('Arial', 20, 'bold'), width=10, command=f6)

main_window_btn_add.pack(pady=10)
main_window_btn_view.pack(pady=10)
main_window_btn_update.pack(pady=10)
main_window_btn_delete.pack(pady=10)
main_window_btn_qotd.pack(pady=10)

add_window = Toplevel(main_window)
add_window.title("Add Employee")
add_window.geometry("500x740+450+35")
 
add_window_lbl_empid = Label(add_window, text="Enter empid", font=('Arial', 10, 'bold'))
add_window_ent_empid = Entry(add_window, bd=10, font=('Arial', 10, 'bold'))
add_window_lbl_name = Label(add_window, text="Enter name", font=('Arial', 10, 'bold'))
add_window_ent_name = Entry(add_window, bd=10, font=('Arial', 10, 'bold'))
add_window_lbl_fname = Label(add_window, text="Enter Fathers name", font=('Arial', 10, 'bold'))
add_window_ent_fname = Entry(add_window, bd=10, font=('Arial', 10, 'bold'))
add_window_lbl_age = Label(add_window, text="Enter age", font=('Arial', 10, 'bold'))
add_window_ent_age = Entry(add_window, bd=10, font=('Arial', 10, 'bold'))
add_window_lbl_dob = Label(add_window, text="Enter dob", font=('Arial', 10, 'bold'))
add_window_ent_dob = Entry(add_window, bd=10, font=('Arial', 10, 'bold'))
add_window_lbl_address = Label(add_window, text="Enter address", font=('Arial', 10, 'bold'))
add_window_ent_address = Entry(add_window, bd=10, font=('Arial', 10, 'bold'))
add_window_lbl_phone = Label(add_window, text="Enter phone", font=('Arial', 10, 'bold'))
add_window_ent_phone = Entry(add_window, bd=10, font=('Arial', 10, 'bold'))
add_window_lbl_emailid = Label(add_window, text="Enter emailid", font=('Arial', 10, 'bold'))
add_window_ent_emailid = Entry(add_window, bd=10, font=('Arial', 10, 'bold'))
add_window_lbl_education = Label(add_window, text="Enter education", font=('Arial', 10, 'bold'))
add_window_ent_education = Entry(add_window, bd=10, font=('Arial', 10, 'bold'))
add_window_lbl_post = Label(add_window, text="Enter post", font=('Arial', 10, 'bold'))
add_window_ent_post = Entry(add_window, bd=10, font=('Arial', 10, 'bold'))
add_window_lbl_aadharno = Label(add_window, text="Enter aadharno", font=('Arial', 10, 'bold'))
add_window_ent_aadharno = Entry(add_window, bd=10, font=('Arial', 10, 'bold'))

add_window_btn_save = Button(add_window, text="Save", font=('Arial', 10, 'bold'), command=f5)
add_window_btn_back = Button(add_window, text="Back", font=('Arial', 10, 'bold'), command=f2)

add_window_lbl_empid.pack()
add_window_ent_empid.pack()
add_window_lbl_name.pack()
add_window_ent_name.pack()
add_window_lbl_fname.pack()
add_window_ent_fname.pack()
add_window_lbl_age.pack()
add_window_ent_age.pack()
add_window_lbl_dob.pack()
add_window_ent_dob.pack()
add_window_lbl_address.pack()
add_window_ent_address.pack()
add_window_lbl_phone.pack()
add_window_ent_phone.pack()
add_window_lbl_emailid.pack()
add_window_ent_emailid.pack()
add_window_lbl_education.pack()
add_window_ent_education.pack()
add_window_lbl_post.pack()
add_window_ent_post.pack()
add_window_lbl_aadharno.pack()
add_window_ent_aadharno.pack()

add_window_btn_save.pack()
add_window_btn_back.pack()

add_window.withdraw()

view_window = Toplevel(main_window)
view_window.title("View Employee")
view_window.geometry("500x540+450+35")

view_window_st_data = ScrolledText(view_window, width=40, height=30, font=('Arial', 10, 'bold'))
view_window_btn_back = Button(view_window, text="Back", font=('Arial', 10, 'bold'), command=f4)
view_window_st_data.pack(pady=10)
view_window_btn_back.pack(pady=10)
view_window.withdraw()

# --> update window
update_window = Toplevel(main_window)
update_window.title("Update Employee")
update_window.geometry("500x740+450+35")

update_window_lbl_empid = Label(update_window, text="Enter empid", font=('Arial', 10, 'bold'))
update_window_ent_empid = Entry(update_window, bd=10, font=('Arial', 10, 'bold'))
update_window_lbl_name = Label(update_window, text="Enter name", font=('Arial', 10, 'bold'))
update_window_ent_name = Entry(update_window, bd=10, font=('Arial', 10, 'bold'))
update_window_lbl_fname = Label(update_window, text="Enter Fathers name", font=('Arial', 10, 'bold'))
update_window_ent_fname = Entry(update_window, bd=10, font=('Arial', 10, 'bold'))
update_window_lbl_age = Label(update_window, text="Enter age", font=('Arial', 10, 'bold'))
update_window_ent_age = Entry(update_window, bd=10, font=('Arial', 10, 'bold'))
update_window_lbl_dob = Label(update_window, text="Enter dob", font=('Arial', 10, 'bold'))
update_window_ent_dob = Entry(update_window, bd=10, font=('Arial', 10, 'bold'))
update_window_lbl_address = Label(update_window, text="Enter address", font=('Arial', 10, 'bold'))
update_window_ent_address = Entry(update_window, bd=10, font=('Arial', 10, 'bold'))
update_window_lbl_phone = Label(update_window, text="Enter phone", font=('Arial', 10, 'bold'))
update_window_ent_phone = Entry(update_window, bd=10, font=('Arial', 10, 'bold'))
update_window_lbl_emailid = Label(update_window, text="Enter emailid", font=('Arial', 10, 'bold'))
update_window_ent_emailid = Entry(update_window, bd=10, font=('Arial', 10, 'bold'))
update_window_lbl_education = Label(update_window, text="Enter education", font=('Arial', 10, 'bold'))
update_window_ent_education = Entry(update_window, bd=10, font=('Arial', 10, 'bold'))
update_window_lbl_post = Label(update_window, text="Enter post", font=('Arial', 10, 'bold'))
update_window_ent_post = Entry(update_window, bd=10, font=('Arial', 10, 'bold'))
update_window_lbl_aadharno = Label(update_window, text="Enter aadharno", font=('Arial', 10, 'bold'))
update_window_ent_aadharno = Entry(update_window, bd=10, font=('Arial', 10, 'bold'))

update_window_btn_save = Button(update_window, text="Save", font=('Arial', 10, 'bold'), command=f9)
update_window_btn_back = Button(update_window, text="Back", font=('Arial', 10, 'bold'), command=f11)


update_window_lbl_empid.pack()
update_window_ent_empid.pack()
update_window_lbl_name.pack()
update_window_ent_name.pack()
update_window_lbl_fname.pack()
update_window_ent_fname.pack()
update_window_lbl_age.pack()
update_window_ent_age.pack()
update_window_lbl_dob.pack()
update_window_ent_dob.pack()
update_window_lbl_address.pack()
update_window_ent_address.pack()
update_window_lbl_phone.pack()
update_window_ent_phone.pack()
update_window_lbl_emailid.pack()
update_window_ent_emailid.pack()
update_window_lbl_education.pack()
update_window_ent_education.pack()
update_window_lbl_post.pack()
update_window_ent_post.pack()
update_window_lbl_aadharno.pack()
update_window_ent_aadharno.pack()
update_window_btn_save.pack()
update_window_btn_back.pack()
update_window.withdraw()

# --> delete window
delete_window = Toplevel(main_window)
delete_window.title("Delete Employee")
delete_window.geometry("500x500+400+100")

delete_window_lbl_empid = Label(delete_window, text="Enter empid", font=('Arial', 10, 'bold'))
delete_window_ent_empid = Entry(delete_window, bd=10, font=('Arial', 10, 'bold'))
delete_window_btn_save = Button(delete_window, text="Save", font=('Arial', 10, 'bold'), command=f10)
delete_window_btn_back = Button(delete_window, text="Back", font=('Arial', 10, 'bold'), command=f12)
delete_window_lbl_empid.pack(pady=10)
delete_window_ent_empid.pack(pady=10)
delete_window_btn_save.pack(pady=10)
delete_window_btn_back.pack(pady=10)
delete_window.withdraw()

main_window.mainloop()
