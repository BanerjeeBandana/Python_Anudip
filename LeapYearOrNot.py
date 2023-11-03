#User Input of Year
year=int(input("Enter the year:"))

#Checking if the year is leap year or not
if (year % 400 == 0) and (year % 100 == 0):
    print(year,"is a leap year")
    
elif(year%4==0) and (year%100!=0):
    print(year,"is a leap year")
    
else:
    print(year,"is not a leap year")


#Output
#Enter the year:2000
#2000 is a leap year

#Enter the year:2023
#2023 is not a leap year
