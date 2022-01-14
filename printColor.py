import colorama

def red(text):
    print(colorama.Fore.RED + text + colorama.Fore.RESET)

def green(text):
    print(colorama.Fore.GREEN + text + colorama.Fore.RESET)

def blue(text):
    print(colorama.Fore.BLUE + text + colorama.Fore.RESET)

def yellow(text):
    print(colorama.Fore.YELLOW + text + colorama.Fore.RESET)

def cyan(text):
    print(colorama.Fore.CYAN + text + colorama.Fore.RESET)
    
def magenta(text):
    print(colorama.Fore.MAGENTA + text + colorama.Fore.RESET)

def white(text):
    print(colorama.Fore.WHITE + text + colorama.Fore.RESET)

def black(text):
    print(colorama.Fore.BLACK + text + colorama.Fore.RESET)

def grey(text):
    print(colorama.Fore.LIGHTBLACK_EX + text + colorama.Fore.RESET)

def lightgrey(text):
    print(colorama.Fore.LIGHTBLACK_EX + text + colorama.Fore.RESET)

def lightred(text):
    print(colorama.Fore.LIGHTRED_EX + text + colorama.Fore.RESET)

def lightgreen(text):
    print(colorama.Fore.LIGHTGREEN_EX + text + colorama.Fore.RESET)

def lightblue(text):
    print(colorama.Fore.LIGHTBLUE_EX + text + colorama.Fore.RESET)

def lightyellow(text):
    print(colorama.Fore.LIGHTYELLOW_EX + text + colorama.Fore.RESET)

def lightcyan(text):
    print(colorama.Fore.LIGHTCYAN_EX + text + colorama.Fore.RESET)

def lightmagenta(text):
    print(colorama.Fore.LIGHTMAGENTA_EX + text + colorama.Fore.RESET)

def getInput(text,color):
    color(text)
    return input()