from math import radians, cos, sin, asin, sqrt,atan,pi
import pandas as pd
import numpy as np

def haversine(lon1, lat1, lon2, lat2):  # 经度1，纬度1，经度2，纬度2 （十进制度数）
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # 地球平均半径，单位为公里
    return c * r * 1000

angle = []
data = pd.read_excel(r"D:\Desktop\第三组数据.xlsx", usecols=range(2, 5))
length = len(data['经度'])
print(data.keys())
for item in range(1, length):
    an = atan(haversine(data['经度'][0], data['纬度'][0], data['经度'][item], data['纬度'][item]) / data['相对高度'][item]) / pi * 180
    angle.append(an)
# print(atan(haversine(114.3497607,30.53591186,114.349895,30.535933)/312.34)/pi*180)
# print(atan(haversine(114.3497607,30.53591186,114.3506233,30.53601247)/312.316)/pi*180)
np.savetxt(r"D:\Desktop\第三组数据_1.csv", angle, fmt='%s', delimiter=' ')
