# -*- coding: utf-8 -*-

from demoprj.page import Login
from demoprj.page import Navigator
from demoprj.page import Profile
import time
from demoprj.page import Hierarchy

def after_each_testcase():
    Navigator.Logout()

def after_each_module():
    Navigator.Quit_Browser()

def TestCase001__Login_logout_NormalInputTest():
    Login.LoginAction.LoginWith('ShareUserB', '123456Qq')
    time.sleep(2)
    #verify that login successful
    Navigator.PlatformAdminButton.Click()
    time.sleep(6)


def TestCase002__ChangePassword():
    Login.LoginAction.LoginWith('ShareUserd', '123456Qq')
    time.sleep(2)

    #verify that login successful
    Navigator.CutomerSelecter().Click_Customer('SOHO China')
    time.sleep(3)

    Profile.ProfileButton.Click()
    time.sleep(2)

    Profile.ProfileSideBarInfo.ModifyPasswordButton.Click()
    time.sleep(2)

    Profile.ChangePassowordInfo.OldPassword.TypeIn('123456Qq')
    time.sleep(1)

    Profile.ChangePassowordInfo.NewPassword.TypeIn('1')
    time.sleep(1)

    Profile.ChangePassowordInfo.NewPasswordAgain.TypeIn('1')
    time.sleep(1)

    Profile.ChangePassowordInfo.CompleteButton.Click()
    time.sleep(3)

    # Logout
    Profile.ProfileButton.Click()
    time.sleep(1)
    Profile.LogoutButton.Click()
    time.sleep(1)
    Profile.LogoutConfirmButton.Click()
    time.sleep(5)
    Login.LoginPop.UserName.VerifyExistence(True)

    # Login with new pwd
    Login.LoginAction.LoginWith('ShareUserd', '1')
    time.sleep(2)

    Navigator.CutomerSelecter().VerifyExistence('SOHO China')
    time.sleep(1)

    Navigator.CutomerSelecter().Click_Customer('SOHO China')
    time.sleep(5)


def TestCase003__EditProfile():
    Login.LoginAction.LoginWith('ShareUserC', '123456Qq')
    time.sleep(2)

    Navigator.PlatformAdminButton.Click()
    time.sleep(5)

    #Verify Change profile
    Profile.ProfileButton.Click()
    time.sleep(5)

    Profile.ProfileSideBarInfo.NickNameEditButton.Click()
    time.sleep(5)

    #Change nickname, mobilephone, mail
    Profile.ProfileInfo.NickName.TypeIn('ShareUserCTo-other')
    time.sleep(1)
    Profile.ProfileInfo.MobilePhone.TypeIn('13245443490')
    time.sleep(1)
    Profile.ProfileInfo.Email.TypeIn('15762131@qq.com')
    time.sleep(1)
    Profile.ProfileInfo.CompleteButton.Click()
    time.sleep(1)

    nickName = Profile.ProfileButton.GetText()
    Profile.VerifyEqual('ShareUserCTo-other',nickName)


def TestCase004__DemoLogin():
    Login.DemoUse.Click()
    time.sleep(15)

    Hierarchy.CustomerCodeLabel.VerifyExistence(True)






