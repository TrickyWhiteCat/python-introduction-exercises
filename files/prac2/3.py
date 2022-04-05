def print_prime(n):
    a = [None for i in range(n)]
    for i in range(2, n):
        if a[i] is None:
            a[i] = True
            print(i, end = ' ')
            for j in range(i * i, n, i):
                a[j] = False
              
def main():
    import time
    start = time.time()
    print_prime(1000000)
    print('Execution time: {}'.format(time.time() - start))

if __name__ == '__main__':
    main()