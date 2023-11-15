# Write a Python program to reverse words in a string.

#Taking user input of a string
string=str(input("Enter a string:"))

#Split the string into words
w=string.split()

#Initialising and storing the reversed string
rev_str=""

#Function to reverse the string
for i in range(len(w)-1,-1,-1):
    rev_str+=w[i]+' '

#Removing the blank spaces and returning the reversed string
rev_str=rev_str.strip()

#Printing the output
print("The original string is:",string)
print("The string after reversing it is:",rev_str)

#Output
#Enter a string:Deeptech python training
#The original string is: Deeptech python training
#The string after reversing it is: training python Deeptech

#Enter a string:My name is Bandana Banerjee
#The original string is: My name is Bandana Banerjee
#The string after reversing it is: Banerjee Bandana is name My

