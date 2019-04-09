import os
import sys

global Loaded_Sparkles

def Main():
    Setup()
    print("")
    print("Parsing fles for valid options, this might take a moment")
    print("")
    Parse()
def Setup():
    global Loaded_Sparkles
    os.system("cd ../")
    Loaded_Sparkles = open("./Configs/Loaded_Sparkles.txt").read()

def Parse():
    # PLS SEND HELPS
    #os.system("cat /dev/null > ./Configs/Parse_Sparkles_Buffer.txt")
    #os.system("cat /dev/null > ./Configs/Parsed_Sparkles.txt")
    Parse_Sparkles_Buffer = open("./Configs/Parse_Sparkles_Buffer.txt" , "a+")

    for i in Loaded_Sparkles.splitlines():
        Sparkle = i.rstrip("py")
        Parse_Sparkles_Buffer.write("###### \n")
        Parse_Sparkles_Buffer.write(Sparkle.rstrip('.') + " Options \n")
        Parse_Sparkles_Buffer.write("###### \n")
        print("######")
        print(Sparkle)
        print("")
        for line in open("./Sparkles/"+ i).read().splitlines():
            if("def" in line):
                Parser = line.strip(' ')
                Parser = Parser.strip('def')
                Parser = Parser.strip(' ')
                if("()" not in line):
                    print("works lol ")
                Parse_Sparkles_Buffer.write(Sparkle+Parser + "\n")


    print("PLS WORK")


    print("")

def Script_Maker():
    # $Cruella.Main(): To append that
    # !$ to add to the front
    # %$ to print out the current buffer

    print("Scripting")
    Script = "test"

def Run_Script(Script):
    print(Script)
