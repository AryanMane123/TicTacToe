'''
    Author: Aryan
    Project Started Date: 14 April 2021
    Purpose: Make Tic tac toe for single and double players
'''
from PIL import Image , ImageTk
import PIL.Image
import PIL.ImageTk
from tkinter import *
import time
import random
import tkinter.messagebox as tmsg
from pygame import mixer

# >>>>>> Matrix colum and rows <<<<<
'''
| 0,0 | 0,1 | 0,2 | = 1  2  3
| 1,0 | 1,1 | 1,2 | = 4  5  6
| 2,0 | 2,1 | 2,2 | = 7  8  9 
'''
#----------------------------------------------------------------------------------------------------------------------------------------------


# Fill the 0,0 matrix by given type( X or O)
def c1(type):
    global com,p,p2
    global r1
    if type=="X":
        p.add(1)
        c1=Label(frame,text="X",font="bold 70",fg="green")
    elif type=="O":
        com.add(1)
        p2.add(1)
        c1=Label(frame,text="O",font="bold 70",fg="red")
    c1.place(x=60,y=55)
    
    r1+=1

# Fill the 0,1 matrix  by given type( X or O)
def c2(type):
    global com,p,p2
    global r2
    if type=="X":
        p.add(2)
        c2=Label(frame,text="X",font="bold 70",fg="green")
    elif type=="O":
        com.add(2)
        p2.add(2)
        c2=Label(frame,text="O",font="bold 70",fg="red")
    c2.place(x=180,y=55)
    
    r2+=1

# Fill the 0,2 matrix  by given type( X or O)
def c3(type):
    global com,p,p2
    global r3
    if type=="X":
        p.add(3)
        c3=Label(frame,text="X",font="bold 70",fg="green")
    elif type=="O":
        com.add(3)
        p2.add(3)
        c3=Label(frame,text="O",font="bold 70",fg="red")
    c3.place(x=300,y=55)
    
    r3+=1

# Fill the 1,0 matrix  by given type( X or O)
def c4(type):
    global com,p,p2
    global r4
    if type=="X":
        p.add(4)
        c4=Label(frame,text="X",font="bold 70",fg="green")
    elif type=="O":
        com.add(4)
        p2.add(4)
        c4=Label(frame,text="O",font="bold 70",fg="red")
    c4.place(x=60,y=175)
    
    r4+=1

# Fill the 1,1 matrix  by given type( X or O)
def c5(type):
    global com,p,p2
    global r5
    if type=="X":
        p.add(5)
        c5=Label(frame,text="X",font="bold 70",fg="green")
    elif type=="O":
        com.add(5)
        p2.add(5)
        c5=Label(frame,text="O",font="bold 70",fg="red")
    c5.place(x=175,y=175)
    
    r5+=1

# Fill the 1,2 matrix  by given type( X or O)
def c6(type):
    global com,p,p2
    global r6
    if type=="X":
        p.add(6)
        c6=Label(frame,text="X",font="bold 70",fg="green")
    elif type=="O":
        com.add(6)
        p2.add(6)
        c6=Label(frame,text="O",font="bold 70",fg="red")
    c6.place(x=299,y=171)
    
    r6+=1

# Fill the 2,0 matrix  by given type( X or O)
def c7(type):
    global com,p,p2
    global r7
    if type=="X":
        p.add(7)
        c7=Label(frame,text="X",font="bold 70",fg="green")
    elif type=="O":
        com.add(7)
        p2.add(7)
        c7=Label(frame,text="O",font="bold 70",fg="red")
    c7.place(x=53,y=291)
    
    r7+=1

# Fill the 2,1 matrix  by given type( X or O)
def c8(type):
    global com,p,p2
    global r8
    if type=="X":
        p.add(8)
        c8=Label(frame,text="X",font="bold 70",fg="green")
    elif type=="O":
        com.add(8)
        p2.add(8)
        c8=Label(frame,text="O",font="bold 70",fg="red")
    c8.place(x=175,y=291)
    
    r8+=1

