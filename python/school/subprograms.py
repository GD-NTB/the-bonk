num1 = int(input("Enter a number! "))
num2 = int(input("Enter another number! "))

total = num1 + num2


def largeNum(l1, l2):
    out = (l1 * 2) + 12
    return out

def smallNum(s1, s2):
    out = s1 + s2
    return out


if (total > 50):
    answer = largeNum(num1, num2)
else:
    answer = smallNum(num1, num2)

print(answer)

