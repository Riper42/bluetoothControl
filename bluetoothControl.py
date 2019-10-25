from os import system as sys
import sys as sy
print('''
 _     _            _              _   _     _____             _             _ 
| |   | |          | |            | | | |   /  __ \           | |           | |
| |__ | |_   _  ___| |_ ___   ___ | |_| |__ | /  \/ ___  _ __ | |_ _ __ ___ | |
| '_ \| | | | |/ _ \ __/ _ \ / _ \| __| '_ \| |    / _ \| '_ \| __| '__/ _ \| |
| |_) | | |_| |  __/ || (_) | (_) | |_| | | | \__/\ (_) | | | | |_| | | (_) | |
|_.__/|_|\__,_|\___|\__\___/ \___/ \__|_| |_|\____/\___/|_| |_|\__|_|  \___/|_|
                                                                               
                                                                               
''')
def xex():
    print("</Success>")

print("Unlocking bluetooth devices... ")
sys("sudo rfkill unblock bluetooth")
xex()

while True:
    function = input("[1]Check device \n[2]Enable device \n[3]Scan bluetooth\n[4]Discover device details{need mac address}\n[0] exit\n")
    if function == "1":
        sys("sudo rfkill list")
        xex()
    elif function == "2":
        device = input("Enter name device examples [hci0]: ")
        sys("sudo hciconfig " + device + " up")
        xex()
    elif function == "3":
        sys("sudo hcitool scan")
        xex()
    elif function == "4":
        macaddr = input("Enter the mac address of the scanning device: ")
        sys("sdptool browse " + macaddr)
        xex()
    elif function == "0":
        sy.exit()
