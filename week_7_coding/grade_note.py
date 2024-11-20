class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    grade_status = ""
    grades = []
    grade_average = 0

    def calculate_average(self, grades, grade_average):
        grade_average = sum(self.grades)/4
        return grade_average
    
    def set_status(grade_average, grade_status):
        if grade_average >=90:
            if grade_average <= 100:
                print("Wrong code")
            else:
                ("A, Excellent")