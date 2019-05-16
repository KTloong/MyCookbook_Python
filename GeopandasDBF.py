import geopandas as gpd
import pandas as pd
import os
pd.set_option("display.precision", 11)

MyFolder = r"D:\Desktop\NNFN\DBF"

MyDBFFileName_List = [pa for pa in os.listdir(MyFolder) if os.path.splitext(os.path.basename(pa))[1] == ".dbf"]
# print(MyDBFFileName_List)
MyDBFFullFileName = []
for name in MyDBFFileName_List:
    MyDBFFullFileName.append(os.path.join(MyFolder, name))
print("Already full files paths!")
print(MyDBFFullFileName)



for sta in ["MEAN", "MAX", "MIN"]:
    MyFrame = pd.DataFrame()
    for pa in MyDBFFullFileName:
        Table = gpd.read_file(pa)
        PTable = pd.DataFrame(Table)
        Keys = list(Table.keys())
        #print(Keys)
        print("{}_{}".format(sta, os.path.splitext(os.path.basename(pa))[0]))
        MyFrame["{}_{}".format(sta, os.path.splitext(os.path.basename(pa))[0])] = PTable.pop(sta)

    #output result
    with pd.ExcelWriter(os.path.join(MyFolder, "{}_StaCollection.xlsx".format(sta))) as MyWriter:
        MyFrame.to_excel(MyWriter, sheet_name=sta, index=False, float_format="%.11f")

print("Mission accomplished!")

