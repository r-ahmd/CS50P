vowels = ['a','e','i','o','u', 'A','E','I','O','U']
a = input('Input: ')
print('Output: ', end='')

for letter in a:
    if letter in vowels:
        pass
    else:
        print(letter, end='')
print('')
