import numpy as np

# Subject names as a list
subjects = ["Maths", "English", "Science"]

# Student scores in Math, Science, and English
# Subjects and corresponding scores for 5 students
data = np.array([[85, 92, 78],  # Scores for student 1 in Math, English, Science
                 [76, 88, 82],  
                 [90, 95, 85],  
                 [82, 78, 90],  
                 [95, 85, 76]]) 


# Calculate the mean scores of each student
average_scores = np.mean(data, axis = 1)

print(average_scores)
