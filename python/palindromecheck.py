def ispalindrome(v):
    if v==v[::-1]: return True
    else: return False

print(ispalindrome(input('Enter any string to check: ')))