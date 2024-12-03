for item in range(5,10,2):
    print(item)

price = [20,30,50]
total=0
for item in price:
    total+=item
print(f'total pirce: {total}')

for x in range(5):
    for y in range(5):
        print(f'({x},{y})')

number = [5,2,5,2,2]
for i in number:
    output = ''
    for j in range(i):
        output +='x'
    print(output)

max_num=number[0]
for i in number:
    if i > max_num:
        max_num=i
    
print(max_num)

number.insert(6,10)
print(number)

print(59 in number)
print(number.count(5))
number.sort()
number.reverse()
print(number)

unique=[]
for item in number:
    if item not in unique:
        unique.append(item)
print(unique)

coordinate  = (1,2,3)
x,y,z = coordinate
print(f'multiplu: ',x*y*z)

phone = input('phone: ')
digit = {
    "1": "One",
    "2": "Two", 
    "3": "Three"
}
output=""
for ch in phone:
    output+=digit.get(ch,"?")+" "
print(output)

message=input(">")
words=message.split(" ")
emojis={
    ":)": "Happy",
    ":(": "Sad"
}
output=""
for word in words: 
    output+=emojis.get(word, word)
print(output)
