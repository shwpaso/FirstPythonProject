#immutable datatypes
# elements with key and value

print({1:"a",2:"b",3:"c"})

a = {"firstname":"shweta","last":"bhaskara","age":26}

print(a)
a["age"]=30 #can update value

a["school"] = "dps" #can ad new element

print(a)

#get method

print(a.get("age"))

print(a.get("dps")) #we cannot get using value only key

print("value : %s" % a.get("age"))  #format operator


#

b= {"class": 10,"age":20}
c = {1:"one",2:"two"}

print(b.keys()) #keys
print(b.values())#values
print(b.items())# prints in form of list


print("keys : %s" % c.keys())
print("values : %s" % c.values())

#clear
print(c)
c.clear() #clears dict
print(c)

#len method
print("lenght : %d" % len(b))

#copy method
e=b.copy()
print(e)


#del method
print(a)

del a["firstname"] #can delete based on key


#del a #deletes entire a dict

print(a)  #throws exception as a is deletes
a.clear() #clears elements
print(a)

#creating dict
tuple1 = ("name","age","school")

dict1= dict.fromkeys(tuple1) #creating dictionary dict1 using keys from tuple1

print("value of dict1 : %s" %str(tuple1))

dict2=dict.fromkeys(tuple1,10) #creating dict2 using tuple1 keys and assigning 10 for all keys

print(dict2) #else u can assign values from user

#dict2["name"]=input("enter name :")
#dict2["age"]=input("enter age :")
#dict2("school")=input("enter school")
