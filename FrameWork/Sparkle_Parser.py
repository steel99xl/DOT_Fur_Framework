import os
import sys

#import time # Testing only

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
    os.remove("./Configs/Parse_Sparkles_Buffer.txt")
    Loaded_Sparkles = open("./Configs/Loaded_Sparkles.txt").read()

def Parse():
    # PLS SEND HELPS

    Parse_Sparkles_Buffer = open("./Configs/Parse_Sparkles_Buffer.txt" , "w+")

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
                    Variable_Line = Parser
                    Variable_Line = Variable_Line.strip("A.B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z")
                    Variable_Line = Variable_Line.strip("a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z")

                    Variables = []

                    if(Variable_Line.find("(") + 1 != Variable_Line.find(")")):
                        Var1 = Variable_Line
                        Var1 = Var1.strip(":")
                        Var1 = Var1.strip("(")
                        Var1 = Var1.rstrip(")")
                        Buffer_Line = Var1
                        if("," in Variable_Line):
                            X = Variable_Line.count(",") - 1
                            Split = Var1.find(",")
                            Var1 = Var1[0:Split]
                            Variables.append(Var1)
                            Buffer = Var1+","

                            while X >= 0:
                                Buffer_Line = Buffer_Line.strip(Buffer)
                                Vars = Buffer_Line
                                if("," in Vars):
                                    Split = Vars.find(",")
                                    Vars = Vars[0:Split]
                                    Buffer = Vars+","
                                else:
                                    pass
                                Variables.append(Vars)
                                X -= 1

                        else:
                            Variables.append(Var1)

                    for x in Variables:
                        for i in open("./Sparkles/"+ Sparkle+"py", "r+"):
                            if(x + "=" in i or x +" =" in i):
                                if('"' in i):
                                    print("String")
                                elif("True" in i or "False" in i):
                                    print("Bool")
                                else:
                                    print("Integer")




                    print("yay")

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
