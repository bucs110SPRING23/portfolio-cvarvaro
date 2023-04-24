class StringUtility:
    """
    Defines functions used to test the strings in main.py
    """
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string
    
    def vowels(self, s):
        count = sum(1 for c in s if c.lower() in 'aeiou')
        if count < 5:
            return str(count)
        else:
            return 'many'
        
    def bothEnds(self, s):
        if len(s) <= 2:
            return ''
        else:
            return s[:2] + s[-2:]
        
    def fixStart(self, s):
        if len(s) <= 1:
            return s
        else:
            return s[0] + s[1:].replace(s[0], '*')
        
    def asciiSum(self, s):
        return sum(ord(c) for c in s)
    
    def cipher(self, s):
        result = ''
        for c in s:
            if c.isalpha():
                shift = len(s)
                if c.isupper():
                    base = ord('A')
                else:
                    base = ord('a')
                result += chr((ord(c) - base + shift) % 26 + base)
            else:
                result += c
        return result