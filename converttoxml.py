import csv
import xml.etree.cElementTree as ET

root = ET.Element("root") # set up root
doc = ET.SubElement(root, "input") # set up input

with open('OfficialDatatoConvert.csv') as csv_file: # import csv file
    csv_reader = csv.reader(csv_file, delimiter=';') # split the file using the | as a delimiter
    for row in csv_reader: # iterate through each row in the file
        blanks_removed_row = ' '.join(row).split() # remove any row in the file that is empty (I've assumed you needed this as the output didn't have blank data)
        input = ET.SubElement(doc, "item") # create an item 
        for i, item in enumerate(blanks_removed_row, start=1): # iterate through each row item and enumerate (to start counting from 1)
            ET.SubElement(input, "data{0}".format(i)).text = item # insert a new data element with the item appending the count number to the data

tree = ET.ElementTree(root) 
tree.write("filename.xml", encoding='utf-8', xml_declaration=True) # save tree