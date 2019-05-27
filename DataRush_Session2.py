import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
subset_columns = ['Job #', 'Doc #', 'Borough', 'Initial Cost', 'Total Est. Fee']
path = r"D:\MyDownloads\DOB_Job_Application_Filings.csv"
#nrows指定读取前100行（注意并不是100条记录），usecols指定需要使用的列名，header指定从第几行开始读
df = pd.read_csv(path, nrows=100, usecols=subset_columns, header=0)
print(df)
#删除列
to_drop = ['Job #', 'Doc #']
df.drop(to_drop, axis=1, inplace=True) #to_drop是指定要删除的行或者列的名称（这里是列名），axis=1表示列，inplace表示不创建新的对象
#删除行
# to_drop = range(0,5)#指定一个连续的行号范围，这里是0-4也就是前五行
# df.drop(to_drop, axis=0, inplace=True) #axis=0表示删除行，inplace表示是否替换

#对列进行重命名
#首先生成一个旧列明和新列明的字典，这个字典由旧名和新名的key-value pair构成
to_rename = {'Borough': '区', 'Initial Cost': '初始成本', "Total Est. Fee": "总附加费用"}
df.rename(columns=to_rename, inplace=True)#columns参数指定替换的字典对象，inplace表示是否重新生成对象

df.set_index("区", inplace=True) #指定列作为索引
df.head()
print(df)

df.index = df.index.str.upper() #利用str的upper方法，别忘了括号！！将所有行变为大写
print(df.index)
df.index = df.index.str.lower() #利用str的lower方法，别忘了括号！！将所有的行变为小写
print(df)
df.index = df.index.str.capitalize() #利用str的Capitalize方法，别忘了括号！！将所有的行首字母大写
print(df)

df["初始成本"] = df["初始成本"].str.replace("$", "") #利用str的replace方法，别忘了括号！！进行字符替换，首先指定原来的字符，后指定替换字符
print(df.初始成本)
df['初始成本'] = df['初始成本'].str.strip() #利用str的strip方法去掉字符串的头尾空格和\n,\t
print(df.初始成本)

df['总附加费用'] = df['总附加费用'].str.split('.') #利用str的split方法根据指定的分割符，对字符串进行分割，分割后前后部分保存为list格式
print(df.总附加费用)
#接着上一步，根据分割后的结果通过str中的get方法获取该列中每行元素列表中的第一个元素组成新列，生成一个新列
df['总附加费用_整数'] = df['总附加费用'].str.get(0)
print(df.总附加费用_整数)

df['总附加费用_整数'].str.contains('0')#利用str中的contain方法判断字符串中是否包括特定字符，如果不是返回False，是返回True
print(df.总附加费用_整数)

print(df['总附加费用_整数'].str.find('0')) #利用str中的find方法，判断字符串中是否包括特定的字符，如果包括返回最开始出现的位置,如果没有返回-1

#2019年5月27日
#参考资料https://mp.weixin.qq.com/s?__biz=MzIxNjM4NDE2MA==&mid=2247490270&idx=2&sn=3ca321fd0ced7d458f4c10233004ddd5&chksm=97888d11a0ff0407e6151aea5e79fb669e04a04bc83c777aa407bc5b266dc6ea82522b93d866&mpshare=1&scene=1&srcid=&key=864f666bf054558473cfb972449b00e1c9d5500194a086a46c7f5a19fa9d7f0ff6eded56c49c1e17003bbc8bc31e80568989e24c54ba47805879f0c4a039fc2d64722ae913f77cbf2d5e0772b58352dd&ascene=1&uin=MjIzODM3NTE0Mw%3D%3D&devicetype=Windows+10&version=62060833&lang=en&pass_ticket=vQVADnlTAFrKs6uvdc0%2Bsx7oKcLgzsM8yloCgW23r5vSVb4hkISf8iXZ%2BxeJmznG


