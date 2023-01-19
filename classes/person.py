class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def info(self) -> str:
        return f"{self.name} is {self.age} years old."
