import string
lowercases = string.ascii_lowercase

n = int(input())
s = input()
#s = ' '.join(s.split())

num_char = {}
char_num = {}
for num, ele in enumerate(lowercases):
    num_char[num] = ele
    char_num[ele] = num
    
print(''.join([char if char not in lowercases else \
        num_char[(char_num[char] + n) % 26]  for char in s]))

# An alternative
a = lambda distance, n: ''.join([(i if i == ' ' else chr(ord('a') + (ord(i) - ord('a') + distance) % 26)) for i in n.lower()]) 
print(a(int(input()), input()))
