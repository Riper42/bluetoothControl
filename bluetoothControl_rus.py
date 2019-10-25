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
    print("</Успех>")

print("Разблокировка блютуз устроиств... ")
sys("sudo rfkill unblock bluetooth")
xex()

while True:
    function = input("[1]Проверить наличие подключенных устроиств \n[2]Включить устроиство \n[3]Сканирование bluetooth устроиств \n[4]Узнать подробную информацию об устройстве{Требуется mac адресс}\n[0] exit\n")
    if function == "1":
        sys("sudo rfkill list")
        xex()
    elif function == "2":
        device = input("Введите название устроиства например [hci0]: ")
        sys("sudo hciconfig " + device + " up")
        xex()
    elif function == "3":
        sys("sudo hcitool scan")
        xex()
    elif function == "4":
        macaddr = input("Введите мак адрес сканирующего устроиства: ")
        sys("sdptool browse " + macaddr)
        xex()
    elif function == "0":
        sy.exit()
