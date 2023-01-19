from classes.school import Shcool
from classes.student import Student
from classes.teacher import Teacher


def main():
    # TODO - rename both schools to something more descriptive
    # TODO - assign an actual uuid4 to each school
    school = Shcool("123")
    school2 = Shcool("456")

    # FIXME - move each function call to the correct place
    student1 = Student("Fahad", "Doe", 12)
    school2.add_student(student2)
    student2 = Student("Khalid", "Doe", 12)
    school.add_student(student1)

    # TODO - add variables to each attribute of the Teacher class
    # TODO - change last name of teacher
    # TODO - add a new teacher to school2
    teacher1 = Teacher("Abdulrhman", "Doe", 30, "Math")

    # TODO - add
    school.add_teacher(teacher1)
