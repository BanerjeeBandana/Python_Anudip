#Defining the function
def low_case(name):
    name=str(input("Enter the name:"))
    return name.lower()

#Calling the function and printing the result
final=low_case('Bandana')
print("The name in lowercase is:",final)

#Output
#Enter the name:Bandana
#The name in lowercase is: bandana

#Enter the name:BANDANA
#The name in lowercase is: bandana

#Enter the name:Mala
#The name in lowercase is: mala
