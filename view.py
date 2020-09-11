from flask import Flask,url_for,render_template,redirect,request
from exam import Exam,Exams
from exam_register import ExamRegister
from student import Student
from examcontroller import ExamController


stu=None
examcontroller=None

app=Flask(__name__)


@app.route('/')
def home():
	return render_template('home.html')


@app.route('/student/login/',methods=['GET','POST'])
def student_login():
	global stu
	
	if request.method=='GET' and stu==None:
		return render_template('studentlogin.html')

	exams=None
	if stu!=None:
		er=ExamRegister(stu)
		e=er.get_registered_exams()
		
		if e!=None:
			exams=[]
			for i in e:
				exam=Exam()
				exam.get_exam(i[0])
				exams+=[exam]

	if request.method=='GET' and stu !=None:
		print(exams)
		return render_template('studenthome.html',exams=exams)

	if request.method=='POST':
		roll=request.form['rollno']
		password=request.form['password']
		s=Student()
		if s.student_login(roll,password):
			stu=s
			er=ExamRegister(s)
			e=er.get_registered_exams()
			
			if e!=None:
				exams=[]
				for i in e:
					exam=Exam()
					exam.get_exam(i[0])
					exams+=[exam]
			print(exams)
			return render_template('studenthome.html',exams=exams)
		return '<script>alert("Details given were wrong")</script>'+render_template('studentlogin.html')


@app.route('/student/signup/',methods=['GET','POST'])
def student_signup():
	global stu
	if request.method=='GET' and stu==None:
		return render_template('studentsignup.html')
		
	roll=request.form['rollno']
	passwd=request.form['password']
	name=request.form['name']
	s=Student()
	if s.student_signup(name,roll,passwd):
		stu=s
		er=ExamRegister(s)
		e=er.get_registered_exams()
		exams=None
		if e!=None:
			exams=[]
			for (i) in exams:
				exam=Exam()
				exam.get_exam(i)
				exams+=[exam]

		return render_template('studenthome.html')
	return '<script>alert("Retry")</script>'+render_template('studentsignup.html')


@app.route('/student/logout/',methods=['GET','POST'])
def student_logout():
	global stu
	if stu is None:
		return '<script>alert("You are not logged in yet..!")</script>'+render_template('home.html')
	stu.student_logout()
	stu=None
	return '<script>alert("You are successfully logged out..!")</script>'+render_template('home.html')





@app.route('/exam/login/',methods=['GET','POST'])
def examcontroller_login():
	global examcontroller
	if request.method=='GET' and examcontroller==None:
		return render_template('examcontrollerlogin.html')

	elif examcontroller!=None:
		return render_template('examcontrollerhome.html',name=examcontroller.name.capitalize())

	name=request.form['username']
	pw=request.form['password']
	ec=ExamController()
	if ec.login(name,pw):
		examcontroller=ec
		return render_template('examcontrollerhome.html',name=ec.name.capitalize())
	return '<script>alert("Wrong details given!")</script>'+render_template('examcontrollerlogin.html')


@app.route('/exam/logout/',methods=['GET','POST'])
def examcontroller_logout():
	global examcontroller
	if examcontroller is None:
		return '<script>alert("You are not logged in yet..!")</script>'+render_template('home.html')
	examcontroller.logout()
	examcontroller=None
	return '<script>alert("You are logged out successfully..")</script>'+render_template('home.html')


@app.route('/exam/addexam/',methods=['GET','POST'])
def addexam():
	global examcontroller
	if examcontroller==None:
		return '<script>alert("You are not logged in")</script>'+render_template('home.html')
	if request.method=='GET':
		return render_template('examcontrolleraddexam.html')
	subjectcode=request.form['subjectcode']
	subjectname=request.form['subjectname']
	domain=request.form['domain']
	examfee=request.form['examfee']
	examdate=request.form['examdate']
	print(examdate)
	e=Exam()
	if e.add_exam(subjectcode,subjectname,domain,examfee,examdate):
		return '<script>alert("Successfully added!")</script>'+render_template('examcontrolleraddexam.html')
	return '<script>alert("Retry !")</script>'+render_template('examcontrolleraddexam.html')


@app.route('/exam/viewexam/',methods=['GET','POST'])
def examcontroller_viewexam():
	global examcontroller
	if examcontroller==None:
		return '<script>alert("You are not logged in")</script>'+render_template('home.html')
	if request.method=='GET':
		e=Exams()
		examins=e.get_exams()
		#subjectname,subjectcode,domain,examfee,examdate
		return render_template('examcontrollerviewexams.html',exams=examins)
	
	subcode=request.form['subjectcode']
	e=Exam()
	er=ExamRegister()
	details=er.get_registered_students(subcode)
	if e.get_exam(subcode):
		return render_template('examcontrollerviewexam.html',exam=e,registered=details)


@app.route('/student/viewexam/',methods=['GET','POST'])
def student_viewexam():
	global stu	
	if stu is None:
		return '<script>alert("You are not logged in")</script>'+render_template('home.html')
	if request.method=='GET':
		e=Exams()
		es=e.get_exams()
		#subjectname,subjectcode,domain,examfee,examdate
		return render_template('studentviewexams.html',exams=es)
	
	subcode=request.form['subjectcode']
	e=Exam()
	if e.get_exam(subcode):
		return render_template('studentviewexam.html',exam=e)


@app.route('/student/register/',methods=['GET','POST'])
def student_registerexam():
	global stu
	if stu is None:
		return '<script>alert("You are not logged in!")</script>'+render_template('home.html')
	if request.method=='POST':
		subcode=request.form['subjectcode']
		er=ExamRegister(stu)
		e=Exam()
		e.get_exam(subcode)
		es=Exams()
		exams=es.get_exams()
		if er.register(e):
			return '<script>alert("Exam registered successfully!")</script>'+render_template('studentviewexams.html',exams=exams)
		return '<script>alert("Error! Exam already registered!")</script>'+render_template('studentviewexams.html',exams=exams)
		 


if __name__=='__main__':
	app.run('127.0.0.1',5000,debug=True)


