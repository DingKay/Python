# -*- coding: utf-8 -*-

import itchat as wx
from pyecharts.charts import Pie

from pyecharts import options as opts

print("start")

wx.login()

friends = wx.get_friends(update = True)[0:]

male = female = total = other = 0

for i in friends[1:]:
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1
    total +=1

print("男性好友: %.2f%%" % (float(male) / total * 100))
print("女性好友：%.2f%%" % (float(female) / total * 100))
print("其他好友: %.2f%%" % (float(other) / total * 100))

# use Pie : pyecharts v1.0+
pie = Pie()

datas = [['male', "{:.2f}".format(float(male) / total * 100)],
         ['female', "{:.2f}".format(float(female) / total * 100)],
         ['other', "{:.2f}".format(float(other) / total * 100)]]

pie.add("", datas, label_opts=opts.LabelOpts(
                position="outside",
                formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
                background_color="#eee",
                border_color="#aaa",
                border_width=1,
                border_radius=4,
                rich={
                    "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                    "abg": {
                        "backgroundColor": "#e3e3e3",
                        "width": "100%",
                        "align": "right",
                        "height": 22,
                        "borderRadius": [4, 4, 0, 0],
                    },
                    "hr": {
                        "borderColor": "#aaa",
                        "width": "100%",
                        "borderWidth": 0.5,
                        "height": 0,
                    },
                    "b": {"fontSize": 16, "lineHeight": 33},
                    "per": {
                        "color": "#eee",
                        "backgroundColor": "#334455",
                        "padding": [2, 4],
                        "borderRadius": 2,
                    },
                },
            ))
pie.set_global_opts(title_opts=opts.TitleOpts(title="WeChat friends male to female ratio"))

pie.render("src/cn/dk/learn/itchat/wx_male_to_female_ratio.html")
