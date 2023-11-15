#Write a program to Count all letters, digits, and special symbols from the given string

#Taking user input of a string
s=str(input("Enter a string:"))

#Initializing the counting of alphabets and symbols
alpha=dig=sym=0

#Calculating the number of characters,digits and symbols
for i in range(len(s)):
    if(s[i].isalpha()):
        alpha+=1
    elif(s[i].isdigit()):
        dig+=1
    else:
        sym+=1

#Printing the outputs
print("The number of alphabets in the given string is",alpha)
print("The number of digits in the given string is",dig)
print("The number of symbols in the given string is",sym)

#Output
#Enter a string:P@#yn26at^&i5ve
#The number of alphabets in the given string is 8
#The number of digits in the given string is 3
#The number of symbols in the given string is 4

#Enter a string:Pr1@Ir2!Ne18_
#The number of alphabets in the given string is 6
#The number of digits in the given string is 4
#The number of symbols in the given string is 3
