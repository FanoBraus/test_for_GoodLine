import string

s = input('Введите фразу: ')

def palindrome(s):
    whitelist = set(string.ascii_lowercase)
    s = s.lower()
    s = ''.join(char for char in s if char in whitelist)
    return s[::1] == s[::-1]

if palindrome(s):
    input('Фраза является палиндромом.')
else:
    input('Фраза не является палиндромом.')
