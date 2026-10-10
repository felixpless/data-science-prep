from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

print(BASE_DIR)

json_path = BASE_DIR / "order.json"

try:
    with json_path.open("r") as file:
        content = file.read()

except FileNotFoundError as error:
    print(f"File not found: {error}")

else:
    print("File loaded successfully.")
    print(content)
