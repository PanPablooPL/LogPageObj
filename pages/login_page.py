from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input_id = "username"
        self.password_input_id = "password"
        self.login_button_name = "login"

    def enter_username(self, username):
        username_input = WebDriverWait(self.driver, 50).until(
            EC.presence_of_element_located((By.ID, self.username_input_id))
        )
        username_input.send_keys(username)

    def enter_password(self, password):
        password_input = WebDriverWait(self.driver, 50).until(
            EC.presence_of_element_located((By.ID, self.password_input_id))
        )
        password_input.send_keys(password)

    def click_login(self):
        login_button = WebDriverWait(self.driver, 50).until(
            EC.element_to_be_clickable((By.NAME, self.login_button_name))
        )
        login_button.click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
