import requests

def getdata():
        r=requests.get("http://localhost:5000/metrics")
        return r.json()
def checkapi():
        try:
                requests.get("http://localhost:5000/status")
                return "Running"
        except requests.exceptions.ConnectionError:
                return "Not running"

def getstat():
        info=requests.get("http://localhost:5000/status")
        return info.json()
def status():
        api=checkapi()
        print("=============")
        print("System Status")
        print("=============")
        if api=="Not running":
                print(f"APi     :{api}")
                return
        else:
                print(f"APi     :{api}")
                stat=getstat()
                if stat["REDIS"]=="Not Connected":
                        print(f"REDIS   :{stat['REDIS']}")
                        print("=============")
                        print("Connection Failed")
                else:
                        data=getdata()
                        print(f"REDIS   :{stat['REDIS']}")
                        print("=============")
                        print(f"CPU     :{data['CPU']}%")
                        print(f"DISK    :{data['DISK']}%")
                        print(f"MEMORY  :{data['MEMORY']}%")
status()