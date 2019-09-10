# -*- coding: utf-8 -*-

import itchat

# wechat sign in
itchat.login()

# send message "Hello" to wechat filehelper
itchat.send("Hello", 'filehelper')