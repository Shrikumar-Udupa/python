row = int(input('enter row'))

for i in range(row):
    for j in range(row-i+1):
        print(" ",end="")

    for j in range(i+1):
        print("*",end=" ")

    print()
###lower half increasing
for i in range(row):
    for j in range(i+1):
        print("*",end="")
    print()
#Number increasing left
for i in range(row):
    for j in range(i,row):
        print("*",end="")
    print()
##Number increasing left
for i in range(row):
    for j in range(1,i+1):
        print(j,end="")
    print()

##
for i in range(row):
    for j in range(1,i+1):
        print(i,end="")
    print()
#
for i in range(row):
    for j in range(row-i-1):
        print(" ",end="")
    for j in range(i,0,-1):
        print(j,end="")
    print()