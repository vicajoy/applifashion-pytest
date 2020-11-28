from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class ProductDetailsPage(BasePage):

    product_name = "shoe_name"
    product_new_price = "new_price"
    product_old_price = "old_price"
    product_description = "P____83"
    product_discount = "discount"

    def __init__(self, driver):
        super().__init__(driver)

    def get_product_name(self):
        return self.get_text((By.ID, self.product_name))

    def get_product_old_price(self):
        return self.get_text((By.ID, self.product_old_price))

    def get_product_new_price(self):
        return self.get_text((By.ID, self.product_new_price))

    def get_product_discount(self):
        return self.get_text((By.ID, self.product_discount))

    def get_product_description(self):
        return self.get_text((By.ID, self.product_description))
