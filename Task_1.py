import requests
import json
result = requests.get("https://api.monobank.ua/bank/currency")

enter_money = int(input("Введіть сумму гривень "))
res = json.loads(result.text)

output = f"Dollar : {res[0]['rateSell']}"

currency = int(res[0]['rateSell'])

print(output)
print(currency * enter_money )

