 # -*- coding: utf-8 -*-

from knitter import executer

from src import conf
from src.testcase.Other import LoginValid
from src.testcase.Other import Jazz_Smoke
from src.testcase.Other import EditUserProfile
from src.testcase.SPManagement import CalendarConfig
from src.testcase.SPManagement import CustomerConfig
from src.testcase.SPManagement import UserConfig
from src.testcase.SPManagement import UserFunctionRole
from src.testcase.CustomerConfig import CreatePtag
from src.testcase.CustomerConfig import CreateVtag
from src.testcase.CustomerConfig import CreateHierarchy
from src.testcase.CustomerConfig import CreateHierarchyDemension
from src.testcase.CustomerConfig import AssociateTags
from src.testcase.CustomerConfig import CreateHierarchyProperty
from src.testcase.CustomerConfig import PtagRawDataView
from src.testcase.CustomerConfig import CreateVEE
from src.testcase.CustomerConfig import SaveWidget
from src.testcase.CustomerConfig import EnergyView
from src.testcase.KPIConfig import CreateNewKPI
from src.testcase.KPIConfig import EditKPI
from src.testcase.KPIConfig import RankingKPI
from src.testcase.KPIConfig import CreateReport



testcaselist1 = [CustomerConfig, UserConfig, UserFunctionRole, CalendarConfig]
testcaselist2 = [CreateHierarchy, CreateHierarchyDemension, CreateHierarchyProperty, AssociateTags]
testcaselist3 = [CreateNewKPI, EditKPI, RankingKPI, CreateReport]
testcaselist4 = [CreatePtag, CreateVtag, PtagRawDataView, CreateVEE]
testcaselist5 = [LoginValid, Jazz_Smoke, EditUserProfile]


# executer.run(conf.ChromeAutoDemo, testcaselist1, testcaselist2, testcaselist3, testcaselist4, testcaselist5)
executer.run(conf.ChromeAutoDemo, CreateReport)


