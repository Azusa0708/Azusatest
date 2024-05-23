###安卓swipe操作###

from airtest.core.android import *


def swipe_android(pos_begin,pos_end,duration=0.8,steps=5,fingers=1):
    dev.swipe(pos_begin,pos_end,duration=duration,steps=steps,fingers=fingers)
    