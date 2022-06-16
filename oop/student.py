class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
        
    def __str__(self) -> str:
        return f"{self.name} from {self.house}"
    
    #setter
    @property
    def name(self):
        return self._name 
    
    #getter    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name
    
    #getter
    @property 
    def home(self):
        return self._house
    
    #setter
    @home.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house
    

def main():
    student = get_student()
    #student.house = "Akinjagunla"
    print(student)
    
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)
    
if __name__ == "__main__":
    main()