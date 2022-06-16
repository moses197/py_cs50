name = input("What's your name? ")

match name: #This just like a switch statement just like other programming languages
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Moses":
        print("Akinjagunla")
    case _: #this means default incase none of the above is included. Just note the underscore
        print("Who? ")