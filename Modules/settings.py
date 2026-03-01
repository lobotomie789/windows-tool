import msvcrt, time, sys, json, os
from colorama import Fore, init
from pathlib import Path
from help_option import is_selected, color

init(autoreset=True)
espace = ' '
red = Fore.LIGHTRED_EX
cyan = Fore.LIGHTCYAN_EX
yellow = Fore.LIGHTYELLOW_EX
green = Fore.LIGHTGREEN_EX
end = Fore.WHITE

base_dir = Path(__file__).resolve().parent  # dossier Modules
json_path = base_dir.parent/"Data"/"settings.json"

all_values = {
    1: "return",
    2: "validate",
    3: "color",
    4: "placeholder",
    5: "placeholder",
    6: "placeholder",
    7: "placeholder",
    8: "placeholder",
    9: "placeholder",
}

classic_values = {
    1: "ESC",
    2: "BACKSPACE",
    3: "TAB",
    4: "ENTER",
    5: "R",
    6: "T",
    7: "Q",
    8: "X",
    9: "G",
}

keys_code = {
    "ESC": b'\x1b',
    "BACKSPACE": b'\x08',
    "TAB": b'\t',
    "ENTER": b'\r',
    "R": b'r',
    "T": b't',
    "Q": b'q',
    "X": b'x',
    "G": b'g',
}

def clear_buffer():
    while msvcrt.kbhit():
        msvcrt.getch()

def load_settings():
    with open(json_path, "r", encoding="utf-8") as read_file:
        return json.load(read_file)
    
def save_settings(settings_dict):
    with open(json_path, "w", encoding="utf-8") as save_file:
        json.dump(settings_dict, save_file, indent=4, ensure_ascii=False)
        
def set_setting(key, value):
    settings = load_settings()
    settings[key] = value
    save_settings(settings)
    
def get_setting(key, default=None):
    settings = load_settings()
    return settings.get(key, default)
    
