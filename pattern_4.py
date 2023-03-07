import re
number=input("Введіть")
pattern=r'(\d+)'
res=re.match(pattern, number)
result=res.group(1)
print(result)
