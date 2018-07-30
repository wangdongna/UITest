# -*- coding: utf-8 -*-

from knitter import executer
from demoprj import conf, testcase

#P1
from demoprj.testcase import FileOperation
from demoprj.testcase import _testalarmbubble



#P1
executer.run(conf.ChromeTestDemo, testcase._testalarmbubble)