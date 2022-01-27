# Instructions
#e.g colorama
#pip install colorama
#pip3 install colorama       for python3

# accessing external python module

import colorama
from colorama import Fore, Back, Style

colorama.init()
message = "hello world from python"

print(message)
print(Fore.RED + message)
print(Fore.GREEN + message)
print(Fore.BLUE + message)
print(Fore.RED + Back.YELLOW + message + Style.RESET_ALL)