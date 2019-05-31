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
                    Variable_Line = Parser
                    Variable_Line = Variable_Line.strip("A.B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z")
                    Variable_Line = Variable_Line.strip("a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z")

                    print(Variable_Line)

                    if("," in line):
                        Var1 = Variable_Line
                        Var1 = Var1.strip(":")
                        Var1 = Var1.strip("(")
                        Var1 = Var1.rstrip(")")
                        if("," in Var1):
                            Var2 = Var1
                            X = Var1.find(",")
                            Y = len(Var1)
                            Var1 = Var1[0:X]
                            Var2 = Var2[X+1:Y]



                        print(Var1)
                        print(Var2)


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
