import sys
import DataBase

class Student:

    def __init__(self):
        self.name=None
        self.rollno=None
        self.alldetails=None

    def student_login(self,rollno=None,password=None):
        details=DataBase.student_login(rollno,password)
        if details!=None:
            self.alldetails=details
            self.rollno=rollno
            self.name=details[0]
            return True
        return False

    def student_signup(self,name=None,rollno=None,password=None):

        if name==None or rollno==None or password==None:
            sys.stderr.write("Can'T SignUp without essential details....")
            return False

        if DataBase.student_signup(rollno,password,name):
            self.name=name
            self.rollno=rollno
            self.alldetails=[rollno,password,name]
            return True
        return False

    def student_profile(self):
        #print(f"name:{self.name}\nrollno:{self.rollno}\ndetails:{self.alldetails}")
        return self.alldetails

    def student_logout(self):
        self.name=None
        self.rollno=None
        self.alldetails=None
        return True

#     Test   here   #

if __name__=='__main__':
    pass
    s=Student()
    print(s.student_signup(3,'789'))
    #print(s.student_login(2,'456'))
    #print(s.student_profile())
    #s.student_logout()
    #print(s.student_profile())


