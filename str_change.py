'''
author:QIANKAI
date:2023-02-24
'''


def cat_str(str):
    element_list = str.splitlines(False)
    if element_list[0] == '':
        element_list = element_list[1:]
    return element_list


def get_tag(element_list):
    list_size = len(element_list)
    tag = [None] * list_size  # 初始化tag,通过标记各个元素的种类
    tag[0] = "n"
    tag[1] = "l"
    for i in range(2, list_size):
        if element_list[i][1] == '.':  # 对序号的.进行标记然后以此为标准加tag
            tag[i] = "t"  # t表示title
            tag[i - 1] = tag[i - 1] + "e"  # e表示end，即每个大括号内最后一项
        else:
            tag[i] = "i"  # i表示isin
    return tag


def creat_new(element_list):
    new_str = "\'name\':\'" + element_list[0] + '\',\n' + "\'lei\':\'" + element_list[1] + '\',\n' + "\'sub_fund\': ["
    tag = get_tag(element_list)
    list_size = len(element_list)
    for i in range(2, list_size):  # 按对应规则编辑字符串
        if tag[i] == "t":
            new_str = new_str + '{\n'
            element_list[i] = element_list[i][2:]  # 去除title前的编号
            new_str = new_str + "\'title': \'" + element_list[i] + "\',\n\'isin\': ["
        elif tag[i] == "te":
            new_str = new_str + "\'title': \'" + element_list[i] + "\'},"
        elif tag[i] == "i":
            new_str = new_str + "\'" + element_list[i] + "\',"
        elif tag[i] == "ie":
            new_str = new_str + "\'" + element_list[i] + "\']\n"
            new_str = new_str + "},"
    new_str.strip(',')
    new_str = new_str + "]\n" + "]"
    return new_str


def main():
    long_text = """
Variopartner SICAV
529900LPCSV88817QH61
1. TARENO GLOBAL WATER SOLUTIONS FUND
LU2001709034
LU2057889995
LU2001709547
2. TARENO FIXED INCOME FUND
LU1299722972
3. TARENO GLOBAL EQUITY FUND
LU1299721909
LU1299722113
LU1299722030
4. MIV GLOBAL MEDTECH FUND
LU0329630999
LU0329630130
"""
    element_list = cat_str(long_text)
    print(get_tag(element_list))
    new_str = creat_new(element_list)
    print(new_str)


if __name__ == "__main__":
    main()
