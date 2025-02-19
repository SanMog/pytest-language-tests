import time
from selenium.webdriver.common.by import By

def test_add_to_cart_button_exists(browser):
    # Открываем страницу товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    # Добавляем задержку для визуальной проверки
    time.sleep(3)
    
    # Проверяем наличие кнопки добавления в корзину
    add_to_cart_button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert len(add_to_cart_button) > 0, "Add to cart button not found!" 