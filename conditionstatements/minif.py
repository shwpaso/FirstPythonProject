x=int(input("give x"))

y=int(input("give y"))

z=int(input("give z"))



if (x<y):

    if x<z:

        minimum=x

    else:

        minimum=z

else:

    if y<z:

        minimum=y

    else:

        minimum=z

print("minimum is:",minimum)


