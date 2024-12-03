
num = [16,8,9,3]

length=len(num)
def buble(num):

    for i in range(length-1):
        for j in range(length-1):
            if num[j] > num[j+1]:
                num[j],num[j+1] = num[j+1],num[j]
    return num

print(f'buble sort of {num} is',buble(num))