# -*- coding: utf-8 -*-

from knitter.webelement import WebElement
from selenium.webdriver.common.by import By
from knitter import log

class ProfileButton(WebElement):
    (by, value) = (By.XPATH, "//div[@class='pop-mainmenu-user']/button/div")

class LogoutButton(WebElement):
    (by, value) = (By.CLASS_NAME, 'pop-userprofile-logout')

class LogoutConfirmButton(WebElement):
    (by, value) = (By.XPATH, "//div[@class='dialog-actions']/button")

class ProfileSideBarInfo():
    class ModifyPasswordButton(WebElement):
        (by, value) = (By.XPATH, "//span[text()='修改密码']")

    class NickNameEditButton(WebElement):
        (by, value) = (By.XPATH, "//div[@class='pop-userprofile-edit-button']/span[text()='编辑']")

    class PositionEditButton(WebElement):
        (by, value) = (By.XPATH, "//div[@class='pop-userprofile-edit-button']/span[text()='编辑']")
        index = 1

    class MobilePhoneButton(WebElement):
        (by, value) = (By.XPATH, "//div[text()='手机']/../../../div/div/span[text()='编辑']")

    class EmailEditButton(WebElement):
        (by, value) = (By.XPATH, "//div[text()='电子邮件']/../../../div/div/span[text()='编辑']")

class ChangePassowordInfo():
    class OldPassword(WebElement):
        (by, value) = (By.XPATH, "//label[text()='原始密码']/../input")

    class NewPassword(WebElement):
        (by, value) = (By.XPATH, "//label[text()='新密码']/../input")

    class NewPasswordAgain(WebElement):
        (by, value) = (By.XPATH, "//label[text()='确认新密码']/../input")

    class CompleteButton(WebElement):
        (by, value) = (By.XPATH, "//span[text()='完成']")

class ProfileInfo():
    class NickName(WebElement):
        (by, value) = (By.XPATH, "//div[@class='dialog-content']//label[text()='昵称']/../input")

    class MobilePhone(WebElement):
        (by, value) = (By.XPATH, "//div[@class='dialog-content']//label[text()='手机']/../input")

    class Email(WebElement):
        (by, value) = (By.XPATH, "//div[@class='dialog-content']//label[text()='电子邮箱']/../input")

    class PositionButton(WebElement):
        (by, value) = (By.XPATH, "//div[text()='职务']/../div[@class='pop-viewableDropDownMenu-ddm']")

    class CompleteButton(WebElement):
        (by, value) = (By.XPATH, "//span[text()='完成']")

    class PositionItem(WebElement):
        (by, value) =(By.XPATH, "//div[@style='opacity: 1;']/span[@label='#@Name']")

        def __init__(self):
            by = WebElement.by
            value = WebElement.value

        def Click(self, name):
            self.value = self.value.replace('@#Name', name)
            super(ProfileInfo.PositionItem, self).Click()

def VerifyEqual(var, act):
    log.step_normal("Verify whether value [%s] is equal to [%s]"%(var, act))

    if var == act:
        log.step_pass('Equal!')
    else:
        log.step_fail('Not equal!')