#extend

a = ["shweta",10,"pavan",20]

b = [200,"python","CRY","*"]



a.extend(b)

print(a)



#append

a.append(3)

a.append([4,5])

print(a)



#inser

a.insert(0,"job")

print(a)

b.insert(2,"play")

print(b)



#enumerate

print(list(enumerate(a)))

print(list(enumerate(b)))



#min and max (spl char < number <capital <lower)



c = ["shweta","*","123","PYTHON"]

print(min(c))

print(max(c))
