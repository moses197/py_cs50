import re

url = input("URL: ").strip()

if matches := re.search("^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))




#username = re.sub("^(https?://)?(www\.)?twitter\.com/", "", url)
#print(f"Username: {username}")

#username = url.removeprefix("https://twitter.com/")
##username = url.replace("https://twitter.com/", "")
#print(f"Username: {username}")