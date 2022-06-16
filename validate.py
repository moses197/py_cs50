import re

email = input("What's your email? ").strip()

if re.search("^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")







#email = input("What's your email? ").strip()
#
#username, domain = email.split("@")
#
#if username and domain.endswith(".edu"):
#    print("Valid")
#else:
#    print("Invalid")