def manage_settings():
    global selected
    selected = 1
    os.system('cls')
    running = True
    while running:
        Continue = True
        print()
        print(f'{cyan}[?] Which parameter do you wish to edit the value of ?')
        options = f'''
{is_selected(1, selected)}{red}[{end}1{red}] {end}{color(1, selected)}Return back key {yellow}({get_setting("return")}){end}
{is_selected(2, selected)}{red}[{end}2{red}] {end}{color(2, selected)}Validate choice key{end} {yellow}({get_setting("validate")}){end}
{is_selected(3, selected)}{red}[{end}3{red}] {end}{color(3, selected)}Main program color{end} {yellow}({get_setting("color")}){end}
{is_selected(4, selected)}{red}[{end}4{red}] {end}{color(4, selected)}Placeholder{end}
{is_selected(5, selected)}{red}[{end}5{red}] {end}{color(5, selected)}Placeholder{end}
{is_selected(6, selected)}{red}[{end}6{red}] {end}{color(6, selected)}Placeholder{end}
{is_selected(7, selected)}{red}[{end}7{red}] {end}{color(7, selected)}Placeholder{end}
{is_selected(8, selected)}{red}[{end}8{red}] {end}{color(8, selected)}Placeholder{end}
{is_selected(9, selected)}{red}[{end}9{red}] {end}{color(9, selected)}Placeholder{end}
'''
        print(options)
        print(f'{green}[+] Use your Arrow keys to navigate between options (UP / DOWN).')
        print(f'{green}[+] Press ENTER to confirm your choice.')
        print(f'{red}[!] Press ESC to go back.')
        
        while Continue:
            clear_buffer()
            key = msvcrt.getch()
            # Si touche spéciale (flèches, F1, etc.)
            if key in (b'\x00', b'\xe0'):
                key = msvcrt.getch()  # On lit le 2e caractère
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
            
            elif key == b'\x1b':  # ESC
                running = False
                Continue = False
            elif key == b'\r':  # ENTER
                def CurrentValue(value):
                    if get_setting(all_values[selected]) == value:
                        return "(Active)"
                    else:
                        return ''
                def isTaken(value):
                    settings = load_settings().values()
                    if value in settings and get_setting(all_values[selected]) != value:
                        return "(Taken)"
                    else:
                        return ''
                    
                os.system('cls')
                running2 = True
                new_option = 1
                while running2:
                    Continue2 = True
                    print()
                    print(f'{cyan}[?] Option {selected} selected, please choose the new value.')
                    print()
                    print(f'Current {yellow}{all_values[selected]}{end} value : {green}{get_setting(all_values[selected])}')
                    print(f'Available values :')
                    options = f'''
{is_selected(1, new_option)}{red}[{end}1{red}] {end}{color(1, new_option)}ESC{end} {yellow}{CurrentValue("ESC")}{red}{isTaken("ESC")}
{is_selected(2, new_option)}{red}[{end}2{red}] {end}{color(2, new_option)}BACKSPACE{end} {yellow}{CurrentValue("BACKSPACE")}{red}{isTaken("BACKSPACE")}
{is_selected(3, new_option)}{red}[{end}3{red}] {end}{color(3, new_option)}TAB{end} {yellow}{CurrentValue("TAB")}{red}{isTaken("TAB")}
{is_selected(4, new_option)}{red}[{end}4{red}] {end}{color(4, new_option)}ENTER{end} {yellow}{CurrentValue("ENTER")}{red}{isTaken("ENTER")}
{is_selected(5, new_option)}{red}[{end}5{red}] {end}{color(5, new_option)}R{end} {yellow}{CurrentValue("R")}{red}{isTaken("R")}
{is_selected(6, new_option)}{red}[{end}6{red}] {end}{color(6, new_option)}T{end} {yellow}{CurrentValue("T")}{red}{isTaken("T")}
{is_selected(7, new_option)}{red}[{end}7{red}] {end}{color(7, new_option)}Q{end} {yellow}{CurrentValue("Q")}{red}{isTaken("Q")}
{is_selected(8, new_option)}{red}[{end}8{red}] {end}{color(8, new_option)}X{end} {yellow}{CurrentValue("X")}{red}{isTaken("X")}
{is_selected(9, new_option)}{red}[{end}9{red}] {end}{color(9, new_option)}G{end} {yellow}{CurrentValue("G")}{red}{isTaken("G")}
'''
                    print(options)
                    print()
                    print(f'{green}[+] Use your Arrow keys to navigate between options (LEFT / RIGHT).')
                    print(f'{green}[+] Press ENTER to confirm your choice.')
                    print(f'{red}[!] Press ESC to go back.')
                    while Continue2:
                        clear_buffer()
                        key = msvcrt.getch()
                        # Si touche spéciale (flèches, F1, etc.)
                        if key in (b'\x00', b'\xe0'):
                            key = msvcrt.getch()  # On lit le 2e caractère                       # IL RESTE A FAIRE EN SORTE DE NE PAS POUVOIR ECRIRE AUTRE CHOSE QUE CE QUI EST PREVU!!!
                            if key == b'H': #UP
                                if new_option > 1 and new_option < 10:
                                    new_option -= 1
                                elif new_option == 1:
                                    new_option = 9
                                elif new_option > 10 and new_option < 19:
                                    new_option -= 1
                                elif new_option == 10:
                                    new_option = 18
                                Continue2 = False
                            elif key == b'P': #DOWN
                                if new_option > 0 and new_option < 9:
                                    new_option += 1
                                elif new_option > 9 and new_option < 18:
                                    new_option += 1
                                elif new_option == 18:
                                    new_option = 10
                                elif new_option == 9:
                                    new_option = 1
                                Continue2 = False

                        elif key == b'\x1b':  # ESC
                            running2 = False
                            Continue2 = False
                            Continue = False
                        elif key == b'\r':  # ENTER
                            settings = load_settings().values()
                            if classic_values[new_option] in settings and get_setting(all_values[selected]) == classic_values[new_option]:
                                pass
                            elif classic_values[new_option] in settings and get_setting(all_values[selected]) != classic_values[new_option]:
                                pass
                            else:
                                set_setting(all_values[selected], classic_values[new_option])
                                Continue2 = False
                                os.system('cls')
                                clear_buffer()

                    os.system('cls')
                    clear_buffer()

        os.system('cls')
        clear_buffer()