# Fill the 2,2 matrix  by given type( X or O)
def c9(type):
    global com,p,p2
    global r9
    if type=="X":
        p.add(9)
        c1=Label(frame,text="X",font="bold 70",fg="green")
    elif type=="O":
        com.add(9)
        p2.add(9)
        c1=Label(frame,text="O",font="bold 70",fg="red")
    c1.place(x=295,y=293)
    
    r9+=1

class GUI(Tk):

    def __init__(self,h,w,title,*argv) -> None:
        '''
        higth , width , Title , min , max
        '''
        super().__init__()
        self.geometry(f"{w}x{h}")
        self.title(title)
        try:
            self.maxsize(argv[0])
            self.minsize(argv[1])
        except:pass

    def image(self,filename,*argv):
            '''
            file name,resize x, resize y --> ruturn modified image

            '''
            F_image =  PIL.ImageTk.PhotoImage(PIL.Image.open(filename).resize((argv[0], argv[1]), PIL.Image.ANTIALIAS))
            return F_image

def xy(e):
    global com_score,player_score,player2_score,l,score,mixer
    l = Label(text="Who score 5 points first he win match")
    # l.place(x=160,y=26)
    l.update()
    global r1,r2,r3,r4,r5,r6,r7,r8,r9,count,click,image
    x = e.x
    y=e.y
    print(x,y)
    if   x > 50 and y>50 and x<400 and y<410:
        click = False  
        score.config(text=f"Computer (O) : {com_score}         V/S            Player (X) : {player_score}")
        score.update()

        # Check which place user click
        if x > 53 and y>53 and x<165 and y<163 and r1==0:
            c1("X")
            click = True
        elif x > 177 and y>54 and x<284 and y<164 and r2==0:
            c2("X")
            click = True
        elif x > 293 and y>48 and x<398 and y<167 and r3==0:
            c3("X")
            click = True
        elif x > 52 and y>170 and x<166 and y<284 and r4==0:
            c4("X")
            click = True
        elif x > 171 and y>171 and x<285 and y<285 and r5==0:
            c5("X")
            click = True
        elif x > 293 and y>172 and x<395 and y<282 and r6==0:
            c6("X")
            click = True
        elif x > 53 and y>292 and x<166 and y<397 and r7==0:
            c7("X")
            click = True
        elif x > 171 and y>289 and x<287 and y<398 and r8==0:
            c8("X")
            click = True
        elif x > 291 and y>291 and x<397 and y<397 and r9==0:
            c9("X")
            click = True

        # check user ckick or not
        if click:
            mixer.music.load("Swoosh.mp3")
            mixer.music.play()
            time.sleep(0.2)
            mixer.music.stop()
            #---------------------- Logic ----------------------------------
            if count==1:
                if r5==0:
                    c5("O")
                else:
                    c9("O")
            else:
                #------------------------- Computer trying to win ---------------------
                #1
                if ((2 in com and 3 in com) or (4 in com and 7 in com )or (5 in com and 9 in com)) and r1==0:
                    c1("O")
                #2
                elif ((1 in com and 3 in com) or (5 in com and 8 in com)) and r2==0:
                    c2("O")
                #3
                elif ((1 in com and 2 in com) or (6 in com and 9 in com) or (5 in com and 7 in com)) and r3==0:
                    c3("O")
                #4
                elif ((1 in com and 7 in com) or (5 in com and 6 in com) ) and r4==0:
                    c4("O")
                #5
                elif ((2 in com and 8 in com) or (4 in com and 6 in com) or (1 in com and 9 in com) or (3 in com and 7 in com)) and r5==0:
                    c5("O")
                #6
                elif ((3 in com and 9 in com) or (4 in com and 5 in com)) and r6==0:
                    c6("O")
                #7
                elif ((1 in com and 4 in com) or (8 in com and 9 in com) or (3 in com and 5 in com)) and r7==0:
                    c7("O")
                #8
                elif ((2 in com and 5 in com) or (7 in com and 9 in com)) and r8==0:
                    c8("O")
                #9
                elif ((3 in com and 6 in com) or (7 in com and 8 in com) or (1 in com and 5 in com)) and r9==0:
                    c9("O")
                
                # ------------------------- Computer trying to defense
                else:
                    #1
                    if ((2 in p and 3 in p) or (4 in p and 7 in p )or (5 in p and 9 in p)) and r1==0:
                        c1("O")
                    #2
                    elif ((1 in p and 3 in p) or (5 in p and 8 in p)) and r2==0:
                        c2("O")
                    #3
                    elif ((1 in p and 2 in p) or (6 in p and 9 in p) or (5 in p and 7 in p)) and r3==0:
                        c3("O")
                    #4
                    elif ((1 in p and 7 in p) or (5 in p and 6 in p) ) and r4==0:
                        c4("O")
                    #5
                    elif ((2 in p and 8 in p) or (4 in p and 6 in p) or (1 in p and 9 in p) or (3 in p and 7 in p)) and r5==0:
                        c5("O")
                    #6
                    elif ((3 in p and 9 in p) or (4 in p and 5 in p)) and r6==0:
                        c6("O")
                    #7
                    elif ((1 in p and 4 in p) or (8 in p and 9 in p) or (3 in p and 5 in p)) and r7==0:
                        c7("O")
                    #8
                    elif ((2 in p and 5 in p) or (7 in p and 9 in p)) and r8==0:
                        c8("O")
                    #9
                    elif ((3 in p and 6 in p) or (7 in p and 8 in p) or (1 in p and 5 in p)) and r9==0:
                        c9("O")
                    else:  
                        set1 = {i for i in range(1,10)}
                        try:
                            choise = random.choice(list(set1.difference(p).difference(com)))
                            if choise==1:c1("O")
                            elif choise==2:c2("O")
                            elif choise==3:c3("O")
                            elif choise==4:c4("O")
                            elif choise==5:c5("O")
                            elif choise==6:c6("O")
                            elif choise==7:c7("O")
                            elif choise==8:c8("O")
                            elif choise==9:c9("O")
                            print(choise)
                        except:pass
            
            
            # Checking Win or Not
            if check2(3,5,7) or check2(1,2,3) or check2(1,4,7) or check2(2,5,8) or check2(3,6,9) or check2(4,5,6) or check2(7,8,9) or check2(1,5,9):
                result = Label(frame,text="You win Against intellegent AI computer",font="lucida 15 bold")
                result.place(x=10,y=430)
                image_2 = window.image("win.jpg",70,70)
                image = Label(image=image_2)
                image.place(x=400,y=520)
                player_score+=1
                count=0
                reset() # Clear the X and O
                return 0

            elif check1(3,5,7) or check1(1,2,3) or check1(1,4,7) or check1(2,5,8) or check1(3,6,9) or check1(4,5,6) or check1(7,8,9) or check1(1,5,9):
                result = Label(frame,text="Computer win this round",font="lucida 18 bold")
                result.place(x=60,y=430)
                image_2 = window.image("sad.jpg",70,70)
                image = Label(image=image_2)
                image.place(x=370,y=530)
                com_score+=1
                count=0
                reset() # Clear the X and O
                return 0

            elif len(com) == 4 and len(p)==5 or count==10:
                result = Label(frame,text="Oops ,This round is Tied !!!",font="lucida 18 bold")
                result.place(x=100,y=430)
                count=0
                reset() # Clear the X and O
            count+=1

        else:
            print("NOt click")
            return 0
