import os
import Sparkle_Parser
###TEST###
def HeadLess():
    os.system("xterm -hold -e python3 ./Sparkle_Runner.py")
##########
def Main():
    os.system("cd ..")
    File = open("./Configs/Loaded_Sparkles.txt")
    ReadFile = open("./Configs/Loaded_Sparkles.txt").read()
    os.system("cd Sparkles")
    Menu(File,ReadFile)

def Menu(File,ReadFile):
    os.system("clear")
    while True:
        print("Sparkle Run Menu")
        print("################")
        print()
        print("[1] Run individual Sparkles")
        print("[2] Script With Sparkles")
        print("[E] Exit Run Menu")
        UserInput = input("Please slelect an option : ")
        if(UserInput ==""):
            print("Please enter a valid option")
            print("")
        else:
            print("OwO notices ... " + UserInput)

        if(UserInput == "1"):
            OneSparkle(File,ReadFile)
        if(UserInput == "2"):
            FurScript_Run_Call()
        if(UserInput.lower() == "e"):
            break

def OneSparkle(File,ReadFile):
    print()

    for i in File:
        print(i)
    print("")

    UserInput = input("Please enter the Sparkle you want run : ")
    if(UserInput not in ReadFile):
        print()
        print("∴ (O艸O★) Sparkle not found... O no")
        print()
        return
    if(".sh" in UserInput):
        print("Bash Script")
    if(".py" in UserInput):
        print("Python Script")
        os.system("python3 ./Sparkles/"+UserInput)

def FurScript_Run_Call():
    print("this loads so yay")
    Sparkle_Parser.Main()
