import requests

def webup(url):
    try:
        response=requests.get(url)
        stat_code=response.status_code
        if 100 <= stat_code <200:
            print("Informational")
        elif 200 <= stat_code <= 299:
            print("Success")
            print(response)
        elif 300 <= stat_code <=399:
            print("Redirection")
            print(response)
        elif 400 <= stat_code <=499:
            print("Client Error")
            print(response)
        elif stat_code >= 500:
            print("Server error")
            print(response)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        

if __name__=="__main__":
    url=input("Enter the URL:")
    webup(url)

