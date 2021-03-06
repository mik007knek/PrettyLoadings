import os
import time


def text_expansion(text: str, times: int = 2, clear: bool = False):
    r"""
    Example:

    t->te->tex->text->tex->te->t

    (example for text == `text`, times == 2)
    """
    clear = 'clear' if clear else 'cls'
    for j in range(times):
        if j % 2 == 0:
            for i in range(len(text) + 1):
                print(text[:i])
                time.sleep(0.2)
                os.system(clear)
        else:
            for i in range(1, len(text)):
                print(text[:len(text) - i])
                time.sleep(0.2)
                os.system(clear)


def symbol_expansion(symbol: str, kol: int = 10, times: int = 2, clear: bool = False):
    r"""
    Example:

    %->%%->%%%->%%%%->%%%->%%->%

    (example for symbol == `%`, kol == 4, times == 2)
    """
    clear = 'clear' if clear else 'cls'
    text = symbol * kol
    for j in range(times):
        if j % 2 == 0:
            for i in range(1, len(text)):
                print(text[:i])
                time.sleep(0.2)
                os.system(clear)
        else:
            for i in range(len(text)):
                print(text[:len(text) - i])
                time.sleep(0.2)
                os.system(clear)


def dot_circling(times: int = 2, clear: bool = False):
    r"""
    Example:

    '-'->'\'->'|'->'/'->'-'->'\'->'|'->'/'

    (example for times == 2)
    """
    clear = 'clear' if clear else 'cls'
    for j in range(times):
        for i in range(4):
            if i == 0:
                print('-')
            elif i == 1:
                print('\\')
            elif i == 2:
                print('|')
            else:
                print('/')
            time.sleep(0.2)
            os.system(clear)


def line_circling(kol: int = 10, times: int = 2, clear: bool = False):
    r"""
    Example:

    '\'->'||'->'///'->'----'->'\\\'->'|'->'/'

     (example for times == 2, kol == 4)
    """
    clear = 'clear' if clear else 'cls'
    for j in range(times):
        if j % 2 == 0:
            for i in range(1, kol):
                if i % 4 == 0:
                    symbol = '-'
                elif i % 4 == 1:
                    symbol = '\\'
                elif i % 4 == 2:
                    symbol = '|'
                else:
                    symbol = '/'
                print(symbol * i)
                time.sleep(0.2)
                os.system(clear)
        else:
            for i in range(kol):
                if i % 4 == 0:
                    symbol = '-'
                elif i % 4 == 1:
                    symbol = '\\'
                elif i % 4 == 2:
                    symbol = '|'
                else:
                    symbol = '/'
                print(symbol * (kol - i))
                time.sleep(0.2)
                os.system(clear)


def owl_dancer(times: int = 3, sleep: int = 0.5, clear: bool = False):
    r"""
    Example:

    (@>@)    (@>@)    (@>@)    (@>@)
    \) )\ -> /| |\ -> /( (/ -> /| |\
     / \      / \      / \      / \

    (example for times == 1)
    """
    clear = 'clear' if clear else 'cls'
    for j in range(times):
        print("(@>@)\n\\) )\\\n / \\")
        time.sleep(sleep)
        os.system(clear)
        print("(@>@)\n/| |\\\n / \\")
        time.sleep(sleep)
        os.system(clear)
        print("(@>@)\n/( (/\n / \\")
        time.sleep(sleep)
        os.system(clear)
        print("(@>@)\n/| |\\\n / \\")
        time.sleep(sleep)
        os.system(clear)


def human_gymnast(times: int = 2, sleep: int = 0.5, clear: bool = False):
    r"""
    Example:

     0              \ /             0
    /|\ ->  ___0 ->  | ->  ___0 -> /|\
    / \    /\ /\    /0\   /\ /\    / \

    (example for times == 1)
    """
    clear = 'clear' if clear else 'cls'
    for j in range(times):
        if j % 2 == 0:
            print(" 0 \n/|\\\n/ \\")
            time.sleep(sleep)
            os.system(clear)
            print("\n ___0\n/\\ /\\")
            time.sleep(sleep)
            os.system(clear)
            print("  \\ /\n   | \n  /0\\")
            time.sleep(sleep)
            os.system(clear)
            print("\n  0___\n  /\\ /\\")
            time.sleep(sleep)
            os.system(clear)
            print("     0 \n    /|\\\n    / \\")
            time.sleep(sleep)
            os.system(clear)
        else:
            print("\n  0___\n  /\\ /\\")
            time.sleep(sleep)
            os.system(clear)
            print("  \\ /\n   | \n  /0\\")
            time.sleep(sleep)
            os.system(clear)
            print("\n ___0\n/\\ /\\")
            time.sleep(sleep)
            os.system(clear)
            print(" 0 \n/|\\\n/ \\")
            time.sleep(sleep)
            os.system(clear)


'''
Tests

human_gymnast()
text_expansion('text', 2)
symbol_expansion('%', 4, 2)
dot_circling(2)
line_circling(4, 2)
owl_dancer(2)

'''
