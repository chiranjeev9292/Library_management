import mysql.connector as a
con=a.connect(host="localhost", database="library", user="root", passwd="Bank@123456")

def addbook():
	bn=input("Enter Book Name: ")
	c=input("Enter Book Code: ")
	t=input("Total Books: ")
	s=input("Enter Subject: ")
	data=(bn, c, t, s)
	sql='insert into books values(%s, %s, %s, %s)'
	c=con.cursor()
	c.execute(sql, data)
	con.commit()
	print(">----------------------------------------<")
	print("Data Entered Sucessfully")
	main()

def issueb():
	n=input("Enter Book Name: ")
	r=input("Enter Reg No: ")
	co=input("Enter Book Code: ")
	d=input("Enter Issue Date: ")
	data=(n, r, co, d)
	sql='insert into issue values(%s, %s, %s, %s)'
	c=con.cursor()
	c.execute(sql, data)
	con.commit()
	print(">-------------------------------------<")
	print("Book Issued to: ", n)
	bookup
	(co,-1)

def submitb():
	n=input("Enter Book Name: ")
	r=input("Enter Reg No: ")
	co=input("Enter Book Code: ")
	d=input("Enter submit Date: ")
	data=(n, r, co, d)
	sql='insert into submit values(%s, %s, %s, %s)'
	c=con.cursor()
	c.execute(sql, data)
	con.commit()
	print(">-------------------------------------<")
	print("Book Submitted from: ", n)
	bookup(co, 1)

def bookup(co,u):
	a="Select TOTAL from books where BCODE=%s"
	data(co,)
	c=con.cursor()
	c.execute(a, data)
	myresult=c.fetchone()
	t=myresult[0]+u
	sql="update books set TOTAL=%s where BCODE=%s"
	d=(co, t)
	c.execute(d, sql)
	con.commit()
	main()

def dbook():
	ac=input("Enter Book Code: ")
	sql="Delete from Book where BCODE=%s"
	data=(ac,)
	c.execute(sql, data)
	con.commit()
	main()

def dispbook():
	a="select*from books"
	c=con.cursor()
	c.execute(a)
	myresult=c.fetchall()
	for i in myresult:
		print("Book Name: ", i[0])
		print("Book Code: ", i[1])
		print("Total: ", i[2])
		print("Subject: ", i[3])
	main()
def main():
	print('''
						library Manager
	1.ADD BOOK
	2.ISSUE BOOK
	3.SUBMIT BOOK
	4.DELETE BOOK
	5.DISPLAY BOOKS
	''')
	choice=input("Enter Task No: ")
	print(">---------------------------------------<")
	if(choice=='1'):
		addbook()
	elif(choice=='2'):
		issueb()
	elif(choice=='3'):
		submitb()
	elif(choice=='4'):
		dbook()
	elif(choice=='5'):
		dispbook()
	else:
		print("Wrong Choice")
		main()

def pswd():
	p = input("Password: ")

	if p=="Bank@123456":

		main()
	else:
   		print("Wrong Password")
   		pswd()
pswd()
