import re
number=input("Введіть")
pattern=r'[A-z]+. (\d+)'
res=re.match(pattern, number)
appeal=res.group(1)
change=re.sub(pattern,"Password",appeal)
print(change)
