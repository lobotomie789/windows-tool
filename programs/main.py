import sys, time, os, random, string, requests, ipaddress, os, msvcrt
from colorama import Fore, init
from dotenv import load_dotenv

from about import about
from system_infos import infos_loop
from password_checker import password_checker

init(autoreset=True)
load_dotenv()

espace = ' '
options_list = ['a','0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27']
available_options = ['a','0','1','2']
cyan = Fore.LIGHTCYAN_EX
red = Fore.LIGHTRED_EX
yellow = Fore.LIGHTYELLOW_EX
end = Fore.WHITE

def restart():
    print(f'{red}[!] Press ENTER to go back.')
    clear_buffer()
    while True:
        key = msvcrt.getch()
        if key == b'\r':
            print()
            break
    os.system('cls')
    
def not_available():
    print()
    print(f'{red}[!] This feature is not available right now, please choose another one.')
    restart()

def clear_buffer():
    while msvcrt.kbhit():
        msvcrt.getch()
    
def limited_input(max_length):
    buffer = ''
    while True:
        key = msvcrt.getch()
        # ENTER
        if key == b'\r':
            print()
            return buffer
        # BACKSPACE
        elif key == b'\x08':
            if len(buffer) > 0:
                buffer = buffer[:-1]
                sys.stdout.write('\b \b')
                sys.stdout.flush()
        # Caractères normaux
        elif len(buffer) < max_length:
            try:
                char = key.decode('utf-8')
                # facultatif : bloquer espaces
                if char.isprintable() and not char.isspace():
                    buffer += char
                    sys.stdout.write(char)
                    sys.stdout.flush()
            except:
                pass

def main():

    featherine = red + fr'''
  _____ _____    _   _____ _   _ _____ ____   ___  _   _ _____
 |  ___| ____|  / \ |_   _| | | | ____|  _ \ |_ _|| \ | | ____|    _ __   _   _
 | |_  |  _|   /_ _\  | | | |_| |  _| | |_) | | | |  \| |  _|     | '_ \ | | | |
 |  _| | |___ / ___ \ | | |  _  | |___|  _ <  | | | |\  | |___    | |_) || |_| |
 |_|   |_____/_/   \_\|_| |_| |_|_____|_| \_\|___||_| \_|_____|(.)| .__/  \__, |
                                                                  |_|     |___/'''

    def main_panel():
        print(featherine)
        print(f'''
{red}[{end}!{red}] {end}Select an Option

{red}[{end}1{red}] {end}System Infos                  {red}[{end}10{red}] {end}/                             {red}[{end}19{red}] {end}/
{red}[{end}2{red}] {end}Password Checker              {red}[{end}11{red}] {end}/                             {red}[{end}20{red}] {end}/
{red}[{end}3{red}] {end}/                             {red}[{end}12{red}] {end}/                             {red}[{end}21{red}] {end}/
{red}[{end}4{red}] {end}/                             {red}[{end}13{red}] {end}/                             {red}[{end}22{red}] {end}/
{red}[{end}5{red}] {end}/                             {red}[{end}14{red}] {end}/                             {red}[{end}23{red}] {end}/
{red}[{end}6{red}] {end}/                             {red}[{end}15{red}] {end}/                             {red}[{end}24{red}] {end}/
{red}[{end}7{red}] {end}/                             {red}[{end}16{red}] {end}/                             {red}[{end}25{red}] {end}/
{red}[{end}8{red}] {end}/                             {red}[{end}17{red}] {end}/                             {red}[{end}26{red}] {end}/
{red}[{end}9{red}] {end}/                             {red}[{end}18{red}] {end}/                             {red}[{end}27{red}] {end}/

{red}[{end}a{red}]{end} About      {red}[{end}h{red}]{end} Help      {red}[{end}0{red}]{end} Exit''')        

# Affichage des options disponibles
    while True:
        os.system('cls')
        main_panel()
        print(f'''
[>]{espace}''', end='', flush=True)
        choix = limited_input(2)
        clear_buffer()

# Choix numéro 1 (System Infos)
        if choix == '1':
            os.system('cls')
            infos_loop()

# Choix numéro 2 (/)
        elif choix == '2':
            os.system('cls')
            password_checker()
            
# Choix autres : 'a' (Affichage des informations du programme)
        elif choix.lower() == 'a':
            os.system('cls')
            about()
            print()
            restart()

# Choix autres : 'h' (Affichage d'aide sur les options)
        elif choix.lower() == 'a':
            os.system('cls')
            
            print()
            restart()

# Choix numéro 0 (Fermeture du programme)
        elif choix == '0':
            os.system('cls')
            sys.exit(1)

# Choix non disponible pour le moment
        elif choix not in available_options and choix in options_list:
            not_available()

# Choix mal sélectionné
        else:
            print(f'''
{red}[-] The feature has been incorrectly selected, you may choose a correct one.''')
            restart()

### Lancement du programme
if __name__ == '__main__':
    main()
