import pytest


def test_eco_friendly_title(sale):
    sale.open_page()
    sale.verify_header_text('Sale')


def test_compare_presenting(sale):
    sale.open_page()
    sale.verify_comparing('Compare Products')

@pytest.mark.skip(reason="Тест нужно обновить")
def test_whats_new_element(sale):
    sale.open_page()
    sale.verify_whats_new("What's New")
