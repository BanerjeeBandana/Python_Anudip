#Write a Python program to count and display the vowels of a given text.

#Taking input from user
string=str(input("Enter a string:"))

#Converting the string in lowercase,Initialising the vowels and count of vowels
string=string.lower()
vowel=""
c=0

#Function to check and calculate if any vowel is present in string or not
for i in string:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        #Incrementing the vowel
        vowel+=i
        #Incrementing the count of vowels
        c+=1

#Checking if any vowels is present in the string
if c==0:
    print("No vowel is present")
else:
    #Printing the number of vowels in the string and displaying them
    print("Number of vowels present in  string is:",c)
    print("The vowels present in the string are:",",".join(vowel))

#Output
#Enter a string:Welcome to python training
#Number of vowels present in  string is: 8
#The vowels present in the string are: e,o,e,o,o,a,i,i

#Enter a string:Why cry?
#No vowel is present

#Enter a string:I learnt English by myself
#Number of vowels present in  string is: 6
#The vowels present in the string are: i,e,a,e,i,e
