'''
author:QIANKAI
date:2023-02-24
'''
# 待解析网页：https://www.chinabond.com.cn/cb/cn/xxpl/ywgg/tgywgg/20230129/161991420.shtml
import requests
import pandas as pd
from lxml import etree


def get_table():
    url = "https://www.chinabond.com.cn/cb/cn/xxpl/ywgg/tgywgg/20230129/161991420.shtml"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'}
    res = requests.get(url, headers=headers, timeout=40)
    res.encoding = "utf-8"  # 要对解析出来的源码重新编码，否则爬出来为乱码
    res_elements = etree.HTML(res.text)
    table = res_elements.xpath('//table')  # 获取网页内所有表格
    table = etree.tostring(table[0], encoding='UTF-8').decode()  # 选择第一个表格进行列表转化
    print(type(table))
    df = pd.read_html(table, encoding='UTF-8', header=0)[0]  # 转化为pands格式
    results = list(df.T.to_dict().values())
    print(results)
    df.to_csv("./data.csv", index=False)  # 存储为csv


if __name__ == "__main__":
    get_table()
