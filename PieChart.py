# Project : Pie Chart using Matplotlib

# Import the libraries
import matplotlib.pyplot as pyplot
import numpy as np


# Add data values
data = np.array([30, 25, 15, 15, 15])

# Add labels
mylabels = ['Python', 'C++', 'JavaScript', 'Java', 'PHP']

# Specify a new color for each wedge
mycolors = ['r', '#4CAF50', 'hotpink', 'c', 'orange']

# Draw a Pie Chart with different Properties
pyplot.pie(data, labels=mylabels, shadow=True, startangle=0, colors=mycolors)

# Add Legend
pyplot.legend()

# Display
pyplot.show()
