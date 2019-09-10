# -*- coding: utf-8 -*-
'''
    WeChat friends male to female ratio
'''
import itchat as wx

wx.login()

# Get friends list
friends = wx.get_friends(update=True)[0:]

# intialization
male = female = other = total = 0

# the frist one is myself, start at 2
for i in friends[1:]:
    sex = i['Sex']
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else :
        other += 1
    total += 1

# last result of the male to female ratio
print("男性好友：%.2f%%" % (float(male) / total * 100))
print("女性好友: %.2f%%" % (float(female) / total * 100))
print("其他好友: %.2f%%" % (float(other) / total * 100))