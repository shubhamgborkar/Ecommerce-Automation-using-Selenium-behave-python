from behave import *
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

@given(u'Launch the browser')
def launch(context):
    context.driver=webdriver.Firefox()
    context.driver.maximize_window()


@when(u'open the website')
def openweb(context):
    context.driver.get('https://demo.nopcommerce.com/')


@then(u'then click register')
def reg(context):
    context.driver.find_element("xpath", " //a[contains(text(),'Register')]").click()


@then(u'fill reg details')
def filldet(context):
    context.driver.find_element("xpath", "//input[@id='gender-male']").click()
    context.driver.find_element("xpath", "//input[@id='FirstName']").send_keys('Shubham')
    context.driver.find_element("xpath", "//input[@id='LastName']").send_keys('Borkar')
    day = context.driver.find_element("xpath", "//body/div[6]/div[3]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/div[4]/div[1]/select[1]")
    select = Select(day)
    select.select_by_visible_text('6')

    month = context.driver.find_element("xpath", "//body/div[6]/div[3]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/div[4]/div[1]/select[2]")
    select = Select(month)
    select.select_by_visible_text('August')

    year = context.driver.find_element("xpath", "//body/div[6]/div[3]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/div[4]/div[1]/select[3]")
    select = Select(year)
    select.select_by_visible_text('1999')

    context.driver.find_element("xpath", "//input[@id='Email']").send_keys('sgb@gmail.com')
    context.driver.find_element("xpath", "//input[@id='Company']").send_keys('sgb')
    context.driver.find_element("xpath", "//input[@id='Password']").send_keys('123456')
    context.driver.find_element("xpath", "//input[@id='ConfirmPassword']").send_keys('123456')


@then(u'click register')
def register(context):
    context.driver.find_element("xpath", "//button[@id='register-button']").click()
    time.sleep(2)
    context.driver.find_element("xpath", "//a[contains(text(),'Continue')]").click()


@then(u'close browser')
def close(context):
    context.driver.close()

#-------------------------------------------------------------------------------- login-------------------

@then(u'then click login')
def login(context):
    context.driver.find_element("xpath","//a[contains(text(),'Log in')]").click()



@then(u'fill log details')
def logdet(context):
    context.driver.find_element("xpath", "//input[@id='Email']").send_keys('sgb@gmail.com')
    context.driver.find_element("xpath", "//input[@id='Password']").send_keys('123456')


@then(u'click login')
def loginbttn(context):
    context.driver.find_element("xpath","//button[contains(text(),'Log in')]").click()
    time.sleep(3)

#---------------------------------------------------------------------------------------------------------


@then(u'click product')
def clkpd(context):
    context.driver.find_element("xpath", "//body/div[6]/div[3]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[2]/div[1]/div[1]/a[1]/img[1]").click()


@then(u'add product')
def addpro(context):
    context.driver.find_element("xpath", "//button[@id='add-to-cart-button-4']").click()


@then(u'click shopping cart')
def cart(context):
    time.sleep(5)
    context.driver.find_element("xpath", "//span[contains(text(),'Shopping cart')]").click()


@then(u'click agree')
def step_impl(context):
    context.driver.find_element("xpath", "//input[@id='termsofservice']").click()


@then(u'click checkout')
def check(context):
    context.driver.find_element("xpath", "//button[@id='checkout']").click()


@then(u'fill details')
def details(context):
    time.sleep(2)
    context.driver.find_element("name", "save").click()


@then(u'click continue')
def cont(context):
    time.sleep(2)
    context.driver.find_element("xpath", "//body/div[6]/div[3]/div[1]/div[1]/div[1]/div[2]/ol[1]/li[3]/div[2]/form[1]/div[2]/button[1]").click()
    time.sleep(2)
    context.driver.find_element("xpath", "//body/div[6]/div[3]/div[1]/div[1]/div[1]/div[2]/ol[1]/li[4]/div[2]/div[1]/button[1]").click()
    time.sleep(2)
    context.driver.find_element("xpath", "//body/div[6]/div[3]/div[1]/div[1]/div[1]/div[2]/ol[1]/li[5]/div[2]/div[1]/button[1]").click()
    time.sleep(2)
    context.driver.find_element("xpath", "//button[contains(text(),'Confirm')]").click()
    time.sleep(3)


