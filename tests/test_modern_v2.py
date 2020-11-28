from conftest import validate_window, validate_element
from pages import HomePage


def test_elements(browser, eyes):
    home_page = HomePage(browser)
    home_page.go_home_v2()
    validate_window(browser, eyes, "Task 1", "Cross-Device Elements Test")


def test_shopping_experience(browser, eyes):
    home_page = HomePage(browser)
    home_page.go_home_v2()
    home_page.filter_shoes_by_black_color_v2()
    validate_element(browser, eyes, home_page.result_grid, "Task 2", "Filter Results Test")


def test_product_details(browser, eyes):
    home_page = HomePage(browser)
    home_page.go_home_v2()
    home_page.filter_shoes_by_black_color_v2()
    home_page.click_result_item(1)
    validate_window(browser, eyes, "Task 3", "Product Details Test")
