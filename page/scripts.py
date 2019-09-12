"""

======================

@author:niuqun

@time:2019/9/11:10:38 AM

@email:17689551930@163.com

======================


"""
cou_list = [ "I'm hungry","Picnic", "What's this?", 'On the farm']
from time import sleep
import page
import allure
from  base.devices import get_devices
class search(get_devices):
    def  __init__(self,deiver):
        get_devices.__init__(self,deiver)
    def click_wx_lojin(self):
        self.click_search("d",page.wx_login)
    # 如何上课
    def click_who(self):
        self.click_search("t",page.who_cou)
    # 如何上课返回
    def click_who_add(self):
        self.click_search("d",page.who_add)
    def click_buy_coiu(self):
        self.click_search("d",page.click_buy)
        self.click_search("d",page.buy_back)
        sleep(1)
    # 点击课堂
    def click_cou(self):
        self.click_search("d",page.click_cou)
    def click_for_cou(self):
        for i in (cou_list):
           print("wosji ",i)
           if i== "What's this?":
               self.driver(text="What's this?").drag_to(text="如何上课", duration=1)
           else:
               pass
           # 点击reciew
           self.click_search("t","%s" % i)
           print(i)
           allure.attach("进入：", "课程:%s" % i)
           # self.driver(scrollable=True).scroll.toEnd(10)
           sleep(1)
           if i =="I'm hungry":
               pcica_lists=(page.customs_list)
           else:
               pcica_lists = (page.pcica_list)
           for b in pcica_lists:
               print(b)
               self.click_search("t", "%s" % b)
               allure.attach("进入：", "关卡:%s" % b)
               sleep(4)
               self.back()
               if b =='Report':
                   self.click_search("d", page.exit)

               else:
                   self.driver(scrollable=True).scroll.toEnd(10)

           sleep(2)
    def click_reivw(self):
        self.click_search("t",page.review)
    def click_go_reviw(self):
        sleep(1)
        self.driver.xpath('//*[@resource-id="app"]/android.view.View[4]').click()
        sleep(3)
        self.back()
        print(123)

        self.click_search("d", page.exit)
    def click_xiaodu(self):
        self.click_search("d",page.xiaodu)
    def click_foud(self):
        self.click_search("d",page.found)
    def click_my(self):
        self.click_search("d",page.my)
    def click_seting(self):
        self.click_search("d",page.click_sys)
    def click_add_login(self):
        self.click_search("t",page.add_login)
        self.click_search("d",page.ok)
