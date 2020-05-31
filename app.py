import random as speedwagon
from playsound import *
import time

localtime = time.asctime( time.localtime(time.time()) )


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
    "Who am I, you ask? Allow me to introduce myself. I\'m Robert E. O. Speedwagon, the meddler.",
    "The time is: {}".format(localtime),
    "Uhh... I\'ll leave that to the narrator\n In 1952, he died of a heart attack at age 89. He remained single."

]

def ask():
    q = input("Ask me anything! ")
    q = q.lower()
    for question in questions:
        if question == q:
            num = questions.index(question)
            print(answers[num])
            playsound(audio[num])
            ask()
    if question != q:
            print("Huh?.. Sorry?")
            playsound("huh.mp3")
            ask()

ask()

