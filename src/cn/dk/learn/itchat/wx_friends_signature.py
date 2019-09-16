# -*- coding: utf-8 -*-

import itchat as wx
import re

wx.login()

friends = wx.get_friends(update = True)[0:]

# for f in friends:
#     # get friends signature
#     signature = f["Signature"]
#     print(f["NickName"] + " Signature:" + signature)

for f in friends:
    signature = f["Signature"].strip().replace("emoji", "").replace("span", "").replace("class", "")
    rep = re.compile(r"1f\d.+")
    signature = rep.sub("", signature)
    print(f["NickName"] + "Signature:" + signature)
