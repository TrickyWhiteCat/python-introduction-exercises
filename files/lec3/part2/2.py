# An alternate: https://github.com/TrickyWhiteCat/python-introduction-exercises/blob/main/files/prac2/2.py
def display_pascal_triangle(n):
    def pline(i):
        def ele(i, j):
            if i == 1 or j == 1 or j == i:
                return 1
            return ele(i - 1, j - 1) + ele(i - 1, j)
        def loopj(j):
            if j == 1:
                print(' ' * (n - i), end = '')
            print(ele(i,j), end = ' ')
            if j != i:
                loopj(j+1)
        loopj(1)
        print()

    def pascal(i):
        pline(i)
        if i != n:
            pascal(i+1)
    
    pascal(1)

