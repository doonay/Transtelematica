from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from random import choice
import time
import logging.config

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'default_formatter': {
            'format': '[%(levelname)s:%(asctime)s] %(message)s'
        },
    },

    'handlers': {
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default_formatter',
        },
    },

    'loggers': {
        'logger': {
            'handlers': ['stream_handler'],
            'level': 'DEBUG',
            'propagate': True
        }
    }
}

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)
logger.debug('init debug log')

desktop_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
                  'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0']

chrome_options = Options()

ua = choice(desktop_agents)
print(ua)
chrome_options.add_argument('user-agent=' + ua)

s = Service('C:/Transtelematica/chromedriver/chromedriver.exe')

#a.	Открыть браузер и развернуть на весь экран.
driver = webdriver.Chrome(service=s, options=chrome_options)
#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
time.sleep(3)
logger.debug('Запустили браузер, максимизировали')
print('Запустили браузер, максимизировали')
print('----------------------------------')

#b.	Зайти на yandex.ru
#
# ---===###!!!   13.09.22 сайт yandex.ru редиректит на яндекс дзэн   !!!###===---
#
#driver.get('http://www.yandex.ru')



'''
try:
    driver.find_element('//div[@class="modal__close"]').click()
except:
    pass
'''

#print(driver.window_handles)
#print(driver.current_window_handle)
#c.	В разделе «Маркет» выбрать «Смартфоны».


'''
while True:
    try:
        market_element = driver.find_element('xpath', "//a[@data-id='market']")
        market_element.click()
        print(market_element.text)
        logger.debug('Перешли на', market_element.text)
        print('--------------')
    except Exception as _ex:
        print(_ex)
        driver.implicitly_wait(15)
    else:
        break


driver.switch_to.window(driver.window_handles[1])

driver.implicitly_wait(10)
logger.debug('переключились на вкладку с маркетом')
print('переключились на вкладку с маркетом')
print('--------------')
driver.implicitly_wait(10)
'''
#Стартуем сразу с яндекс маркета
driver.get('https://market.yandex.ru')
logger.debug('Открыли yandex.market.ru')
print('Открыли yandex.market.ru')
print('--------------')

time.sleep(10)

while True: #при капче капчуем пока руками
    try:
        catalog = driver.find_element('xpath', '//div[@data-tid="f5f0a469"]')
        print(catalog)
        #catalog = driver.find_element('xpath', '//button[text()="Каталог"]')
        '''
        div = driver.find_element('xpath', '//div[@data-tid="f5f0a469"]')
        button = div.find_element('xpath', 'button[@id="catalogPopupButton"]')
        button.click()
        '''
        driver.implicitly_wait(10)
        catalog.click()
        break
    except Exception as _ex:
        print(_ex)
        driver.implicitly_wait(10)
print('Каталог')
logger.debug('Каталог')
print('--------------')

driver.implicitly_wait(10)

while True: #при капче капчуем пока руками
    try:
        smartphones = driver.find_element('xpath', '//a[text()="Смартфоны"]')
        driver.implicitly_wait(10)
        smartphones.click()
        break
    except Exception as _ex:
        print(_ex)
        driver.implicitly_wait(10)
print('Смартфоны')
logger.debug('Смартфоны')
print('--------------')

#d.	Перейти в «Все фильтры».

while True: #при капче капчуем пока руками
    try:
        all_filters_button = driver.find_element('xpath', '//a[@data-auto="allFiltersButton"]')
        driver.implicitly_wait(10)
        all_filters_button.click()
        break
    except Exception as _ex:
        print(_ex)
        driver.implicitly_wait(10)
print('все фильтры')
logger.debug('все фильтры')
print('--------------')

#e.	Задать параметр поиска до 20000 рублей


driver.implicitly_wait(15)

input_divs_glprice = driver.find_elements('xpath', '//div[@data-filter-id="glprice"]//div[@data-tid="d3871ccf"]')
print('find input divs done')
input_glprice_ot = input_divs_glprice[0].find_element('xpath', 'input')
input_glprice_do = input_divs_glprice[1].find_element('xpath', 'input')
print('find do done')

print(input_glprice_do.get_attribute('placeholder'))
input_glprice_do.send_keys('20000')
print('выставили 20000')
print(input_glprice_do.get_attribute('placeholder'))
print(input_glprice_do.get_attribute('value'))
driver.implicitly_wait(10)

print('---')
input_divs_14805766 = driver.find_elements('xpath', '//div[@data-filter-id="14805766"]//div[@data-tid="d3871ccf"]')
print('find input divs done')
print('find ot done')



#e. и Диагональ экрана от 3 дюймов.

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.implicitly_wait(2)
butt = driver.find_element('xpath', '//div[@data-filter-id="14805766"]//button')
butt.click()

input_14805766_ot = driver.find_element('xpath', '//*[@data-filter-id="14805766"]//input[1]')
input_14805766_ot.send_keys('3')
print(input_14805766_ot.get_attribute('placeholder'))
print(input_14805766_ot.get_attribute('value'))
print('выставили 3')


driver.implicitly_wait(15)


print('Добрались до кнопки')
final_button = driver.find_element('xpath', '//a[@class="_2qvOO _3qN-v _1Rc6L"]')
print('set final button done')
driver.implicitly_wait(5)
final_button.click()
print('push button done')
driver.implicitly_wait(15)


#f.	Выбрать не менее 5 любых производителей.

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.implicitly_wait(10)
print('скрольнулись вниз')
all_companies = driver.find_element('xpath', '//span[text()="Показать всё"]/parent::*')
print('перешли к родителю', all_companies.text)
driver.implicitly_wait(10)
print(all_companies.text, 'найден') #Все производители

all_companies.click()
print('Все производители нажат')
driver.implicitly_wait(10)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
print('скрольнулись вниз')
driver.implicitly_wait(10)

five_companies = driver.find_elements('xpath', '[//div[@class="_2XVtn"]')
for company in five_companies:
    print(company)

'''
enabled = five.find_element('xpath', '//input[@aria-disabled="false"]')
enabled.click()
print(enabled.get_attribute('name'))
'''

'''
//*[title="50"]/parent::store
This XPath will only select the parent node if it is a store.
But you can also use one of these
//*[title="50"]/parent::*
//*[title="50"]/..
#g.	Нажать кнопку «Показать».
#h.	Посчитать кол-во смартфонов на одной странице.
#i.	Запомнить последний из списка.
#j.	Изменить Сортировку на другую (по цене/ по рейтингу/ по скидке).
#k.	Найти и нажать по имени запомненного объекта.
#l.	Вывести рейтинг выбранного товара.
#m.	Закрыть браузер.
time.sleep(30) # Let the user actually see something!
#search_box = driver.find_element_by_name('q')
#search_box.send_keys('ChromeDriver')
#search_box.submit()
#time.sleep(5) # Let the user actually see something!
driver.quit()
	
'''