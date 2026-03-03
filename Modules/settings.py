import msvcrt, time, sys, json, os
from colorama import Fore, init
from pathlib import Path

init(autoreset=True)
espace = ' '
red = Fore.RED
lightred = Fore.LIGHTRED_EX
blue = Fore.BLUE
lightblue = Fore.LIGHTBLUE_EX
green = Fore.GREEN
lightgreen = Fore.LIGHTGREEN_EX
cyan = Fore.CYAN
lightcyan = Fore.LIGHTCYAN_EX
lightmagenta = Fore.LIGHTMAGENTA_EX
yellow = Fore.LIGHTYELLOW_EX
end = Fore.WHITE

base_dir = Path(__file__).resolve().parent  # dossier Modules
json_path = base_dir.parent/"Data"/"settings.json"

all_settings = {
    1: "return",
    2: "validate",
    3: "mainColor",
    4: "otherColor",
    5: "placeholder",
    6: "placeholder",
    7: "placeholder",
    8: "placeholder",
    9: "placeholder",
}

key_values = {
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

key_code = {
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

color_values = {
    1: "RED",
    2: "LIGHTRED",
    3: "BLUE",
    4: "LIGHTBLUE",
    5: "GREEN",
    6: "LIGHTGREEN",
    7: "CYAN",
    8: "LIGHTCYAN",
    9: "LIGHTMAGENTA",
}

color_codes = {
    "RED": red,
    "LIGHTRED": lightred,
    "BLUE": blue,
    "LIGHTBLUE": lightblue,
    "GREEN": green,
    "LIGHTGREEN": lightgreen,
    "CYAN": cyan,
    "LIGHTCYAN": lightcyan,
    "LIGHTMAGENTA": lightmagenta,
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

MC = color_codes[get_setting("mainColor")]
OC = color_codes[get_setting("otherColor")]

def is_selected(number, selected):
    global OC
    if selected == number:
        return f'{OC}--> '
    else:
        return '    '
    
def color(number, selected):
    global OC
    if selected == number:
        return OC
    else:
        return ''

def upArrow(var):
    if var > 1 and var < 10:
        var -= 1
    elif var == 1:
        var = 9
    elif var > 10 and var < 19:
        var -= 1
    elif var == 10:
        var = 18
    return var
        
def downArrow(var):
    if var > 0 and var < 9:
        var += 1
    elif var > 9 and var < 18:
        var += 1
    elif var == 18:
        var = 10
    elif var == 9:
        var = 1
    return var
    
def manage_settings():
    global selected, MC, OC
    selected = 1
    os.system('cls')
    ring0 = True
    
    while ring0:
        ring1 = True
        print(f'''
{lightcyan}[?] Which parameter do you wish to edit the value of ?{end}

{is_selected(1, selected)}{MC}[{end}1{MC}] {end}{color(1, selected)}Return back{yellow} ({get_setting("return")}){end}
{is_selected(2, selected)}{MC}[{end}2{MC}] {end}{color(2, selected)}Validate choice{end}{yellow} ({get_setting("validate")}){end}
{is_selected(3, selected)}{MC}[{end}3{MC}] {end}{color(3, selected)}Main Color{end}{yellow} ({get_setting("mainColor")}){end}
{is_selected(4, selected)}{MC}[{end}5{MC}] {end}{color(4, selected)}Others Colors{end}{yellow} ({get_setting("otherColor")}){end}
{is_selected(5, selected)}{MC}[{end}6{MC}] {end}{color(5, selected)}Placeholder{end}{yellow} ({get_setting("placeholder")}){end}
{is_selected(6, selected)}{MC}[{end}7{MC}] {end}{color(6, selected)}Placeholder{end}{yellow} ({get_setting("placeholder")}){end}
{is_selected(7, selected)}{MC}[{end}8{MC}] {end}{color(7, selected)}Placeholder{end}{yellow} ({get_setting("placeholder")}){end}
{is_selected(8, selected)}{MC}[{end}9{MC}] {end}{color(8, selected)}Placeholder{end}{yellow} ({get_setting("placeholder")}){end}
{is_selected(9, selected)}{MC}[{end}9{MC}] {end}{color(9, selected)}Placeholder{end}{yellow} ({get_setting("placeholder")}){end}

{OC}[+] Use your Arrow keys to navigate between options (UP / DOWN).
{OC}[+] Press ENTER to confirm your choice.
{MC}[!] Press ESC to go back.''')
        
        while ring1:
            MC = color_codes[get_setting("mainColor")]
            OC = color_codes[get_setting("otherColor")]
            clear_buffer()
            key = msvcrt.getch()
            # Si touche spéciale (flèches, F1, etc.)
            if key in (b'\x00', b'\xe0'):
                key = msvcrt.getch()  # On lit le 2e caractère
                if key == b'H': #UP
                    selected = upArrow(selected)
                    ring1 = False
                elif key == b'P': #DOWN
                    selected = downArrow(selected)
                    ring1 = False
            
            elif key == b'\x1b':  # ESC
                ring0, ring1 = False, False
                
            elif key == b'\r':  # ENTER
                def CurrentValue(value):
                    if get_setting(all_settings[selected]) == value:
                        return "(Active)"
                    else:
                        return ''
                    
                def isTaken(value):
                    settings = load_settings().values()
                    if value in settings and get_setting(all_settings[selected]) != value:
                        return "(Taken)"
                    else:
                        return ''
                    
                os.system('cls')
                ring2 = True
                new_option = 1
                
                while ring2:
                    if selected != 3:
                        ring3 = True
                        print(f'''
{lightcyan}[?] Option {selected} selected, please choose the new value.{end}

Current {yellow}{all_settings[selected]}{end} value : {OC}{get_setting(all_settings[selected])}{end}
Available values :

{is_selected(1, new_option)}{MC}[{end}1{MC}] {end}{color(1, new_option)}ESC{end} {yellow}{CurrentValue("ESC")}{red}{isTaken("ESC")}
{is_selected(2, new_option)}{MC}[{end}2{MC}] {end}{color(2, new_option)}BACKSPACE{end} {yellow}{CurrentValue("BACKSPACE")}{red}{isTaken("BACKSPACE")}
{is_selected(3, new_option)}{MC}[{end}3{MC}] {end}{color(3, new_option)}TAB{end} {yellow}{CurrentValue("TAB")}{red}{isTaken("TAB")}
{is_selected(4, new_option)}{MC}[{end}4{MC}] {end}{color(4, new_option)}ENTER{end} {yellow}{CurrentValue("ENTER")}{red}{isTaken("ENTER")}
{is_selected(5, new_option)}{MC}[{end}5{MC}] {end}{color(5, new_option)}R{end} {yellow}{CurrentValue("R")}{red}{isTaken("R")}
{is_selected(6, new_option)}{MC}[{end}6{MC}] {end}{color(6, new_option)}T{end} {yellow}{CurrentValue("T")}{red}{isTaken("T")}
{is_selected(7, new_option)}{MC}[{end}7{MC}] {end}{color(7, new_option)}Q{end} {yellow}{CurrentValue("Q")}{red}{isTaken("Q")}
{is_selected(8, new_option)}{MC}[{end}8{MC}] {end}{color(8, new_option)}X{end} {yellow}{CurrentValue("X")}{red}{isTaken("X")}
{is_selected(9, new_option)}{MC}[{end}9{MC}] {end}{color(9, new_option)}G{end} {yellow}{CurrentValue("G")}{red}{isTaken("G")}

{OC}[+] Use your Arrow keys to navigate between options (UP / DOWN).
{OC}[+] Press ENTER to confirm your choice.
{MC}[!] Press ESC to go back.''')

                        while ring3:
                            clear_buffer()
                            key = msvcrt.getch()
                            # Si touche spéciale (flèches, F1, etc.)
                            if key in (b'\x00', b'\xe0'):
                                key = msvcrt.getch()  # On lit le 2e caractère
                                if key == b'H': #UP
                                    new_option = upArrow(new_option)
                                    ring3 = False
                                elif key == b'P': #DOWN
                                    new_option = downArrow(new_option)
                                    ring3 = False

                            elif key == b'\x1b':  # ESC
                                ring1, ring2, ring3 = False, False, False

                            elif key == b'\r':  # ENTER
                                settings = load_settings().values()
                                if key_values[new_option] in settings and get_setting(all_settings[selected]) == key_values[new_option]:
                                    pass
                                elif key_values[new_option] in settings and get_setting(all_settings[selected]) != key_values[new_option]:
                                    pass
                                else:
                                    set_setting(all_settings[selected], key_values[new_option])
                                    ring3 = False
                                    MC = color_codes[get_setting("mainColor")]                  # FAIRE EN SORTE D'ACTUALISER LA COULEUR A CHAQUE CHANGEMENT DE COULEUR DU PANEL
                                    OC = color_codes[get_setting("otherColor")]                 # FAIRE EN SORTE D'ACTUALISER LA COULEUR A CHAQUE CHANGEMENT DE COULEUR DU PANEL
                                    os.system('cls')
                                    clear_buffer()

                        os.system('cls')
                        clear_buffer()
                        
                    else: # Si c'est l'option de la couleur
                        ring3 = True
                        print(f'''
{lightcyan}[?] Option {selected} selected, please choose the new value.{end}

Current {yellow}{all_settings[selected]}{end} value : {OC}{get_setting(all_settings[selected])}{end}
Available values :

{is_selected(1, new_option)}{MC}[{end}1{MC}] {end}{color(1, new_option)}RED{end} {yellow}{CurrentValue("RED")}{red}{isTaken("RED")}
{is_selected(2, new_option)}{MC}[{end}2{MC}] {end}{color(2, new_option)}LIGHTRED{end} {yellow}{CurrentValue("LIGHTRED")}{red}{isTaken("LIGHTRED")}
{is_selected(3, new_option)}{MC}[{end}3{MC}] {end}{color(3, new_option)}BLUE{end} {yellow}{CurrentValue("BLUE")}{red}{isTaken("BLUE")}
{is_selected(4, new_option)}{MC}[{end}4{MC}] {end}{color(4, new_option)}LIGHTBLUE{end} {yellow}{CurrentValue("LIGHTBLUE")}{red}{isTaken("LIGHTBLUE")}
{is_selected(5, new_option)}{MC}[{end}5{MC}] {end}{color(5, new_option)}GREEN{end} {yellow}{CurrentValue("OC")}{red}{isTaken("OC")}
{is_selected(6, new_option)}{MC}[{end}6{MC}] {end}{color(6, new_option)}LIGHTGREEN{end} {yellow}{CurrentValue("LIGHTGREEN")}{red}{isTaken("LIGHTGREEN")}
{is_selected(7, new_option)}{MC}[{end}7{MC}] {end}{color(7, new_option)}CYAN{end} {yellow}{CurrentValue("CYAN")}{red}{isTaken("CYAN")}
{is_selected(8, new_option)}{MC}[{end}8{MC}] {end}{color(8, new_option)}LIGHTCYAN{end} {yellow}{CurrentValue("LIGHTCYAN")}{red}{isTaken("LIGHTCYAN")}
{is_selected(9, new_option)}{MC}[{end}9{MC}] {end}{color(9, new_option)}LIGHTMAGENTA{end} {yellow}{CurrentValue("LIGHTMAGENTA")}{red}{isTaken("LIGHTMAGENTA")}

{OC}[+] Use your Arrow keys to navigate between options (UP / DOWN).
{OC}[+] Press ENTER to confirm your choice.
{MC}[!] Press ESC to go back.''')

                        while ring3:
                            clear_buffer()
                            key = msvcrt.getch()
                            # Si touche spéciale (flèches, F1, etc.)
                            if key in (b'\x00', b'\xe0'):
                                key = msvcrt.getch()  # On lit le 2e caractère
                                if key == b'H': #UP
                                    new_option = upArrow(new_option)
                                    ring3 = False
                                elif key == b'P': #DOWN
                                    new_option = downArrow(new_option)
                                    ring3 = False

                            elif key == b'\x1b':  # ESC
                                ring1, ring2, ring3 = False, False, False

                            elif key == b'\r':  # ENTER
                                settings = load_settings().values()
                                if key_values[new_option] in settings and get_setting(all_settings[selected]) == key_values[new_option]:
                                    pass
                                elif key_values[new_option] in settings and get_setting(all_settings[selected]) != key_values[new_option]:
                                    pass
                                else:
                                    set_setting(all_settings[selected], color_values[new_option])
                                    ring3 = False
                                    os.system('cls')
                                    clear_buffer()

                        os.system('cls')
                        clear_buffer()

        os.system('cls')
        clear_buffer()
