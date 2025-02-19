import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: en, es, fr, etc.")

@pytest.fixture(scope="function")
def browser(request):
    # Получаем параметр language из командной строки
    user_language = request.config.getoption("language")
    
    # Настраиваем опции браузера
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    
    # Запускаем браузер с нужными опциями
    browser = webdriver.Chrome(options=options)
    
    yield browser
    browser.quit() 