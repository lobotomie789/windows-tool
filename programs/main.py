def main():
    import sys, time, os, random, string, requests, ipaddress, os, msvcrt
    import colorama
    from colorama import Fore
    from discord import SyncWebhook
    from dotenv import load_dotenv

    load_dotenv()

    colorama.init(autoreset=True)

    espace = ' '
    options_list = ["a","0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27"]
    available_options = ["a","0","1","2"]
    lightcyan = Fore.LIGHTCYAN_EX
    lightred = Fore.LIGHTRED_EX
    lightyellow = Fore.LIGHTYELLOW_EX
    end = Fore.WHITE

    featherine = lightred + fr'''
  _____ _____    _   _____ _   _ _____ ____   ___  _   _ _____
 |  ___| ____|  / \ |_   _| | | | ____|  _ \ |_ _|| \ | | ____|    _ __   _   _
 | |_  |  _|   /_ _\  | | | |_| |  _| | |_) | | | |  \| |  _|     | '_ \ | | | |
 |  _| | |___ / ___ \ | | |  _  | |___|  _ <  | | | |\  | |___    | |_) || |_| |
 |_|   |_____/_/   \_\|_| |_| |_|_____|_| \_\|___||_| \_|_____|(.)| .__/  \__, |
                                                                  |_|     |___/'''

    about = fr'''
 {lightred} _____ _____    _   _____ _   _ _____ ____   ___  _   _ _____
 {lightred}|  ___| ____|  / \ |_   _| | | | ____|  _ \ |_ _|| \ | | ____|    _ __   _   _
 {lightred}| |_  |  _|   /_ _\  | | | |_| |  _| | |_) | | | |  \| |  _|     | '_ \ | | | |
 {lightred}|  _| | |___ / ___ \ | | |  _  | |___|  _ <  | | | |\  | |___    | |_) || |_| |
 {lightred}|_|   |_____/_/   \_\|_| |_| |_|_____|_| \_\|___||_| \_|_____|(.)| .__/  \__, |
 {lightred}                                                                 |_|     |___/

{lightcyan}═════════ : CREDITS : ═════════
{lightyellow}Developper {end}: lobotomie789
{lightyellow}Discord {end}: @featherine.py

{lightcyan}═════════ : INFORMATIONS : ═════════
{lightyellow}Version       {end}: 1.0
{lightyellow}Creation Date {end}: 25/02/2026
{lightyellow}Last Update   {end}: 25/02/2026
{lightyellow}Dev Language  {end}: Python
{lightyellow}Description   {end}: Program with a multitude of usefull options.'''
        
    def main_panel():
        print(featherine)
        print(f'''
{lightred}[{end}!{lightred}] {end}Select an Option

{lightred}[{end}1{lightred}] {end}/                             {lightred}[{end}10{lightred}] {end}/                             {lightred}[{end}19{lightred}] {end}/
{lightred}[{end}2{lightred}] {end}/                             {lightred}[{end}11{lightred}] {end}/                             {lightred}[{end}20{lightred}] {end}/
{lightred}[{end}3{lightred}] {end}/                             {lightred}[{end}12{lightred}] {end}/                             {lightred}[{end}21{lightred}] {end}/
{lightred}[{end}4{lightred}] {end}/                             {lightred}[{end}13{lightred}] {end}/                             {lightred}[{end}22{lightred}] {end}/
{lightred}[{end}5{lightred}] {end}/                             {lightred}[{end}14{lightred}] {end}/                             {lightred}[{end}23{lightred}] {end}/
{lightred}[{end}6{lightred}] {end}/                             {lightred}[{end}15{lightred}] {end}/                             {lightred}[{end}24{lightred}] {end}/
{lightred}[{end}7{lightred}] {end}/                             {lightred}[{end}16{lightred}] {end}/                             {lightred}[{end}25{lightred}] {end}/
{lightred}[{end}8{lightred}] {end}/                             {lightred}[{end}17{lightred}] {end}/                             {lightred}[{end}26{lightred}] {end}/
{lightred}[{end}9{lightred}] {end}/                             {lightred}[{end}18{lightred}] {end}/                             {lightred}[{end}27{lightred}] {end}/

{lightyellow}[{end}a{lightyellow}]{end} About      {lightyellow}[{end}0{lightyellow}]{end} Exit''')        
        
    def restart():
        print(f"{lightred}[!] Press ENTER to restart the program.")
        while True:
            key = msvcrt.getch()
            if key == b'\r':
                print()
                break
        os.system("cls")
            
    def not_available():
        print()
        print(f'{lightred}[!] This feature is not available right now, please choose another one.')
        restart()
        
    def limited_input(max_length):
        buffer = ""

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
                    char = key.decode("utf-8")

                    # facultatif : bloquer espaces
                    if char.isprintable() and not char.isspace():
                        buffer += char
                        sys.stdout.write(char)
                        sys.stdout.flush()
                except:
                    pass

# Affichage des options disponibles
    while True:
        os.system("cls")
        main_panel()
        print(f'''
[>]{espace}''', end="", flush=True)
        choix = limited_input(2)

# Choix numéro 1 (Env generator)
        if choix == "1":
            os.system("cls")
            print(f'''
{lightcyan}''')

# Choix numéro 2 (/)
        elif choix == "2":
            not_available()
            
# Choix autres : "a" (Affichage des informations du programme)
        elif choix == "a":
            os.system("cls")
            print(about)
            print()
            restart()

# Choix numéro 0 (Fermeture du programme)
        elif choix == "0":
            os.system("cls")
            sys.exit(1)

# Choix non disponible pour le moment
        elif choix not in available_options and choix in options_list:
            not_available()

# Choix mal sélectionné
        else:
            print(f'''
{lightred}[-] The feature has been incorrectly selected, you may choose a correct one.''')
            restart()

### Lancement du programme
if __name__ == "__main__":
    main()
