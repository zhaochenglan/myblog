import prometheus_client
from prometheus_client import Counter, Gauge
from prometheus_client.core import CollectorRegistry
from flask import Response, Flask
from functools import wraps
import time
import socket


def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


def func_time(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print(f.__name__, 'took', end - start, 'seconds')
        requests_access_total.labels(
            f.__name__, get_host_ip()).set(end - start)
        return result
    return wrapper


app = Flask(__name__)


# 定义一个仓库，存放数据
REGISTRY = CollectorRegistry(auto_describe=True)

requests_access_total = Gauge(
    "requests_access_total", "Total request error cout of the host", registry=REGISTRY, labelnames=('func_name', 'clientip'))


# 定义路由
@app.route("/metrics")
def ApiResponse():
    return Response(prometheus_client.generate_latest(REGISTRY), mimetype="text/plain")


@app.route('/')
@func_time
def index():
    time.sleep(2)
    return "Hello World"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
