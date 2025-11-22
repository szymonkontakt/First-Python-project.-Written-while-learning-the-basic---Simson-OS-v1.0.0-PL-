import os
import sys
import time
from colorama import init, Fore, Style
from opis import opis
from mini_gra import mini_gra
from odswiez import odswiez
from load import load
from kalkulator import kalkulator, his_kal
from fun_spr import fun_spr
from autoryzacja import logowanie, vip_control, inicjalizuj_baze

init()
inicjalizuj_baze()
zalogowany = logowanie()

while True:

    print(Fore.CYAN + Style.BRIGHT)
    print("╔" + "═" * 48 + "╗")
    print("║" + " " * 48 + "║")
    print("║" + "     SimsonOS v1.0.0 BETA".center(48) + "║")
    print("║" + "     System operacyjny made in Poland, Slobity".center(48) + "║")
    print("║" + f"     Zalogowany: {zalogowany}".center(48) + "║")
    print("║" + " " * 48 + "║")
    print("╚" + "═" * 48 + "╝")
    print(Style.RESET_ALL)
    try:
        with open('vip_list1.json', 'r', encoding='utf-8') as f:
            vip_list = json.load(f)
        if zalogowany in vip_list:
            print("  ★ VIP USER ★")
    except:
        pass
    print("-" * 17, "MENU", "-" * 17)
    print(
        "1. Kalkulator\n2. Historia kalkulatora\n3. Opis programu\n4. Odśwież\n5. VIP Panel\n6. Test funkcja\n7. Wyłącz\n8. Stan systemu\n9. Mini Gra")
    load()

    wybor = input("Wybierz: ")

    if wybor == "1":
        kalkulator()
    elif wybor == "2":
        his_kal()
    elif wybor == "3":
        opis()
    elif wybor == "4":
        odswiez()
    elif wybor == "5":
        vip_control()
    elif wybor == "6":
        n = int(input("Ile razy: "))
        txt = input("Tekst: ")
        for i in range(n):
            load()
            print(i + 1, txt)
    elif wybor == "7":
        print("Do widzenia!")
        load()
        break
    elif wybor == "8":
        fun_spr()
    elif wybor == "9":
        mini_gra()
    elif wybor == "awaryjne wylaczanie":
        print(Fore.RED + "AWARYJNE WYŁĄCZANIE SYSTEMU" + Style.RESET_ALL)
        load()
        sys.exit(1)
    else:
        print("Nie ma takiej opcji")
        load()

