import os

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.core.utils import ChromeType
from pathlib import Path  ##################
import logging  ##################

# @pytest.fixture(scope="function")
# def driver():
#     o = webdriver.ChromeOptions()
#     o.headless = False
#     driver = webdriver.Chrome(
#         service=ChromeService(ChromeDriverManager().install()), options=o
#     )
#     yield driver
#     driver.quit()

#####################################################################
drv = None  ##################
directory = "report/screens/"  ##################


@pytest.fixture(scope="function")
def driver(browser, headless):
    global drv  ##################
    Path(directory).mkdir(parents=True, exist_ok=True)
    if browser == "firefox":
        o = webdriver.FirefoxOptions()
        o.headless = headless
        drv = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()), options=o
        )
    else:
        o = webdriver.ChromeOptions()
        o.headless = headless
        drv = webdriver.Chrome(
            service=ChromeService(
                ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
            ),
            options=o,
        )
    return drv


# ------- 2 функции определяют параметр, котрый принимает pytest (browser)
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="chrome",
        help="define browser: chrome or firefox, --firefox",
    )
    parser.addoption(
        "--headless", action="store_true", help="headless mode on or off. --headless"
    )


@pytest.fixture(scope="function")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="function")
def headless(request):
    return request.config.getoption("--headless")


######################################################################
@pytest.fixture(scope="function", autouse=True)
def setup(driver):
    logging.info("***** start fixture = setup *****")
    driver.get("https://www.saucedemo.com/")
    yield driver
    logging.info("***** end fixture = teardown *****")
    driver.quit()


# Credentials = namedtuple('Credentials', 'username password')
#
# credentials = [
#         Credentials("standard_user", "secret_sauce"),
#         Credentials("problem_user", "secret_sauce"),
#         Credentials("performance_glitch_user", "secret_sauce"),
#         # Credentials(pytest.param("locked_out_user", "secret_sauce", marks=pytest.mark.xfail)),
#     ]
# @pytest.fixture(params=credentials, scope="class")
# def login_password(request):
#     return request.param

# -----------------------------------------------
# --------- Параметризованные фикстуры ----------
# -----------------------------------------------

# Person = namedtuple("Person", "name age")
#
# persons = [Person("John", 1982),
#             Person("Mike", 1998)]
#
# # данная функция показывает идентификаторы:
# # test_names[Person (John, 1982)]
# # test_names[Person (Mike, 1998)]
# # Без данной функции результат будет в виде: test_names[person0] PASSED
# def id_func(test_data):
#     return [f'Person ({p.name}, {p.age})' for p in test_data]
#
# @pytest.fixture(params=persons, ids=id_func(persons))
# def person(request):
#     return request.param
#
# # @pytest.mark.parametrize("a", [1, 2])
# def test_names(person):
#     assert isinstance(person.name, str)
#     assert isinstance(person.age, int)


# @pytest.fixture(params=["chrome", "firefox", "safari"])
# def DRIVER(request):
#     browser_list = request.config.getoption("--browser")
#     driver_map = {
#         "chrome": webdriver.Chrome,
#         "firefox": webdriver.Firefox,
#         "safari": webdriver.Safari,
#     }
#     if request.param in browser_list:
#         driver = driver_map[request.param]()
#         return driver
#     else:
#         pytest.skip("Not running tests for browser: {}".format(request.param))


# -------------------------------------------
# -------- Add screenshots to report --------
# -------------------------------------------
def pytest_html_report_title(report):
    report.title = "Saucedemo_Lets_do_it"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call":  # or report.when == "setup":
        # always add url to report
        extra.append(pytest_html.extras.url(drv.current_url))
        # extra.append(pytest_html.extras.url("https://www.saucedemo.com/"))
        xfail = hasattr(report, "wasxfail")

        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            file_name_ = "." + directory + file_name
            file_name_html = "screens/" + file_name
            drv.get_screenshot_as_file(file_name_)

            if file_name_:
                html = f"<div><img src='{file_name_html}' alt='screenshot'"
                html += "onclick='window.open(this.src)' style='width:400px;'"
                html += " align='right'/></div>"
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


#
#
# @pytest.fixture(scope='session', autouse=True)
# def browser_s():
#     global driver
#     if driver is None:
#         # driver = webdriver.Firefox()
#         driver = webdriver.Chrome()
#     return driver
# @pytest.fixture(scope="class", autouse=True)
# def g(driver):
#     print("\n***** start fixture = setup *****\n")
#     driver.get("https://www.saucedemo.com/")
#     yield driver
#     driver.quit()
#     print("\n***** end fixture = teardown *****\n")


## --------------------------------------------------------------------индус

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item):
#     pytest_html = item.config.pluginmanager.getplugin("html")
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, "extra", [])
#
#     if report.when == "call":
#         extra.append(pytest_html.extras.url("some string", name="BLABLA1"))
#         xfail = hasattr(report, "wasxfail")
#
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             report_directory = os.path.dirname(item.config.option.htmlpath)
#             # file_name = str(int(round(time.time()*1000))) + ".png"
#             file_name = report.nodeid.replace("::", "_") + "png"
#             destinationFile = os.path.join(report_directory, file_name)
#             d.save_screenshot(destinationFile)
#
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:300px;height:200px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
#             extra.append(pytest_html.extras.html(html))
#         report.extra = extra

# --------------------------------------------------------------------ОРИГИНАЛ
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item):
#     pytest_html = item.config.pluginmanager.getplugin("html")
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, "extra", [])
#
#     if report.when == "call":
#         extra.append(pytest_html.extras.url("some string", name="BLABLA1"))
#         xfail = hasattr(report, "wasxfail")
#
#         if (report.skipped and xfail) or (report.failed and not xfail):
#
#             # only add additional html on failure
#             extra.append(pytest_html.extras.html("<div>Additional HTML</div>"))
#         report.extra = extra
#
