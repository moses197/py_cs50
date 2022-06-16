class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name


class Student(Wizard):
    def __init__(self, name, house) -> None:
        super().__init__(name)
        self.house = house

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        
    def __str__(self) -> str:
        return f"Professor name is {self.name} and he teaches {self.subject}"

wizard = Wizard("Albus")
student = Student("Harry", "Akinjagunla")
professor = Professor("Moses", "CSC")

print(professor)