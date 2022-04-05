import math
def newton_sqrt(n: int, precision: float) -> float:
    diff = 2**31 - 1
    sqrt = n
    prev_sqrt = n
    while (diff > precision):
        prev_sqrt = sqrt
        sqrt = (sqrt + n/sqrt)/2
        diff = abs(prev_sqrt - sqrt)
    return sqrt

def main():
    n = int(input())
    print(newton_sqrt(n, 0.0000001))

if __name__ == '__main__':
    main()