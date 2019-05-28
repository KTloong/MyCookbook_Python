import geopandas as gpd
import pandas as pd
import numpy as np
import os
from tkinter import filedialog

pd.set_option("display.precision", 11)
pd.set_option('expand_frame_repr', False)  # 当列太多时不自动换行

MyFolder = filedialog.askopenfilename()

data = pd.read_excel(MyFolder)
in_keys = data.keys()

new_keys_dic = dict(zip(in_keys, range(1, len(in_keys) + 1)))
# print(new_keys)
data.rename(columns=new_keys_dic, inplace=True)
new_keys = data.keys()

data["Max"] = data[new_keys].max(axis=1)
data["Min"] = data[new_keys].min(axis=1)

data["MaxID"] = data[new_keys].idxmax(axis=1)
data["MinID"] = data[new_keys].idxmin(axis=1)

old_keys_dic = dict(zip(range(1, len(in_keys) + 1), in_keys))
data.rename(columns=old_keys_dic, inplace=True)

data["Std"] = data[in_keys].std(ddof=0, axis=1)  # ddof表示自由度的数目x，即n-x的数目
# print(data.head())
with pd.ExcelWriter(os.path.join(os.path.dirname(MyFolder), "{}_StaCollection.xlsx".format(1))) as MyWriter:
    data.to_excel(MyWriter, index=False, float_format="%.11f")
print("Finish!")