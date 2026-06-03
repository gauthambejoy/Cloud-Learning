import subprocess
from concurrent.futures import ThreadPoolExecutor

def ping(host):
    result = subprocess.run(["ping", "-c", "1", host], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"{host} is UP")
    elif result.returncode == 1:
        print(f"{host} is DOWN (unreachable)")
    else:
        print(f"{host} is INVALID (invalid host or ping failed)")
        
if __name__=='__main__':
    n = int(input("Enter the number of hosts:"))
    
    hosts=[]

    for i in range(n):
        host=input("Enter the hostname:")
        hosts.append(host)
    
    with ThreadPoolExecutor() as executor:
        executor.map(ping, hosts)