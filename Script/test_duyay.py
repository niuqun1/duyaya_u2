"""

======================

@author:niuqun

@time:2019/9/11:11:10 AM

@email:17689551930@163.com

======================

"""

import uiautomator2 as u2
import sys,os
sys.path.append(os.getcwd())
from page.scripts import search
from time import sleep
import allure
d=u2.connect()
d.session("ai.zile.app")
class Test_1:
    def setup_class(self):
        self.obj=search(d)
        @allure.step(title="点击微信登陆")
        def test_001(self):
            self.obj.click_wx_lojin()
        @allure.step(title="点击如何上课")
        def test_002(self):
            self.obj.click_who()
            self.obj.click_who_add()
        @allure.step(title="点击购买课程")
        def test_007(self):
            sleep(1)
            self.obj.click_buy_coiu()
        @allure.step(title="点击课堂")
        def test_003(self):
            self.obj.click_cou()
            sleep(1)
            d(scrollable=True).scroll.toEnd(10)
            sleep(2)
        @allure.step(title="操作关卡内部")
        def test_005(self):
            self.obj.click_for_cou()
        def test_008(self):
            self.obj.click_reivw()
            self.obj.click_go_reviw()
            self.obj.back()
        def test_009(self):
            self.obj.click_foud()
            self.obj.click_xiaodu()
            self.obj.click_my()
            self.obj.click_seting()
            self.obj.click_add_login()
