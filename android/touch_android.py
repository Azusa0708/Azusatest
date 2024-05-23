###安卓touch操作###

from airtest.core.android import *


def touch_android(pos,duration=0.01):
    dev.touch(pos = pos,duration=duration)