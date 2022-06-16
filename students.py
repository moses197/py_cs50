import csv
################################### Writing in CSV file #######################33333
name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})



################################## Reading for CSV file
#students = []
#
#with open("students.csv") as file:
#    reader = csv.DictReader(file)
#    for row in reader:
#        students.append({"name": row["name"],
#                         "home": row["home"]})
#        
#    ## OR     
#    #for line in file:
#    #    name, house = line.rstrip().rsplit(",")
#    #    student = {"name": name, "house": house}
#    #    #student["name"] = name
#    #    #student["house"] = house
#    #    students.append(student) 
#        
#        
##def get_name(student): # This function can be use as "key=get_name"
##    return student["name"]
#
#
#for student in sorted(students, key=lambda student: student["name"]):
#    print(f"{student['name']} is in {student['home']}")       
#        

#        students.append(f"{name} is in {house}")
#        
#for student in sorted(students):
#    print(student)
    
    
    
#####################################################
#with open("students.csv") as file:
#    for line in file:
#        name, house = line.rstrip().rsplit(",")
#        print(f"{name} is in {house}")
#        
#        #OR 
#        #row = line.rstrip().rsplit(",")
#        #print(f"{row[0]} is in {row[1]}")