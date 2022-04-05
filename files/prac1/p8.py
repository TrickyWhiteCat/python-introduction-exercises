import math
def newton_sqrt_step(n:int, precision) -> int:
    true_value = math.sqrt(n)
    diff = 2**31 - 1
    sqrt = n
    prev_sqrt = n
    iter = 1
    print('{num_iter}\t{val:<16}\t\t{dif}'.format(num_iter = 'Step', val = 'Value', dif = 'Difference'))
    while (diff > precision):
        print('{num_iter}\t{val:<16}\t\t{dif}'.format(num_iter = iter, val = sqrt, dif = (sqrt - true_value)))
        iter += 1
        prev_sqrt = sqrt
        sqrt = (sqrt + n/sqrt)/2
        diff = abs(prev_sqrt - sqrt)
    return sqrt

def main():
    n = int(input())
    print(newton_sqrt_step(n, precision=0.0000001))

if __name__ == '__main__':
    main()