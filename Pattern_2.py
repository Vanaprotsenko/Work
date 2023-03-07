import re
number=input("Введіть ваші дані таким чином :Компанія:Агропром Власник:Адрій Капіталізація:3млн")
pattern=r'^Компанія:[А-я]+.Власник:[А-я]+.Капіталізація:\d[А-я]+'
res=re.match(pattern,number)
if res:
    print("Valid pattern")
else:
    print("Invalid pattern")
