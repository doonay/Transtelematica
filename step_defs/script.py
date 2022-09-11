from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from random import choice
import time

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
print('Запустили браузер, максимизировали')
print('----------------------------------')
time.sleep(3)

#b.	Зайти на yandex.ru
driver.get('http://www.yandex.ru/')
print('зашли в яндекс')
print('--------------')
time.sleep(2)
print(driver.window_handles)
print(driver.current_window_handle)

#c.	В разделе «Маркет» выбрать «Смартфоны».
market_element = driver.find_element('xpath', "//a[@data-id='market']")
#market_link = market_element.get_attribute('href')
print(market_element.text)
market_element.click()

print(driver.window_handles)
print(driver.current_window_handle)
driver.switch_to.window(driver.window_handles[1])
#driver.close()
print(driver.window_handles)
print(driver.current_window_handle)
print('зашли в маркет')
print('----------------------------')
driver.implicitly_wait(10)

button = driver.find_element('xpath', '//button[@id="catalogPopupButton"]')
#button = driver.find_element('xpath', '//noindex[@class="q2jz_"]')
button.click()
print(button.text, 'нажата')
driver.implicitly_wait(7)

smartphones = driver.find_element('xpath', '//a[text()="Смартфоны"]')
print(smartphones.text)
smartphones.click()
print(smartphones.text, 'нажата')
driver.implicitly_wait(5)

#d.	Перейти в «Все фильтры».
all_filters_button = driver.find_element('xpath', '//a[@data-auto="allFiltersButton"]')
all_filters_button.click()
print(all_filters_button.text, 'нажата')


#driver.findElement(By.Xpath("//*[contains(@class,'class1 class2')]"));
#driver.findElement(By.cssSelector(".class1.class2"));
driver.implicitly_wait(3)

#e.	Задать параметр поиска до 20000 рублей
#driver.find_element('class', '_2xtC2').send_keys('20000')
#driver.find_element('xpath', "//*[@class='_2xtC2']").send_keys('20000')
#'_3i0uk'
#driver.findElement(By.Xpath("//*[contains(@class,'class1 class2')]"));
#driver.findElement(By.cssSelector(".class1.class2"));

element1 = driver.find_element('xpath', "//*[@data-filter-id='glprice']")
name1 = element1.find_element('xpath', "//*[@class='_8zv18']").text
print(name1)
print(element1.get_attribute('placeholder'))

element2 = driver.find_element('xpath', "//*[@data-filter-id='14805766']")
name2 = element2.find_element('xpath', "//*[@class='_8zv18']").text
print(name2)
print(element2.get_attribute('placeholder'))

element1.send_keys('20000')
print('---20000---')
#driver.findElement(By.Xpath("//*[contains(@class,'class1 class2')]"));
#driver.findElement(By.cssSelector(".class1.class2"));

'''
#попробовать без клика
#driver.find_element('xpath', "//*[@class='_1RgR0']").click()
driver.find_element('xpath', "//*[@class='_1RgR0 _2k6P8']").click()


#и Диагональ экрана от 3 дюймов.
driver.find_element('xpath', '/html/body/div[4]/section/div[2]/div/div/div[2]/div[1]/div[12]/div/div/div/div[1]/input').send_keys('3')
print('---3---')

#print('---click---')
#верхний класс 'yXKAc _1H_kO'
#driver.find_element('xpath', "//*[@class='_2xtC2']").send_keys('20000')

#класс кнопки '_2qvOO _3qN-v _1Rc6L'
#final_button_link = 
time.sleep(2)

final_link = driver.find_element('xpath', "//*[@class='_2qvOO _3qN-v _1Rc6L']").get_attribute('href')
print('---final click---')

driver.get(final_link)


driver.find_element('type', 'text').send_keys('20000')

driver.find_element('xpath', '/html/body/div[4]/section/div[2]/div/div/div[2]/div[1]/div[13]/div/div/div/div[2]/input').send_keys('3')

#кликаем на кнопку
show_button = driver.find_element('xpath', '/html/body/div[4]/section/div[2]/div/div/div[3]/div/div/a[2]').click()

#либо переходим по ссылке, тут не важно
#show_button_link = driver.find_element('xpath', '/html/body/div[4]/section/div[2]/div/div/div[3]/div/div/a[2]').get_attribute('href')
#print(show_button_link)
#driver.get(show_button_link)



#f.	Выбрать не менее 5 любых производителей.
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