names = [ ]

for i in range(5):
   a = input("Enter a name! ")
   names.append(a)

print(names)

b = int(input("Enter a number! "))
if (0 <= b <= 4):
   print(names[b-1])
   c = input("Do you want to delete this or change this? (del/chng)")
   if (c == "del"):
      names.pop(b-1)
   if (c == "chng"):
      d = input("What do you want to change it to? ")
      names[b-1] = d
   print(names)
   
