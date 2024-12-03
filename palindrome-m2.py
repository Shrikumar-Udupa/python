def palindrome(string):
    revstring = string[::-1]
    return string == revstring


word = input('Enter string: ')

if palindrome(word):
    print(f'{word} is pali')

else:
    print(f'{word} is not pal')
