from os import path, system, name

dir = path.dirname(path.realpath(__file__)) # Current working directory

def fswitch(mode): # Shorthand for opening 'output.txt'
    return open(dir + '\\output.txt', mode)

def clear(): # Try to clear stdout
    try: system('cls' if name == 'nt' else 'clear')
    except: pass

def output(input): # Output to wherever
    fswitch('w').write(input)

def interpret(code): # Converts Small to ASCII
    output = ''

    code = code.replace(' ', '') # Remove whitespace
    code = code.replace('\n', '') # Remove line breaks
    code = code.replace('_', '') # Remove underscores

    pointer = 0

    for instruction in code:
        if pointer == 250: # Reset pointer to 0 and skip an instruction
            pointer = 0

        if instruction == '+': # Increment pointer
            pointer += 1

        if instruction == '.': # Outputs pointer value as an ASCII character
            output += chr(pointer)

    return output

def compile(string): # Converts ASCII to Small
    output = ''

    for char in string:
        asciicode = ord(char)

        for i in range(asciicode): # Increment pointer until requested ASCII char
            output += '+'
        
        output += '.' # Print ASCII char
            
        for j in range(250 - asciicode): # Increment pointer back to 0
            output += '+'

        output += '_' # Print instruction skip comment

    return output

while True: # User input loop
    clear()
    uinput = input('Type \'interpret\' to execute \'output.txt\'\nType \'compile\' to compile \'small.txt\' to Small\nType \'exit\' to exit\n')

    if uinput.lower() == 'interpret': # Execute 'interpret' command
        f = fswitch('r').read()
        output(interpret(f))

        clear()
        print('Finished \'interpret\' task!\nPress the \'Enter\' key to continue.')
        input()
        
    if uinput.lower() == 'compile': # Execute 'compile' command
        f = fswitch('r').read()
        output(compile(f))

        clear()
        print('Finished \'compile\' task!\nPress the \'Enter\' key to continue.')
        input()

    if uinput.lower() == 'exit': # Exit the environment
        clear()
        quit()
