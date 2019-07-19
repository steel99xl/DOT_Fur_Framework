#!/bin/python3

#Main script that the framework will run from
import os
import time
import sys
sys.path.append('./FrameWork')
import Sparkle_Runner


def Main():
    print("Main Function")
    Menu()

def SubSystems():
    print("SubSystem Check")

def Menu():
    print("Main Menu")
    while True:
        print()
        print("[1] Load Sparkles (removes currently loaded ones)")
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
            Sparkle_Menu()
        if(UserInput == "2"):
            Sparkle_Run_Call()



def Sparkle_Menu():
    os.system("clear")
    os.system("cat /dev/null > ./Cruella/Loaded_Sparkles.txt")
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
            f = open("./Configs/Loaded_Sparkles.txt", "a+")
            f.write(UserInput)
            f.write("\n")
            f.close()
        else:
            print("Error can load " + UserInput)
            print("Please make sure it is spelled right")
        UserInput = input ("Would you like to continue to add Sparkles : ")
        if(UserInput.lower() == "yes" or UserInput.lower() == "y"):
            print("")
            print("")
        else:
            break
            print("If you see this somthing went wrong")




def SubMenu():
    print("General SubMenu System")

def Loader_System():
    print()
    print("Loading Sparkles")
    time.sleep(2)
    os.system("ls ./Sparkles > ./Configs/Found_Sparkles.txt")
    print("################")

def Sparkle_Run_Call():
    print("Sparkle Runner")
    print("##############")
    print()
    Sparkle_Runner.Main()




try:
    Main()
except KeyboardInterrupt:
    print("\n")
    print("Cloasing Framework Console \n")
