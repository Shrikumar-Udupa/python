number = [9,2,3,5]
n=len(number)

for i in range(n-1):
    for j in range(n-1):
        if number[j]>number[j+1]:
            number[j],number[j+1] = number[j+1],number[j]
print(number)