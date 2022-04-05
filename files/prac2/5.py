import time

def fibo(n):
    a = [0, 1]
    for i in range(n - 1):
        a.append(None)
    if a[n] is not None:
        return a[n]
    a[n] = fibo(n - 2) + fibo(n - 1)
    return a[n]
    
def b_fibo(n, cache:list = [0, 1, 1]):
    if n < len(cache):
        return cache[n]
    cache.append(b_fibo(n - 1) + b_fibo(n - 2))
    return cache[n]

def fibo_loop(n):
    f = [1, 1]
    for i in range(2, n):
        f.append(f[i - 1] + f[i - 2])
    return f[-1]

def fibo_compare(x: int, y: int):
    print('Execution time for Fibonacci function using loop with n from {} to {}: '.format(x, y))
    print('{:<5}{:<10}{:<16}'.format('n', 'Result', 'Time'))
    for i in range(x, y+1):
        start = time.time()
        res = fibo_loop(i)
        et = time.time() - start
        print('{:<5}{:<10}{:<16f}'.format(i, res, et))

    print('Execution time for Fibonacci function using recursion with n from {} to {}: '.format(x, y))
    print('{:<5}{:<10}{:<16}'.format('n', 'Result', 'Time'))
    for i in range(x, y+1):
        start = time.time()
        res = fibo(i)
        et = time.time() - start
        print('{:<5}{:<10}{:<5.16f}'.format(i, res, et))

    
def main():
    fibo_compare(10, 20)

if __name__ == '__main__':
    main()