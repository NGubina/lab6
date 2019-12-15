import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome("C:\chromedriver\chromedriver.exe")

# команда time.sleep устанавливает паузу в 3 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(3)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://portal.edu.asu.ru/")
time.sleep(3)

# Метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему. 
# Ищем поле для ввода текста
textinput = driver.find_element_by_css_selector(".search-box__input")

# Напишем текст для поиска в найденное поле
textinput.send_keys("О.В. Журенков")
time.sleep(3)

# Найдем кнопку, которая отправляет введенный текст
submit_button = driver.find_element_by_css_selector(".search-box__button")

# Скажем драйверу, что нужно нажать на кнопку. 
submit_button.click()
time.sleep(10)

# После выполнения всех действий мы не должны забыть закрыть окно браузера
driver.quit()
