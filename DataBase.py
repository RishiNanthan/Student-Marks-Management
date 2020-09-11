
import sqlite3 as sql

########     Queries    ###########

query1=''' insert into student values({},'{}','{}'); '''

query2=''' create table if not exists student(
		rollno int primary key,
		password varchar(50),
		name varchar(30)
		); '''

query3=''' select * from student where rollno={} '''

query4=''' create table if not exists exam(
		subjectcode int primary key,
		subjectname varchar(25),
		domain char(3),
		examfee int,
		examdate date
		)	'''

query5=''' insert into exam values({},'{}','{}',{},'{}'); '''

query6=''' select subjectname,subjectcode,domain,examfee,examdate from exam ; '''

query7=''' select domain from exam group by domain; '''

query8=''' select * from exam where subjectcode='{}'; '''

query9=''' create table if not exists exam_register(
		rollno int,
		subjectcode int,
		foreign key (rollno) references student(rollno) ,
		foreign key (subjectcode) references exam(subjectcode)
	); '''

query10=''' insert into exam_register values({},{}); '''

query11=''' select subjectcode from exam_register where rollno={} ;'''

query12=''' create table if not exists examcontroller(
		username varchar(50) primary key,
		password varchar(50)
		); '''

query13=''' insert into examcontroller values('{}','{}')'''

query14=''' select password from examcontroller where username='{}' ;'''

query15=''' select name,rollno from student where rollno in
 (select rollno from exam_register where subjectcode={});
 '''

###################################

con=sql.connect("Exam_Registration.db")
cur=con.cursor()

con.execute(query2)
con.execute(query4)
con.execute(query9)
con.execute(query12)

############################   Data Base Functions  ##########################

def student_signup(rollno=None,password=None,name=None):
	try:
		con=sql.connect("Exam_Registration.db")
		cur=con.cursor()

		q=query1.format(rollno,password,name)
		con.execute(q)
		con.commit()
		return True
	except Exception as e:
		print(e) 
		return False

def student_login(rollno,password):
	try:
		con=sql.connect("Exam_Registration.db")
		cur=con.cursor()

		q=query3.format(rollno)
		cur.execute(q)
		details=cur.fetchall()+[]
		if details==[] or details[0][1]!=password:
			return None
		return details[0]
	except Exception as e: 
		print(e) # // No Chance or Rare //
		return None


def add_exam(subjectcode,subjectname,domain,examfee,examdate):
	try:
		con=sql.connect("Exam_Registration.db")
		cur=con.cursor()

		q=query5.format(subjectcode,subjectname,domain,examfee,examdate)
		con.execute(q)
		con.commit()
		return True

	except Exception as e:
		print(e)  # // No Chance or Rare //
		return False


def get_exam(subjectcode):
	try:
		con=sql.connect("Exam_Registration.db")
		cur=con.cursor()

		q=query8.format(subjectcode)
		cur.execute(q)
		details=cur.fetchone()+()
		return details
	except Exception as e:
		print(e) #// Often // No Worries // Unsupported operands types for '+' NoneType and list 
		return None

def get_domains():
	con=sql.connect("Exam_Registration.db")
	cur=con.cursor()

	q=query7
	cur.execute(q)
	details=cur.fetchall()+[]
	if details==[]:
		return None
	return details


def get_exams():
	con=sql.connect("Exam_Registration.db")
	cur=con.cursor()

	q=query6
	cur.execute(q)
	details=cur.fetchall()+[]
	#subjectname,subjectcode,domain,examfee,examdate
	return details


def get_registered_exams(rollno):
	con=sql.connect("Exam_Registration.db")
	cur=con.cursor()

	q=query11.format(rollno)
	cur.execute(q)
	details=cur.fetchall()+[]
	if details==[]:
		return None
	return details


def get_registered_students(subcode):
	con=sql.connect('Exam_Registration.db')
	cur=con.cursor()
	q=query15.format(subcode)
	cur.execute(q)
	details=cur.fetchall()+[]
	if details==[]:
		return None
	return details


def register_exam(rollno,subjectcode):
	try:
		con=sql.connect("Exam_Registration.db")
		cur=con.cursor()

		q=query10.format(rollno,subjectcode)
		con.execute(q)
		con.commit()
		return True 
	except Exception as e:
		print(e)        # // Rare //
		return False

def add_examcontroller(username,password):
	q=query13.format(username,password)
	con=sql.connect("Exam_Registration.db")
	cur=con.cursor()
	try:
		con.execute(q)
		con.commit()
		return True
	except Exception as e:
		print(e)
		return False
	
def examcontroller_login(username,password):
	q=query14.format(username)
	con=sql.connect("Exam_Registration.db")
	cur=con.cursor()
	try:
		cur.execute(q)
		pw=cur.fetchone()[0]+""
		if pw == password:
			return True
		return False
	except Exception as e:
		print(e)
		return False



 #         Test   Here    #

if __name__=='__main__':
	pass
	#print(student_signup(1,'123','Aaa'))
	#print(student_login(1,'123'))
	#print(get_exam(1))
	#print(add_exam(3,'MP','ECE',500,'2019-10-10'))
	#print(get_exams('CSE'))
	#print(get_domains())