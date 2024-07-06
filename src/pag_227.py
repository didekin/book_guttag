from statistics import mean


class Grades(object):
    def __init__(self, students, gradesin):
        self.__students = students
        self.__grades = gradesin

    def get_students_above(self, grade):
        """Return the students a mean grade > g one at a time"""
        for student in self.__students:
            if mean(self.__grades[student]) > grade:
                yield student


students_1 = ['Pedro', 'Luis', 'Paco']
grades_1 = {'Pedro': [3, 2, 4], 'Luis': [4, 5, 6], 'Paco': [6, 7, 8]}
gradesClass_1 = Grades(students_1, grades_1)

for s in gradesClass_1.get_students_above(6):
    print(s)
