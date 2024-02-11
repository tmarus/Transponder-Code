from colorama import init, Back, Style, Fore
init()
a = int(input(Back.GREEN + Style.BRIGHT + Fore.LIGHTBLACK_EX + "Wpisz swój kod: "))


if a == 7700:
    print(Back.RED + f"ALARM: Samolot zgłosił zagrożenie ogólne: {a}")
elif a == 7600:
    print(Back.MAGENTA + f"UWAGA: Samolot zgłosił utratę łączności radiowej: {a}")
elif a == 7500:
    print(Back.MAGENTA + f"UWAGA: Samolot zgłosił porwanie samolotu: {a}")
elif a == 2000:
    print(Back.YELLOW + f"UWAGA: Samolot zgłosił, że jest w locie IFR: {a}")
elif a == 1200:
    print(Back.BLUE + f"UWAGA: Samolot zgłosił, że jest w locie VFR: {a}")
elif a == 7000:
    print(Back.BLUE + f"UWAGA: Samolot zgłosił, że jest w locie VFR: {a}")
else:
    print(Back.CYAN + f"Kod: {a} nie jest rozpoznany.")
