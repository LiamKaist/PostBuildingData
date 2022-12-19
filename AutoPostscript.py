import requests
import time

url='https://gs1buildingsource.herokuapp.com/insert/' #different from java where editor= has to be in the string I think


with open("BuildingData.txt",'r') as f:
    fileline=f.readline()
    while fileline != "":
        xml=""
        fileline=f.readline()
        if "<row>" in fileline:
            fileline=f.readline()
            while "</row>" not in fileline:
                xml=xml+fileline
                fileline=f.readline()
                
            
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            r = requests.post(url, 
                data={"editor": xml},
            )
            
            
        
    




print(r.text)


