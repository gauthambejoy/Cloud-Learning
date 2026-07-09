import psutil

def monitor():
    cpu=psutil.cpu_percent(interval=1)
    disk=psutil.disk_usage("/")
    memory=psutil.virtual_memory()
    
    return({
        "CPU": cpu,
        "DISK": disk.percent,
        "MEMORY": memory.percent
    })
