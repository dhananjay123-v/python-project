import re

email = input("What's your email?: ").strip()

# Updated regular expression for Gmail addresses
# if re.search(r"^\w+@gmail\.(com|edu|gov|net|org)$", email,re.IGNORECASE): // check gmail with domain
# if re.search(r"^\w+@\w+\.edu$", email,re.IGNORECASE):                     // check sub domain after @ .edu
# if re.search(r"^\w+@(\w+\.)?\w+\.(edu|com|org)$", email,re.IGNORECASE): # (?)check @sub domain and another sub domain with .domain
if re.search(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email,re.IGNORECASE):
    print("Valid")
else:
    print("Invalid") 


