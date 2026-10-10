from pathlib import Path
import csv

file_path = Path("01-python/08-professional-python/orders_final.csv")
print(file_path.exists())

print()


def load_orders() -> list[dict]:
    order_list = []
    with file_path.open("r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            order_list.append(row)

    return order_list



orders = load_orders()

print(orders)

print()

def validate_order(order: dict) -> dict:

    revenue = float(order["revenue"])
    cost = float(order["cost"])

    if revenue < 0:
        raise ValueError("Revenue cant be negative")
    if cost < 0:
        raise ValueError("Cost cannot be negative")

    validated_order = {
        "order_id": order["order_id"],
        "revenue": revenue,
        "cost": cost,
        "delivered": order["delivered"] == "True"
    }

    return validated_order

def process_orders(orders: list[dict]) -> list[dict]:
    valid_orders = []

    for order in orders:
        try:
            validated_order = validate_order(order)
            valid_orders.append(validated_order)

        except ValueError as error:
            print(f"The order_id is {order["order_id"]} and the error is {error}")

    return valid_orders

orders = load_orders()
valid_orders = process_orders(orders)

print(f"Valid orders: {len(valid_orders)}")

print()

def calculate_kpis(valid_orders: list[dict]) -> dict[str, float]:
    kpis = {}
    total_revenue = 0
    total_cost = 0
    delivered_count = 0

    for order in valid_orders:
        if order["delivered"]:
            total_revenue += order["revenue"]
            total_cost += order["cost"]
            delivered_count += 1
    total_profit = total_revenue - total_cost

    if len(valid_orders) == 0:
        delivery_rate = 0.0
    else:
        delivery_rate = delivered_count / len(valid_orders)


    kpis = {
        "total_revenue": total_revenue,
        "total_profit": total_profit,
        "delivery_rate": delivery_rate
    }

    return kpis

calculated_kpis = calculate_kpis(valid_orders)

print(calculated_kpis)