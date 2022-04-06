def get_element( i :int, k: int, cache: dict[str, int] = {}) -> int:
    '''get the element at i'th row and k'th column

    cache -- a dict used to store precomputed values. If it isn't provided, an empty dict will be created to boost performance'''
    if i == 1 or k == 1 or k == i:
        cache[i, k] = 1
        return 1
    if (i, k) in cache:
        return cache[i, k]
    temp = get_element(i - 1, k - 1, cache) + get_element(i - 1, k, cache)
    cache[i, k] = temp
    return temp

def get_triangle(num_lines: int, triangle = []) -> list:
    '''Return a list of <num_lines> lists of elements on each line'''
    triangle = []
    for line in range (1, num_lines + 1):
        elems_in_line = []
        for elem in range (1, line + 1):
            elems_in_line.append(get_element(line, elem))
            ''' There is no need to store precalculated values in another dictionary before <get_element()> is terminated 
            because default values of a function are evaluated once the function is defined, not each time the function is called.'''
        triangle.append(elems_in_line)
    return triangle

def pascal_triangle(n:int):
    '''Print the first n'th line of pascal triangle'''
    triangle = get_triangle(n)
    total_length = len(' '.join(str(elem) for elem in triangle[-1]))
    for row in triangle:
        print(' '.join(str(elem) for elem in row).center(total_length))


count = 0
def main():
    pascal_triangle(10)

if __name__ == '__main__':
    main()
