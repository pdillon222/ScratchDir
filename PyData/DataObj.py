#!/data/data/com.termux/files/usr/bin/python3

import pandas as pd
import numpy as np
import datetime, re
from datetime import datetime as dto
from pandas import DataFrame as df
from pandas import Series as ser

class DataObjects:
    def __init__(self):
        self.initdate = dto.now()
        self.dateRanges = {
          1:31,2:28,3:31,
          4:30,5:31,6:30,
          7:31,8:31,9:30,
          10:31,11:31,12:31
        }
        '''a leap year is determined by
           divisibility of 400,100,4,2
           if leap year: 2==29'''
        intNow = int(self.initdate.strftime("%y"))
        moduloTests = [400,200,100,4,2]
        if all([(intNow%i==0) for i in moduloTests]):
            self.dateRanges[2]=29

    @classmethod
    def monthList(date_object):
        '''arg date_object must be a python
        datetime object'''
        pass

doTest = DataObjects()
print(doTest.dateRanges)

