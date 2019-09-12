# """
#
# ======================
#
# @author:niuqun
#
# @time:2019/9/10:6:00 PM
#
# @email:17689551930@163.com
#
# ======================
#
# """
# # coding: utf-8
# #
# import uiautomator2 as u2
# from  time import sleep
# d = u2.connect()
# print(d.device_info)
# #
# d.session("ai.zile.app")
# # # 点击微信登陆
# # d(resourceId="ai.zile.app:id/btn_wechat_login").click()
# # sleep(1)
# # # 点击如何上课
# # d(text="如何上课").click()
# # sleep(1)
# # # 如何上课返回
# # d(resourceId="ai.zile.app:id/iv_back_pressed").click()
# # sleep(1)
# # # 点击购买课程
# # d(resourceId="ai.zile.app:id/card_view").click()
# # sleep(1)
# # # 购买课程返回
# # d(resourceId="ai.zile.app:id/relativeBack").click()
# sleep(1)
# # 点击课堂
# d.xpath('//*[@resource-id="ai.zile.app:id/nav_course"]/android.widget.ImageView[1]').click()
# sleep(1)
# # 滑动到如何上课
# d.swipe(155, 2359, 155, 400)
# cou_list = [ 'Picnic', "What's this?", 'On the farm']
# customs_list = ['Cartoon', 'Video', "Word",'Reading', 'Speaking', 'Game', 'Song', 'Report']
# pcica_list = ['Song', 'Word', 'Reading', 'Game', 'Speaking', 'Video', 'Report']
# for i in cou_list:
#     # 点击reciew
#     d(text="%s" % i).click()
#     print(i)
#     sleep(1)
#     if i =="I'm hungry":
#         pcica_lists=customs_list
#     else:
#         pcica_lists = pcica_list
#     for b in pcica_lists:
#         d(text="%s" % b).click()
#         print(b)
#         # 退出课程
#         sleep(4)
#         d.press("back")
#         print("fanhui ")
#         d.swipe(155, 2359, 155, 2100)
#         sleep(1)
#
#     d(resourceId="ai.zile.app:id/relativeBack").click()
#     sleep(2)
# d(text="Review").click()
# # 进入review
# d.xpath('//*[@resource-id="app"]/android.view.View[3]/android.view.View[3]').click()
# # 退出关卡
# d.press("back")
# # 返回课程列表
# d(resourceId="ai.zile.app:id/relativeBack").click()
# d = u2.connect()
# # 点击小杜
# d(resourceId="ai.zile.app:id/nav_schedule").click()
# # 点击发现
# d(resourceId="ai.zile.app:id/nav_discover").click()
# # 点击我的
# d(resourceId="ai.zile.app:id/nav_user").click()
# # 点击设置
# d(resourceId="ai.zile.app:id/ibtn_setting").click()
# # 点击退出登陆
# d(text="退出登录").click()
# # 点击确定
# d(resourceId="ai.zile.app:id/textViewConfirm").click()
# # from base import devices
# #
# # devices.click_search('ID', "ai.zile.app:id/btn_wechat_login")
# # devices.click_search('text', "如何上课")
import uiautomator2 as u2

d = u2.connect()
d.xpath('//*[@resource-id="app"]/android.view.View[3]/android.view.View[1]/android.view.View[1]').click()
d.xpath().click()