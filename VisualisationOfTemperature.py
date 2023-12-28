#Visualize the daily temperature changes over time in a city and give your conclusion

#Importing the Numpy library as np
import numpy as np

#Importing the Pyplot sub-module of Matplotlib library as plt
import matplotlib.pyplot as plt

#Storing the days of a month of 31 days in a list
days=list(range(1,32))

#Printing the days
print("The days are:",days)

#Storing the temperature of these days
temperature=[65,65,63,62,64,62,62,63,64,63,63,64,63,60,63,65,64,66,63,64,64,65,54,59,63,60,62,57,55,62,64]

#Printing the temperatures
print("The temperatures are:",temperature)

#Plotting the visualisation where days and temperature are the x-axis and y-axis of the plot,the colour is red,the marker edge colour is blue
plt.plot(days,temperature, color='red',mec='blue',marker='.')

#The title of the plot
plt.title('Temp. of Shimla (August)')

#Providing the xlabel and ylabel of the plot 
plt.xlabel('Days of the month------->')
plt.ylabel('Temperature------->')

print("The visualisation is shown below:")

#Showing the plot
plt.show()

#Output
#The days are: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
#The temperatures are: [65, 65, 63, 62, 64, 62, 62, 63, 64, 63, 63, 64, 63, 60, 63, 65, 64, 66, 63, 64, 64, 65, 54, 59, 63, 60, 62, 57, 55, 62, 64]
#The visualisation is shown below:
