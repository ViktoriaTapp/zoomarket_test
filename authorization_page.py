from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from pathlib import Path

BASE_DIR = Path(__file__).parent

WEBDRIVER_PATH = BASE_DIR / "chromedriver/chromedriver"

URL = "https://zoomarket.kz/auth/registration/?register=yes&backurl=%2Fauth%2F"


class AuthorizationPage():

    def __init__(self, WEBDRIVER_PATH: str, URL: str):
        self._url = URL
        service = Service(executable_path=WEBDRIVER_PATH)
        self._driver = webdriver.Chrome(service=service)
        self._driver.get(self._url)

    def input_name(self, name):
        user_name = self._driver.find_element(By.ID, "input_NAME")
        user_name.send_keys(name)
        user_name.send_keys(Keys.ENTER)

    def get_username_error_message(self, name):
        self.input_name(name=name)
        time.sleep(3)
        user_name_error_message = self._driver.find_element(By.ID, "input_NAME-error").text
        self._driver.find_element(By.ID, "input_NAME").clear()
        return user_name_error_message

    def input_email(self, email):
        user_email = self._driver.find_element(By.ID, "input_EMAIL")
        user_email.send_keys(email)
        user_email.send_keys(Keys.ENTER)

    def get_email_error_message(self, email):
        self.input_email(email=email)
        time.sleep(5)
        email_error_message = self._driver.find_element(By.ID, "input_EMAIL-error").text
        self._driver.find_element(By.ID, "input_EMAIL").clear()
        return email_error_message


    def input_phone_number(self, phone_number):
        phone = self._driver.find_element(By.ID, "input_PERSONAL_PHONE")
        phone.send_keys(phone_number)
        phone.send_keys(Keys.ENTER)

    def get_phone_number_error_message(self,phone_number):
        self.input_phone_number(phone_number=phone_number)
        time.sleep(3)
        error_number_phone = self._driver.find_element(By.ID, "input_PERSONAL_PHONE-error").text
        self._driver.find_element(By.ID, "input_PERSONAL_PHONE").clear()
        return error_number_phone

    def input_password(self, password):
        user_password = self._driver.find_element(By.ID, "input_PASSWORD")
        user_password.send_keys(password)
        user_password.send_keys(Keys.ENTER)

    def get_password_error_message(self, password):
        self.input_password(password=password)
        time.sleep(3)
        error_password_message = self._driver.find_element(By.ID, "input_PASSWORD-error").text
        self._driver.find_element(By.ID, "input_PASSWORD").clear()
        return error_password_message

    def input_repeat_password(self, repeat_password):
        repeat_password_el = self._driver.find_element(By.ID, "input_CONFIRM_PASSWORD")
        repeat_password_el.send_keys(repeat_password)
        repeat_password_el.send_keys(Keys.ENTER)

    def get_repeat_password_error_message(self, repeat_password):
        self.input_repeat_password(repeat_password=repeat_password)
        time.sleep(3)
        error_repeat_password_message = self._driver.find_element(By.ID, "input_CONFIRM_PASSWORD-error").text
        self._driver.find_element(By.ID, "input_CONFIRM_PASSWORD").clear()
        return error_repeat_password_message

    def driver_quit(self):
        self._driver.quit()

AUTH_PAGE = AuthorizationPage(WEBDRIVER_PATH=WEBDRIVER_PATH, URL=URL)
#AuthorizationPage(WEBDRIVER_PATH=WEBDRIVER_PATH, URL=URL).driver_quit()
