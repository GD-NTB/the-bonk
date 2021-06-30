array = [ ]

adding = True

while adding:
    n = input("Enter a name: ")
    accepted = input("Have the accepted your invitation? (y/n) ")
    if(accepted == "y"): a = True
    else: a = False
        
    array.append([n, a])
    
    user = input("Add another name? (y/n)")
    if(user == "n"):
        adding = False

def addcol():
    total = 0
    for i in range(len(array)):
        print(i)
        if (array[0][i]):
            total += 1
    return total

print(addcol())


print(array)
