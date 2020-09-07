import os


def text_expansion(text: str, times: int = 2, clear: bool = False):
    clear = 'clear' if clear else 'cls'
    for j in range(times):
        if j % 2 == 0:
            for i in range(len(text) + 1):
                print(text[:i])
                os.system(clear)
        else:
            for i in range(len(text) + 1):
                print(text[:len(text) - i])
                os.system(clear)


def symbol_expansion(symbol: str, kol: int = 10, times: int = 2, clear: bool = False):
    clear = 'clear' if clear else 'cls'
    text = symbol * kol
    for j in range(times):
        if j % 2 == 0:
            for i in range(len(text)):
                print(text[:i])
                os.system(clear)
        else:
            for i in range(len(text)):
                print(text[:len(text) - i])
                os.system(clear)


def dot_circling(times: int = 2, clear: bool = False):
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
            os.system(clear)


def line_circling(kol: int = 10, times: int = 2, clear: bool = False):
    clear = 'clear' if clear else 'cls'
    for j in range(times):
        if j % 2 == 0:
            for i in range(kol):
                if i % 4 == 0:
                    symbol = '-'
                elif i % 4 == 1:
                    symbol = '\\'
                elif i % 4 == 2:
                    symbol = '|'
                else:
                    symbol = '/'
                print(symbol * i)
                os.system('cls')
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
                os.system('cls')


'''
Tests

text_expansion("abcdef", 1)
symbol_expansion('%', 4, 4)
dot_circling(3)
line_circling(17, 2)'''
