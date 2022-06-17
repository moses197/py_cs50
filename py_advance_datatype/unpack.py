# unpacking *list,turple  **dictionary

def total(galleons, sickels, knuts):
    return (galleons * 17 + sickels) * 29 + knuts

coins = {"galleons":100, "sickels":50, "knuts":25}
print(total(**coins), "Knuts") 
# print(total(coins["galleons"], coins["sickels"], coins["knuts"]), "Knuts")

# coins = [100, 50, 25]
# print(total(*coins), "Knuts")
# print(total(coins[0], coins[1], coins[2]), "Knuts")


# first, _ = input("What's your name? ").split(" ")
# print(f"hello {first}")

