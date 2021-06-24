array = [ ]

def asknum(n):
    value = input("Enter {0} more numbers: ".format(10 - n))

    if value.isnumeric():
        value = int(value)
        array.append(value)
    else:
        asknum(n)

for i in range(10):
    asknum(i)

print(sorted(array))