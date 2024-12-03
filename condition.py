is_hot=False
if is_hot:
    print('hot day')

else:
    print('cold day')

name = "Binu"
if len(name)<5:
    print("user name is less than 3 char")
elif len(name)>50:
    print("name is less than 50")

secret_number = 9
guess_count = 0
while guess_count < 3:
    guess = int(input("guess "))
    guess_count+=1
    if guess == secret_number:
        print('won')
        break
else:
    print("failed")


