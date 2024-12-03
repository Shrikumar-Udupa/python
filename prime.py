number =2

if number>1:
    for item in range(2, (number//2)+1):
        if (number%item) == 0:
            print('Not Prime')
            break
    else:
        print('prime')
else:
    print('prime')