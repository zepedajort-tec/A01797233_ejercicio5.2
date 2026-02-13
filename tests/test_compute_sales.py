"""
Unit tests for computeSales module.
"""

from src.compute_sales import (
    build_price_dictionary,
    compute_total_sales,
)


def test_compute_sales_valid_data():
    """Test total sales computation with valid data."""
    catalogue = [
        {"title": "Product1", "price": 10},
        {"title": "Product2", "price": 20},
    ]

    sales = [
        {"Product": "Product1", "Quantity": 2},
        {"Product": "Product2", "Quantity": 1},
    ]

    price_dict = build_price_dictionary(catalogue)
    total = compute_total_sales(price_dict, sales)

    assert total == 40


def test_invalid_price_entries():
    """Test catalogue with invalid price entries."""
    catalogue = [
        {"title": "Product1", "price": "invalid"},
        {"title": "Product2", "price": -10},
        {"price": 50},
        "not a dict",
    ]

    price_dict = build_price_dictionary(catalogue)

    assert not price_dict


def test_sales_with_invalid_quantity():
    """Test sales with invalid quantities."""
    catalogue = [{"title": "Product1", "price": 10}]

    sales = [
        {"Product": "Product1", "Quantity": "invalid"},
        {"Product": "Product1", "Quantity": -2},
    ]

    price_dict = build_price_dictionary(catalogue)
    total = compute_total_sales(price_dict, sales)

    assert total == 0


def test_product_not_in_catalogue():
    """Test sales where product does not exist in catalogue."""
    catalogue = [{"title": "Product1", "price": 10}]

    sales = [{"Product": "Unknown", "Quantity": 5}]

    price_dict = build_price_dictionary(catalogue)
    total = compute_total_sales(price_dict, sales)

    assert total == 0


def test_invalid_sales_structure():
    """Test invalid sales structure input."""
    catalogue = [{"title": "Product1", "price": 10}]

    price_dict = build_price_dictionary(catalogue)

    total = compute_total_sales(price_dict, "invalid structure")

    assert total == 0


def test_invalid_catalogue_structure():
    """Test invalid catalogue structure input."""
    price_dict = build_price_dictionary("invalid structure")

    assert not price_dict
