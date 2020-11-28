from selenium.webdriver.common.by import By
from pages.ProductDetailsPage import ProductDetailsPage
from pages.BasePage import BasePage


class HomePage(BasePage):
    profile_icon = "A__accesslink__56"
    wishlist_icon = "A__wishlist__52"
    cart_icon = "A__cartbt__49"
    grid_view_icon_v1 = "I__tiviewgrid__202"
    grid_view_icon_v2 = "I__tiviewgrid__203"
    list_view_icon_v1 = "I__tiviewlist__204"
    list_view_icon_v2 = "I__tiviewlist__205"
    search_field = "INPUTtext____42"
    filter_sidebar = "filter_col"
    open_filters_icon_v1 = "A__openfilter__206"
    open_filters_icon_v2 = "A__openfilter__207"
    black_color_checkbox = "LABEL__containerc__104"
    filter_btn = "filterBtn"
    result_item = "grid_item"
    result_grid = (By.ID, "product_grid")

    def __init__(self, driver):
        super().__init__(driver)

    def go_home_v1(self):
        self.driver.get("https://demo.applitools.com/gridHackathonV1.html")

    def go_home_v2(self):
        self.driver.get("https://demo.applitools.com/gridHackathonV2.html")

    def is_profile_icon_visible(self):
        return self.find((By.ID, self.profile_icon)).is_displayed()

    def is_wishlist_icon_visible(self):
        return self.find((By.ID, self.wishlist_icon)).is_displayed()

    def is_cart_icon_visible(self):
        return self.find((By.ID, self.cart_icon)).is_displayed()

    def is_grid_view_icon_v1_visible(self):
        return self.find((By.ID, self.grid_view_icon_v1)).is_displayed()

    def is_grid_view_icon_v2_visible(self):
        return self.find((By.ID, self.grid_view_icon_v2)).is_displayed()

    def is_list_view_icon_v1_visible(self):
        return self.find((By.ID, self.list_view_icon_v1)).is_displayed()

    def is_list_view_icon_v2_visible(self):
        return self.find((By.ID, self.list_view_icon_v2)).is_displayed()

    def is_search_field_visible(self):
        return self.find((By.ID, self.search_field)).is_displayed()

    def is_filters_icon_v1_visible(self):
        return self.find((By.ID, self.open_filters_icon_v1)).is_displayed()

    def is_filters_icon_v2_visible(self):
        return self.find((By.ID, self.open_filters_icon_v2)).is_displayed()

    def is_filter_sidebar_visible(self):
        return self.find((By.ID, self.filter_sidebar)).is_displayed()

    def open_filters_v1(self):
        self.find((By.ID, self.open_filters_icon_v1)).click()

    def open_filters_v2(self):
        self.find((By.ID, self.open_filters_icon_v2)).click()

    def filter_shoes_by_black_color_v1(self):
        if self.is_filter_sidebar_visible() is False:
            self.open_filters_v1()
        self.click((By.ID, self.black_color_checkbox))
        self.click((By.ID, self.filter_btn))

    def filter_shoes_by_black_color_v2(self):
        if self.is_filter_sidebar_visible() is False:
            self.open_filters_v2()
        self.click((By.ID, self.black_color_checkbox))
        self.click((By.ID, self.filter_btn))

    def get_filter_results_count(self):
        return len(self.find_all((By.CLASS_NAME, self.result_item)))

    def click_result_item(self, index):
        self.click((By.CLASS_NAME, self.result_item), index)
        return ProductDetailsPage(self.driver)
