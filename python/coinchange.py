def change(n):
    # 500, 100, 25, 10, 5, 1
    total = (n // 500)+((n % 500) // 100)+(((n % 500) % 100) // 25)+((((n % 500) % 100) % 25) // 10) + (((((n % 500) % 100) % 25) % 10) // 5) + ((((((n % 500) % 100) % 25) % 10) % 5) // 1)

    return total

print(change(0))
print(change(3))
print(change(468))
print(change(123456))
