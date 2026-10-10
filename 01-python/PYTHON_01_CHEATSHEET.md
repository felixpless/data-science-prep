# Python 01 — Essential Cheat Sheet

> Handwritten review of Chapter 01 — Python. Key concepts, methods, syntax, and analytics patterns.

## 1. Variables, Data Types & Operators

```python
name = "Felix"       # str
age = 28             # int
revenue = 120.5      # float
delivered = True     # bool
nothing = None       # NoneType

type(revenue)
isinstance(revenue, float)
int("120")           # 120
float("120.5")       # 120.5
str(120)             # "120"
bool(1)              # True
bool("False")        # True: any nonempty string is truthy
```

| Operator | Meaning | Example |
|---|---|---|
| `+`, `-`, `*`, `/` | Arithmetic | `5 / 2 == 2.5` |
| `//`, `%`, `**` | Floor division, remainder, exponent | `5 // 2 == 2` |
| `==`, `!=`, `<`, `>`, `<=`, `>=` | Comparison | `5 >= 3` |
| `=` | Assignment | `total = 0` |
| `+=`, `-=` | Update accumulator | `total += 100` |

**Remember:** `=` assigns a value; `==` compares values.

## 2. Data Structures — Lists, Dictionaries, Tuples & Sets

### Lists `[]` — ordered, mutable

```python
revenues = [120, 75, 200]
revenues[0]         # 120, first item; indexing starts at 0
revenues[-1]        # 200, last item
revenues[0:2]       # [120, 75]
revenues[:2]        # [120, 75]
revenues[1:]        # [75, 200]
revenues.append(150)
revenues.remove(75)
len(revenues)
sum(revenues)
max(revenues)
min(revenues)
```

### Dictionaries `{}` — key–value pairs

```python
order = {
    "order_id": "O-101",
    "revenue": 120,
    "cost": 80,
    "delivered": True,
}
order["revenue"]           # 120
order.get("revenue")       # 120
order.get("customer_id")   # None if missing
order["revenue"] = 150
order["profit"] = 70
order.keys()
order.values()
order.items()
```

**Critical distinction:** `revenues[0]` accesses a **list by index**. `order["revenue"]` accesses a **dictionary by key**.

### Lists of dictionaries — multiple observations

```python
orders = [
    {"order_id": "O-101", "revenue": 120},
    {"order_id": "O-102", "revenue": 75},
]
orders[0]               # First dictionary
orders[0]["revenue"]    # 120
```

**Mental model:** `orders` = many observations → `orders[0]` = one observation → `orders[0]["revenue"]` = one value.

### Tuples `()` — ordered, immutable

```python
coordinates = (52.52, 13.40)
coordinates[0]
revenue, profit = (470, 170)   # Tuple unpacking
```

### Sets — unique values

```python
cities = {"Berlin", "Hamburg", "Berlin"}
unique_cities = set(["Berlin", "Hamburg", "Berlin"])
```

### Mutable vs immutable, object references

| Mutable | Immutable |
|---|---|
| `list`, `dict`, `set` | `int`, `float`, `str`, `tuple` |

```python
a = [1, 2]
b = a                   # Both variables refer to SAME list
b.append(3)
print(a)                # [1, 2, 3]
b = a.copy()            # Shallow copy, separate outer list
```

For nested lists or dictionaries, `.copy()` is **shallow**: nested mutable objects can remain shared.

## 3. Control Flow — Conditions, Loops, Comprehensions

### `if`, `elif`, `else`

```python
if revenue > 100:
    print("High revenue")
elif revenue == 100:
    print("Exactly 100")
else:
    print("Low revenue")

if revenue > 100 and delivered:
    ...
if revenue > 100 or delivered:
    ...
if not delivered:
    ...
```

`and` = both conditions true; `or` = at least one true; `not` = reverse Boolean.

### `for` loops and accumulators

```python
total_revenue = 0                 # Initialize BEFORE +=
for order in orders:              # order is the current observation
    if order["delivered"]:
        total_revenue += order["revenue"]
```

```python
for number in range(5):
    if number == 2:
        continue                 # Skip this iteration
    if number == 4:
        break                    # Stop loop
```

### Comprehensions

```python
revenues = [120, 75, 200]
high_revenues = [r for r in revenues if r > 100]  # [120, 200]

profits = {
    order["order_id"]: order["revenue"] - order["cost"]
    for order in orders
}
```

A normal loop is preferable when the logic becomes complex.

## 4. Functions — Reusable Business Logic

