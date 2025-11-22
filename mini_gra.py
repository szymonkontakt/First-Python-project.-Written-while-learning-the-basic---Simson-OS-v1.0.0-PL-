import time
from load import load
from random import randint
def mini_gra():
    load()
    print("Wlaczanie mini gry...")
    load()
    ruchy = 0
    print("Witaj w Mini-Grze !")
    load()
    gra_szer = 10
    gra_wys = 10

    key_x = randint(0, gra_szer - 1)
    key_y = randint(0, gra_wys - 1)

    player_x = 0
    player_y = 0

    player_znalazl_klucz = False

    while not player_znalazl_klucz:

        ruch = input("Uzyj W / A / S / D aby sie poruszac")

        match ruch.lower():
            case 'w':
                load()
                player_y += 1
                ruchy += 1
                print(player_x, player_y)
                print(f"Odległość od klucza: {abs(player_x - key_x) + abs(player_y - key_y)} kroków")
                if player_y > gra_wys:
                    print("Tu jest granica")
                    player_y = gra_wys
            case 's':
                load()
                player_y -= 1
                ruchy += 1
                print(player_x, player_y)
                print(f"Odległość od klucza: {abs(player_x - key_x) + abs(player_y - key_y)} kroków")
                if player_y < 0:
                    print("Tu jest granica")
                    player_y = 0
            case 'a':
                load()
                player_x -= 1
                ruchy += 1
                print(player_x, player_y)
                print(f"Odległość od klucza: {abs(player_x - key_x) + abs(player_y - key_y)} kroków")
                if player_x < 0:
                    print("Tu jest granica")
                    player_x = 0
            case 'd':
                load()
                player_x += 1
                ruchy += 1
                print(player_x, player_y)
                print(f"Odległość od klucza: {abs(player_x - key_x) + abs(player_y - key_y)} kroków")
                if player_x > gra_szer:
                    print("Tu jest granica")
                    player_x = gra_szer
            case 'q':
                load()
                print("Wychodzenie z gry...")
                load()
                return
            case _:
                load()
                print("Nie ma takiego ruchu")
                load()
                continue
        if player_x == key_x and player_y == key_y:
            print("ZNALEZIONO KLUCZ")
            print("Gratulacje")
            print("Znalazles klucz w : ", ruchy, "Ruchy/Ruchow")
            load()
            return