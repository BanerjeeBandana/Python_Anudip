#Write a Python program to check if the given string is a palindrome.

#Taking user input of a string
s=str(input("Enter a string:"))
w=""

#Checking whether the string is a palindrome or not
for i in s:
    w=i+w

#Printing the output
print("The string is palindrome" if (s==w) else "The string is not palindrome")

#Output
#Enter a string:refer
#The string is palindrome

#Enter a string:bandana
#The string is not palindrome

