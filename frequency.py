num = [1,3,5,7,3]

frequency = {}

for item in num:
    if item in frequency:
        frequency[item]+=1
    else:
        frequency[item]=1
print(frequency)