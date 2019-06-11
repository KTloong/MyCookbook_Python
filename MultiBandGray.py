from osgeo import gdal
import numpy as np
import os
from tkinter import filedialog



def KLReadGeotiff(inpath):
     ds=gdal.Open(inpath)
     col=ds.RasterXSize #get columns
     row=ds.RasterYSize #get rows
     band=ds.RasterCount #get the count of bands
     GeoTran = ds.GetGeoTransform() #get geoTransformation information
     proj=ds.GetProjection() #get projection info
     data=np.zeros([row,col,band]) #create a framework by numpy with the dimension of input raster
     for i in range(band): #write data to our framwork
         dt=ds.GetRasterBand(i+1)
         if i==0 :
              data[:,:,i]=dt.ReadAsArray(0,0,col,row)/3
         else:
              data[:,:,i]= data[:,:,i] + dt.ReadAsArray(0,0,col,row)/3
     xy = [col, row]
     return data,band,proj,xy,GeoTran #return pixels, band numbers and projection information

inputPath = r"D:\Desktop\20"
bandList = [inputPath + "\\" + band for band in os.listdir(inputPath)]
bandList.sort(reverse=False)
print(bandList)
print(len(bandList))
xy = KLReadGeotiff(bandList[0])[3] #get col and row, and save it in a list
# proj = KLReadGeotiff(bandList[0])[2] #get projection
# GeoTran = KLReadGeotiff(bandList[0])[4] #get GeoTran




driver = gdal.GetDriverByName('GTiff')  # create a writing driver according to the type you wanna export
outfile = driver.Create("D:\\Desktop\\0_g\\b_collection.tif", xy[0], xy[1], len(bandList), gdal.GDT_Float64)#specify output name, col number, row number,band number and pixeltype
# outfile.SetProjection(proj)  #set projection info
# outfile.SetGeoTransform(GeoTran) #set geoTransformation info

for idx, path in enumerate(bandList):
     outfile.GetRasterBand(idx+1).WriteArray(KLReadGeotiff(bandList[idx])[0][:,:,0])  # from numpy-array write pixel data to the framework

outfile.FlushCache() #Flush all write cached data to disk.
outfile = None #release RAM
print("end!!")
