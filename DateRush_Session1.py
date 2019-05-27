import pandas as pd
import numpy as np
import tushare as ts #tushare是国内现有的免费数据包中最好的股票/基金数据获取方式
import matplotlib.pyplot as plt


pd.set_option('display.max_columns', 100)  # 设置显示数据的最大列数，防止出现省略号…，导致数据显示不全
pd.set_option('expand_frame_repr', False)  # 当列太多时不自动换行

#网站注册tushare账号后，登录，点击头像，点击接口token，获取token
token = "7e00606212f81efca4a179ea33542f82ea57ac2da117df574c3da74e"
ts.set_token(token)

pro = ts.pro_api()#创建Api对象
df = pro.daily(ts_code='600000.SH', start_date='20190401', end_date='20190430')#获取日数据，指定名称和起止时间

df.head(5)#查看前五行
df.tail(5)#查看后五行

print(df.shape) #获取DataFrame的形状
print(df.columns) #获取列名
print(df.info) #获取阵列的信息（包括列名，条目的数量，每列的数类型，统计各列的数据类型各有多少个，索引）

print(df.describe())#获取每列的统计信息（条目的数量，平均值，标准差，最小值，25%分位，50%分位，75%分位，最大值）
print(df.close.value_counts()) #获取列中值各出现了多少次（包括空值）
print(df.close.value_counts(dropna=True))#获取列中值除了空值各出现了多少次

df.close.plot(kind="hist", rot=0) #利用某列数据绘制直方图
plt.show()

df.boxplot(column="close", by="ts_code", rot=0)#对某一列利用ts_code字段对close列进行分组然后绘制箱形图
plt.show()
#下面的画图方法不正确，因为series对象没有boxplot方法（“Series” object has no attribute “boxplot”）
#只能利用dataframe对象绘制boxplot
# df.close.boxplot(rot=0)
# plt.show()

df.plot(kind="scatter", x="close", y="pre_close", rot=0)#绘制散点图
plt.show()

