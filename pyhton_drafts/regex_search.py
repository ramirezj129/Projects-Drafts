import re

email = input("Enter an email: ").strip()

if re.search(r"^\w+@(\w+\.)*?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
