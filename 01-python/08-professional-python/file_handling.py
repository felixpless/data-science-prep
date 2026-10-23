from pathlib import Path
import csv

file_path = Path("01-python/08-professional-python/orders.txt")
# file_path.write_text("O-101,120,80\nO-102,75,50")
print(file_path)
print(type(file_path))
print(file_path.exists())

content = file_path.read_text()

print(content)
print(type(content))

# rows = content.splitlines()

# print(rows)
# print(type(rows))

# first_row = rows[0]
# columns = first_row.split(",")

# print(columns)
# print(type(columns))

# order_id = columns[0]
# revenue = int(columns[1])
# cost = int(columns[2])

# print(order_id, type(order_id))
# print(revenue, type(revenue))
# print(cost, type(cost))

# orders = []
# rows = content.splitlines()

# for row in rows:
#     columns = row.split(",")
#     order = {"order_id": columns[0],
#              "revenue": int(columns[1]),
#              "cost": int(columns[2])
#              }
#     orders.append(order)


# print(orders)

print()
orders = []
with file_path.open("r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row["revenue"] = int(row["revenue"])
        row["cost"] = int(row["cost"])

        orders.append(row)

print(orders)

total_revenue = 0

for order in orders:
    total_revenue += order["revenue"]

print(total_revenue)