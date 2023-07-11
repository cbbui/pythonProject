import json

data = '{"var1":"Muskan", "var2":56}'
# print(data)

par = json.loads(data)
print((par))




data2 = {
    "channel_name": "Muskankaur",
    "cars": ['bmw', 'audi a8', 'ferrari'],
    "fridge": ('banana', 'apples'),
    "isbad": False
}

jscomp = json.dumps(data2)
print(jscomp)



