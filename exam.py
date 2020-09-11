import DataBase as DB
import sys


class Exam:

	def __init__(self):
		self.subjectcode=None
		self.subjectname=None
		self.domain=None
		self.examfee=None
		self.examdate=None


	def add_exam(self,subjectcode=None,subjectname=None,domain=None,examfee=None,examdate=None):
		if subjectcode==None or subjectname==None or domain==None or examfee==None or examdate==None:
			sys.stderr.write("Fill all details to include exam .!")
			return False
		if DB.add_exam(subjectcode,subjectname,domain,examfee,examdate):
			return True
		return False

	def get_exam(self,subjectcode=None):
		if subjectcode==None:
			sys.stderr.write("No subjectcode given")
			return False
		details=DB.get_exam(subjectcode)
		if details==None:
			return False
		self.subjectcode=details[0]
		self.subjectname=details[1]
		self.domain=details[2]
		self.examfee=details[3]
		self.examdate=details[4]
		return True

	

class Exams:
	def __init__(self):
		self.exams=None
		self.domains=DB.get_domains()


	def get_exams(self):		
		details=DB.get_exams()
		#subjectname,subjectcode,domain,examfee,examdate
		if details==[]:
			return None
		self.exams=details
		return details


	def get_domains(self):
		return self.domains


#      Test   Here      ##

if __name__=='__main__':
	pass
	e=Exams()
	print(e.get_exams('ECE'))


