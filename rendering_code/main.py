import os
from sys import platform
import time


def render(text,*args):
    #simple rendering by clearing the screen...
    if platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')
        #and printing
    print(text)
    #now here is a bunch of argument stuff
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
    #split it with y
    text2=text.split('\n')
    #add x
    for i in enumerate(text2):
        text2[i[0]] = list(i[1])
    #replace it
    text2[y][x] = new
    #join everything back together
    for i in enumerate(text2):
        text2[i[0]] = ''.join(i[1])
    final = '\n'.join(text2)
    return final


def tell(text,x,y):
    #split the text so it can be used as a list
    text2=text.split('\n')
    #GO THROUGH IT TO FIND THE THING YOU ARE TRYING TO
    for i in enumerate(text2):
        text2[i[0]] = list(i[1])
    return text2[y][x]


def all_y(text):
    #find all y values
    text2 = text.split('\n')
    for i in enumerate(text2):
        if i[1] != '':
            yield i[0],i[1]


def all_x(text):
    #find all x values
    sizes = []
    final = []
    all_val = []
    text2 = text.split('\n')
    for i in enumerate(text2):
        if i[1] != '':
            all_val.append(i[1])

    for n in enumerate(all_val):
        sizes.append(len(all_val[n[0]]))
    size = max(sizes)
    for m in range(size):
        for i in enumerate(all_val):
            if len(i[1]) != size:
                all_val[i[0]] += ' '
            

    for i in range(size):
        first = ''
        for l in all_val:
            first += l[i]
        final.append(first)
    for end in final:
        yield end
    

def raw_modify(text,new,loc):
    text2 = list(text)
    if text2[loc] == '\n':
        raise Exception("Raw cannot be \\n")
    text2[loc] = new
    
    return "".join(text2)
