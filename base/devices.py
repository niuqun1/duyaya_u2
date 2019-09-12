"""

======================

@author:niuqun

@time:2019/9/11:8:41 AM

@email:17689551930@163.com

======================

"""
import subprocess
class get_devices:
    def __init__(self, d):
        #初始化driver -- 供find_element 和 find_elements使用
        self.driver = d
    def search_element(self,loc,values=None):
        if loc == "d":
            return self.driver(resourceId=values)
        elif loc == "x":
            return self.driver(xpath=values)
        elif loc == "t":
            return  self.driver(text=values)
        else:print("输入错误")
    def click_search(self,loc,values):
        # 点击事件
        """
        :param loc:定位方法
        :param values: 元素值
        :return:
        """
        return self.search_element(loc,values).click()
    def input_element(self,loc,values,text):
        """
        :param loc:
        :param values:
        :param text: 要输入的内容
        :return:
        """
        input_text = self.search_element(loc,values)
        input_text.clear_text()
        input_text.send_keys(text)
    def  get_screen(self,name):
        """
        :param name: 截图的名字
        :return:
        """
        self.driver.screenshot(name)
    # 获取设备id
    def getphonelist():
        cmd = r'adb logcat >/Users/edz/Desktop/log/1.txt'  # % apk_file
        pr = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        # pr.wait()  # 不会马上返回输出的命令，需要等待
        out = pr.stdout.readlines()  # out = pr.stdout.read().decode("UTF-8")
        # devices = []
        # for i in (out)[1:-1]:
        #     device = str(i).split("\\")[0].split("'")[-1]
        #     devices.append(device)
        # return devices  # 手机设备列表
    # print(getphonelist())
    def slide(self,startx, starty, endx, endy, duration=None ):
        """

        :param startx:开始x
        :param starty:开始
        :param endx: 结束x
        :param endy:结束y
        :param duration: 滑动的时间
        :return:
        """
        return self.driver.swipe(startx, starty, endx, endy, duration)
    def back(self):
        return self.driver.press("back")







