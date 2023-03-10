import re
number=input("Введіть")
pattern=r'(^диагноз:[А-я]+)'
result=re.findall(pattern,number)
print(result)
