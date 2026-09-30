import financial_metrics

# Objects, references and copying

daily_orders = [124, 156, 143, 189, 201]

original_orders = daily_orders.copy()

daily_orders[2] = 148

daily_orders.append(176)
print("Original Orders", original_orders)
print("Daily Orders", daily_orders)

print()

# List reassignment

orders = [100, 200, 300]
backup = orders

orders = orders + [400]

print("Orders: ",orders)
print("Backup: ",backup)
print()
print(id(orders))
print(id(backup))

# DATA STRUCTURES 

customer = {
    "customer_id": "C1024",
    "city": "Vienna",
    "orders": 7,
    "revenue": 842.50
}
print(customer["revenue"])

shipment = {
    "shipment_id":"S-2048",
    "origin":"Berlin",
    "destination":"Vienna",
    "weight_in_kgs": 420,
    "delivered": False
}
print("Destination is: ",shipment["destination"])
print("Delivery is: ",shipment["delivered"])

# Modyfing a dictionary

shipment["delivered"] = True
shipment["destination"] = ["Witzehausen"]
print("Destination is: ",shipment["destination"])
print("Delivery is: ",shipment["delivered"])

# Adding a new key to a dictionary
shipment["delivery_time"] = "14:35"

print(shipment)

# a list containing dictionaries

shipments = [
    {"shipment_id":"S-1001",
     "origin":"Berlin",
     "destination":"Vienna",
     "weight_kg":420
    },
    {"shipment_id":"S-1002",
     "origin":"Hamburg",
     "destination":"Munich",
     "weight_kg":180
    },
    {"shipment_id":"S-1003",
     "origin":"Berlin",
     "destination":"Prague",
     "weight_kg":250
    }
]

print(shipments)

print("kg of shipment from HAM to MUC: ", shipments[1]["weight_kg"])

# Next task: iterate through the shipments

for shipment_x in shipments:             #“For every element in shipments, temporarily call that element shipment_x.”
    print(shipment_x["destination"])     #'--> in that dictionary print element[]'

total_shipment_weight = 0
for i in shipments:
    total_shipment_weight += i["weight_kg"] 
print("Total Shipment in kg: ",total_shipment_weight)


total_shipment_weight_average = total_shipment_weight / len(shipments)

print("Shipment Weight Avg.:", round(total_shipment_weight_average))

overweight_shipment_weight = 0
for shipment in shipments:
    if shipment["weight_kg"] > 200:
        overweight_shipment_weight += shipment["weight_kg"]
print(overweight_shipment_weight)

# Tetrieval Excercise

orders = [
    {"order_id": "O-101", "revenue": 120, "delivered": True},
    {"order_id": "O-102", "revenue": 75, "delivered": False},
    {"order_id": "O-103", "revenue": 210, "delivered": True},
    {"order_id": "O-104", "revenue": 95, "delivered": True},
]

total_revenue = 0
for order in orders:
    if order["delivered"] == True:
        total_revenue += order["revenue"]
print("Total Revenue is: ", total_revenue) 

for order in orders:
    if order["delivered"] == False:
        print(order["order_id"], "Not delivered")
    else:
        print(order["order_id"], "Delivered")

for order in orders:
    if order["revenue"] >= 200:
        print("Order", order["order_id"], "has a High Value")
    elif order["revenue"] >= 100:
        print("Order", order["order_id"], "has a Medium Value")
    else:
        print("Order", order["order_id"], "has a Low Value")

# FUNCTIONS
print("FUNCTIONS")
def classify_order(revenue):
    if revenue >= 200:
        return " has a High Value"
    elif revenue >= 100:
        return " has a Medium Value"
    else:
        return " has a Low Value"

classify_order(120)
category = classify_order(120)
print(category)

for order in orders:
    print(order["order_id"], classify_order(order["revenue"]))

# MULTIPLE PARAMETERS
print("MULTIPLE PARAMTERS")
def calculate_shipping_cost(weight_kg, distance_km):
    cost = weight_kg * 0.05 + distance_km * 0.02
    return cost

shipping_cost = calculate_shipping_cost(420,680)
print("Shipping Cost of ", shipping_cost)

# SCOPE
def calculate_cost(weight_kg, fuel_surcharge):
    cost = weight_kg * 0.05 + fuel_surcharge
    return cost

shipping_cost = calculate_cost(100,5)
print(shipping_cost)

def calculate_cost(weight_kg, distance_km, fuel_surcharge=5):
    cost = weight_kg * 0.05 + distance_km * 0.02 + fuel_surcharge
    return cost
print()
shipping_cost_1 = calculate_cost(420,680, fuel_surcharge=5)
shipping_cost_2 = calculate_cost(weight_kg = 420, distance_km = 680, fuel_surcharge=12)
print(shipping_cost_1)
print(shipping_cost_2)

# passing a dictionary to a function

