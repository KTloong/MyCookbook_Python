from osgeo import gdal
import os

#Input and output paths
#inputPath = '../Images/'
inputPath = "D:\\Desktop\\envi配准最终版"
outputPath = "D:\\Desktop\\envi最终配准后裁剪"

#Input Raster and Vector Paths
bandList = [band for band in os.listdir(inputPath) if band[-4:]=='.tif']
print(bandList)

#Shapefile of Area of Influence
shp_clip = "D:\\Desktop\\扩大后的SHP(包括楼后排球场)\\01_扩到楼后排球场.shp"

for band in bandList:
    print(outputPath + "\\"+band[:-4]+'_trim'+band[-4:])
    options = gdal.WarpOptions(cutlineDSName=shp_clip,cropToCutline=True)
    outBand = gdal.Warp(srcDSOrSrcDSTab=inputPath +"\\"+band,
                        destNameOrDestDS=outputPath +"\\" + band[:-4]+'_c2'+band[-4:],
                        options=options)
    outBand = None

print("Misson accomplished!")