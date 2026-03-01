import msvcrt, time, sys, json, os
from colorama import Fore, init
from pathlib import Path

init(autoreset=True)
espace = ' '
red = Fore.LIGHTRED_EX
cyan = Fore.LIGHTCYAN_EX
yellow = Fore.LIGHTYELLOW_EX
green = Fore.LIGHTGREEN_EX
end = Fore.WHITE

def clear_buffer():
    while msvcrt.kbhit():
        msvcrt.getch()

def get_json_data(option_nb):
    base_dir = Path(__file__).resolve().parent  # dossier Modules
    json_path = base_dir.parent/"Data"/"help_text.json"
    
    with open(json_path, mode="r", encoding="utf-8") as read_file:
        data = json.load(read_file)
        return data[f"option{option_nb}"]

def is_selected(number, selected):
    if selected == number:
        return f'{green}--> '
    else:
        return '    '
    
def color(number, selected):
    if selected == number:
        return Fore.LIGHTGREEN_EX
    else:
        return ''

def get_help():
    global selected
    selected = 1
    os.system('cls')
    running = True
    while running:
        Continue = True
        print()
        print(f'{cyan}[?] For which option do you need to get informations on ?')
        options = f'''
{is_selected(1, selected)}{red}[{end}1{red}] {end}{color(1, selected)}System Infos{end}       {is_selected(10, selected)}{red}[{end}10{red}] {end}{color(10, selected)}Placeholder{end}
{is_selected(2, selected)}{red}[{end}2{red}] {end}{color(2, selected)}Password Checker{end}   {is_selected(11, selected)}{red}[{end}11{red}] {end}{color(11, selected)}Placeholder{end}
{is_selected(3, selected)}{red}[{end}3{red}] {end}{color(3, selected)}Placeholder{end}        {is_selected(12, selected)}{red}[{end}12{red}] {end}{color(12, selected)}Placeholder{end}
{is_selected(4, selected)}{red}[{end}4{red}] {end}{color(4, selected)}Placeholder{end}        {is_selected(13, selected)}{red}[{end}13{red}] {end}{color(13, selected)}Placeholder{end}
{is_selected(5, selected)}{red}[{end}5{red}] {end}{color(5, selected)}Placeholder{end}        {is_selected(14, selected)}{red}[{end}14{red}] {end}{color(14, selected)}Placeholder{end}
{is_selected(6, selected)}{red}[{end}6{red}] {end}{color(6, selected)}Placeholder{end}        {is_selected(15, selected)}{red}[{end}15{red}] {end}{color(15, selected)}Placeholder{end}
{is_selected(7, selected)}{red}[{end}7{red}] {end}{color(7, selected)}Placeholder{end}        {is_selected(16, selected)}{red}[{end}16{red}] {end}{color(16, selected)}Placeholder{end}
{is_selected(8, selected)}{red}[{end}8{red}] {end}{color(8, selected)}Placeholder{end}        {is_selected(17, selected)}{red}[{end}17{red}] {end}{color(17, selected)}Placeholder{end}
{is_selected(9, selected)}{red}[{end}9{red}] {end}{color(9, selected)}Placeholder{end}        {is_selected(18, selected)}{red}[{end}18{red}] {end}{color(18, selected)}Placeholder{end}
'''
        print(options)
        print(f'{green}[+] Use your Arrow keys to navigate between options (UP / DOWN / LEFT / RIGHT).')
        print(f'{green}[+] Press ENTER to confirm your choice.')
        print(f'{red}[!] Press ESC to go back.')
        
        while Continue:
            clear_buffer()
            key = msvcrt.getch()
            # Si touche spéciale (flèches, F1, etc.)
            if key in (b'\x00', b'\xe0'):
                key = msvcrt.getch()  # On lit le 2e caractère                       # IL RESTE A FAIRE EN SORTE DE NE PAS POUVOIR ECRIRE AUTRE CHOSE QUE CE QUI EST PREVU!!!
                if key == b'H': #UP
                    if selected > 1 and selected < 10:
                        selected -= 1
                    elif selected == 1:
                        selected = 9
                    elif selected > 10 and selected < 19:
                        selected -= 1
                    elif selected == 10:
                        selected = 18
                    Continue = False
                elif key == b'P': #DOWN
                    if selected > 0 and selected < 9:
                        selected += 1
                    elif selected > 9 and selected < 18:
                        selected += 1
                    elif selected == 18:
                        selected = 10
                    elif selected == 9:
                        selected = 1
                    Continue = False
                elif key == b'K': #LEFT
                    if selected > 9:
                        selected -= 9
                    else:
                        selected += 9
                    Continue = False
                elif key == b'M': #RIGHT
                    if selected < 10:
                        selected += 9
                    elif selected > 9 and selected < 19:
                        selected -= 9
                    else:
                        selected = 0
                    Continue = False

            elif key == b'\x1b':  # ESC
                running = False
                Continue = False
            elif key == b'\r':  # ENTER
                os.system('cls')
                print()
                print(f'{cyan}[?] Option {selected} selected, displaying the help message below :')
                print()
                print(get_json_data(selected))
                print()
                print(f'{red}[!] Press ESC to go back.')
                clear_buffer()
                while True:
                    key = msvcrt.getch()
                    if key == b'\x1b':
                        print()
                        Continue = False
                        break
                
        os.system('cls')
        clear_buffer()
