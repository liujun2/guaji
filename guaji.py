# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time

import sys
path = '/usr/local/bin/chromedriver' #your chromedriver path
sys.path.append(path)

driver = webdriver.Chrome()
driver.get("https://www.bjjnts.cn/") 
time.sleep(60)

import pandas as pd
data = pd.read_csv('course_1.csv', header = None)
print(type(data))
for index, row in data.iterrows():
    chapter_name = row[0].split(' ')[0]
    chapter_time = int(row[1].split(':')[0])*3600 + int(row[1].split(':')[1])*60 + int(row[1].split(':')[2])
    print(index,chapter_name,chapter_time)
    chapter_index = int(row[0].split(' ')[1].split('-')[1]) - 1
    print(chapter_index)
    elements = driver.find_elements_by_class_name(chapter_name)
    print(elements)
    if len(elements) > 0:
        elements[chapter_index].click()
    count_down_number = chapter_time + 60
    while (count_down_number > 0):
        print('倒计时',count_down_number)
        time.sleep(1)
        try:
            elements = driver.find_elements_by_class_name('layui-layer-btn0')
            if len(elements) == 0:
                print('no dialog')
            else:
                print('elements',elements)
                for ele in elements:
                    ele.click()
        except Exception as e:
            print(e)
        count_down_number -= 1
