#Create a bar chart to represent monthly expenses in different spending categories and give your conclusion.

#Importing the Numpy library as np
import numpy as np

#Importing the Pyplot sub-module of Matplotlib library as plt
import matplotlib.pyplot as plt

#Storing the categories of expenses in a list
categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation']

#Printing the categories
print("THe categories of expenses are:",categories)

#Monthly expenses in dollars
expenses=[2500,500,300,250,350]

#Printing the expenses
print("The category-wise expenses are:",expenses)

#Setting the figure size of the bar chart
plt.figure(figsize=(12,6))

#Plotting the bar chart where categories and expenses are the x-axis and y-axis of the chart
plt.bar(categories,expenses)

#The title of the chart
plt.title('Monthly Expense Breakdown')

#Providing the xlabel and ylabel of the chart
plt.xlabel('Expense Categories ------->')
plt.ylabel('Monthly Expenses (USD) ------->')

print("The representation of category-wise monthly expenses is shown below:")

#Showing the chart
plt.show()
