#coding=utf-8

import re
url = "http://news.sina.com.cn/o/2018-01-27/doc-ifyqyqni3775084.shtml"

newurl = re.search("doc-i(.+).shtml",url)

print(newurl.group(0)) # 匹配到的整个字符串
print(newurl.group(1)) # 匹配到的 括号中的字符串
