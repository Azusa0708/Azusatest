from airtest.core.api import *
import sys




devices_list = [] #连接设备URL列表
dev = [] #设备已初始化后存储

num_of_devices = len(devices_list) #设备个数

if(num_of_devices == 0):  #未连接设备
    print("未连接设备！！！")
    sys.exit()

for i in range(num_of_devices):
    dev[i] = connect_device(devices_list[i])

auto_setup(__file__,devices=devices_list) #设备连接