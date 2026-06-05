import requests

url=input("Enter the URL:")
response=requests.get(url)
print(response)
print(response.status_code)