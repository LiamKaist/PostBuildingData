import requests
import xml.etree.ElementTree as et

url='https://gs1buildingsource.herokuapp.com/insert/' #different from java where editor= has to be in the string I think

xml="""<product_data:productData xmlns:product_data="urn:gs1:tsd:product_data:xsd:1" xmlns:room_module="urn:gs1:tsd:room_module:xsd:1" xmlns:building_services_module="urn:gs1:tsd:building_services_module:xsd:1">
    <serializedGLN>880002690101302003353226161z</serializedGLN>
    <buildingName languageCode='en' >Dept. of Industrial Design B/D</buildingName>
    <buildingCode languageCode='en' >N25</buildingCode>
    <longitude>127.3622123</longitude>
    <latitude>36.37385223</latitude>
    <buildingRecord>
        <buildingDescription languageCode="en">Description</buildingDescription>
        <module></module>
    </buildingRecord>
</product_data:productData>"""

print(xml)

headers = {'Content-Type': 'application/x-www-form-urlencoded'}

r = requests.post(url, 
    data={"editor": xml},
)

print(r.text)


