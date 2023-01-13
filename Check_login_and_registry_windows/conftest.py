import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    # задаем предпочтительные браузеры, в которых будут запускаться тесты
    parser.addoption(
        '--name_browser', action='store', default='chrome', help='Browsers: chrome or firefox')
    # задаем язык, который будут использовать браузеры при запуске
    parser.addoption(
        '--language', action='store', default='None', help='Choose language: ru, en, es, fr')

@pytest.fixture(scope='function')
def browser(request):
    # вычитываем браузер, который указал пользователь в командной строке
    name_browser = request.config.getoption('name_browser')
    # вычитывем язык, который указал пользователь в командной строке
    browser_language = request.config.getoption('language')

    # for Chrome
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})

    # for Firefox
    fp = webdriver.FirefoxProfile()
    fp.set_preference('intl.accept_languages', browser_language)

    if name_browser == 'chrome':
        print('\nstart Chrome browser for test..')
        browser = webdriver.Chrome(options=options)
    elif name_browser == 'firefox':
        print('\nstart Firefox browser for test..')
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')
    yield browser
    print('\nquit browser..')
    browser.quit()