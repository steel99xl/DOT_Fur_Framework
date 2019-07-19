import os
from threading import Thread

def Main():
    print("Loading Scripting Referance system")
    os.system("cd ../")
    Thread_Manager()

def Load_Scripting_Referance():
    os.system("xterm -hold -e cat Configs/Parse_Sparkles_Buffer.txt")

def Writer():
    print("test")


def Thread_Manager():
    LSR_Thread = Thread(target = Load_Scripting_Referance)
    LSR_Thread.start()

    Writer_Thread = Thread(target = Writer)
    Writer_Thread.start()
