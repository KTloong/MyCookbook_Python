import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = r"D:\MyPrj\python-data-cleaning\Datasets\BL-Flickr-Images-Book.csv"

df = pd.read_csv(path)
print(df['Place of Publication'].head(10))
print(df["Place of Publication"].tail(10))

# 利用numpy where(condition, then, else 结构对数据列进行修复)
london = df['Place of Publication'].str.contains("london")
oxford = df['Place of Publication'].str.contains("oxford")
df['Place of Publication'] = np.where(london, "London",
                                      np.where(oxford, "Oxford",
                                               df['Place of Publication'].str.replace("-", " ")))

print(df['Place of Publication'])

# 规范化数据
path = r"D:\MyPrj\python-data-cleaning\Datasets\university_towns.txt"
university_towns = []

with open(path, "r") as file:
    for line in file:
        if "[edit]" in line:
            state = line
        else:
            university_towns.append((state, line))

print(university_towns[:5])

# 利用含有tuple的list生成一个DataFrame，指定列明为State和RegionName
towns_df = pd.DataFrame(university_towns, columns=["State", "RegionName"])
print(towns_df.head())


# 利用applymap方法作用于整个DataFrame的元素
def get_citystate(item):
    if " (" in item:
        return item[:item.find(" (")]
    elif "[" in item:
        return item[:item.find("[")]
    else:
        return item


# 使用applymap时，输入为函数名没有括号
towns_df = towns_df.applymap(get_citystate) #需要重新弄个变量
print(towns_df.head())

##
#fillna()函数可以填补空值，操作对象是Series

#2019年5月27日
#参考资料https://mp.weixin.qq.com/s?__biz=MzIxNjM4NDE2MA==&mid=2247490270&idx=2&sn=3ca321fd0ced7d458f4c10233004ddd5&chksm=97888d11a0ff0407e6151aea5e79fb669e04a04bc83c777aa407bc5b266dc6ea82522b93d866&mpshare=1&scene=1&srcid=&key=864f666bf054558473cfb972449b00e1c9d5500194a086a46c7f5a19fa9d7f0ff6eded56c49c1e17003bbc8bc31e80568989e24c54ba47805879f0c4a039fc2d64722ae913f77cbf2d5e0772b58352dd&ascene=1&uin=MjIzODM3NTE0Mw%3D%3D&devicetype=Windows+10&version=62060833&lang=en&pass_ticket=vQVADnlTAFrKs6uvdc0%2Bsx7oKcLgzsM8yloCgW23r5vSVb4hkISf8iXZ%2BxeJmznG
