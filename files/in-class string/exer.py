# exercise 1
def last_repeat(s : str):
    for i in range(len(s)-1, -1, -1):
        if s[i] == ' ':
            continue
        if s[i] in s[:i]:
            return s[i]

# exercise 2
def transform_string(s: str):
    return s[1::2] if len(s) % 4 else s[::-1]
