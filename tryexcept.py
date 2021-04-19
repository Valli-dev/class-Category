"""x = 10
f = open("demofile.txt")
try:

    f = open("demofile.txt")
    f.write("lorum ipsum")
    # print(x)

except:
    print("something went wrong when writng into file")
else:
    print("try executed with no error")

finally:
    print("\nI am from finally")
    f.close() """
import os
x = lambda a: a + 10

print(x(10))

y= lambda a, b : a*b

print(y(5,6))


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))



def func(n):
    return lambda a: a*n

v= (func(5))
print(v(3))

mydoubler=myfunc(11)
mytripler=myfunc(11)

print(mydoubler(2))
print(mytripler(3))

x = lambda a, b, c : a * b * c


print(x(2, 6, 5))
try:

    f = open("demofile.txt", "rt")
    for x in f:
        print(x)
        #print(f.read())
except:
    print("file not exist")
finally:
    f.close()

f=open("demofile2.txt", "w")
f.write("Hi I am new file opened in write mode")
f.close()


f=open("demofile2.txt","a" )
f.write("I Added lines in append mode ")
f.close()

f=open("demofile2.txt", "w")
f.write("freshly overwritten")
f.close()

#f=open("demofile3.txt", "x")

if os.path.exists("file3.txt"):
    os.remove("file3.txt")
else:
    print("file not exist")
