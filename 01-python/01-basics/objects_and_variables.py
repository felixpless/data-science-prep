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
