import random
import time

def question():
    print("What is your question?")
    que = input()
    if '?' in que:
        q=random.sample(("Excellent question.","Stupid question."),1)
        print(q[0],"Give me 1 second to think about it.")
        time.sleep(1)
        s=random.sample(("No","Yes", "Ask me later", "Bad question", "Maybe",
                         "I don't want to answer that question",
                         "Defintely no","Defintely yes"),1)
        print("My answer to your question is:",s[0])
        print("")
        time.sleep(1)
    else:
        print("I don't hear any question. You can ask me a new one if you want.")


def theOracle():
    print("")
    print("")
    print("")
    print("     _______ _    _ ____   ____   ____       __      _      ____   ____ ")
    print("    |__   __| |  | |  __| / __ \ |    \     /  \    | |    / __ \ |  __|")
    print("       | |  | |__| | |__|/ /  \ \|    /    / /\ \   | |   / /  \_\|  __ ")
    print("       | |  |  __  |  __| |    | | | \    / /__\ \  | |  | |    __|  __|")
    print("       | |  | |  | | |__ \ \__/ /| |\ \  / ______ \ | |___\ \__/ /| |__ ")
    print("       |_|  |_|  |_|____| \____/ |_| \_|/_/      \_\|_____|\ ___/ |____|")
    print("")
    print("")
    print("")
    print("")
    print("What is your name:")
    name = input()
    print("Welcome",name,"and I hope that I may provide you with an answer.")
    print("")
    print("")

    runque = "y"
    while runque == "y":
        runque = question()
        print("Type Y if you want to ask me another question.")
        runque = input()
