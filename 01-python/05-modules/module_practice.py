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

wrong_type_order = {
    "order_id": "O-106",
    "revenue": 150,
    "cost": "80 EUR",
    "delivered": True
}

test_orders = [
    {"order_id": "O-101", "revenue": 120, "cost": 80, "delivered": True},
    {"order_id": "O-105", "revenue": 150, "delivered": True},
    {"order_id": "O-106", "revenue": 150, "cost": "80 EUR", "delivered": True},
]

def main():

    for order in test_orders:
        try:
            profit = financial_metrics.calculate_realized_profit(order)

        except KeyError as error:
            print(f"Missing key: {error}")

        except TypeError as error:
            print(f"Invalid data type: {error}")

        else:
            print(f"Successfully processed {order['order_id']}: profit = {profit}")

if __name__ == "__main__":
    main()


