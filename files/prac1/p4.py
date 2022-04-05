def Collatz(n:int):
    n = int(n)
    while n != 1:
        print(n, end = ' ')
        if n % 2:
            n = n * 3 + 1
        else:
            n //= 2
    print(1)

def main():
    n = int(input())
    Collatz(n)

if __name__ == '__main__':
    main()