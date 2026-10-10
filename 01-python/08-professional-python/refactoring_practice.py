orders = [
    {"order_id": "O-101", "revenue": 120, "cost": 80, "delivered": True},
    {"order_id": "O-102", "revenue": 75, "cost": 50, "delivered": False},
    {"order_id": "O-103", "revenue": 200, "cost": 130, "delivered": True},
]



def calculate_metrics(orders: list[dict])-> dict[str, float]:

    total_revenue = 0
    total_profit = 0
    
    for order in orders:
        if order["delivered"]:
            total_revenue += order["revenue"]
            total_profit += order["revenue"] - order["cost"]

    return {
        "revenue": total_revenue,
        "profit": total_profit
    }

def main(orders: list[dict]) -> None:
    metrics = calculate_metrics(orders)

    print(f"Revenue: {metrics['revenue']}")
    print(f"Profit: {metrics['profit']}")

if __name__ == "__main__":
    main(orders)
