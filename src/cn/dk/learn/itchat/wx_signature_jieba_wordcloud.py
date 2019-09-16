# -*- coding: utf-8 -*-

import itchat as wx
import jieba

import wordcloud
import re

import matplotlib.pyplot as plt
from wordcloud import WordCloud

import PIL.Image as Image

wx.login()

friends = wx.get_friends(update = True)[0:]

signatures = []
for i in friends:
    signature = i["Signature"].strip().replace("emoji", "").replace("span", "").replace("class", "").replace("</>", "").replace('\n', "")
    regex = re.compile(r"1f\d.+")
    signature = regex.sub("", signature)
    signatures.append(signature)

text = "".join(signatures)

word_list = jieba.cut(text, cut_all = True)

# splice words
word_split = " ".join(word_list)

my_wordCloud = WordCloud(background_color = 'white', max_words = 2000,
        max_font_size = 40, random_state = 42,
        font_path = r'fonts/msyh.ttf').generate(word_split)

plt.imshow(my_wordCloud)

plt.axis('off')
plt.show()