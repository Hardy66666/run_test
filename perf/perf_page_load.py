#encoding utf-8
import uiautomator2 as u2
from time import sleep
#from uiautomator2.ext.htmlreport import HTMLReport
import pytest
# import allure
import os
from common import logger
from common import compimgs_similar
import time
import datetime
import xlwt


from device.android_device import device as d
from scene.app_store_oppo import OppoScene

def loadSearchPage(pkg_name):

    t = OppoScene(pkg_name)
    t.stopApp()
    t.startApp()
    # t.searchPage()
    # t.searchWord("vpn")
    # sleep 3 s获取基准图片
    time.sleep(3)
    temp_img1 = t.getDevice().screenshot("../tmp_image/search_base.jpg")

    # 重新启动App
    t.stopApp()
    t.startApp()
    # time.sleep(3)

    # t.searchPage()
    # t.searchWord("vpn")
    # 测试
    t1 = time.perf_counter()
    while 1:
        t3 = time.perf_counter()
        temp_img2 = t.getDevice().screenshot("../tmp_image/search_test.jpg")
        h = compimgs_similar.runImgSimilar(temp_img1, temp_img2)
        t4 = time.perf_counter()
        print(f'screenshot coast:{t4 - t3:.8f}s')
        if h < 8:
            end_time = time.perf_counter()
            break
    print(f'coast:{ end_time - t1:.8f}s')



if __name__ == '__main__':
    for i in range (10):
        loadSearchPage("com.heytap.market")


