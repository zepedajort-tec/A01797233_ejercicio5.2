"""
Compute total sales cost based on catalogue and sales records.
"""

import json
import sys
import time


def load_json_file(filename):
    """Load JSON file safely."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"ERROR: File '{filename}' not found.")
    except json.JSONDecodeError:
        print(f"ERROR: File '{filename}' contains invalid JSON.")
    except Exception as exc:  # pylint: disable=broad-except
        print(f"Unexpected error reading '{filename}': {exc}")

    return None


def build_price_dictionary(price_catalogue):
    """Create dictionary with product prices validating entries."""
    price_dict = {}

    if not isinstance(price_catalogue, list):
        print("ERROR: Price catalogue must be a list.")
        return price_dict

    for index, item in enumerate(price_catalogue):

        if not isinstance(item, dict):
            print(f"Invalid catalogue entry at index {index}: Not a dict")
            continue

        title = item.get("title")
        price = item.get("price")

        if title is None:
            print(f"Catalogue entry missing 'title': {item}")
            continue

        try:
            price = float(price)

            if price < 0:
                print(f"Negative price detected for '{title}'")
                continue

            price_dict[title] = price

        except (TypeError, ValueError):
            print(f"Invalid price for product '{title}': {price}")

    return price_dict


def compute_total_sales(price_dict, sales_record):
    """Compute total cost of sales validating entries."""
    total_cost = 0.0

    if not isinstance(sales_record, list):
        print("ERROR: Sales record must be a list.")
        return total_cost

    for index, sale in enumerate(sales_record):

        if not isinstance(sale, dict):
            print(f"Invalid sale entry at index {index}: Not a dict")
            continue

        product = sale.get("Product")
        quantity = sale.get("Quantity")

        if product is None:
            print(f"Sale entry missing 'Product': {sale}")
            continue

        if quantity is None:
            print(f"Sale entry missing 'Quantity': {sale}")
            continue

        try:
            quantity = float(quantity)

            if quantity <= 0:
                print(f"Invalid quantity for '{product}': {quantity}")
                continue

        except (TypeError, ValueError):
            print(f"Quantity is not numeric for '{product}': {quantity}")
            continue

        if product not in price_dict:
            print(f"Product '{product}' not found in catalogue.")
            continue

        total_cost += price_dict[product] * quantity

    return total_cost


def save_results(total_cost, elapsed_time):
    """Save results into file."""
    with open("output/SalesResults.txt", "w", encoding="utf-8") as file:
        file.write("SALES RESULTS\n")
        file.write("====================\n")
        file.write(f"Total Cost: {total_cost:.2f}\n")
        file.write(f"Execution Time: {elapsed_time:.4f} seconds\n")


def main():
    """Main execution."""
    if len(sys.argv) != 3:
        print("Usage: python computeSales.py priceCatalogue.json "
              "salesRecord.json")
        sys.exit(1)

    start_time = time.time()

    price_catalogue = load_json_file(sys.argv[1])
    sales_record = load_json_file(sys.argv[2])

    if price_catalogue is None or sales_record is None:
        sys.exit(1)

    price_dict = build_price_dictionary(price_catalogue)

    total_cost = compute_total_sales(price_dict, sales_record)

    elapsed_time = time.time() - start_time

    print("\nSALES RESULTS")
    print("====================")
    print(f"Total Cost: {total_cost:.2f}")
    print(f"Execution Time: {elapsed_time:.4f} seconds")

    save_results(total_cost, elapsed_time)


if __name__ == "__main__":
    main()
