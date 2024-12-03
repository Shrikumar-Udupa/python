n1=0
n2=1
term = 7
count = 0
if term<=0:
    print('invalid')
elif term == 0:
    print(n1)
else:
    while count<term:
        print('fib:', n1)
        nth = n1+n2
        n1=n2
        n2=nth
        count+=1
