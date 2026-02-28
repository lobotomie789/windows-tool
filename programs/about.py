from colorama import Fore, init

init(autoreset=True)
red = Fore.LIGHTRED_EX
cyan = Fore.LIGHTCYAN_EX
yellow = Fore.LIGHTYELLOW_EX
end = Fore.WHITE
version = "1.1.0"

def about():
    print(fr'''
 {red} _____ _____    _   _____ _   _ _____ ____   ___  _   _ _____
 {red}|  ___| ____|  / \ |_   _| | | | ____|  _ \ |_ _|| \ | | ____|    _ __   _   _
 {red}| |_  |  _|   /_ _\  | | | |_| |  _| | |_) | | | |  \| |  _|     | '_ \ | | | |
 {red}|  _| | |___ / ___ \ | | |  _  | |___|  _ <  | | | |\  | |___    | |_) || |_| |
 {red}|_|   |_____/_/   \_\|_| |_| |_|_____|_| \_\|___||_| \_|_____|(.)| .__/  \__, |
 {red}                                                                 |_|     |___/

{cyan}═════════ : CREDITS : ═════════{end}
Developper : {yellow}lobotomie789{end}
Discord    : {yellow}@featherine.py{end}

{cyan}═════════ : INFORMATIONS : ═════════{end}
Version       : {yellow}{version}{end}
Creation Date : {yellow}25/02/2026{end}
Last Update   : {yellow}28/02/2026{end}
Dev Language  : {yellow}Python{end}
Description   : {yellow}Program with a multitude of usefull options.{end}''')
