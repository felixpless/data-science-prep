def calculate_profit(revenue: float, cost: float) -> float:
    return revenue - cost

print(calculate_profit(120.0, 80.0))
print(calculate_profit(120, 80))

def calculate_total_revenue(revenues: list[float]) -> float:
    return sum(revenues)