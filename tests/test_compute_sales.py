"""
Unit tests for computeSales module.
"""

from src.compute_sales import build_price_dictionary, compute_total_sales


def test_compute_sales():
    """Test total sales computation using sample data."""
    catalogue = [
        {"title": "Product1", "price": 10},
        {"title": "Product2", "price": 20}
    ]

    sales = [
        {"Product": "Product1", "Quantity": 2},
        {"Product": "Product2", "Quantity": 1}
    ]

    price_dict = build_price_dictionary(catalogue)

    total = compute_total_sales(price_dict, sales)

    assert total == 40
