# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
import random

import sys
path = '/usr/local/bin/chromedriver' #your chromedriver path
sys.path.append(path)

def conform_dialog():
    elements_confor_dialog = driver.find_elements_by_class_name('layui-layer-btn0')
    if len(elements_confor_dialog) == 0:
        print('no dialog')
    else:
        print('conform')
        try:
            for ele_dialog in elements_confor_dialog:
                ele_dialog.click()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://www.bjjnts.cn/login") 
    time.sleep(60)
    num_course_unlock = 0

    while True:
        time.sleep(random.randint(20,120))
        conform_dialog()
        time.sleep(random.randint(20,120))
        elements = driver.find_elements_by_class_name('change_chapter')
        print(len(elements))
        if len(elements) > 0:
            elements_un_lock = list(filter(lambda element : int(element.get_attribute('data-lock')) == 0, elements))
            print(len(elements_un_lock))
            if len(elements_un_lock) != num_course_unlock:
                num_course_unlock = len(elements_un_lock)
                elements_un_lock[len(elements_un_lock) - 1].click()

