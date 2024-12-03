string = input('enter word: ')
revstring = ""
for i in string:
    revstring  = i + revstring
    print(revstring)
if revstring == string:
    print(f'{string} is pal')
else:
    print(f'{string} is NOT pal')

number = int(input("Number"))
temp=number
rev=0
while (number>1):
    last=number%10
    rev = rev*10+last
    number = number//10
    print(rev)
if(temp==rev):
    print(f'{temp} is Pal')
else:
    print(f'Not')
