# -*- coding: utf-8 -*-


from knitter.webelement import WebElement
from selenium.webdriver.common.by import By
import time


class LoginPop:
    class UserName(WebElement):
        (by, value) = (By.XPATH, "//div[@class='jazz-login-dialog-input-container']/input")
    
    class Password(WebElement):
        (by, value) = (By.XPATH, "//div[@class='jazz-login-dialog-input-container']/input")
        index = 1

class LoginButton(WebElement):
    (by, value) = (By.CLASS_NAME, 'login-button')

class SubmitButton(WebElement):
    (by, value) = (By.XPATH, "//span[text()='登录']")

class CustomerSelectorLabel(WebElement):
    (by, value) = (By.XPATH, "//span[text()='请选择客户']")

class RightArrowButton(WebElement):
    (by, value) = (By.CLASS_NAME, 'icon-arrow-right')

class ErrorMessage(WebElement):
    (by, value) = (By.XPATH, "//span[text()='抱歉，发生未知错误。']")

class LoginAction():
    @classmethod
    def LoginWith(cls, name, password):
        LoginButton.WaitForAppearing()
        LoginButton.Click()
        time.sleep(2)
        LoginPop.UserName.Click()
        LoginPop.UserName.TypeIn(name)
        LoginPop.Password.Click()
        LoginPop.Password.TypeIn(password)

        SubmitButton.Click()
        #CustomerSelectorLabel.WaitForAppearing()
        time.sleep(3)












