from classes.student import Student
from classes.teacher import Teacher


# FIXME - fix class name misspelling
class Shcool:
    def __init__(self, id: str):
        self.id = id
        self.students: list[Student] = []
        self.teachers: list[Teacher] = []

    def add_student(self, student: Student):
        self.students.append(student)

    def add_teacher(self, teacher: Teacher):
        self.teachers.append(teacher)

    def info(self):
        student_list = ", ".join([student.name for student in self.students]
        teacher_list = ", ".join([teacher.name for teacher in self.teachers])
        return f"School {self.id} has {student_list} and {teacher_list}."  # FIXME Use len() to get the number of students and teachers
