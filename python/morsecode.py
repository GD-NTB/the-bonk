morsecode = '.- -... -.-. -.. . ..-. --. .... .. .--- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..'.split()
alphabet = list('abcdefghijklmnopqrstuvwxyz')

stringtoencode = input('String: ')
encodedstring = ''

for char in stringtoencode:

    encodedstring += morsecode[alphabet.index(char.lower())] + ' '

print (encodedstring)
    