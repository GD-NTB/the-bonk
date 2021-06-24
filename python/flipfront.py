def flipfront(a, n): return a[0:n][::-1] + a[n:len(a)]

print(flipfront(input('Enter any string: '), int(input('Enter any number to flip to: '))))