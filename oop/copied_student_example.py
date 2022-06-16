def main(): # this is turple concept which is immutable unlike list which its value(s) can be change
    student = get_student()
    if student['name'] == "moses":
        student['house'] = "Akinjagunla"
    print(f"{student['name']} from {student['house']}")
    #print(f"{student[0]} from {student[1]}") #This is use for turples
    
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}
    
    #student = {}
    #student["name"] = input("Name: ")
    #student["house"] = input("House: ")
    #return student    
    
    #name = input("Name: ")
    #house = input("House")
    #return (name, house)
    
if __name__ == "__main__":
    main()