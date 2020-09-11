import DataBase as db

class ExamController:

    def __init__(self):
        self.name=None

    def login(self,name,pw):
        if db.examcontroller_login(name,pw):
            self.name=name
            return True
        return False

    def logout(self):
        self.name=None
        return True

#    Test here  #

if __name__=='__main__':
    pass