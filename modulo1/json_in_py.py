import json
import re # RegEx

x = {
    "name": "John",
    "age": 99999999,
    "city": "NYC"
}

y = json.dumps(x)

txt = "O rato roeu a rolha da garrafa do rei da Rússia"
z = re.search("^O.*rolha", txt)
print(z)

print(x)
print(y)