import re
number=input("Введіть")
pattern=r'(^имя:[А-я]+ диагноз:[А-я]+)'
result=re.findall(pattern,number)
print(result)