```python
def calculate_profit(revenue, cost):
    return revenue - cost

profit = calculate_profit(120, 80)  # 40
```

- **Parameters:** `revenue`, `cost` in the definition.
- **Arguments:** `120`, `80` in the function call.
- `return` sends a value back; `print()` displays it.
- No explicit `return` means the function returns `None`.

### Default arguments

```python
def calculate_price(price, tax_rate=0.19):
    return price * (1 + tax_rate)

calculate_price(100)
calculate_price(100, tax_rate=0.07)
```

### Multiple returns / unpacking

```python
def calculate_metrics(revenue, cost):
    profit = revenue - cost
    margin = profit / revenue
    return profit, margin

profit, margin = calculate_metrics(120, 80)
```

### Early return / guard clause

```python
def calculate_margin(revenue, cost):
    if revenue == 0:
        return None
    return (revenue - cost) / revenue
```

### Scope and one-vs-many

```python
def calculate_profit(order):           # ONE observation
    return order["revenue"] - order["cost"]

for order in orders:                   # MANY observations
    profit = calculate_profit(order)
```

Keep variables local and pass data explicitly rather than relying on hidden global state.

## 5. Modules, Imports & Program Structure

A module is a Python file with reusable functions and definitions.

**`financial_metrics.py`:**

```python
def calculate_profit(revenue, cost):
    return revenue - cost
```

**Another Python file:**

```python
from financial_metrics import calculate_profit
profit = calculate_profit(120, 80)

# Alternatively:
import financial_metrics
profit = financial_metrics.calculate_profit(120, 80)
```

### Main guard

```python
def main():
    print("Starting analysis")

if __name__ == "__main__":
    main()
```

This runs `main()` only when the script is executed directly, not when its functions are imported by other modules or tests.

## 6. Errors, Validation & Exception Handling

| Exception | Meaning |
|---|---|
| `KeyError` | Missing dictionary key |
| `TypeError` | Incompatible types / operation |
| `ValueError` | Invalid value, e.g., failed numeric conversion |
| `FileNotFoundError` | File does not exist |
| `ZeroDivisionError` | Division by zero |
| `UnboundLocalError` | Local variable referenced before assignment |

```python
def validate_revenue(revenue):
    if revenue < 0:
        raise ValueError("Revenue cannot be negative")
    return revenue

try:
    revenue = float(order["revenue"])
except ValueError as error:
    print(f"Invalid revenue: {error}")
```

**`raise` signals invalid data; `except` decides how to handle it.**

For batch processing, place `try/except` **inside the loop** so an invalid observation need not stop all later observations:

```python
valid_orders = []
for order in orders:
    try:
        validated_order = validate_order(order)
        valid_orders.append(validated_order)
    except ValueError as error:
        print(f"{order['order_id']}: {error}")
```

```python
try:
    ...
except ValueError:
    ...
else:
    ...   # Only if try succeeded
finally:
    ...   # Always executes
```

## 7. Files — CSV, JSON, Pathlib

### File paths with pathlib

```python
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / "orders.csv"
file_path.exists()
```

- `Path()` represents a path; it does not create a file.
- `__file__` refers to the script, while `Path.cwd()` returns the current working directory.
- `.resolve()` gives an absolute path; `.parent` gives the containing folder.

### Read a CSV with `DictReader`

```python
import csv
orders = []
with file_path.open("r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        orders.append(row)

revenue = float(orders[0]["revenue"])
```

`DictReader` returns dictionaries. **CSV data values start as strings** and may need conversion.

### JSON

```python
import json
order = {"order_id": "O-101", "revenue": 120}

json_string = json.dumps(order)       # Python object -> JSON string
loaded_order = json.loads(json_string)  # JSON string -> Python object

with (BASE_DIR / "order.json").open("w", encoding="utf-8") as file:
    json.dump(order, file)             # Python object -> JSON file

with (BASE_DIR / "order.json").open("r", encoding="utf-8") as file:
    loaded_order = json.load(file)     # JSON file -> Python object
```

Nested structures:

```python
order = {
    "customer": {"city": "Berlin"},
    "items": ["Laptop", "Mouse"],
}
order["customer"]["city"]    # Berlin
order["items"][1]           # Mouse
```

**CSV** = typically tabular; **JSON** = structured or nested data, often used by APIs.

## 8. Object-Oriented Programming (OOP)

```python
class Order:
    def __init__(self, order_id, revenue, cost):
        self.order_id = order_id
        self.revenue = revenue
        self.cost = cost

    def calculate_profit(self):
        return self.revenue - self.cost

order_1 = Order("O-101", 120, 80)
order_1.revenue
order_1.calculate_profit()
```

