#Write a Python program to check if a given number is an Armstrong number.

#Taking user input of a number
n=int(input("Enter a number:"))

#Assigning the number to the s variable
s=n

#Storing the length of the number
l=len(str(n))

#Initializing the new number
new_n=0

#Loop for checking the number is Armstrong Number or not
while n!=0:
    r=n%10
    new_n+=(r**l)
    n//=10

#Printing the Output
print(s,"is an Armstrong number") if (s==new_n) else  print(s,"is not an Armstrong number")

#Output
#Enter a number:125
#125 is not an Armstrong number

#Enter a number:1634
#1634 is an Armstrong number

#Enter a number:29
#29 is not an Armstrong number
    
