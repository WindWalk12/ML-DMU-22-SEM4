import matplotlib.pyplot as plt
import numpy as np

# Generating random data
x_values = 2 * np.random.rand(100, 1)
y_values = 4 + 3 * x_values + np.random.randn(100, 1)

# Performing linear regression
slope, intercept = np.polyfit(x_values.flatten(), y_values.flatten(), 1)

# Generating points for the regression line
max_x = np.max(x_values)
regression_x = np.linspace(0, max_x)  # Adjust range if needed
regression_y = slope * regression_x + intercept

# Plotting the points and regression line
plt.scatter(x_values, y_values, color='blue', label='Data Points')
plt.plot(regression_x, regression_y, color='red', label='Linear Regression')

# Adding labels and title
plt.title('Scatter Plot with Linear Regression')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()

# Displaying the plot
plt.show()