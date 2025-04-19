students_score = int(input('Enter your grade score:\n'))
print(f'Score: {students_score}%')

if students_score >= 90 and students_score <= 100:
    print('A*, Excellent')
elif students_score <= 90 and students_score >= 80:
    print('B, Good')
elif students_score <= 80 and students_score >= 70:
    print('C, Satisfactory')
elif students_score <= 70 and students_score >= 60:
    print('D, Needs improvement')
else:
    print('F, Fail')