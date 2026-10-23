# 04 — Data Structures

Choosing the right data structure makes analytics code easier to understand and maintain.

## Lists — ordered, mutable sequences

```python
revenues = [120, 75, 200]
revenues[0]       # 120 (zero-based index)
revenues[-1]      # 200
revenues[:2]      # [120, 75]
revenues.append(150)
len(revenues)
sum(revenues)
```

## Dictionaries — named fields (key/value pairs)

```python
order = {"order_id": "O-101", "revenue": 120, "delivered": True}
order["revenue"]          # 120
order.get("cost")         # None if key missing
order["cost"] = 80        # Add field
order.keys()
order.values()
order.items()
```

**Common mistake:** `order[0]` does not access the first field of a dictionary. Use a key such as `order["revenue"]`.

## Lists of dictionaries — multiple observations

```python
orders = [
    {"order_id": "O-101", "revenue": 120},
    {"order_id": "O-102", "revenue": 75},
]
orders[0]              # First dictionary
orders[0]["revenue"]   # 120

for order in orders:
    print(order["order_id"])
```

## Tuples and sets

```python
coordinates = (52.52, 13.40)  # Tuple: ordered, immutable
latitude, longitude = coordinates

cities = {"Berlin", "Hamburg", "Berlin"}  # Set: unique values
unique_cities = set(["Berlin", "Hamburg", "Berlin"])
```

## Mutability and references

```python
a = [1, 2]
b = a           # Both names refer to the same list
b.append(3)
print(a)        # [1, 2, 3]

c = a.copy()    # Independent *shallow* copy
```

Mutable: `list`, `dict`, `set`. Immutable: `str`, `int`, `float`, `tuple`. A shallow copy does **not** recursively copy nested objects.

## Comprehensions

```python
revenues = [120, 75, 200]
high = [value for value in revenues if value > 100]  # [120, 200]

orders = [
    {"order_id": "O-101", "revenue": 120, "cost": 80},
    {"order_id": "O-102", "revenue": 75, "cost": 50},
]
profits = {
    order["order_id"]: order["revenue"] - order["cost"]
    for order in orders
}
```

**Review questions:** Is this a list or dictionary? Should I use an index or a key? Am I changing the original object? Does a comprehension improve readability here?
