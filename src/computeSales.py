import json
import sys
import time

def load_json_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {filename}.")
        return None

def main():
    if len(sys.argv) != 3:
        print("Usage: python computeSales.py priceCatalogue.json salesRecord.json")
        sys.exit(1)

    start_time = time.time()

    price_file = sys.argv[1]
    sales_file = sys.argv[2]

    price_catalogue = load_json_file(price_file)
    sales_record = load_json_file(sales_file)

    if price_catalogue is None or sales_record is None:
        sys.exit(1)

    price_dict = { }
    for item in price_catalogue:
        try:
            price_dict[item["title"]] = float(item["price"])
        except (KeyError, ValueError, TypeError):
            print(f"Invalid product entry detected: {item}")

    total_cost = 0.0
    for sale in sales_record:
        try:
            product = sale["Product"]
            quantity = float(sale["Quantity"])

            if product not in price_dict:
                print(f"Product '{product}' not found in catalogue.")
                continue

            total_cost += price_dict[product] * quantity

        except (KeyError, ValueError, TypeError):
            print(f"Invalid sales entry detected: {sale}")

    elapsed_time = time.time() - start_time

    print("SALES RESULTS")
    print("====================")
    print(f"Total Cost: {total_cost:.2f}")
    print(f"Execution Time: {elapsed_time:.4f} seconds")
    with open("../output/SalesResults.txt", "w", encoding="utf-8") as file:
        file.write("SALES RESULTS\n")
        file.write("====================\n")
        file.write(f"Total Cost: {total_cost:.2f}\n")
        file.write(f"Execution Time: {elapsed_time:.4f} seconds\n")

if __name__ == "__main__":
    main()