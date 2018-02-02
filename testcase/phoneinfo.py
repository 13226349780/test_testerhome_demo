__author__ = 'lqf'


import os
import sys


def phoneInfo():
    size_str = os.popen('adb shell wm size').read()
    device = os.popen('adb shell getprop ro.product.model').read()
    pyInfo = sys.platform + "\n" + sys.version
    print(size_str,device,pyInfo)
    return (size_str, device, pyInfo)
if __name__ == "__main__":
    phoneInfo()
