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

#2019年5月27日
#参考资料https://mp.weixin.qq.com/s?__biz=MzIxNjM4NDE2MA==&mid=2247490270&idx=2&sn=3ca321fd0ced7d458f4c10233004ddd5&chksm=97888d11a0ff0407e6151aea5e79fb669e04a04bc83c777aa407bc5b266dc6ea82522b93d866&mpshare=1&scene=1&srcid=&key=864f666bf054558473cfb972449b00e1c9d5500194a086a46c7f5a19fa9d7f0ff6eded56c49c1e17003bbc8bc31e80568989e24c54ba47805879f0c4a039fc2d64722ae913f77cbf2d5e0772b58352dd&ascene=1&uin=MjIzODM3NTE0Mw%3D%3D&devicetype=Windows+10&version=62060833&lang=en&pass_ticket=vQVADnlTAFrKs6uvdc0%2Bsx7oKcLgzsM8yloCgW23r5vSVb4hkISf8iXZ%2BxeJmznG