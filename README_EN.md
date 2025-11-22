# SimsonOS v1.0.0 Beta

## About the Project

SimsonOS is a test project written in Python during the early stages of learning programming. The program simulates a simple operating system with login functionality, calculator, game, and VIP system.

## Requirements

- Python 3.6+
- colorama (install: `pip install colorama`)

## How to Run

```
python main.py
```

## Project Structure

| File | Description |
|------|-------------|
| **main.py** | Main file - system menu |
| **autoryzacja.py** | User login, VIP system |
| **kalkulator.py** | Calculator with history saving |
| **mini_gra.py** | Game - find the key |
| **load.py** | Loading function (visual effect) |
| **opis.py** | Display program information |
| **fun_spr.py** | System status check |
| **odswiez.py** | System refresh |
| **uzytkownicy1.json** | User database (login:password) |
| **vip_list1.json** | VIP users list |
| **historia_kalkulatora.txt** | Calculator history |

## Features

### 1. Login
- Enter login and password from `uzytkownicy1.json`
- System checks if user is VIP

### 2. Calculator (option 1)
- Addition, subtraction, multiplication, division
- Automatic result saving with timestamp
- History saved in `historia_kalkulatora.txt`

### 3. Calculator History (option 2)
- Display all previous calculations

### 4. Program Description (option 3)
- Version and author information
- VIP users list

### 5. Refresh (option 4)
- Clear console and refresh menu

### 6. VIP Panel (option 5)
- Add/remove users from VIP list
- Display VIP list

### 7. Mini Game (option 9)
- Game to find the key
- Controls: W/A/S/D
- Shows distance from target
- Counts number of moves

## Default Login Credentials

Check `uzytkownicy1.json`:
```json
{
  "admin": "admin123",
  "test": "test123"
}
```

## Notes

- Program requires `uzytkownicy1.json` to run
- Calculator history is saved automatically
- VIP system is saved after each change
- Some messages contain Polish characters (UTF-8)

## Author

Szymon Szturo - test project for learning Python
Created: 22.11.2025
