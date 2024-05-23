###切换当前使用设备###

from airtest.core.api import *

def change_device(number):
    set_current(number)
    dev = device()
    if dev.info["platform"] == "Android":
        dev = Android()
    elif dev.info["platform"] == "Ios":
        dev = IOS()
    elif dev.info["platform"] == "Windows":
        dev = Windows()
    else:
        print("切换设备出错")
    print("切换设备 %s 成功"% number)