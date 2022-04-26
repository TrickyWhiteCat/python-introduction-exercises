def digit_sum_greater(a, b):
    a_sum = sum(int(i) for i in str(a))
    b_sum = sum(int(i) for i in str(b))
    if a_sum > b_sum:
        return 'YES'
    else:
        return 'NO'
