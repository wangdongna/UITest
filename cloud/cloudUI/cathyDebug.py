# -*- coding: utf-8 -*-

from knitter import executer

from src import conf
from src.testcase.Other import LoginValid
from src.testcase.SPManagement import BenchmarkConfig
from src.testcase.SPManagement import LabelingConfig
from src.testcase.SPManagement import CarbonFactor
from src.testcase.SPManagement import CustomerConfig
from src.testcase.SPManagement import CustomerConsumption
from src.testcase.SPManagement import UserConfig
from src.testcase.SPManagement import UserFunctionRole

from src.testcase.CustomerConfig import CreatePtag
from src.testcase.CustomerConfig import CreateVtag

from src import conf

#executer.run(conf.ChromeTestDemo, src.testcase.SPManagement.LabelingConfig)
#executer.run(conf.ChromeAutoDemo, LabelingConfig)
#executer.run(conf.ChromeAutoDemo, BenchmarkConfig)
#executer.run(conf.ChromeAutoDemo, CreatePtag.TestCase08__ModifyEnergyLabelAndVerify)
executer.run(conf.ChromeAutoDemo, CreatePtag)


