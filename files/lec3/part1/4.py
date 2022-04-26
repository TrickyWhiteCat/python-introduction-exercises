# This function hasn't yet optimized but I'm too lazy to do so
def calculate(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return 2*calculate(n-1) + calculate(n-2)
