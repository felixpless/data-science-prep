import financial_metrics


orders = [
    {"order_id": "O-101", "revenue": 120, "cost": 80, "delivered": True},
    {"order_id": "O-102", "revenue": 75, "cost": 50, "delivered": False},
    {"order_id": "O-103", "revenue": 210, "cost": 130, "delivered": True},
    {"order_id": "O-104", "revenue": 95, "cost": 60, "delivered": True},
]

bad_order = {
    "order_id": "O-105",
    "revenue": 150,
    "delivered": True
}

def main():
    current_profit = {
        order["order_id"]: financial_metrics.calculate_realized_profit(order)
        for order in orders
    }

    print(current_profit)

    try:
        print(financial_metrics.calculate_realized_profit(bad_order))
    except KeyError as error:
        print(f"Order {bad_order["order_id"]} is missing key: {error}")


if __name__ == "__main__":
    main()

