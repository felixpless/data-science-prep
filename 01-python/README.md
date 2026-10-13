# 03 — Functions

Functions encapsulate **reusable logic**. Prefer small functions with one clear responsibility, explicit inputs, and a useful return value.

## Define, call, and return

```python
def calculate_profit(revenue, cost):
    return revenue - cost

profit = calculate_profit(120, 80)  # 40
print(profit)
```

- **Parameters** are names in the definition (`revenue`, `cost`).
- **Arguments** are values passed in a call (`120`, `80`).
- `return` sends a result to the caller; `print` displays it.
- Without an explicit `return`, a function returns `None`.

## One record versus many records

```python
def realized_profit(order):
    if not order["delivered"]:
        return 0
    return order["revenue"] - order["cost"]

orders = [
    {"revenue": 120, "cost": 80, "delivered": True},
    {"revenue": 75, "cost": 50, "delivered": False},
]

total_profit = 0
for order in orders:
    total_profit += realized_profit(order)

print(total_profit)  # 40
```

**Mental model:** `realized_profit(order)` handles **one** observation; the `for` loop processes **many**.

## Defaults, keyword arguments, guard clauses

```python
def price_with_tax(price, tax_rate=0.19):
    return price * (1 + tax_rate)

price_with_tax(100)
price_with_tax(100, tax_rate=0.07)

def margin(revenue, cost):
    if revenue == 0:
        return None  # Undefined margin: avoid division by zero
    return (revenue - cost) / revenue
```

## Multiple return values and scope

```python
def financial_metrics(revenue, cost):
    profit = revenue - cost  # Local variable
    return profit, profit / revenue if revenue else None

profit, profit_margin = financial_metrics(120, 80)
```

Avoid functions that silently depend on global variables. Pass required data as parameters.

## Separate calculations from execution

```python
def calculate_total_revenue(orders):
    return sum(order["revenue"] for order in orders if order["delivered"])

def main():
    orders = [{"revenue": 120, "delivered": True}]
    print(calculate_total_revenue(orders))

if __name__ == "__main__":
    main()
```

**Review questions:** Does the function process one item or a collection? Does it return a value? Could it be tested without reading a file? Does it handle zero denominators?
