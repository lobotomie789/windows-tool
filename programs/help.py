import msvcrt, os, time, sys
from colorama import Fore, init
from main import clear_buffer

init(autoreset=True)
espace = ' '
red = Fore.LIGHTRED_EX
cyan = Fore.LIGHTCYAN_EX
yellow = Fore.LIGHTYELLOW_EX
green = Fore.LIGHTGREEN_EX
end = Fore.WHITE

selected = 1
needs_refresh = True

def is_selected(number):
    if selected == number:
        return f'{cyan}--> '
    else:
        return '    '
    
def color(number):
    if selected == number:
        return Fore.LIGHTCYAN_EX
    else:
        return ''

def help():
    global selected
    os.system('cls')
    while True:
        print()
        options = f'''
{is_selected(1)}{red}[{end}1{red}] {color(1)}System Infos{end}       {is_selected(10)}{red}[{end}10{red}] {color(10)}Placeholder{end}
{is_selected(2)}{red}[{end}2{red}] {color(2)}Password Checker{end}   {is_selected(11)}{red}[{end}11{red}] {color(11)}Placeholder{end}
{is_selected(3)}{red}[{end}3{red}] {color(3)}Placeholder{end}        {is_selected(12)}{red}[{end}12{red}] {color(12)}Placeholder{end}
{is_selected(4)}{red}[{end}4{red}] {color(4)}Placeholder{end}        {is_selected(13)}{red}[{end}13{red}] {color(13)}Placeholder{end}
{is_selected(5)}{red}[{end}5{red}] {color(5)}Placeholder{end}        {is_selected(14)}{red}[{end}14{red}] {color(14)}Placeholder{end}
{is_selected(6)}{red}[{end}6{red}] {color(6)}Placeholder{end}        {is_selected(15)}{red}[{end}15{red}] {color(15)}Placeholder{end}
{is_selected(7)}{red}[{end}7{red}] {color(7)}Placeholder{end}        {is_selected(16)}{red}[{end}16{red}] {color(16)}Placeholder{end}
{is_selected(8)}{red}[{end}8{red}] {color(8)}Placeholder{end}        {is_selected(17)}{red}[{end}17{red}] {color(17)}Placeholder{end}
{is_selected(9)}{red}[{end}9{red}] {color(9)}Placeholder{end}        {is_selected(18)}{red}[{end}18{red}] {color(18)}Placeholder{end}
'''
        print(options)
        print()
        print(f'{cyan}[?] For which option do you need to get informations ?')
        print(f'{green}[+] Use your Arrow keys to navigate between options (UP / DOWN).')
        print(f'{green}[+] Press ENTER to confirm your choice.')
        print(f'{red}[!] Press ESC to go back.')
        
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
            elif key == b'P': #DOWN
                if selected > 0 and selected < 9:
                    selected += 1
                elif selected > 9 and selected < 18:
                    selected += 1
                elif selected == 18:
                    selected = 10
                elif selected == 9:
                    selected = 1
            elif key == b'K': #LEFT
                if selected > 9:
                    selected -= 9
                else:
                    selected += 9
            elif key == b'M': #RIGHT
                if selected < 10:
                    selected += 9
                elif selected > 9 and selected < 19:
                    selected -= 9
                else:
                    selected = 0
            else:
                pass

        elif key == b'\x1b':  # ESC
            break
        elif key == b'\r':  # ENTER
            print()
            print(f'Option {selected} selected.')
            time.sleep(0.5)
        else:
            pass
        os.system('cls')
help()
