from python_final_exercise import calculate_kpis


def test_calculate_kpis():
    orders = [
        {"revenue": 120.0, "cost": 80.0, "delivered": True},
        {"revenue": 75.0, "cost": 50.0, "delivered": False},
        {"revenue": 200.0, "cost": 130.0, "delivered": True},
    ]

    result = calculate_kpis(orders)

    assert result["total_revenue"] == 320.0
    assert result["total_profit"] == 110.0
    assert result["delivery_rate"] == 2 / 3

def test_calculate_kpis_empty_orders():
    result = calculate_kpis([])

    assert result["total_revenue"] == 0
    assert result["total_profit"] == 0
    assert result["delivery_rate"] == 0.0

def main() -> None:
    orders = load_orders()
    valid_orders = process_orders(orders)

    print(f"Valid orders: {len(valid_orders)}")

    calculated_kpis = calculate_kpis(valid_orders)
    print(calculated_kpis)


if __name__ == "__main__":
    main()