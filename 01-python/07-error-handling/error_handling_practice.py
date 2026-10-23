test_orders = [
    {"order_id": "O-101", "revenue": 120, "cost": 80, "delivered": True},
    {"order_id": "O-105", "revenue": 150, "delivered": True},
    {"order_id": "O-106", "revenue": 150, "cost": "80 EUR", "delivered": True},
    {"order_id": "O-107", "revenue": -500, "cost": 80, "delivered": True},
    {"order_id": "O-108", "revenue": 300, "cost": -890, "delivered": True}
]


def calculate_realized_profit(order):    
    if not order["delivered"]:
        return 0

    if order["revenue"] < 0:
        raise ValueError("Revenue cannot be negative")

    if order["cost"] < 0:
        raise ValueError("Cost cannot be negative")

    return order["revenue"] - order["cost"]
for order in test_orders:
    try:
        profit = calculate_realized_profit(order)
        print(order["order_id"], profit)
    except KeyError as error:
        print(f"{order["order_id"]}: {error}")

    except TypeError as error:
        print(f"{order["order_id"]}: {error}")

    except ValueError as error:
        print(f"{order["order_id"]}: {error}")
