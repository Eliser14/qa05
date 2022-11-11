from selenium.common import NoSuchElementException


class BasePage:
    def __init__(self, driver, link):
        self.driver = driver
        self.link = link

    def open_page(self):
        self.driver.get(self.link)

    def element_is_NOT_present(self, method, locator):
        try:
            self.driver.find_element(method, locator)
        except NoSuchElementException:
            return True
        return False


#     public boolean
#     isElementPresent(By by) {
#     try {driver.findElement(by);
#         return true;}
#     catch(NoSuchElementException e)
#     return false;
#
#
# public boolean
# elementIsNotPresent(String xpath)
# {return driver.findElements(By.xpath(xpath)).isEmpty();}
