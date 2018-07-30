# -*- coding: utf-8 -*-

from knitter import executer
from demoprj import conf, testcase
from demoprj.testcase import CustomerConfig
from demoprj.testcase import UserConfig
from demoprj.testcase import FunctionRoleConfig
from demoprj.testcase import Hierarchy_Other
from demoprj.testcase import BuildingFileOperation
from demoprj.testcase import TicketConfig
from demoprj.testcase import MaintanenceConfig
from demoprj.testcase import FileManagement
from demoprj.testcase import DeviceRelated
from demoprj.testcase import HierarchyConfig
from demoprj.testcase import Hierarchy_SceneLog
from demoprj.testcase import LoginRelated
from demoprj.testcase import FaultAlarmConfig
from demoprj.testcase import BuildingAlarm

testcaselist1 = [CustomerConfig, UserConfig, FunctionRoleConfig]
testcaselist2 = [HierarchyConfig, Hierarchy_Other, Hierarchy_SceneLog, DeviceRelated, BuildingFileOperation]
testcaselist3 = [TicketConfig, MaintanenceConfig, FileManagement]
testcaselist4 = [BuildingAlarm, FaultAlarmConfig, LoginRelated]

executer.run(conf.ChromeAutoDemo, testcaselist1, testcaselist2, testcaselist3, testcaselist4)
