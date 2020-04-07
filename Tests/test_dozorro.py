from selenium import webdriver
import time
import pytest
import read_email_content as API
import user_credentials as user
driver = None
user_email = user.user_email_method()
user_pass = user.user_pass_method()

def test_setup():
    global driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    # driver = webdriver.Chrome(chrome_options=chrome_options)
    driver = webdriver.Chrome("drivers\\chromedriver.exe",chrome_options=chrome_options)
    driver.set_page_load_timeout(10)
    driver
    driver.maximize_window()

def test_login():
    driver.get("https://dev.dozorro.work/")
    time.sleep(1)
    driver.find_element_by_xpath("//div[@id='review_form3']//a[contains(@class,'delete')]").click()
    time.sleep(1)
    driver.find_element_by_xpath("//div[contains(@class,'login_link')]//a").click()
    driver.find_element_by_xpath("//a[contains(@class,'btn btn-block btn-social btn-google')]").click()
    assert "Увійти" == driver.find_element_by_id("headingText").text

def test_google_login():
   driver.find_element_by_name("identifier").send_keys(user_email)
   driver.find_element_by_id("identifierNext").click()
   time.sleep(2)
   driver.find_element_by_name("password").send_keys(user_pass)
   driver.find_element_by_id("passwordNext").click()
   time.sleep(1)
   assert "Test Email" == driver.find_element_by_class_name("name").text


def test_check_redirects_after_google_login():
     driver.find_element_by_class_name("dropdown-toggle").click()
     assert "true" == driver.find_element_by_class_name("dropdown-toggle").get_attribute("aria-expanded")
     driver.find_element_by_link_text("Сповіщення").click()
     time.sleep(2)
     assert "https://dev.dozorro.work/user/settings" == driver.current_url

def test_subscribe():
     driver.get("https://dev.dozorro.work/user/settings")
     assert "Активувати" == driver.find_element_by_xpath("//tr[1]//td[3]").text
     driver.find_element_by_xpath("//tr[1]//td[3]").click()
     assert "Перевірте пошту" == driver.find_element_by_xpath("//tr[1]//td[3]").text

def test_callGMAILapi():
    time.sleep(10)
    m = API.getMsgValue()
    strList = m.split(" ")
    driver.get(strList[11])
    time.sleep(2)


def test_down():
    time.sleep(1)
    driver.close()
    driver.quit()