#is
#is not


#stings and integers are immutable
x1=5
y1=5


print(id(x1))

print(id(y1))

print(x1 is y1)

x2="Hello"
y2="Hello"

print(id(x2))

print(id(y2))

print(x2 is y2)
x3=[1,2,3]  #different since dictionaries and lists are mutable
y3=[1,2,3]

print(id(x3))

print(id(y3))

print(x3 is y3)
