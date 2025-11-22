
from load import load
menu_programu = True
dziala = True

def fun_spr():
    print("Sprawdzam stan programu: ")
    print("1. Menu")
    load()
    if menu_programu == True:
        print("Menu aktywne")
        load()
    else:
        print("Menu nieaktywne")
        load()
    print("2. Kalkulator")
    load()
    if dziala == True:
        print("Kalkulator aktywny")
        load()
    else:
        print("Kalkulator nieaktywny")
        load()
    print("Reszta funkcji - Aktywna bez zmian")
    load()
    print("Pomyslnie zakonczono sprawdzanie programu")
    load()