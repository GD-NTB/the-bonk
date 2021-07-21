from os import path, system, name
from random import random
from sys import maxsize

dir = path.dirname(path.realpath(__file__)) # Current working directory

def fswitch(mode): # Shotrhand for opening 'output.txt'
    return open(dir + '\\output.txt', mode)

def clear(): # Try to clear stdout
    try: system('cls' if name == 'nt' else 'clear')
    except: pass

def output(input): # Output to wherever
    fswitch('w').write(input)

def interpret(code): # Executes * code
    output = ''

    code = code.replace('\n', '') # Remove line breaks

    if code == '*': # Hello, world!
        output += 'Hello, world!'
    
    if code == ' * ': # Random value (0 -> 1 * sys.maxsize)
        output += str(random() * maxsize)

    if code == '*+*': # Infinite loop
        while True: pass

    return output

clear()
print('Executing output.txt...')
f = fswitch('r').read()
output(interpret(f))

clear()
input('Finished \'interpret\' task!\nPress the \'Enter\' key to exit.')
