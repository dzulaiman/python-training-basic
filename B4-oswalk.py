#!/usr/bin/env python
#Example B4: oswalk
#Python Crash Course
#dzulaiman@nm.gov.my
#2015/12/08

import os

for root, dirs, files in os.walk(r"C:\Users", topdown=False):
    for name in files:
        print(os.path.join(root, name))

