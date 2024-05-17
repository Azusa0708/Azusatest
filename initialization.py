###初始化设备连接###

from airtest.core.api import *
import sys

def initialization():
    devices_list = [] #连接设备URL列表

    num_of_devices = len(devices_list) #设备个数

    if(num_of_devices == 0):  #未连接设备
        print("未连接设备！！！")
        sys.exit()

    auto_setup(__file__,devices=devices_list)  #自动设置Airtest运行环境 连接设备

    set_current(0)  #设置当前设备为第一个设备

    