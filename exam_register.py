from exam import Exam
from student import Student
import DataBase as DB


class ExamRegister:
	def __init__(self,student=None):
		self.student=student
		if student is not None:
			exam=DB.get_registered_exams(student.rollno)
			if exam is None:
				self.exams=[]
			else:
				self.exams=exam

	def register(self,exam):
		if (exam.subjectcode,) not in self.exams:
			return DB.register_exam(self.student.rollno,exam.subjectcode)
		print('already registered')
		return False

	def get_registered_exams(self):
		exam_registered=DB.get_registered_exams(self.student.rollno)
		if exam_registered==[]:
			return None
		return exam_registered

	def get_registered_students(self,subcode):
		details=DB.get_registered_students(subcode)
		return details

if __name__=='__main__':
	pass