import requests
import json

def getmet():
        r=requests.get("http://localhost:5000/metrics")
        return r.json()

def status():
        data=getmet()
        print("System Status")
        print("=============")
        print(f"CPU     :{data['CPU']}%")
        print(f"DISK    :{data['DISK']}%")
        print(f"MEMORY  :{data['MEMORY']}%")
status()