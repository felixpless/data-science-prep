from refactoring_practice import calculate_metrics


def test_calculate_metrics():
    orders = [
        {"order_id": "O-101", "revenue": 120, "cost": 80, "delivered": True},
        {"order_id": "O-102", "revenue": 75, "cost": 50, "delivered": False},
    ]

    result = calculate_metrics(orders)

    assert result["revenue"] == 120
    assert result["profit"] == 40

def test_calculate_metrics_no_delivered_orders():
    orders = [
        {"order_id": "O-103", "revenue": 120, "cost": 80, "delivered": False},
        {"order_id": "O-104", "revenue": 75, "cost": 50, "delivered": False},
    ]

    result = calculate_metrics(orders)

    assert result["revenue"] == 0
    assert result["profit"] == 0