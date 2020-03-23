import random
import time

print("")
print("")
print("     _     _      __     ____  _   ___    __  __        __      _     _     ")
print("    | \   / |    /  \   / __ \| | / _ \  / .\|    \    /  \    | |   | |    ")
print("    |  \_/  |   / /\ \ | /  \ | |/ / \_\ \  /|    /   / /\ \   | |   | |    ")
print("    | |\_/| |  / /__\ \| |  __| | |   __ /  \|    \  / /__\ \  | |   | |    ")
print("    | |   | | / ______ \ \__/ | |\ \_/ /|  + |     |/ ______ \ | |___| |___ ")
print("    |_|   |_|/_/      \_\____/|_| \___/  \__/|____//_/      \_\|_____|_____|")
print("")
print("")
print("")
print("What is your name:")
name = input()
print("Welcome",name,"and I hope that I may provide you with an answer.")
print("")
print("")


def magiceightball():
    print("What is your question?")
    que = input()
    if '?' in que:
        q=random.sample(("Excellent question.","Stupid question."),1)
        print(q[0],"Give me 1 second to think about it.")
        time.sleep(1)
        s=random.sample(("No","Yes", "Ask me later", "Bad question", "Maybe",
                         "I don't want answer that question",
                         "Defintely no","Defintely yes"),1)
        print("My answer to your question is:",s[0])
        print("")
        time.sleep(1)
    else:
        print("I don't hear any question. You can ask me a new one if you want.")

runque = "y"
while runque == "y":
    runque = magiceightball()
    print("Type Y if you want to ask me another question.")
    runque = input()
