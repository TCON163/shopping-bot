from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# This open a window
driver = webdriver.Chrome("C:/Users/Tyler/PycharmProjects/pythonProject/chromedriver.exe")





driver.get("https://www.footlocker.com/product/new-balance-vision-racer-mens/MSVRCJS1.html")

sleep(3)

agree_button = driver.find_element_by_id("touAgreeBtn").click()

sleep(4)


closer = driver.find_element_by_class_name("closeButtonWhite")
closer.click()


sleep(8)
pick_size = driver.find_element_by_xpath("//div[input/@id='ProductDetails_radio_size_095']")

pick_size.click()
sleep(5)
check_out = driver.find_element_by_class_name('ProductDetails-form__action')

check_out.click()
sleep(8)
view_cart = driver.find_element_by_class_name('c-cart-added__cta')

view_cart.click()