order_dictionary = {
    "order_id": "O-102",
    "revenue": 75,
    "delivered": False
}

def get_order_status(order_dictionary):
        if order_dictionary["delivered"]:
            return "Delivered"
        else: 
            return "Not Delivered"

status = get_order_status(order_dictionary)
print(status)

# use multiple dictionary fields

order_dictionary["cost"]=50
print(order_dictionary)

def calculate_profit(order):
    profit = order["revenue"] - order["cost"]
    return profit

profit = calculate_profit(order_dictionary)
print("The profit of the order ist ",profit)

# one function using multiple fields from a dictionary plus business logic.
order_dictionary["delivered"] = True

# def calculate_realized_profit(order):
#     if order["delivered"]:
#         profit = order["revenue"] - order["cost"]
#     else:
#         profit = 0
#     return profit

# print("The Realized Profit of the order is ", calculate_realized_profit(order_dictionary))

# Early Returns
print("Early returns")

# def calculate_realized_profit(order):
#     if order["delivered"]:
#         return order["revenue"] - order["cost"]
#     else:
#         return 0

# print("The Realized Profit of the order is ", calculate_realized_profit(order_dictionary))

# Next: applying our function to multiple orders
# Now we’re ready to combine the two ideas Ive learned:
# function → handles one order
# loop → applies it to many orders 
print("Multiple Orders")

orders = [
    {"order_id": "O-101", "revenue": 120, "cost": 80, "delivered": True},
    {"order_id": "O-102", "revenue": 75, "cost": 50, "delivered": False},
    {"order_id": "O-103", "revenue": 210, "cost": 130, "delivered": True},
    {"order_id": "O-104", "revenue": 95, "cost": 60, "delivered": True},
]


# for order in orders:
#     print(order["order_id"], calculate_realized_profit(order))

# What is the total realized profit across all orders?

total_realized_profit = 0 

# for order in orders:
#     total_realized_profit += calculate_realized_profit(order)

print(total_realized_profit)

# print("Returning multiple values")
# def calculate_financial_metrics(orders):
#     total_revenue = 0
#     total_realized_profit = 0
#     for order in orders:
#         total_revenue += order["revenue"]
#         total_realized_profit += calculate_realized_profit(order)
#     return total_revenue, total_realized_profit
    

# print(calculate_financial_metrics(orders))

# revenue = calculate_financial_metrics(orders)[0]
# print("Revenue is ", revenue)
# profit = calculate_financial_metrics(orders)[1]
# print("Profit is ", profit)

print()

orders = [
    {"order_id": "O-101", "revenue": 120, "cost": 80, "delivered": True},
    {"order_id": "O-102", "revenue": 75, "cost": 50, "delivered": False},
    {"order_id": "O-103", "revenue": 210, "cost": 130, "delivered": True},
    {"order_id": "O-104", "revenue": 95, "cost": 60, "delivered": True},
]

def calculate_realized_profit(order):
    if order["delivered"]:
        return order["revenue"] - order["cost"]
    else:
        return 0

# Next concept: functions returning dictionaries
print()
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
metrics = calculate_financial_metrics(orders)
print(metrics["realized_profit"])

# LIST COMPREHENSION

order_ids = [order["order_id"] for order in orders]

delivered_order_ids = [
    order["order_id"]
    for order in orders
    if order["delivered"]
]

print(delivered_order_ids)
print()
delivered_profits = [
    calculate_realized_profit(order)
    for order in orders
    if order["delivered"]
]
print(delivered_profits)

print()

high_revenue_orders = [
    order["order_id"]
    for order in orders
    if order["revenue"] >= 100
]
print(high_revenue_orders)

# DICTIONARY COMPREHENSION
print()
revenue_by_order = {
    order["order_id"]: order["revenue"]
    for order in orders
}
print(revenue_by_order)
print()
delivered_profit_by_order = {
    order["order_id"]: calculate_realized_profit(order)
    for order in orders
    if order["delivered"]
}
print(delivered_profit_by_order)

# TUPLES

# List → mutable
#coordinates = [52.52, 13.40]
#coordinates[0] = 48.20      # ✅

# Tuple → immutable
#coordinates = (52.52, 13.40)
#coordinates[0] = 48.20      # ❌

# SETS
print()
delivery_status = {
    order["delivered"]
    for order in orders
}
print(delivery_status)

print()

# filtering vs conditional transformation.
revenue_categories = [
    "High" if order["revenue"] >= 100 else "Standard"
    for order in orders
]
print(revenue_categories)

print("mapping each order ID to High or Standard:")

revenue_category_by_order = {
    order["order_id"]: "High" if order["revenue"] >= 100 else "Standard"
    for order in orders
}
print(revenue_category_by_order)

print("module import")

for order in orders:
    print(order["order_id"], financial_metrics.calculate_realized_profit(order))