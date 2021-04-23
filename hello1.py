print("Hello world")
print(1,2,3,4)
print("Hello {name}, {greeting}".format(greeting="congratulations", name= "Valli"))
#print(1,2,3,4,sep='*', end='&')
a= 1+2+3+\
    4+5+6\
        +7+8+9
c=( 5,6.7,"hello",90,56,"---")
print(a)
print("The value of a= {0} and c= {1} ".format(a,c))
print(c[0])
print(c[0:2])
print(c[2:3])


f= 1.1234567890123456789
aa= 2+3j
print(aa , "is complex type ", isinstance(2+3j,complex))
print(f)
def square(a):
    """ sample test programs"""
    return a*a

print (square (a))
print(square.__doc__)