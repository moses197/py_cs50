i = 1
while i < 5:
    print(i)
    j = 1
    if i==j:
        print("NULL", end="")
    while j < i:
        print(j, end="")
        j+=1
            
    i+=1
    print("\n", end="")
    print("----------------------")