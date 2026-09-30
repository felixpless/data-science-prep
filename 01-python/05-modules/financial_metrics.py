def calculate_realized_profit(order):
    if not order["delivered"]:
        return 0
    return order["revenue"] - order["cost"]


def calculate_financial_metrics(orders):
    total_revenue = 0
    total_realized_profit = 0

    for order in orders:
        total_revenue += order["revenue"]
        total_realized_profit += calculate_realized_profit(order)

    return {
        "revenue": total_revenue,
        "realized_profit": total_realized_profit
    }
