import numpy as np

# Create a numpy array directly with the data
data = np.array([
    [85, 92, 78],
    [76, 88, 82],  
    [90, 95, 85],  
    [82, 78, 90],  
    [95, 85, 76]
])

# Calculate the average score for each student
average_scores = np.mean(data, axis = 1)

# Find the student with the highest average score using ArgMax (Argument max) for index
highest_avg_student_index = np.argmax(average_scores)

# Calculate the overall average score for each subject (column)
subject_averages = np.mean(data, axis = 0)

# Print the results
print("The average score for each student:", average_scores)
print("Index of student with the highest average score:", highest_avg_student_index)
print("Overall average score for each subject:", subject_averages)