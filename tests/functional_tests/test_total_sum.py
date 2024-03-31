import time

from base_class import BaseClass
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestOne(BaseClass):

    def test_total_sum_for_cart(self, setup):
        log = self.getLogger()
        log.info("open start window")

        animal = "Кошки"
        self.driver.find_element(By.LINK_TEXT, animal).click()

        product_category = "Лежанки и домики"
        self.driver.find_element(By.LINK_TEXT, product_category).click()

        id_product = "bx_3966226736_235370"
        log.info(f"selection of a specific product with id {id_product}")
        self.driver.find_element(By.ID, id_product).click()

        price = self.driver.find_element(By.CLASS_NAME, "price_value").text
        price = self.get_price(price=price)

        self.driver.find_element(By.ID, self.increase_quanitity_btn_xpath).click()
        self.driver.find_element(By.ID, "bx_117848907_235370_basket_actions").click()

        button_cart = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "В корзине"))
        )
        button_cart.click()
        log.info("entrance to cart")
        time.sleep(5)

        quantity = int(
            self.driver.find_element(By.XPATH, "//tbody//input").get_attribute("value")
        )

        total_sum = self.driver.find_element(
            By.XPATH, "//td[@class='basket-items-list-item-price']/div/div/span"
        ).text
        total_sum = self.get_total_sum(total_sum=total_sum)

        assert price * quantity == total_sum
