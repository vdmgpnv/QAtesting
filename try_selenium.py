import webbrowser
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import math
import os



link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    value1 = 'input'
    value2 = 'last_name'
    value3 = 'firstname'
    value4 = 'country'

    input1 = browser.find_element_by_tag_name(value1)
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name(value2)
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name(value3)
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id(value4)
    input4.send_keys("Russia")
    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
try:
    driver = webdriver.Chrome()
    driver.get('http://suninjuly.github.io/find_link_text')
    right_link = driver.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
    right_link.click()
    value1 = 'input'
    value2 = 'last_name'
    value3 = 'firstname'
    value4 = 'country'

    input1 = driver.find_element_by_tag_name(value1)
    input1.send_keys("Ivan")
    input2 = driver.find_element_by_name(value2)
    input2.send_keys("Petrov")
    input3 = driver.find_element_by_name(value3)
    input3.send_keys("Smolensk")
    input4 = driver.find_element_by_id(value4)
    input4.send_keys("Russia")
    button = driver.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(12)
    driver.quit()
    
try:
    value = 'input'
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_tag_name(value)
    for element in elements:
        element.send_keys("Хуй")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
    

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    f_name = browser.find_element_by_xpath("//input[@placeholder = 'Input your first name']")
    f_name.send_keys('fdsg')
    l_name = browser.find_element_by_xpath("//input[@placeholder = 'Input your last name']")
    l_name.send_keys('dsaf')
    email = browser.find_element_by_xpath("//input[@placeholder = 'Input your email']")
    email.send_keys('sdafdg')
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
  
     
try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/get_attribute.html')
    x = browser.find_element_by_id('input_value').text
    y = calc(x)
    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)
    checkbox = browser.find_element_by_css_selector('[for="robotCheckbox"]')
    checkbox.click()
    radiobutton = browser.find_element_by_id('robotsRule')
    radiobutton.click()
    time.sleep(5)
    submit_button = browser.find_element_by_xpath('//button[text()="Submit"]')
    submit_button.click()    
finally:
    time.sleep(10)
    browser.quit()
    
try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/get_attribute.html')
    x = browser.find_element_by_id('treasure').get_attribute('valuex')
    y = calc(x)
    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)
    checkbox = browser.find_element_by_css_selector('#robotCheckbox')
    checkbox.click()
    radiobutton = browser.find_element_by_id('robotsRule')
    radiobutton.click()
    time.sleep(5)
    submit_button = browser.find_element_by_xpath('//button[text()="Submit"]')
    submit_button.click()    
finally:
    time.sleep(10)
    browser.quit()
    
    
try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/selects1.html')
    total = int(browser.find_element_by_id('num1').text) + int(browser.find_element_by_id('num2').text)
    print(total)
    select = Select(browser.find_element_by_id('dropdown'))
    select.select_by_value(str(total))
    submit_button = browser.find_element_by_xpath('//button[text()="Submit"]')
    submit_button.click()
finally:
    time.sleep(10)
    browser.quit()
    
try: 
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    x = int(browser.find_element_by_id('input_value').text)
    result = math.log(abs(12 * math.sin(x)))
    answer = browser.find_element_by_id('answer')
    answer.send_keys(result)
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    checkbox = browser.find_element_by_css_selector('#robotCheckbox')
    checkbox.click()
    radiobutton = browser.find_element_by_id('robotsRule')
    radiobutton.click()
    button.click()
finally:
    time.sleep(10)
    browser.quit()
    
    
try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')
    f_name = browser.find_element_by_xpath("//input[@placeholder = 'Enter first name']")
    f_name.send_keys('fdsg')
    l_name = browser.find_element_by_xpath("//input[@placeholder = 'Enter last name']")
    l_name.send_keys('dsaf')
    email = browser.find_element_by_xpath("//input[@placeholder = 'Enter email']")
    email.send_keys('sdafdg') 
    file_butt = browser.find_element_by_id('file')
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'ID.txt')           # добавляем к этому пути имя файла 
    file_butt.send_keys(file_path)
    button = browser.find_element_by_tag_name("button")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
    
    
try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/alert_accept.html') 
    button = browser.find_element_by_tag_name("button")
    button.click()
    alert = browser.switch_to.alert
    alert.accept()
    x = int(browser.find_element_by_id('input_value').text)
    result = math.log(abs(12 * math.sin(x)))
    answer = browser.find_element_by_id('answer')
    answer.send_keys(result)
    button = browser.find_element_by_tag_name("button")
    button.click()
finally:
    time.sleep(40)
    browser.quit() 

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html') 
    button = browser.find_element_by_tag_name("button")
    button.click()
    time.sleep(3)
    browser.switch_to.window(browser.window_handles[1])
    x = int(browser.find_element_by_id('input_value').text)
    result = math.log(abs(12 * math.sin(x)))
    answer = browser.find_element_by_id('answer')
    answer.send_keys(result)
    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(40)
    browser.quit() 
    
    


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '100')
    )
    button = browser.find_element(By.ID, 'book')
    button.click()
    x = int(browser.find_element_by_id('input_value').text)
    result = math.log(abs(12 * math.sin(x)))
    answer = browser.find_element_by_id('answer')
    answer.send_keys(result)
    button = browser.find_element_by_id("solve")
    button.click()
finally:
    time.sleep(40)
    browser.quit()