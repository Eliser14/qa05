from selenium.common import NoSuchElementException


class BasePage:
    def __init__(self, d, link):
        self.d = d
        self.link = link

    def open_page(self):
        self.d.get(self.link)

    def element_is_NOT_present(self, method, locator):
        try:
            self.d.find_element(method, locator)
        except NoSuchElementException:
            return True
        return False
