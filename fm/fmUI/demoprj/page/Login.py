# -*- coding: utf-8 -*-


from knitter.webelement import WebElement
from selenium.webdriver.common.by import By
import time

class LoginPop:
    class UserName(WebElement):
        (by, value) = (By.CLASS_NAME, 'username')
    
    class Password(WebElement):
        (by, value) = (By.CLASS_NAME, 'password')

    class label(WebElement):
        (by, value) = (By.XPATH, "//div[text()='用户名密码登录']")

class DemoUse(WebElement):
    (by, value) = (By.XPATH, "//span[text()='产品试用']")

class SubmitButton(WebElement):
    #(by, value) = (By.XPATH, '//div[@class="pop-login-form init"]//div[@class="pop-login-form-content-button"]')
    (by, value) = (By.XPATH, "//span[text()='登录']")
    index = 1

class CustomerSelectorLabel(WebElement):
    (by, value) = (By.XPATH, "//span[text()='请选择客户']")

class RightArrowButton(WebElement):
    (by, value) = (By.CLASS_NAME, 'icon-arrow-right')


class LoginAction():
    @classmethod
    def LoginWith(cls, name, password):
        SubmitButton.WaitForAppearing()
        LoginPop.UserName.Click()
        LoginPop.UserName.TypeIn(name)
        LoginPop.Password.Click()
        LoginPop.Password.TypeIn(password)

        SubmitButton.Click()
        CustomerSelectorLabel.WaitForAppearing()
        time.sleep(1)

    @classmethod
    def LoginWithIE(cls, name, password):
        SubmitButton.WaitForAppearing()
        LoginPop.UserName.Click()
        LoginPop.UserName.TypeIn(name, False)
        LoginPop.Password.Click()
        LoginPop.Password.TypeIn(password, False)
        time.sleep(2)

        LoginPop.label.Click()
        time.sleep(0.5)
        LoginPop.label.Click()

        SubmitButton.Click()
        CustomerSelectorLabel.WaitForAppearing()
        time.sleep(1)












