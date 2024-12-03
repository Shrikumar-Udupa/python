
'''Assignment___02(Date: 28,29 of Sep 2024)
----------------------------------------

1) Generate this numbers by using range function:
   -24, -20, -16,..........,8 '''
#Ans Start=-24, end=9, step=4, forward direction
a = range(-24,9,4)
for i in a:
    print(i)

#########

'''
2) Generate this numbers by using range function:
	-5,-7,-9,-11,-13,-99'''
#Ans start=-5, end=-2,step=-2, reverse direction
b = range(-5,-100,-2)
for i in b:
    print(i)
#######

'''3) x = range(-99,0,5)
		Which direction?
		is it possible to generate the number by this values? if yes? why? if No? why? '''
#Ans
#Forward diretion, left to right direction and last variabe is len(variable) - 1
#Possible to generate number by this range, step is positive(5), and sequence increments from left to right, ie end number alwayson right (-99, -94 to -4).
x = range(-99,0,5)
for i in x:
    print(i)

##############
'''
4) y = range(0,-2,-1)
		Which direction?
		is it possible to generate the number by this values? if yes? why? if No? why?
'''
#Ans
#Reverse direction in the number line, step is -ve. 
#Possible to generate numbers by this range, sequence decreate from 0 to -2, end number always on left side of number line.(-1,0) 
y = range(0,-2,-1)
for i in y:
    print(i)

###############
'''
5) How to check a given variable as iterable? Given me some non-iterable vairable with a proof?
'''
#Ans
#Length function used to check if the variable is iterable, if it's iterable len() will return > 0.
w = range(5,200,-2)
print(len(w))
p = range(-155,-320,5)
print(len(p))