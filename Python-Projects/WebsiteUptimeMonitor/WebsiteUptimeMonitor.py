import requests
from concurrent.futures import ThreadPoolExecutor

def webup(url):
    try:
        response=requests.get(url, timeout=5)
        stat_code=response.status_code
        resp_time=response.elapsed.total_seconds() * 1000
        if 100 <= stat_code <200:
            status="INFO"
            # print(f"URL: {url}")
            # print("Status: INFO")
            # print(f"Response Time: {resp_time:.2f} ms")
        elif 200 <= stat_code <= 299:
            status="HEALTHY"
            # print(f"URL: {url}")
            # print("Status: HEALTHY")
            # print(f"Status Code: {stat_code}")
            # print(f"Response Time: {resp_time:.2f} ms")
        elif 300 <= stat_code <=399:
            status="HEALTHY(redirect)"
            # print(f"URL: {url}")
            # print("Status: HEALTHY(redirect)")
            # print(f"Status Code: {stat_code}")
            # print(f"Response Time: {resp_time:.2f} ms")
        elif 400 <= stat_code <=499:
            status="UNHEALTHY"
            # print(f"URL: {url}")
            # print("Status: UNHEALTHY")
            # print(f"Status Code: {stat_code}")
            # print(f"Response Time: {resp_time:.2f} ms")
        elif stat_code >= 500:
            status="DOWN"
            # print(f"URL: {url}")
            # print("Status: DOWN")
            # print(f"Status Code: {stat_code}")
            # print(f"Response Time: {resp_time:.2f} ms")
        
        print(
            f"URL: {url}\n"
            f"STATUS: {status}\n"
            f"STATUS CODE: {stat_code}\n"
            f"RESPONSE TIME: {resp_time:.2f} ms"
        )
    except requests.exceptions.RequestException as e:
        print(f"URL:{url}")
        print(type(e).__name__)
        

if __name__=="__main__":
    url=input("Enter the URL(seperated by comma):")
    arr=[item.strip() for item in url.split(',')]
    
    with ThreadPoolExecutor() as executor:
        executor.map(webup,arr)