| Term | Meaning |
|---|---|
| Class | Blueprint |
| Object / instance | Specific entity built from class |
| Attribute | State/data on an object |
| Method | Function belonging to a class |
| `__init__` | Initializes instance |
| `self` | Current instance |

`order_1.calculate_profit` is a **method reference**; `order_1.calculate_profit()` **calls the method**.

## 9. Professional Python — Hints, Tests, Logging, Dependencies, Git

### Type hints

```python
def calculate_profit(revenue: float, cost: float) -> float:
    return revenue - cost

def total_revenue(revenues: list[float]) -> float:
    return sum(revenues)

def calculate_margin(revenue: float, cost: float) -> float | None:
    if revenue == 0:
        return None
    return (revenue - cost) / revenue

def main() -> None:
    ...
```

Type hints describe intended types but **do not enforce them at runtime**.

### Automated testing with pytest

```python
def test_calculate_profit():
    result = calculate_profit(120, 80)
    assert result == 40

def test_empty_orders():
    result = calculate_kpis([])
    assert result["total_revenue"] == 0
```

Run `pytest 01-python/`. Tests catch regressions and edge cases. Our final exercise uncovered two control-flow bugs in the empty-dataset case.

### Logging

```python
import logging
logging.basicConfig(level=logging.INFO)
logging.info("Starting analysis")
logging.warning("Missing values detected")
logging.error("Could not load data")
```

Levels: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`.

### Environments, dependencies, Git

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
pytest 01-python/

git status
git diff
git add 01-python/ PROGRESS.md requirements.txt
git commit -m "Complete Python chapter"
git push origin main
```

`.venv/` belongs in `.gitignore`; dependencies belong in `requirements.txt`.

## 10. The Most Important Pattern — Analytics Pipeline

```text
CSV -> load_orders() -> validate_order() / process_orders()
    -> calculate_kpis() -> main() / presentation
```

```python
def main():
    orders = load_orders()
    valid_orders = process_orders(orders)
    kpis = calculate_kpis(valid_orders)
    print(kpis)

if __name__ == "__main__":
    main()
```

| Function | Responsibility |
|---|---|
| `load_orders()` | Data ingestion |
| `validate_order(order)` | Validate and transform one record |
| `process_orders(orders)` | Loop through many records; handle errors |
| `calculate_kpis(valid_orders)` | Business metric calculations |
| `main()` | Orchestrate workflow |

In our logistics exercise: **6 loaded**, **4 valid**, **2 rejected**, realized **revenue 470**, **profit 170**, **delivery rate 75%**. Four tests passed.

## 11. The 15 Snippets to Memorize

| # | Concept | Syntax / mental model |
|---|---|---|
| 1 | List access | `orders[0]` |
| 2 | Dictionary access | `order["revenue"]` |
| 3 | Nested access | `orders[0]["revenue"]` |
| 4 | Append | `orders.append(order)` |
| 5 | Loop | `for order in orders:` |
| 6 | Condition | `if order["delivered"]:` |
| 7 | Accumulator | `total += value` |
| 8 | Function | `def fn(x): return x` |
| 9 | Call | `result = fn(value)` |
| 10 | Guard clause | `if revenue == 0: return None` |
| 11 | Raise error | `raise ValueError("Invalid value")` |
| 12 | Catch error | `try: ... except ValueError:` |
| 13 | CSV | `csv.DictReader(file)` |
| 14 | Main guard | `if __name__ == "__main__":` |
| 15 | Test assertion | `assert result == expected` |

### Five Essential Principles

1. **A variable references an object.** Assignment does not necessarily copy data.
2. **A function should have one responsibility.** Accept explicit inputs and return results.
3. **One vs many observations.** A function can process one record; a loop iterates over the collection.
4. **Indentation is logic.** It controls conditions, loops, functions, and exception handlers.
5. **Test edge cases.** Empty datasets, invalid types, missing keys, negative values, and division by zero reveal bugs.

## 12. Preparation for Chapter 02 — NumPy & Pandas

Manual aggregation in Chapter 01:

```python
total_revenue = 0
for order in orders:
    if order["delivered"]:
        total_revenue += order["revenue"]
```

A corresponding Pandas expression on correctly typed data:

```python
total_revenue = df.loc[df["delivered"], "revenue"].sum()
```

**The business logic stays the same; the data representation and tools become more powerful.**
