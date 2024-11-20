class Student:
    """
    This class represents a student with name, age and grades,
    it will include a method to calculate the student's garde status
    """
    
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def get_grade_status(self):
        """
        This method uses nested if statements to determine the student's grade status based
        on their average grade
        """

        average_grade = sum(self.grades) / len(self.grades)

        if average_grade >= 90:
            status = "Excellent!"
        else:
            if average_grade >= 80:
                status = "Good"
            else:
                if average_grade >= 70:
                    status = "Fair"
                else:
                    status = "Needs improvement!"

        return status
    
# Create a student object
student1 = Student("Alice", 16, [85, 97, 78, 95])

# Get the students grade status
grade_status = student1.get_grade_status()
print(f"{student1.name}'s grade status: {grade_status}")