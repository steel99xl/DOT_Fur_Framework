#Main script that the framework will run from
import os
import time


def Main():
    print("Main Function")
    Menu()

def SubSystems():
    print("SubSystem Check")

def Menu():
    print("Main Menu")
    while True:
        print()
        print("[1] Load Sparkles")
        print("[2] Run Modules")
        print("[3] Craft Custom Run")
        print("[4] Expot Payload")
        print("[5] Import FurScript")
        UserInput = input("Please Select an option : ")
        if(UserInput ==""):
            print("Please enter a valid option")
            print("")
        else:
            print("OwO notices ... " + UserInput)

        if(UserInput == "1"):
            Loader_System()
        if(UserInput == "2"):
            Sparkle_Menu()


def Sparkle_Menu():
    os.system("clear")
    print("Sparkle Manager")
    print("###############")
    print()
    print("List of found Sparkles")
    print("**********************")
    while True:
        with open('./Configs/Found_Sparkles.txt') as User_Readable:
            for i in User_Readable:
                print(i)
        UserInput = input("Please enter the Sparkle you wan to load : ")
        if(UserInput in open("./Configs/Found_Sparkles.txt").read()):
            f = open("./Configs/Loaded_Sparkles.txt", "+w")
            f.write(UserInput)
        else:
            print("Error can load " + UserInput)
            print("Please make sure it is spelled right")
        UserInput = input ("Would you like to continue to add Sparkles : ")
        if(UserInput.lower() != "yes" or UserInput.lower() != "y"):
            print("")
            print("")
            break
            print("If you see this somthing went wrong")
        else:
            pass




def SubMenu():
    print("General SubMenu System")

def Loader_System():
    print()
    print("Loading Sparkles")
    time.sleep(2)
    os.system("ls ./Sparkles > ./Configs/Found_Sparkles.txt")
    print("################")




try:
    Main()
except KeyboardInterrupt:
    print("\n")
    print("Cloasing Framework Console \n")
