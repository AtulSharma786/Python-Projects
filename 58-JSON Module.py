import json

data = '{"var1":"atul", "var2":56}'

parsed = json.loads(data)

print(parsed["var1"])
print(type(parsed))


data2 = {
    "channel_name": "codewithharry",
    "cars": ["bmw", "audi", "ferrari"],
    "fridge": ('roti', 540),
    "isbad": False
}

jscomp = json.dumps(data2)
print(jscomp)
