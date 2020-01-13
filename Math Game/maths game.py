from tkinter import *
from tkinter import messagebox
from random import *
import math

def leaderboard(p):
    canvas.delete(ALL)

    canvas.create_text(w/2, h/5, text="Game Over!", font=("Arial", 35), fill='red')
    canvas.create_text(w/2, h*0.27, text="Results", font=("Arial", 25), fill='green')
    
    for i in range(int(p)):
        canvas.create_text(w/2, h*(0.35+i*0.1), text="#"+str(i+1)+" Team "+str(i+1)+": "+str(beforeScore[i]), font=("Arial", 35-i*5))

    canvas.create_window(w-100, h-50, window=Button(root, text="Continue", command=lambda:levelSelect(p), font=("Arial",25)))
    
def questionGen(diff):
    
    op = math.floor(random()*3)
    firstNum = math.floor(random()*diff*5)-math.floor(random()*diff*5)
    secondNum = math.floor(random()*diff*5)-math.floor(random()*diff*5)
    
    if (op == 0):
        operation="+"
        answer = firstNum+secondNum
        operation
    elif (op == 1):
        operation="-"
        answer = firstNum-secondNum
    else:
        operation="x"
        answer = firstNum*secondNum
    return ([answer,
             (str(firstNum)+" "+operation+" "+str(secondNum)+" = ?"),
              sample(
                 [answer,
                  int((random()*firstNum*secondNum-random()*firstNum*secondNum)+(random()*diff*3-random()*diff*3)),
                  int((random()*firstNum*secondNum-random()*firstNum*secondNum)+(random()*diff*3-random()*diff*3)),
                  int((random()*firstNum*secondNum-random()*firstNum*secondNum)+(random()*diff*3-random()*diff*3))], 4
              )
            ]
           )

def results(p,level):
    canvas.delete(ALL)

    canvas.create_text(w/4, h/4, text="Before", font=("Arial", 35))
    for i in range(int(p)):
        canvas.create_text(275, h*(0.4+i*0.05), text="Team "+str(i+1)+": "+str(beforeScore[i]), font=("Arial", 25))

    for i in range(int(p)):
        canvas.create_text(w/2, h*(0.4+i*0.05), text="+"+str(score[i]-beforeScore[i]), font=("Arial", 30), fill='green')

    canvas.create_text(w*0.75, h/4, text="After", font=("Arial", 35))
    for i in range(int(p)):
        canvas.create_text(w-275, h*(0.4+i*0.05), text="Team "+str(i+1)+": "+str(score[i]), font=("Arial", 25))

    canvas.create_window(w-100, h-50, window=Button(root, text="Continue", command=lambda:levelPlay(level, p, 1), font=("Arial",25)))
    
def start(beginning):
    
    canvas.delete(ALL)
    
    group = Entry(root)
    groupButton = Button(root, text="Submit", command=lambda:levelSelect(group.get()))

    canvas.create_text(w/2, h*0.35, text="How many people are playing?", font=("Arial",35))
    canvas.create_window(w/2,h/2-25, window=group)
    canvas.create_window(w/2,h/2+25, window=groupButton)

    if (not beginning):
        canvas.create_text(w/2, h/2-65, text="Please enter a valid integer number", fill='red', font=("Arial",20))

def submit (option, team, level, p):
    global score
    if (question[0] == question[2][option.get()]):
        score[team-1] += level*5
    if (team >= int(p)):
        results(p, level)
    else:
        levelPlay(level, p, team+1)
        

