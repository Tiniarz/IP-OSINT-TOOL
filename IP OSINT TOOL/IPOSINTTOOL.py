import os
import sys
import time
import random
import subprocess
from colorama import init, Fore

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def start_animation():
    clear_screen()
    try:
        columns, rows = os.get_terminal_size()
    except Exception:
        columns, rows = 80, 24

    chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']
    streams = [-1] * columns
    start_time = time.time()

    while time.time() - start_time < 20:
        output = []
        for col in range(columns):
            if streams[col] == -1:
                if random.random() < 0.05:
                    streams[col] = 0
            
            if streams[col] != -1:
                output.append(Fore.GREEN + random.choice(chars))
                streams[col] += 1
                if streams[col] >= rows or random.random() < 0.05:
                    streams[col] = -1
            else:
                output.append(" ")
        
        sys.stdout.write("".join(output) + "\n")
        sys.stdout.flush()
        time.sleep(0.05)
    
    clear_screen()

def slow_print(text, speed=0.05):
    for line in text.split('\n'):
        print(line)
        time.sleep(speed)

def execute_option(script_name):
    clear_screen()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(base_dir, "Program", script_name)
    try:
        subprocess.run([sys.executable, script_path])
    except Exception:
        pass

def main():
    start_animation()
    
    ascii_art = f"""{Fore.GREEN}
 ██▓ ██▓███      ▒█████    ██████  ██▓ ███▄    █ ▄▄▄█████▓    ▄▄▄█████▓ ▒█████   ▒█████   ██▓   
▓██▒▓██░  ██▒   ▒██▒  ██▒▒██    ▒ ▓██▒ ██ ▀█    █ ▓  ██▒ ▓▒    ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒   
▒██▒▓██░ ██▓▒   ▒██░  ██▒░ ▓██▄   ▒██▒▓██  ▀█ ██▒▒ ▓██░ ▒░    ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░   
░██░▒██▄█▓▒ ▒   ▒██   ██░  ▒   ██▒░██░▓██▒  ▐▌██▒░ ▓██▓ ░      ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░   
░██░▒██▒ ░  ░   ░ ████▓▒░▒██████▒▒░██░▒██░   ▓██░  ▒██▒ ░        ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
░▓  ▒▓▒░ ░  ░   ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ▒ ▒   ▒ ░░          ▒ ░░   ░ ▒░▒░▒░  ░ ▒░▒░▒░ ░ ▒░▓  ░
 ▒ ░░▒ ░          ░ ▒ ▒░ ░ ░▒  ░ ░ ▒ ░░ ░░   ░ ▒░    ░            ░       ░ ▒ ▒░    ░ ▒ ▒░ ░ ░ ▒  ░
 ▒ ░░░          ░ ░ ░ ▒  ░  ░  ░   ▒ ░   ░   ░ ░   ░            ░       ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
 ░                  ░ ░        ░   ░           ░                          ░ ░      ░ ░      ░  ░
    """
    
    menu_text = f"""{Fore.RED}
[01] IP Generator
[02] IP Lookup
[03] IP Pinger
[04] IP Port Scanner
[05] IP Scanner
    """
    
    slow_print(ascii_art, 0.05)
    slow_print(menu_text, 0.05)
    
    while True:
        choice = input(Fore.RED + "\nSelect an option: ").strip()
        
        if choice == "01":
            execute_option("01.py")
        elif choice == "02":
            execute_option("02.py")
        elif choice == "03":
            execute_option("03.py")
        elif choice == "04":
            execute_option("04.py")
        elif choice == "05":
            execute_option("05.py")

if __name__ == "__main__":
    main()