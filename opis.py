from colorama import init, Fore, Back, Style
import json
import time

def opis():

    with open('vip_list1.json', 'r', encoding='utf-8') as vip_list1:
        vip_list1 = json.load(vip_list1)
    print(Back.LIGHTWHITE_EX, Fore.RED, Style.BRIGHT, "Opis i dane programu: ", Style.RESET_ALL)

    print(Fore.LIGHTCYAN_EX, "Wersja programu:", Style.RESET_ALL, Fore.RED, ": v1.0.0", Style.RESET_ALL)

    print(Fore.LIGHTCYAN_EX, "Twórca programu:", Style.RESET_ALL, Fore.RED, ": Szymon Szturo", Style.RESET_ALL)

    print(Fore.LIGHTCYAN_EX, "Liczba uzytkownikow VIP:", Style.RESET_ALL, Fore.RED, len(vip_list1), Style.RESET_ALL)

    print(Fore.LIGHTCYAN_EX, "Uzytkownicy VIP: ", Style.RESET_ALL)
    for uzytkownik in vip_list1:
        time.sleep(0.28)
        print(Fore.LIGHTYELLOW_EX, uzytkownik, Style.RESET_ALL)

    print(Fore.LIGHTCYAN_EX, "Data utworzenia programu:", Style.RESET_ALL, Fore.RED, "22.11.2025", Style.RESET_ALL)

