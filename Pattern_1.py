import re
number=input("Введіть посилання ")
pattern=r'[A-z]+\d{3,5}.[a-z]{5}$'
res=re.match(pattern,number)
if res:
    print("Valid pattern")
else:
    print("Invalid pattern")
