class string_utilities():
    def __init__(self):
        pass
    
    def is_valid_parenthese(self, s):
        open = ('{', '[', '(')
        close = ('}', ']', ')')
        open_stack = []
        for character in s:
            if character in open:
                open_stack.append(character)
            if character in close:
                if open[close.index(character)] != open_stack.pop():
                    return False
        return not open_stack

    def reverse_words(self, words):
        return ' '.join(words.split()[::-1])
