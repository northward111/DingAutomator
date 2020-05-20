import os
import time
import uiautomator2 as u2
from util.ding_util import send_msg


def send_ding(msg):
    ding_token = "99de3b9549d59caf5b445ef2d24a68b64f89498a5fda4b43c0b3098a3a57657e"
    ding_url = "https://oapi.dingtalk.com/robot/send?access_token={}".format(ding_token)
    send_msg(ding_url, "提醒：{}".format(msg))


def exec_cmd(cmd):
    print(cmd)
    os.system(cmd)


def sleep(secs):
    print("sleep {} seconds".format(secs))
    time.sleep(secs)


##根据x和y坐标进行屏幕定位点击事件
def on_click(x, y):
    ##触摸屏幕进行点击
    exec_cmd('adb shell input tap {x1} {y1}'.format(x1=x, y1=y))


##滑动屏幕从(x, y)坐标点到(ex, ey)坐标点
def slide(x, y, ex, ey):
    exec_cmd('adb shell input swipe {x1} {y1} {x2} {y2}'.format(x1=x, y1=y, x2=x + ex, y2=y + ey))


##手机屏幕响应操作
def touch(key):  # 按动相应的按键
    if key == "back":
        print("> back按键")
        exec_cmd('adb shell input keyevent 4')
    elif key == "power":
        print("> power按键")
        exec_cmd('adb shell input keyevent 26')
    elif key == "home":
        print("> home按键")
        exec_cmd('adb shell input keyevent 3')
    sleep(3)  # 等待1s等手机反应


##判断是否黑屏
def is_black():
    d = u2.connect()
    screen = d.info
    if not screen["screenOn"]:
        print("熄屏状态...")
        return True


def start():
    ##由于我的是密码锁屏，姑且要输入密码
    ##如果将密码锁去掉则可以注释掉一下代码了，只需要亮屏即可
    slide(550, 1200, 0, -800)
    sleep(1)
    touch("home")
    touch("home")
    ##1、点击屏幕钉钉软件，坐标可根据手机自行调节
    exec_cmd("adb shell am start -n com.alibaba.android.rimet/com.alibaba.android.rimet.biz.LaunchHomeActivity")
    sleep(5)
    touch("home")
    touch("home")
    touch("power")


def once():
    try:
        if is_black():
            touch("power")  ##点击亮屏幕
            start()
        else:
            start()
    except Exception as ex:
        err_msg = "exception {}".format(repr(ex))
        print(err_msg)
        send_ding(err_msg)


def start_main():
    count = 0
    while True:
        count = count + 1
        exec_msg = "exec times {count}".format(count=count)
        print(exec_msg)
        send_ding(exec_msg)
        once()
        sleep(60 * 10)


if __name__ == "__main__":
    start_main()
