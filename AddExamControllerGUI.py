import DataBase as db
import PySimpleGUI as gui

layout=[
    [ gui.Text(" "*20+"Add Exam Controller",size=(70,3)) ],
    [ gui.Text("Name      :"), gui.InputText(size=(30,0)) ],
    [ gui.Text("Password:"), gui.InputText(size=(30,0)) ],
    [ gui.Text("Confirm Password") ],
    [ gui.Text("Password:"), gui.InputText(size=(30,0)) ],
    [ gui.Text("",size=(70,4)) ],
    [ gui.Button("Cancel"),gui.Text("",size=(20,0)), gui.Button("Add Exam Controller")]
]


def add_exam_controller():
    while True:
        win=gui.Window("Add Exam Controller")
        win.Layout(layout)
        b,values=win.Read()
        if b=='Cancel':
            win.Disappear()
            break
        elif b=='Add Exam Controller':
            name=values[0]
            pw=values[1]
            pw1=values[2]
            if name=="":
                gui.Popup("Name is empty!")
            elif pw=="":
                gui.Popup("Password is empty!")
            elif pw!=pw1:
                gui.Popup("Password doesnt match!")
            else:
                if db.add_examcontroller(name,pw):
                    gui.Popup("Exam Controller successfully added!")
                else:
                    gui.Popup("Username already exists")
                    

if __name__=='__main__':
    add_exam_controller()
