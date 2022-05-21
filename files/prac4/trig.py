def _abs(x):
    return (x>0)*x + (x<0)*(-x)

def _factorial(x):
    res = 1
    for i in range(1, x+1):
        res *= i
    return res

def exp(x, err = 10**-10):
    res = 0
    prev = 0
    index = 0
    diff = err + 1
    while (True):
        if diff < err: break
        prev = res
        res += x**index/_factorial(index)
        index += 1
        diff = _abs(res - prev)
    return res

def sin(x, err = 10**-10):
    res = 0
    prev = 0
    index = 0
    diff = err + 1
    while (True):
        if diff < err: break
        prev = res
        res += x**(2*index+1)*(-1)**index/_factorial(2*index+1)
        index += 1
        diff = _abs(res - prev)
    return res

def cos(x, err = 10**-10):
    res = 0
    prev = 0
    index = 0
    diff = err + 1
    while (True):
        if diff < err: break
        prev = res
        res += x**(2*index)*(-1)**index/_factorial(2*index)
        index += 1
        diff = _abs(res - prev)
    return res


def main():
    import time
    start = time.time()
    print(cos(2, 10**-10))
    print(time.time() - start)

if __name__ == "__main__":
    main()