# Return True if Player win
def check1(n1,n2,n3):
    if (n1 in com and n2 in com and n3 in com):
        return TRUE
    else:
        return False

# Return True if computer win
def check2(n1,n2,n3):
    if (n1 in p and n2 in p and n3 in p):
        return TRUE
    else:
        return False

# Clear X and O
def reset():
    global r1,r2,r3,r4,r5,r6,r7,r8,r9,count,p,com,p2
    r1,r2,r3,r4,r5,r6,r7,r8,r9,count,p,p2,com = 0,0,0,0,0,0,0,0,0,1,set(),set(),set()
    frame.update()
    time.sleep(2)
    frame.destroy()
    main()

def restart():
    global r1,r2,r3,r4,r5,r6,r7,r8,r9,count,p,com,p2,score,l,title,entry,image,win,b,mixer
    mixer.music.stop()
    r1,r2,r3,r4,r5,r6,r7,r8,r9,count,p,p2,com = 0,0,0,0,0,0,0,0,0,1,set(),set(),set()
    entry = True
    win.destroy()
    image.destroy()
    b.destroy()
    main()
# r1=0 ,r2=0,r3=0,r4=0,r5=0,r6=0,r7=0,r8=0,r9=0,com_score = 0,player_score = 0,player2_score = 0,count=1,p=set(),p2=set(),com=set()
r1,r2,r3,r4,r5,r6,r7,r8,r9,com_score,player_score,player2_score,count,p,p2,com = 0,0,0,0,0,0,0,0,0,0,0,0,1,set(),set(),set()

