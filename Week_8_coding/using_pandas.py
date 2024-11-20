# Using pandas
import pandas as pd

# Create a DataFrame using the given student data (Similar to NumPy)
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Emily"],
    "Maths": [85, 75, 90, 82, 95],
    "Science": [92, 88, 95, 78, 85],
    "English": [78, 82, 85, 90, 76]
}

df = pd.DataFrame(data)

# Calculate the average score for each student
df["Average"] = df[["Maths", "Science", "English"]].mean(axis=1)

# Find the student with the highest average score
highest_average_student = df.loc[df["Average"].idxmax(), "Name"]

# Calculate the overall average score for each subject
subject_average = df[["Maths", "Science", "English"]].mean(axis=0)

# Print the results
print("Average score for each student:\n", df["Average"])
print("\nStudent with the highest average score: ", highest_average_student)
print("\nOverall average score for each subject:\n", subject_average)