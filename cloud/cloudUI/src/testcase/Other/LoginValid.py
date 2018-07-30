# -*- coding: utf-8 -*-

from src.page import Login
from src.page import Navigator
from src.page import Profile
import time

def TestCase001__Login_logout_NormalInputTest():
    Login.LoginAction.LoginWith('jazz.user1', '123456Qq')
    time.sleep(2)

    Navigator.CutomerSelecter().Click_Customer('jazz.customer1')
    time.sleep(5)

    Navigator.GroupProjectSelecter().Click('jazz.customer1')
    time.sleep(5)

    #Verify Logout
    Profile.ProfileButton.Click()
    time.sleep(1)
    Profile.LogoutButton.Click()
    time.sleep(1)
    Profile.LogoutConfirmButton.Click()
    time.sleep(5)
    Login.LoginButton.VerifyExistence(True)


def TestCase002__Login_DemoUser():
    Login.LoginAction.LoginWith('DemoUser', '123456Qq')
    time.sleep(5)

    # Navigator.CutomerSelecter().Click_Customer('jazz.customer1')
    # time.sleep(5)

    #Verify Logout
    Profile.ProfileButton.Click()
    time.sleep(1)
    Profile.LogoutButton.Click()
    time.sleep(1)
    Profile.LogoutConfirmButton.Click()
    time.sleep(5)
    Login.LoginButton.VerifyExistence(True)

def TestCase003__Login_DanXiangMu():
    Login.LoginAction.LoginWith(u'单客户单项目经理', '123456Qq')
    time.sleep(2)

    #Verify Logout
    Login.ErrorMessage.VerifyExistence(False)
    time.sleep(1)
    Profile.ProfileButton.Click()
    time.sleep(1)
    Profile.LogoutButton.Click()
    time.sleep(1)
    Profile.LogoutConfirmButton.Click()
    time.sleep(5)
    Login.LoginButton.VerifyExistence(True)

def TestCase004__Login_ShangWuRenYuan():
    Login.LoginAction.LoginWith(u'单客户商务人员', '123456Qq')
    time.sleep(2)

    Login.ErrorMessage.VerifyExistence(False)
    time.sleep(1)
    #Verify Logout
    Profile.ProfileButton.Click()
    time.sleep(1)
    Profile.LogoutButton.Click()
    time.sleep(1)
    Profile.LogoutConfirmButton.Click()
    time.sleep(5)
    Login.LoginButton.VerifyExistence(True)

def TestCase005__Login_GongChengRenYuan():
    Login.LoginAction.LoginWith(u'单客户工程人员', '123456Qq')
    time.sleep(2)

    Login.ErrorMessage.VerifyExistence(False)
    time.sleep(1)
    #Verify Logout
    Profile.ProfileButton.Click()
    time.sleep(1)
    Profile.LogoutButton.Click()
    time.sleep(1)
    Profile.LogoutConfirmButton.Click()
    time.sleep(5)
    Login.LoginButton.VerifyExistence(True)

def TestCase006__Login_ZiXunGuWen():
    Login.LoginAction.LoginWith(u'单客户咨询顾问', '123456Qq')
    time.sleep(2)

    Login.ErrorMessage.VerifyExistence(False)
    time.sleep(1)
    #Verify Logout
    Profile.ProfileButton.Click()
    time.sleep(1)
    Profile.LogoutButton.Click()
    time.sleep(1)
    Profile.LogoutConfirmButton.Click()
    time.sleep(5)
    Login.LoginButton.VerifyExistence(True)

def TestCase007__Login_KeHuGuanLiYuan():
    Login.LoginAction.LoginWith(u'单客户客户管理员', '123456Qq')
    time.sleep(2)

    Login.ErrorMessage.VerifyExistence(False)
    time.sleep(1)
    #Verify Logout
    Profile.ProfileButton.Click()
    time.sleep(1)
    Profile.LogoutButton.Click()
    time.sleep(1)
    Profile.LogoutConfirmButton.Click()
    time.sleep(5)
    Login.LoginButton.VerifyExistence(True)

def TestCase008__Login_ZiXunRenYuan():
    Login.LoginAction.LoginWith(u'单客户咨询人员', '123456Qq')
    time.sleep(2)

    Login.ErrorMessage.VerifyExistence(False)
    time.sleep(1)
    #Verify Logout
    Profile.ProfileButton.Click()
    time.sleep(1)
    Profile.LogoutButton.Click()
    time.sleep(1)
    Profile.LogoutConfirmButton.Click()
    time.sleep(5)
    Login.LoginButton.VerifyExistence(True)