# THis main Function reset all info
def main():
    print("In Main")
    global frame,window,can,com_score,player_score,score,entry,image,image_1,win,b,mixer
    if entry:
        print("Entry")
        entry = False
        score = Label(window,text=f"Computer (O) : {com_score}                      Player (X) : {player_score}",font="lucida 17 bold",fg="dark orange",bg="white")
        score.pack()

    l.config(text="- Who Score 3 Points First He Win Game -",fg="blue",font="lucida 12 bold",bg="white")
    l.update()
    frame = Frame(window,height=500,width=500,bg="white")
    frame.pack()
    can = Canvas(frame, width=800, height=800)
    can.pack()
    can.create_rectangle(50,50,400,410)
    can.create_line(170,50,170,400)
    can.create_line(290,50,290,400)

    can.create_line(50,170,400,170)
    can.create_line(50,290,400,290)

    score_num = 3
    # After wining
    if com_score == score_num or player_score == score_num:
        score.config(text=f"Computer (O) : {com_score}         V/S            Player (X) : {player_score}")
        score.update()

        frame.destroy()
        score.destroy()
        l.destroy()
        window.config(bg="white")
        if com_score == score_num:
            win = Label(text="!! Well Try but Computer \n win this Game !!",font="lucida 25 bold",fg="dark orange",bg="white")
            image_1 = window.image("gameover.png",240,240)
            image = Label(image=image_1)
            win.pack(pady=50)

        if player_score == score_num:
            win = Label(text="!!Congrats You win this Match\n You are Winner of the Game !!",font="lucida 25 bold",fg="dark orange",bg="white")
            win.pack(pady=50)
            mixer.stop()
            mixer.music.load("claping.wav")
            mixer.music.play()
        
        image_1 = window.image("gameover.png",240,240)
        image = Label(image=image_1)
        image.pack()
        b = Button(text="Next",command=restart,font="bold 20")
        b.pack(pady=20)
        com_score=0
        player_score=0
        window.update()

    else:
        if com_score!=5 and player_score!=5:
            pass
        score.config(text=f"Computer (O) : {com_score}         V/S            Player (X) : {player_score}")
        score.update()

        window.bind('<Button-1>', xy)
colours = ["magenta4","orange","deep pink","green2","gold","purple","blue2"]

n = 0
def title1():
    global colours,size,title,n
    title.config(text="!!! Welcome Tic Tac Toe !!!",font=f"lucida 20 bold",fg=colours[n],bg="white")
    title.update()
    if n==len(colours)-1:
        n=0
    else:
        n+=1
    title.after(2000,title1) 
if __name__ == '__main__':
    window = GUI(600,500,"TIc Tac Toe",(500,600),(500,600))
    window.config(bg="white")
    title = Label()
    title.pack(pady=10)
    entry = True
    l = Label()
    l.pack()
    mixer.init()
    main() # Calling main function
    title1()
    window.mainloop()
