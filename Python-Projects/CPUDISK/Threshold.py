import psutil
import time
import logging
logging.basicConfig(
    filename="threshold.log",
    encoding="utf-8",
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(message)s"
    )
cpu_threshold=50
disk_threshold=30
logging.info("CPU Threshold = 50, DISK Threshold = 30")


# print(f"{cpu} %")
# print(f"{disk.percent} %")

def alert_cpu(cpu):
    if cpu >= cpu_threshold:
        print("Alert: CPU usage exceeded threshold")
        logging.warning(f"CPU Thrreshold exceeded, Current = {cpu}, Threshold = {cpu_threshold}")
def alert_disk(disk_per):
    if disk_per >= disk_threshold:
        print("Alert: Disk usage exceeded threshold")
        logging.warning(f"Disk Thrreshold exceeded, Current = {disk_per}, Threshold = {disk_threshold}")

if __name__ == "__main__":
    # print(cpu)
    # print(disk_per)
    while True:
        cpu=psutil.cpu_percent()
        disk=psutil.disk_usage("/")
        disk_per=disk.percent
        
        if cpu >= cpu_threshold:
            print(f"CPU Threshold: {cpu_threshold}")
            print(f"CPU Percentage: {cpu}")
            alert_cpu(cpu)
        if disk_per >= disk_threshold:
            print(f"Disk Threshold: {disk_threshold}")
            print(f"Disk Percentage: {disk_per}")
            alert_disk(disk_per)
            
        time.sleep(5)
