#Write a program to remove duplicate characters of a given string.

#Taking user input of a string
string=str(input("Enter a string:"))

#Initializing the duplicate characters removed string
dup_rem_str=""

#Removing all the duplicate characters from the string
for i in string.split():
    if i not in dup_rem_str:
        dup_rem_str=dup_rem_str+" "+i

#Printing the output
print("The original string is:",string)
print("The string after removing duplicate words is:",dup_rem_str)

#Output
#Enter a string:String and String Function
#The original string is: String and String Function
#The string after removing duplicate words is:  String and Function

#Enter a string:Fear leads to anger and anger leads to hatred
#The original string is: Fear leads to anger and anger leads to hatred
#The string after removing duplicate words is:  Fear leads to anger and hatred
