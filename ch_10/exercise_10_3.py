import exercise_10_2 as person


class Student(person.Person):
    _next_id = 0

    def __init__(self, name):
        super().__init__(name)
        self._id = Student._next_id
        Student._next_id += 1

    def get_id_num(self):
        return self._id


class Grades(object):
    def __init__(self):
        """Create empty grade book"""
        self._students = []
        self._grades = {}
        self._is_sorted = True

    def add_student(self, student):
        """Assumes: student is of type Student
        Add student to the grade book"""
        if student in self._students:
            raise ValueError('Duplicate student')
        self._students.append(student)
        self._grades[student.get_id_num()] = []
        self._is_sorted = False

    def add_grade(self, student, grade):
        """Assumes: grade is a float
        Add grade to the list of grades for student"""
        try:
            self._grades[student.get_id_num()].append(grade)
        except:
            raise ValueError('Student not in mapping')

    def grades(self, student):
        """Return a list of grades for student"""
        try:
            return self._grades[student.get_id_num()][:].copy()
        except:
            raise ValueError('Student not in mapping')

    def get_students(self):
        """Return a sorted list of the students in the grade book"""
        if not self._is_sorted:
            self._students.sort()
            self._is_sorted = True
        return self._students[:]

    def get_students_above(self, grade):
        """Return the students a mean grade > g one at a time"""
        for s in self._students:
            grades_s = self._grades[s.get_id_num()]
            if len(grades_s) > 0 and sum(grades_s) / len(grades_s) > grade:
                yield s


student_1 = Student('Student One')
student_2 = Student('Student Two')
student_3 = Student('Student Three')
grades_in = Grades()
grades_in.add_student(student_1)
grades_in.add_student(student_2)
grades_in.add_student(student_3)
grades_in.add_grade(student_1, 2)
grades_in.add_grade(student_1, 3)
grades_in.add_grade(student_2, 5)
grades_in.add_grade(student_2, 6)

for st in grades_in.get_students_above(4):
    print(st.get_name())
