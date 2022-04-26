def floyd(n):
    for i in range(1, n+1):
        print(''.join([str((i - j)%2) for j in range(i)]))
        
# Debug: 0
def floyd(n): print('\n'.join([''.join([str((i - j)%2) for j in range(i)]) for i in range(1, n+1)]))
