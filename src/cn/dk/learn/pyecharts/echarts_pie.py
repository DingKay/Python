# -*- coding: utf-8 -*-
from pyecharts.charts import Pie
from pyecharts import options as opts

pie = Pie()

data = [list(z) for z in zip(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"], [1, 2, 3, 4, 4, 1, 7])]
print(data)

pie.add("", data)
pie.set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例"))
pie.render("abc.html")
