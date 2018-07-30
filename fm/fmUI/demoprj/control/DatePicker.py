# -*- coding: utf-8 -*-

from knitter.webelement import WebElement
import datetime
from selenium.webdriver.common.by import By

class DatePicker(WebElement):
    currentDate = datetime.date.today()


