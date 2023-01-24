import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def pytest_addoption(parser):
    parser.addoption('--name_browser', action='store', default='chrome',\
                     help='Choose browser: chrome or firefox')

    parser.addoption('--language', action='store', default='ru',\
                     help='Choose language: ru, en, es, fr')



@pytest.fixture(scope='function')
def browser(request):
    name_browser = request.config.getoption('name_browser')
    browser_language = request.config.getoption('language')

    # for Chrome
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})

    # for Mozilla
    fp = webdriver.FirefoxProfile()
    fp.set_preference('intl.accept_languages', browser_language)

    if name_browser == 'chrome':
        browser = webdriver.Chrome(options=options)
    elif name_browser == 'firefox':
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError('--please set acceptable browser: chrome or firefox')
    yield browser
    browser.quit()

