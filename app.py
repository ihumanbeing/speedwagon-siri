import random as speedwagon
from playsound import *
import time
from tkinter import *

localtime = time.asctime( time.localtime(time.time()) )

root = Tk()
root.geometry(("350x100"))


questions = [
    "who are you?",
    "what time is it?",
    "how are you?"


]

audio = [
    "iamspeedwagon.mp3",
    "time.mp3",
    "death.mp3"

]

answers = [
    "Who am I, you ask?\nAllow me to introduce myself.\nI\'m Robert E. O. Speedwagon, the meddler.",
    "The time is: {}".format(localtime),
    "Uhh... I\'ll leave that to the narrator\n In 1952, he died of a heart attack at age 89. He remained single."

]

answer = StringVar()

def ask():
    global answer, textentry, respond
    q = answer.get()
    textentry.delete(0, END)
    q = q.lower()
    try:
        for question in questions:
            question.lower()
            if question == q:
                num = questions.index(question)
                respond['text'] = answers[num]
                print(answers[num])
                playsound(audio[num])
    except:
            respond['text'] = "What?.."
            playsound("huh.mp3")
            
respond = Label(root)
respond.pack()

textentry = Entry(root, textvariable=answer, bd=0, width=47)
textentry.pack(side=LEFT)

subtn = Button(root, width=3, height=1, text=">", bd=0, command=ask)
subtn.pack(side=LEFT)



#ask()

root.mainloop()



