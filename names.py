############## Sort and Read the file #######################333
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip()) #rstrip is use to strip spaces
        
for name in sorted(names, reverse=True):
    print(f"hello, {name}")


######################### Read the file ###########################3333
#with open("names.txt", "r") as file:
#    for line in file:
#        print(f"hello, {line}", end="")
        
        
#    lines = file.readlines()    
#for line in lines:
#    print(f"hello,", line.rstrip()) # end="" can also be use too



########################## Create and Write to file ##################
#name = input("What's your name? ")
#
#with open("names.txt", "a") as file:
#    file.write(f"{name}\n")

###########################################################################################
#file = open("names.txt", "a")
#file.write(f"{name}\n")
#file.close()

#names = []
#
#for _ in range(3):
#    name = input("What's your name? ")
#    names.append(name)
#    # OR
#    #names.append(input("What's your name? "))
#    
#for name in sorted(names):
#    print(f"hello, {name}")
    
