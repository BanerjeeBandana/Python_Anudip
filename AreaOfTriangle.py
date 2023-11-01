#s1,s2 and s3 are three sides of a triangle

s1=3
s2=4
s3=5

#Calculating the semi-perimeter of the triangle

s=(s1+s2+s3)/2

#Finding the area of the triangle

area=(s*(s-s1)*(s-s2)*(s-s3))**0.5
print("The area of the triangle is %0.2f"%area)

#output
#The area of the triangle is 6.00