def info(p):
    canvas.delete(ALL)

    canvas.create_text(w/2, h*0.1, text="How to play", font=("Arial",35))
    canvas.create_text(w/2, h*0.3, text="Start by going to the level select and select the difficulty", font=("Arial", 20))
    canvas.create_text(w/2, h*0.35, text="Make your groups and give them numbers. i.e. Team 1, Team 2 etc.", font=("Arial", 20))
    canvas.create_text(w/2, h*0.4, text="When you see your team number in blue, confer amongst yourselves,", font=("Arial", 20))
    canvas.create_text(w/2, h*0.45, text="Select the answer that your group calculates, and submit", font=("Arial", 20))
    canvas.create_text(w/2, h*0.5, text="Go through all the other groups until you see the results of that round", font=("Arial", 20))
    canvas.create_text(w/2, h*0.55, text="Each game is 5 questions, the results will appear on the screen.", font=("Arial", 20))
    canvas.create_text(w/2, h*0.6, text="You may then procced to the level select", font=("Arial", 20))
    canvas.create_text(w/2, h*0.65, text="GLHF :)", font=("Arial",20))

    
    canvas.create_window(w/2, h*0.75, window=Button(root, text="Got it", command=lambda:levelSelect(p), font=("Arial", 25)))
    
def levelSelect(peoplePlaying):
    global score
    global beforeScore
    global r

    r=1
    
    if (peoplePlaying.isalpha() or peoplePlaying == ""):
        start(False)
    else:
        score=[0]*int(peoplePlaying)
        beforeScore=[0]*int(peoplePlaying)
        canvas.delete(ALL)
        canvas.create_text(w/2, h*0.25, text="Difficulty Select", font=("Arial",35))

        for i in range(10):
            canvas.create_window(w/2, (0.35+i*0.05)*h, window=Button(root, text="Level "+str(i+1), command=lambda i=i:levelPlay(i+1, peoplePlaying, 1), font=("Arial",25)))

        canvas.create_window (w-75, 75, window = Button(root, text="?", command=lambda:info(peoplePlaying), font=("Arial", 40)))

def levelPlay(level, peoplePlaying, personToPlay):
    global question
    global beforeScore
    global r
    print(level)

    if (math.ceil(r/int(peoplePlaying)) > 5):
        leaderboard(peoplePlaying)
    else:
        canvas.delete(ALL)

        canvas.create_text(w/2, h*0.25, text="Level: "+ str(level), font=("Arial",35))
        canvas.create_text(150, h/2, text="Team "+str(personToPlay), fill='blue', font=("Arial", 25))
        canvas.create_text(w/2, h/2, text="Question #"+str(math.ceil(r/int(peoplePlaying)))+" out of 5", font=("Arial",25))
        if (personToPlay==1):
            beforeScore=score.copy()

        question = questionGen(level)

        canvas.create_text(w/2, h*0.4, text=question[1], font=("Arial",25))
        var = IntVar()

        a = Radiobutton(root, text="A: "+str(question[2][0]), variable=var, value=0)
        b = Radiobutton(root, text="B: "+str(question[2][1]), variable=var, value=1)
        c = Radiobutton(root, text="C: "+str(question[2][2]), variable=var, value=2)
        d = Radiobutton(root, text="D: "+str(question[2][3]), variable=var, value=3)

        submitButton = Button(root, text="Submit", command=lambda:submit(var, personToPlay, level, peoplePlaying), font=("Arial",20))
        backButton = Button(root, text="Back", command=lambda:back(peoplePlaying), font=("Arial",20))
        
        canvas.create_window(border, h*0.75, window=a)
        canvas.create_window(border+(w-2*border)/3, h*0.75, window=b)
        canvas.create_window(w-(border+(w-2*border)/3), h*0.75, window=c)
        canvas.create_window(w-border, h*0.75, window=d)

        canvas.create_window(w/2, h-50, window=submitButton)
        canvas.create_window(50,50, window=backButton)

        r+=1    

def back(p):
    result = messagebox.askyesno("Warning","Are you sure?\nThis game won't be saved")
    if (result):
        levelSelect(p)

w = 1080
h = 720
border=200

question = None
r = 1

beforeScore=[]
score=[]

root = Tk()
root.title("Maths Game")

canvas = Canvas(root, width=w, height=h, bg="light grey")
canvas.pack()

start(True)

root.mainloop()
