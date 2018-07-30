# -*- coding: utf-8 -*-

from knitter import executer

from src import conf, testcase
from src.testcase.SPManagement import CustomerConsumption
from src.testcase.SPManagement import CustomerConfig
from src.testcase.SPManagement import UserConfig
from src.testcase.CustomerConfig import CreateHierarchy
from src.testcase.CustomerConfig import CreateHierarchyDemension
from src.testcase.Other import LoginValid
from src.testcase.CustomerConfig import CreateHierarchyProperty
from src.testcase.CustomerConfig import CreateVEE
from src.testcase.SPManagement import CalendarConfig

#executer.run(conf.ChromeAutoDemo, CustomerConsumption)
#executer.run(conf.ChromeAutoDemo, UserConfig)
#executer.run(conf.ChromeAutoDemo, UserConfig)
#executer.run(conf.ChromeAutoDemo, CustomerConsumption)
#executer.run(conf.ChromeAutoDemo, CustomerConfig)

#executer.run(conf.ChromeAutoDemo, CreateHierarchy.TestCase012__CreateOrgnization5Level)
executer.run(conf.ChromeAutoDemo,CreateVEE.TestCase007__ModifyOtherInfo)




