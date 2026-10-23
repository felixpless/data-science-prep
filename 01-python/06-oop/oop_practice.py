class Order:
    def __init__(self, order_id, revenue, cost, delivered):
        self.order_id = order_id
        self.revenue = revenue
        self.cost = cost
        self.delivered = delivered
    def calculate_profit(self):
        if not self.delivered:
            return 0

        return self.revenue - self.cost
    def get_margin(self):
        if self.revenue == 0 or not self.delivered:
            return None
        

        return self.calculate_profit() / self.revenue
    
    def mark_as_delivered(self):
        self.delivered = True
            

order_1 = Order("O-101", 120, 80, True)
order_2 = Order("0-102", 75, 50, False)
order_3 = Order("O-103", 0, 20, True)

print(f"{order_1.order_id} Profit: {order_1.calculate_profit()} & Margin: {order_1.get_margin()}")
print(f"{order_2.order_id} Profit: {order_2.calculate_profit()} & Margin: {order_2.get_margin()}")
print(f"{order_3.order_id} Profit: {order_3.calculate_profit()} & Margin: {order_3.get_margin()}")

print("Changing Obect State")
print(order_2.delivered)
order_2.mark_as_delivered()
print(order_2.delivered)
print(order_2.calculate_profit())
print(order_2.get_margin())


print("My Own OOP Method")
class Shipment:
    def __init__(self, shipment_id, distance_km, cost, delivered):
        self.shipment_id = shipment_id
        self.distance_km = distance_km
        self.cost = cost 
        self.delivered = delivered

    def cost_per_km(self):
        if self.distance_km == 0:
            return None
        return self.cost / self.distance_km

    def mark_as_delivered(self):
        self.delivered = True

shipment_1 = Shipment("S-001", 500, 750, False)

print(shipment_1.cost_per_km())

print(shipment_1.delivered)

shipment_1.mark_as_delivered()

print(shipment_1.delivered)