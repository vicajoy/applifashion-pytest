import pytest
from pages import HomePage
import softest


class TraditionalTestsV1(softest.TestCase):

    @pytest.fixture(autouse=True)
    def _setup(self, browser):
        self._browser = browser

    def test_elements(self):
        home_page = HomePage(self._browser)
        home_page.go_home_v1()
        self.soft_assert(self.assertTrue, home_page.report(1, "Profile icon is displayed",
                                                           home_page.profile_icon,
                                                           home_page.is_profile_icon_visible()))
        self.soft_assert(self.assertTrue, home_page.report(1, "Cart icon is displayed",
                                                           home_page.cart_icon, home_page.is_cart_icon_visible()))

        if home_page.get_device_name() == "Laptop":
            self.soft_assert(self.assertTrue, home_page.report(1, "Wishlist icon is displayed",
                                                               home_page.wishlist_icon,
                                                               home_page.is_wishlist_icon_visible()))
            self.soft_assert(self.assertTrue, home_page.report(1, "Grid view icon is displayed",
                                                               home_page.grid_view_icon_v1,
                                                               home_page.is_grid_view_icon_v1_visible()))
            self.soft_assert(self.assertTrue, home_page.report(1, "List view icon is displayed",
                                                               home_page.list_view_icon_v1,
                                                               home_page.is_list_view_icon_v1_visible()))
            self.soft_assert(self.assertTrue, home_page.report(1, "Search field is displayed",
                                                               home_page.search_field,
                                                               home_page.is_search_field_visible()))
            self.soft_assert(self.assertTrue, home_page.report(1, "Filter sidebar is displayed",
                                                               home_page.filter_sidebar,
                                                               home_page.is_filter_sidebar_visible()))
            self.soft_assert(self.assertTrue, home_page.report(1, "Filters icon is not displayed",
                                                               home_page.open_filters_icon_v1,
                                                               home_page.is_filters_icon_v1_visible() is False))
            self.assert_all()

        elif home_page.get_device_name() == "Tablet":
            self.soft_assert(self.assertTrue, home_page.report(1, "Wishlist icon is not displayed",
                                                               home_page.wishlist_icon,
                                                               home_page.is_wishlist_icon_visible() is False),
                             "Wishlist icon is displayed")
            self.soft_assert(self.assertTrue, home_page.report(1, "Grid view icon is not displayed",
                                                               home_page.grid_view_icon_v1,
                                                               home_page.is_grid_view_icon_v1_visible() is False))
            self.soft_assert(self.assertTrue, home_page.report(1, "List view icon is not displayed",
                                                               home_page.list_view_icon_v1,
                                                               home_page.is_list_view_icon_v1_visible() is False))
            self.soft_assert(self.assertTrue, home_page.report(1, "Search field is displayed",
                                                               home_page.search_field,
                                                               home_page.is_search_field_visible()))
            self.soft_assert(self.assertTrue, home_page.report(1, "Filter sidebar is not displayed",
                                                               home_page.filter_sidebar,
                                                               home_page.is_filter_sidebar_visible() is False))
            self.soft_assert(self.assertTrue, home_page.report(1, "Filters icon is displayed",
                                                               home_page.filter_sidebar,
                                                               home_page.is_filters_icon_v1_visible()))
            self.assert_all()

        elif home_page.get_device_name() == "Mobile":
            self.soft_assert(self.assertTrue, home_page.report(1, "Wishlist icon is not displayed",
                                                               home_page.wishlist_icon,
                                                               home_page.is_wishlist_icon_visible() is False))
            self.soft_assert(self.assertTrue, home_page.report(1, "Grid view icon is not displayed",
                                                               home_page.grid_view_icon_v1,
                                                               home_page.is_grid_view_icon_v1_visible() is False))
            self.soft_assert(self.assertTrue, home_page.report(1, "List view icon is not displayed",
                                                               home_page.list_view_icon_v1,
                                                               home_page.is_list_view_icon_v1_visible() is False))
            self.soft_assert(self.assertTrue, home_page.report(1, "Search field is not displayed",
                                                               home_page.search_field,
                                                               home_page.is_search_field_visible() is False))
            self.soft_assert(self.assertTrue, home_page.report(1, "Filter sidebar is not displayed",
                                                               home_page.filter_sidebar,
                                                               home_page.is_filter_sidebar_visible() is False))
            self.soft_assert(self.assertTrue, home_page.report(1, "Filters icon is displayed",
                                                               home_page.filter_sidebar,
                                                               home_page.is_filters_icon_v1_visible()))
            self.assert_all()

    def test_shopping_experience(self):
        home_page = HomePage(self._browser)
        home_page.go_home_v1()
        home_page.filter_shoes_by_black_color_v1()
        self.soft_assert(self.assertTrue, home_page.report(2, "Filter results' count is 2",
                                                           home_page.result_item,
                                                           home_page.get_filter_results_count() == 2))
        self.assert_all()

    def test_product_details(self):
        product_description = "These boots are comfortable enough to wear all day. Well made. I love the “look”. " \
                              "Best Used For Casual Everyday Walk fearlessly into the cooler months in the Sorel " \
                              "Joan Of Arctic Wedge II Chelsea Boot. Boasting the iconic wedge platform that's as " \
                              "comfortable as it is stylish, this boot features a waterproof upper"

        home_page = HomePage(self._browser)
        home_page.go_home_v1()
        home_page.filter_shoes_by_black_color_v1()
        details_page = home_page.click_result_item(1)
        self.soft_assert(self.assertTrue, home_page.report(3, "Product name is correct",
                                                           details_page.product_name,
                                                           details_page.get_product_name() == "Appli Air x Night"))
        self.soft_assert(self.assertTrue, home_page.report(3, "Product old price is correct",
                                                           details_page.product_old_price,
                                                           details_page.get_product_old_price() == "$48.00"))
        self.soft_assert(self.assertTrue, home_page.report(3, "Product new price is correct",
                                                           details_page.product_new_price,
                                                           details_page.get_product_new_price() == "$33.00"))
        self.soft_assert(self.assertTrue, home_page.report(3, "Product discount is correct",
                                                           details_page.product_discount,
                                                           details_page.get_product_discount() == "-30% discount"))
        self.soft_assert(self.assertTrue, home_page.report(3, "Product description is correct",
                                                           details_page.product_description,
                                                           product_description in details_page.get_product_description()))
        self.assert_all()
