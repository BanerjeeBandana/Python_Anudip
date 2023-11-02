#User input of distance
dist=int(input("Enter the distance:"))

#Calculating fare according to given distances 
if dist>0 and dist<51:
    print("The cost is Rs.",8*dist)
elif dist>50 and dist<101:
    print("The cost is Rs.",10*dist)
else:
    print("The cost is Rs.",12*dist)


#Output
#Enter the distance:5
#The cost is Rs. 40

#Enter the distance:60
#The cost is Rs. 600

#Enter the distance:125
#The cost is Rs. 1500

