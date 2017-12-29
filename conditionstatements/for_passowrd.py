password=""

count=0

while password!="redhat" and count<3:

    count=count+1

    print("allows",count,"times")

    password=input("enter password")

    if password =="redhat":

        print("correct")

    else:

        print("wrong")



print("out of loop")
