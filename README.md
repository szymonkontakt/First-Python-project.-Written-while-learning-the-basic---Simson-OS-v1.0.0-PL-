# SimsonOS v1.0.0 Beta

## O projekcie

SimsonOS to testowy projekt napisany w Pythonie na początkowych etapach nauki programowania. Program symuluje prosty system operacyjny z logowaniem, kalkulatorem, grą i systemem VIP.

## Wymagania

- Python 3.6+
- colorama (instalacja: `pip install colorama`)

## Uruchomienie

```
python main.py
```

## Struktura projektu

| Plik | Opis |
|------|------|
| **main.py** | Główny plik - menu systemu |
| **autoryzacja.py** | Logowanie użytkowników, system VIP |
| **kalkulator.py** | Kalkulator z zapisywaniem historii |
| **mini_gra.py** | Gra polegająca na znalezieniu klucza |
| **load.py** | Funkcja ładowania (efekt wizualny) |
| **opis.py** | Wyświetlanie informacji o programie |
| **fun_spr.py** | Sprawdzanie stanu systemu |
| **odswiez.py** | Odświeżanie systemu |
| **uzytkownicy1.json** | Baza danych użytkowników (login:hasło) |
| **vip_list1.json** | Lista użytkowników VIP |
| **historia_kalkulatora.txt** | Historia obliczeń kalkulatora |

## Funkcje

### 1. Logowanie
- Wpisz login i hasło z pliku `uzytkownicy1.json`
- System sprawdza czy użytkownik jest VIP

### 2. Kalkulator (opcja 1)
- Dodawanie, odejmowanie, mnożenie, dzielenie
- Automatyczne zapisywanie wyników z czasem
- Historia zapisana w `historia_kalkulatora.txt`

### 3. Historia kalkulatora (opcja 2)
- Wyświetlenie wszystkich poprzednich obliczeń

### 4. Opis programu (opcja 3)
- Informacje o wersji i autorze
- Lista użytkowników VIP

### 5. Odświeżenie (opcja 4)
- Czyszczenie konsoli i odświeżenie menu

### 6. Panel VIP (opcja 5)
- Dodawanie/usuwanie użytkowników z listy VIP
- Wyświetlanie listy VIP

### 7. Mini Gra (opcja 9)
- Gra polegająca na znalezieniu klucza
- Sterowanie: W/A/S/D
- Wyświetla odległość od celu
- Liczy ilość ruchów

## Dane logowania (domyślne)

Obejrzyj plik `uzytkownicy1.json`:
```json
{
  "admin": "admin123",
  "test": "test123"
}
```

## Uwagi

- Program wymaga pliku `uzytkownicy1.json` do uruchomienia
- Historia kalkulatora jest zapisywana automatycznie
- System VIP jest zapisywany po każdej zmianie
- Niektóre komunikaty zawierają polskie znaki (UTF-8)

## Autor

Szymon Szturo - projekt testowy do nauki Pythona
Data utworzenia: 22.11.2025
