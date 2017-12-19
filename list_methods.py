list1=["shweta",20,"pavan",234]

list2=["python",25,"class",50,25]







#pop--to delete elements  -- can give index value

print(list1.pop(2))

print(list1)

#if we dont mention the index..it removes the last element by default

print(list1.pop())

print(list1)



#remove-- can give value

print(list2.remove("python"))

print(list2)



list2.remove(25) #removes only the first occurence of the element

print(list2)





del list2 #to delee entire list

 # throws exception as list2 is deleted



del list1[1] #can even delete using index

print(list1)



#revers

list3=[10,5,20,15,45,60]

print(list3)

list3.reverse()

print(list3)



#sort  sort is performed on same datatypes eg:strings,int etc

list4=["A","*","23","ab"] #sorts in this order  special char,number,upper case,lower case

list4.sort()

print(list4)



#min,max

list5=[20,10,50,150,60]

list_5=["d","a","b","e"]

print(max(list5))

print(min(list5))



print(min(list_5))

print(max(list_5))





#covertion to list

list6=("shweta",10,"class",50)

new_list=list(list6)
print(new_list)
