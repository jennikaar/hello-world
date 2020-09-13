# https://www.learnpython.org/en/Hello%2C_World%21

print("Hello world!")

x = 1
if x ==1:
   #indented four spaces
   print("x is 1.")
myint = 7
print(myint)
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)
mystring = 'hello'
print(mystring)
a, b = 4,3
print(a,b)

# exercise from learnpython.org
mystring = 'hello'
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)