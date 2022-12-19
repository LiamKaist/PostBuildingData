import csv

xmlFile = 'myDataPolygon.xml'


xmlData = open(xmlFile, 'w')
xmlData.write('<?xml version="1.0"?>' + "\n")
# there must be only one top-level tag
xmlData.write('<csv_data>' + "\n")



import shapefile
import matplotlib.pyplot as plt
import ctypes

shape= shapefile.Reader("Kaist_shp.shp")
#first feature of the Shapefile

for k in range(len(shape.shapeRecords())-1):

    feature = shape.shapeRecords()[k]
    if feature.shape.shapeType==5:

        first=feature.shape.__geo_interface__

    xmlData.write('<row>' + "\n")
    for i in range(len(first['coordinates'][0])-1):
        xmlData.write('<point number=' + str(i) + '>' + "\n")
        xmlData.write('    ' + '<CartesianPoint>' + str(first['coordinates'][0][i][0]) + '</CartesianPoint>'+ "\n")
        xmlData.write('    ' + '<CartesianPoint>' + str(first['coordinates'][0][i][1]) + '</CartesianPoint>' + "\n")
        xmlData.write('</point>'+"\n")
    xmlData.write('</row>' + "\n")  

    
    
xmlData.write('</csv_data>' + "\n")
xmlData.close()


