# Import matplotlib
import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 3, 9]

# Create the plot
plt.plot(x, y)

# Add labels and title
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Simple line plot")

# Display the plot
plt.show()