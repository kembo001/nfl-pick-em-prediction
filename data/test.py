#Problem 1

import random
def cost():
    dollar = random.randrange(0,10)
    cents = ((random.randrange(0, 99)//5) * 5) * .01
    price = dollar + cents
    return price

print(f'{cost():.2f}')

#Problem 2
def less_than(x, y):
    if x > y:
        return True
    else:
        return False

print(less_than(6, 8))

#Problem 3
def celing(x):
    high = (x // 1) + 1
    return high

print(celing(7.9))

#Problem 4
def round(x):
    if x - (x // 1) >= .5:
        x = (x // 1) + 1
    else:
        x = (x // 1)
    return x

print(int(round(9.7)))

#problem 5
def absolute(y):
    if y < 0:
        y = y*(-1)
        return y
    else:
        return y
print(absolute(-67))

#Problem 6
def spacey(y):
    word = int(len(y))
    i = 0
    while word != i:
      print(y[i], end=' ')
      i+=1
    print() 
        
spacey('Brandon')

#Problem 7
def uname(x):
    at = x.index("@")
    return x[:at]

print(uname('kemboi@outlook.com'))

def pos2neg(y):
    i = (y/-1) - 1
    while i < y:
        print(y, end=' ')
        y-=1
    print()
    
pos2neg(5)

def weave(x, y):
    xlen = int(len(x))
    ylen = int(len(y))
    i = 0
    while xlen > i and ylen > i:
        candy = print(x[i]+y[i], end = "")
        i+=1
    print()
    return candy


weave('hello','world')
      
def palindrom(x):
    palindrom_len = int(len(x))
    xlen = 0
    ylen = -1
    i = 0
               
    if x[0] == x[-1]:
     while xlen < palindrom_len and ylen > ((palindrom_len/-1)-11):
        if x[xlen] == x[ylen]:      
            xlen= xlen+1
            ylen= ylen+1
            candy = print('x is a palindrom!')
        else:
            break
            candy = print('No no no')
    else:
        candy = print('Nojo')
    return candy
        
    

palindrom('wopw')

def tens (x):
    tens_of = x//10
    y = 0
    while y <= x:
        z = print(y, end=' ')
        y+=10
    return z
tens(90)
print()
def evens(x, y):
    if y%2 == 1:
        y = y+1
    else:
        y = y
    i = 0
    while i < x:
        z = print (y, end=' ')
        y+=2
        i+=1
    return z

evens( 4, 9 )
print()

def tentest(x):  
    i = 0
    if x < 10:
        x = x*10
    while x >= i:
        print(i, end=' ')
        i+=10

tentest(40)
print()

