import os
from sys import platform
import time
def render(text,*args):
    if platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')
    print(text)
    success = False
    try:
        time.sleep(args[0])
    except IndexError:
        pass
    try:
        outputval2 = input(args[1])
        success = True
    except IndexError:
        pass
    if success:
        return outputval2
def modify(text,new,x,y):
    text2=text.split('\n')
    for i in enumerate(text2):
        text2[i[0]] = list(i[1])
    text2[y][x] = new
    for i in enumerate(text2):
        text2[i[0]] = ''.join(i[1])
    final = '\n'.join(text2)
    return final
def tell(text,x,y):
    text2=text.split('\n')
    for i in enumerate(text2):
        text2[i[0]] = list(i[1])
    return text2[y][x]
def all_y(text):
    text2 = text.split('\n')
    for i in enumerate(text2):
        if i[1] != '':
            yield i[0],i[1]
