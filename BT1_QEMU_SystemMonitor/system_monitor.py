import psutil
from datetime import datetime
from time import sleep
cpu_list = psutil.cpu_percent(interval=1, percpu=True)
cpu_avg = sum(cpu_list) / len(cpu_list)
ram = psutil.virtual_memory()
ram_used_mb = ram.used // (1024 ** 2)
ram_total_mb = ram.total // (1024 ** 2)
ram_pct = ram.percent

disk = psutil.disk_usage('/')
disk_pct = disk.percent
while True:
	# ... doc CPU, RAM, DISK nhu tren ...
	now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	line = f'[{now}] CPU: {cpu_avg: .1f}% | RAM: {ram_used_mb}/{ram_total_mb} MB({ram_pct}%) | Disk: {disk_pct}%'
	print(line)
sleep(2)
