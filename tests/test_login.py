from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage


def test_login():

    chrome_options = Options()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)

    driver.get("http://seleniumdemo.com/?page_id=7")

    assert "seleniumdemo.com/?page_id=7" in driver.current_url

    login_page = LoginPage(driver)

    login_page.login("user@seleniumacademy.com", "tester")


    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".woocommerce-MyAccount-navigation"))
        )
        print("Logowanie udane")
    except:
        print("Logowanie nieudane")

    driver.quit()


if __name__ == "__main__":
    test_login()
