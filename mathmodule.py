#!/usr/bin/python

# Importing additional functionality



import math



#abs

print("absolute value of :",abs(-11.2))  #can use abs method even instead of math module

print("abs value :",abs(31)) #abs prints int value



#fabs

print("fabs value:",math.fabs(-11.2)) #fabs requires math module

print("fabs of :",math.fabs(31))  #fabs prints float value



#ceil-- round offs to next highest value

print("ceil of :",math.ceil(61.1))

print("ceil of :",math.ceil(-45.4))





#floor -- round offs to the least value

print("floor of:",math.floor(66.1))

print("floor of :",math.floor(-45.4))





#exp methods -- prints exp value

print("exp value :",math.exp(66.1))

print("exp value :",math.exp(-45.1))



#log methods -- log,log10.log1p

print("log :",math.log(math.pi))

print("log10:",math.log10(math.pi))

print("log1p:",math.log1p(math.pi))



#min and max functions not part of math



print("min of :",min(10,20,-10,50))

print("max of :",max(10,50,-30,20))



#modf

print("mod of :",math.modf(22.67))



#pow --
print("pow of :",math.pow(10,3))

#round

print("round :",round(3.6523,2))

#sqrt
print("sqrt :",math.sqrt(49))

