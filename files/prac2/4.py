def GCD(a, b):
    if a % b == 0: return b
    return GCD(b, a % b)
