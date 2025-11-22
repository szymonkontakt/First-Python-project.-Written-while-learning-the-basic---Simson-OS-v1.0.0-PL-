import json
import os
import sys
from load import load

uzytkownicy = {}
vip_list = []


def inicjalizuj_baze():
    global uzytkownicy, vip_list


    if not os.path.exists('uzytkownicy1.json'):
        load()
        print("✗ Brak pliku uzytkownicy1.json!")
        load()
        sys.exit(1)

    with open('uzytkownicy1.json', 'r', encoding='utf-8') as f:
        uzytkownicy = json.load(f)


    if os.path.exists('vip_list1.json'):
        with open('vip_list1.json', 'r', encoding='utf-8') as f:
            vip_list.extend(json.load(f))
        print(f"✓ Załadowano {len(vip_list)} użytkowników VIP")
    else:
        print("⚠ Lista VIP nie istnieje – będzie tworzona przy pierwszym dodaniu")


def logowanie():
    print("Logowanie do SimsonOS v1.0")
    load()
    while True:
        login = input("Login: ")
        haslo = input("Hasło: ")
        load()

        if login in uzytkownicy and uzytkownicy[login] == haslo:
            print("Logowanie pomyślne!")
            if login in vip_list:
                print("★ WITAJ VIP ★")
            load()
            return login
        else:
            print("✗ Nieprawidłowe dane")
            load()


def vip_control():
    print("Panel zarządzania VIP")
    load()

    wybor = input("dodaj / usun / lista: ").lower()

    if wybor == "dodaj":
        user = input("Podaj login do dodania: ")
        if user in vip_list:
            print("Już jest VIP")
        else:
            vip_list.append(user)
            zapisz_vip()
            print("Dodano do VIP!")

    elif wybor == "usun":
        user = input("Podaj login do usunięcia: ")
        if user in vip_list:
            vip_list.remove(user)
            zapisz_vip()
            print("Usunięto z VIP")
        else:
            print("Nie ma takiego VIPa")

    elif wybor == "lista":
        print("=== LISTA VIP ===")
        for v in vip_list:
            print("★", v)
        print("================")

    load()


def zapisz_vip():
    with open("vip_list1.json", "w", encoding="utf-8") as f:
        json.dump(vip_list, f, ensure_ascii=False, indent=4)