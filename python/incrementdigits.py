def incrementdigits(n):
    newnumber = 0
    for i in range(len(str(n))):
        newnumber = int(str(newnumber) + str(int(str(n)[i]) + 1))
    return newnumber

print(incrementdigits(input('Enter a number: ')))