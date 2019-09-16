import jieba
from wordcloud import WordCloud

import matplotlib.pyplot as plt

mystr = "小妹妹，你跟谁撒娇呢，我不吃你这套！\n 十块钱的电\n子手表，正能量!".replace('\n', "")

print(mystr)

wordsplitList = jieba.cut(mystr, cut_all=True) # 切割, 全部切割
# print('/'.join(wordsplitList))
# wordsplitListforSearch = jieba.cut_for_search(mystr) # 按搜索方式切割
# print('/'.join(wordsplitListforSearch))

word_split = " ".join(wordsplitList)

print(word_split)

my_wordCloud = WordCloud(background_color = 'white', max_words = 2000,
        max_font_size = 40, random_state = 42,
        font_path = 'fonts/msyh.ttf').generate(word_split)

plt.imshow(my_wordCloud)

plt.axis('off')
plt.show()