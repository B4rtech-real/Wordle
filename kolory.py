# ANSI escape codes for colors
GREEN = '\033[92m'
YELLOW = '\033[93m'
GRAY = '\033[90m'
RESET = '\033[0m'

def koloruj_litery(player_answer: str, check_list: list[int]) -> str:
    wynik = ""
    for litera, ocena in zip(player_answer, check_list):
        if ocena == 1:
            wynik += f"{GREEN}{litera.upper()}{RESET}"
        elif ocena == 0:
            wynik += f"{YELLOW}{litera.upper()}{RESET}"
        else:
            wynik += f"{GRAY}{litera.upper()}{RESET}"
    return wynik