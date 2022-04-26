def friendly(a, b):
    if a == sum(i for i in range(1, b) if b % i == 0) and b == sum(i for i in range(1, a) if a % i == 0):
        return 'YES'
    else:
        return 'NO'
