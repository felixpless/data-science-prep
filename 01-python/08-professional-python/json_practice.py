import json
from pathlib import Path

json_path = Path("01-python/08-professional-python/order.json")

order = {
    "order_id": "O-101",
    "customer": {
        "customer_id": "C-42",
        "city": "Berlin"
    },
    "items": ["Laptop", "Mouse"],
    "revenue": 1200,
    "delivered": True
}

print(order)
print(type(order))

json_string = json.dumps(order)

print(json_string)
print(type(json_string))

parsed_order = json.loads(json_string)

print(parsed_order)
print(type(parsed_order))

with json_path.open("w") as file:
    json.dump(order, file)

with json_path.open("r") as file:
    loaded_order = json.load(file)

print(loaded_order["customer"]["city"])
print(type(loaded_order))