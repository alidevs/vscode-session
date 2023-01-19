from classes.person import Person
from classes.school import Shcool


class Student(Person):
    def __init__(self, name: str, age: int, grade: int):
        """
        Initialize a new student object with the given name, age, and grade.
        The student is not enrolled in a school by default.
        The student's school is set to None.

        :param name: The name of the student
        :param age: The age of the student
        :param grade: The grade of the student

        :type name: str
        :type age: int
        :type grade: int

        :return: None
        """
        super().__init__(name, age)
        self.grade = grade

    def info(self) -> str:
        """
        Return a string containing the student's name, age, and grade.
        The string is formatted as follows:
        "{name} is {age} years old and in grade {grade}."
        :return: A string containing the student's name, age, and grade.
        :rtype: str

        """
        # TODO - extract the return statement to a variable
        return f"{self.name} is {self.age} years old and in grade {self.grade}."

    def assign_school(self, school):
        """
        Assign the student to a school.
        This method is called by the school's enroll method.
        It should not be called directly.
        The school should be assigned to the student's school attribute.
        The student should be added to the school's students list.
        The student's school should be assigned to the school's students list.

        :param school: The school to assign to the student.
        :type school: Shcool

        :return: None
        """
        self.school = school

    def enroll(self, school: Shcool):
        """
        Enroll the student in a school.
        This method should call the school's add_student method.
        This method should call the student's assign_school method.

        :param school: The school to enroll the student in.
        :type school: Shcool

        :return: None
        """
        school.add_student(self)
        self.assign_school(school)
