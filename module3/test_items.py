from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
def test_add_to_bin_button(browser):
    browser.get(link)
    button = browser.find_element(By.XPATH, '//*[@id="add_to_basket_form"]/button')
    assert button is not None, 'Кнопка нет!'
    