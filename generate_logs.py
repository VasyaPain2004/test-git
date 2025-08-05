import random
from datetime import datetime, timedelta

ips = [f"192.168.0.{i}" for i in range(1, 21)]
urls = ["/", "/about", "/contact", "/login", "/api/data", "/api/login", "/dashboard"]
methods = ["GET", "POST"]
statuses = [200, 200, 200, 404, 500, 403]  # с перекосом в сторону 200

now = datetime.now()

with open("access.log", "w") as f:
    for _ in range(1000):  # 1000 строк логов
        ip = random.choice(ips)
        url = random.choice(urls)
        method = random.choice(methods)
        status = random.choice(statuses)
        size = random.randint(100, 5000)
        timestamp = (now - timedelta(seconds=random.randint(0, 3600))).strftime("%d/%b/%Y:%H:%M:%S +0000")

        line = f'{ip} - - [{timestamp}] "{method} {url} HTTP/1.1" {status} {size}\n'
        f.write(line)

print("Файл access.log сгенерирован.")
