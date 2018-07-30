# -*- coding: utf-8 -*-

from knitter.webelement import WebElement
from knitter import executer, env
from selenium.webdriver.common.by import By
import Hierarchy, Login, time, Profile

def Quit_Browser():
    executer.quit_browser(env.threadlocal.BROWSER)

def Logout():
    Profile.ProfileButton.Click()
    time.sleep(1)
    Profile.LogoutButton.Click()
    time.sleep(1)
    Profile.LogoutConfirmButton.Click()
    time.sleep(5)
    Login.LoginPop.UserName.VerifyExistence(True)

def NavigateToPlatform(username, password):
    Login.LoginAction.LoginWith(username, password)

    PlatformAdminButton.Click()
    time.sleep(10)

def NavigateToUserAdmin(username, password):
    Login.LoginAction.LoginWith(username, password)

    PlatformAdminButton.Click()
    time.sleep(10)

    UserAdmin.Click()
    time.sleep(1)
    UserAdminButton.Click()
    time.sleep(5)

def NavigateToFunctionRole(username, password):
    Login.LoginAction.LoginWith(username, password)

    PlatformAdminButton.Click()
    time.sleep(3)

    UserAdmin.Click()
    time.sleep(1)
    FunctionPermissionButton.Click()
    time.sleep(5)

def NavigateToCustomer(name, password, customer):
    Login.LoginAction.LoginWith(name, password)

    CutomerSelecter().Click_Customer(customer)
    time.sleep(3)


class PlatformAdminButton(WebElement):
    (by, value) = (By.CLASS_NAME, 'pop-select-sp-manage')

class CustomerAdminButton(WebElement):
    (by, value) = (By.LINK_TEXT, '/zh-cn/spadmin/customer/')

class UserAdmin(WebElement):
    (by, value) = (By.CLASS_NAME, 'pop-mainmenu-main-title')

class UserAdminButton(WebElement):
    (by, value) = (By.XPATH, "//body/div[2]/div/div/div/div/span/div/div/div[text()='用户管理']")

class FunctionPermissionButton(WebElement):
    (by, value) = (By.XPATH, "//body/div[2]/div/div/div/div/span/div/div/div[text()='功能权限角色']")

class RightArrow(WebElement):
    (by, value) = (By.XPATH, "//em[@class ='icon-arrow-right']")

class CustomerName(WebElement):
    (by, value) = (By.XPATH, "//span[@class='pop-select-customer-ct-title']")

class CutomerSelecter(WebElement):
    (by, value) = (By.XPATH, "//span[@class = 'pop-select-customer-ct-title' and text() = '#@Name']")

    def __init__(self):
        by = WebElement.by
        value = WebElement.value

    def Click_Customer(self, name):
        self.value = self.value.replace('#@Name', name)
        super(CutomerSelecter, self).Click()
        Hierarchy.CustomerCodeLabel.WaitForAppearing()

    def VerifyExistence(self, name):
        self.value = self.value.replace('#@Name', name)
        super(CutomerSelecter, self).VerifyExistence(True)



class MyAsset(WebElement):
    (by, value) = (By.XPATH, "//a[text() = '我的资产']")

class Alarm(WebElement):
    (by, value) = (By.XPATH, "//a[text() = '故障报警']")

class Maintanence(WebElement):
    (by, value) = (By.XPATH, "//a[text() = '维护计划']")

class Ticket(WebElement):
    (by, value) = (By.XPATH, "//a[text() = '工单管理']")

class File(WebElement):
    (by, value) = (By.XPATH, "//a[text() = '文档管理']")

class GateWay(WebElement):
    (by, value) = (By.XPATH, "//a[text() = '网关管理']")

class ReportManagement(WebElement):
    (by, value) = (By.XPATH, "//a[text() = '报告管理']")
