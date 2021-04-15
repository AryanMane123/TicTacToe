from tkinter import *
from PIL import Image , ImageTk

class GUI(Tk):
    def __init__(self) -> None:
        super().__init__()

    def CreateLable(self,*argv):
        '''
        1) text, font, x position ,y position , bg, fg
        2) text,padx,pady, font, x position ,y position ,bg,fg 
        3) text, font 
        '''
        a=0
        try:
            variable = Label(text=argv[0],font=argv[1],bg=argv[4],fg=argv[5])
            variable.place(x=argv[2],y=argv[3])
            a+=1
        except:
            pass
        if a == 0:
            try:
                variable=Label(text=argv[0],padx=argv[1],pady=argv[2],font=argv[3])
                variable.place(x=argv[4],y=argv[5])
                a+=1
            except:
                pass
        elif a == 0:
                variable=Label(text=argv[0],font=argv[1])
                variable.pack()  
        
        return variable

    def CreateButton(self,variable,*argv):
        '''
        1) text, font, function name, x position and y position
        2) text, font, Borderwidth, x position and y position , function name
        3) text, font, Borderwidth, function name  
         '''
        a=0
        try:
            variable=Button(text=argv[0],font=argv[1],command=argv[5],borderwidth=argv[2])
            variable.place(x=argv[3],y=argv[4])
            a+=1
        except:
         pass
        if a == 0:
            try:
                variable=Button(self,text=argv[0],font=argv[1],command=argv[2])
                variable.place(x=argv[3],y=argv[4])
                a+=1
            except:
                pass
        elif a == 0:
                variable=Button(text=argv[0],font=argv[1],command=argv[2],borderwidth=argv[2])
                variable.pack()
        return variable
    
    def jpg(self,filename,*argv):
        '''
        file name ,position x ,position y ,resize x, resize y
        '''
        global image2
        photo1 = Image.open(filename)
        image1 = photo1.resize((argv[2], argv[3]), Image.ANTIALIAS)
        image2 = ImageTk.PhotoImage(image1)
        varname= Label(image=image2)
        varname.place(x=argv[0],y=argv[1])
        return varname