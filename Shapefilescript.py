import shapefile
import matplotlib.pyplot as plt
import ctypes

shape= shapefile.Reader("Kaist_shp.shp")
#first feature of the Shapefile

for k in range(len(shape.shapeRecords())-1):

    feature = shape.shapeRecords()[k]
    
    print(feature.shape.shapeType)
    if feature.shape.shapeType==5:

        first=feature.shape.__geo_interface__

    #print(first) #(GeoJSON format)
    #print(first['type'])  #To access the data in dict , use the keys as an index and don't forget apostrophes for str keys
    #print(first['coordinates'])

    #print(first['coordinates'][0][1]) #Gets the second point 

    
    for i in range(len(first['coordinates'][0])-1):
        x_val=[first['coordinates'][0][i][0],first['coordinates'][0][i+1][0]]
        y_val=[first['coordinates'][0][i][1],first['coordinates'][0][i+1][1]]
        plt.plot(x_val,y_val)

plt.show()