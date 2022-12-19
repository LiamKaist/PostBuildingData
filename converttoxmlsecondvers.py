import csv

csvFile = 'OfficialDatatoConvert.csv'
xmlFile = 'myData.xml'

csvData = csv.reader(open(csvFile), delimiter=';')
xmlData = open(xmlFile, 'w')
xmlData.write('<?xml version="1.0"?>' + "\n")
# there must be only one top-level tag
xmlData.write('<csv_data>' + "\n")

rowNum = 0
for row in csvData:
    if rowNum == 0:
        tags = row
        # replace spaces w/ underscores in tag names
        for i in range(len(tags)):
            tags[i] = tags[i].replace(' ', '_')
    else: 
        xmlData.write('<row>' + "\n")
        xmlData.write('<product_data:productData xmlns:product_data="urn:gs1:tsd:product_data:xsd:1" xmlns:room_module="urn:gs1:tsd:room_module:xsd:1" xmlns:building_services_module="urn:gs1:tsd:building_services_module:xsd:1">'+"\n")
        for i in range(len(tags)):
            if tags[i]=='buildingName' or tags[i]=='buildingCode':
                xmlData.write('    ' + '<' + tags[i] + " languageCode='en' >" \
                            + row[i] + '</' + tags[i] + '>' + "\n")
            else:
                xmlData.write('    ' + '<' + tags[i] + '>' \
                            + row[i] + '</' + tags[i] + '>' + "\n")

        xmlData.write('    ' +'<buildingRecord>' + "\n")
        xmlData.write('    ' + '    ' +'<buildingDescription languageCode="en">Description</buildingDescription>' + "\n")
        xmlData.write('    ' + '    ' + '<module></module>' + "\n")
        xmlData.write('    ' +'</buildingRecord>' + "\n")
        xmlData.write('</product_data:productData>' + "\n")
        
   


            
        xmlData.write('</row>' + "\n")
            
    rowNum +=1

xmlData.write('</csv_data>' + "\n")
xmlData.close()