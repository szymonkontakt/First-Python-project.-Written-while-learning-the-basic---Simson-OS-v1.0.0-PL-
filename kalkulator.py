import time
from datetime import datetime
from load import load

wyniki_kal = []
try:
    with open("historia_kalkulatora.txt", "r", encoding="utf-8") as f:
        wyniki_kal = [linia.strip() for linia in f.readlines() if linia.strip()]

except FileNotFoundError:
    print("Brak zapisanej historii – tworzę nową")
    wyniki_kal = []

def kalkulator():

    def dodaj(x, y):
        return x + y

    def odejmij(x, y):
        return x - y

    def pomnoz(x, y):
        return x * y

    def podziel(x, y):
        if y == 0:
            return "Błąd: dzielenie przez zero!"
        return x / y

    dziala = True
    print("Przechodze do kalkulatora")
    for loading in range(3):
        time.sleep(1)
        print("...........................")
    while dziala:

        print("---Witaj w kalkulatorze!---")
        print("Jakie dzialanie chcialbys wykonac?")
        print("1. Dodaj")
        print("2. Odejmij")
        print("3. Pomnoz")
        print("4. Podziel")
        wybor = input("Podaj wybor: ")
        try:
            a = float(input("Podaj pierwsza liczbe: "))
        except:
            print("To nie jest liczba")
            continue

        try:
            b = float(input("Podaj druga liczbe: "))
        except:
            print("To nie jest liczba")
            continue

        if wybor == "1":
            wynik = dodaj(a, b)
            teraz = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            wpis = f"[{teraz}] {a} + {b} = {wynik}"
            print("Wynik : ", wynik)
            wyniki_kal.append(wpis)
            with open("historia_kalkulatora.txt", "a", encoding="utf-8") as f:
                f.write(wpis + "\n")

        elif wybor == "2":
            wynik = odejmij(a, b)
            teraz = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            wpis = f"[{teraz}] {a} - {b} = {wynik}"
            print("Wynik: ", wynik)
            wyniki_kal.append(wpis)
            with open("historia_kalkulatora.txt", "a", encoding="utf-8") as f:
                f.write(wpis + "\n")

        elif wybor == "3":
            wynik = pomnoz(a, b)
            teraz = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            wpis = f"[{teraz}] {a} * {b} = {wynik}"
            print("Wynik :", wynik)
            wyniki_kal.append(wpis)
            with open("historia_kalkulatora.txt", "a", encoding="utf-8") as f:
                f.write(wpis + "\n")

        elif wybor == "4":
            wynik = podziel(a, b)
            teraz = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            wpis = f"[{teraz}] {a} / {b} = {wynik}"
            if isinstance(wynik, str):
                print(wynik)
            else:
                print("Wynik:", wynik)
                wyniki_kal.append(wpis)
                with open("historia_kalkulatora.txt", "a", encoding="utf-8") as f:
                    f.write(wpis + "\n")
        else:
            print("Nieprawidlowy wybor")
        kontynuuj = input("Czy chcesz wykonac kolejne obliczenie: tak/nie: ")

        if kontynuuj == "tak":
            dziala = True

        elif kontynuuj == "nie":
            dziala = False
            print("Okej, przechodze do menu")

        else:
            print("Nieprawidlowy wybor akcji.")
            dziala = False
    return
def his_kal():
    load()
    print("Przechodze do historii obliczen kalkulatora")
    load()

    if len(wyniki_kal) == 0:
        print("Brak wynikow")
        load()
    else:

        print("Liczba wynikow: ", len(wyniki_kal))
        load()
        for wpis in wyniki_kal:
            print(f"Wynik:", wpis)
            load()