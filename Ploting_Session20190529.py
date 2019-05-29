import pandas as pd
import matplotlib.pyplot as plt

pd.set_option("display.precision", 11)
pd.set_option('expand_frame_repr', False)  # 当列太多时不自动换行

data = pd.read_excel(r"D:\Desktop\0528\DBFbackup\DBFnew\Fishnet.xlsx", usecols=range(2, 7))
print(data.head())

# data.boxplot(column=["Max"], rot=0, figsize=(10.8,7.2))
# plt.show()
# data.boxplot(column=["Min"], rot=0, figsize=(10.8,7.2))
# plt.show()
# data.boxplot(column=["Std"], rot=0, figsize=(10.8,7.2))
# plt.show()

print(data.describe())
data["MinID"].plot(kind="pie", rot=0, figsize=(10.8, 7.2), by="MinID")
plt.show()
data["MaxID"].plot(kind="pie", rot=0, figsize=(10.8, 7.2), by="MaxID")
plt.show()
