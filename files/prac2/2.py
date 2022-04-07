def get_element( i :int, k: int, cache: dict = {}) -> int:
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

def get_element_m( i :int, k: int, cache: dict = None) -> int:
    '''This is a modified version of `get_element()`, which is probably easier to understand and doesn't fuck up your PC's memory.

    Performance will be a bit worse than `get_element()` if it is only called once or external cache is provided when its being called multiple times
    and will be much worse if there isn't external cache when called continuously.

    get the element at i'th row and k'th column

    `cache` -- a dict used to store precomputed values. If it isn't provided, an empty dict will be created to boost performance.'''
    if cache == None:
        cache = {}
    if i == 1 or k == 1 or k == i:
        cache[i, k] = 1
        return 1
    if (i, k) in cache:
        return cache[i, k]
    temp = get_element_m(i - 1, k - 1, cache) + get_element_m(i - 1, k, cache)
    cache[i, k] = temp
    return temp

def get_triangle(num_lines: int, triangle = []) -> list:
    '''Return a list of `num_lines` lists of elements on each line
    
    After being executed, if there exists at least one reference to this function, memory used won't be released.'''
    for line in range (1, num_lines + 1):
        elems_in_line = []
        for elem in range (1, line + 1):
            elems_in_line.append(get_element(line, elem))
            ''' There is no need to store precalculated values in another dictionary before `get_element()` is terminated 
            because default values of a function are evaluated once the function is defined, not each time the function is called.'''
        triangle.append(elems_in_line)
    return triangle

def get_triangle_m(num_lines: int, triangle = [], use_cache: bool = True) -> list:
    '''A modified version of `get_triangle()` to use `get_element_m()` instead of `get_element()`. This function will release used memory after being terminated.
    
    Return a list of `num_lines` lists of elements on each line.
    
    Argument:
    
    `use_cache` (bool) -- For whatever reason, you can choose to not use external cache by setting this argument to `False`'''
    if use_cache:
        precomputed = {}
    for line in range (1, num_lines + 1):
        elems_in_line = []
        for elem in range (1, line + 1):
            try:
                elems_in_line.append(get_element_m(line, elem, precomputed))
            except UnboundLocalError:
                elems_in_line.append(get_element_m(line, elem))
        triangle.append(elems_in_line)
    return triangle

def pascal_triangle(n:int):
    '''Print the first n'th line of pascal triangle'''
    triangle = get_triangle(n)
    max_length = len(' '.join(str(elem) for elem in triangle[-1]))
    for row in triangle:
        print(' '.join(str(elem) for elem in row).center(max_length))

def main():
    pascal_triangle(10)

if __name__ == '__main__':
    main()
