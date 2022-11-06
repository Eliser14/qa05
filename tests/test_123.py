from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_example():
    o = webdriver.ChromeOptions()
    o.headless = True

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=0
    )

    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    title = driver.title
    assert title == "Web form"

    driver.quit()
