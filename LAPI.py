from flask import Flask, request
import requests
import json
import platform
import subprocess
import psutil

version = "DEV"

# 调用Flask框架
LAPI = Flask(__name__)

# 从GitHub release获取最新版本
def 获取版本(库名):
    url = f"https://api.github.com/repos/lxdklp/{库名}/releases/latest"
    响应 = requests.get(url)
    if 响应.status_code == 200:
        版本信息 = 响应.json()
        最新版本 = 版本信息.get("tag_name")
        return 最新版本
    else:
        return None


# 处理GET请求
@LAPI.route('/', methods=["GET"])
def handle_get():
    API = request.args.get("API")

    # 处理info
    if API == "info":
        响应 = "LAPI" + version

    # 处理website
    if API == "website":
        响应 = "lxdklp.top"

    # 处理github
    if API == "github":
        响应 = "github.com/lxdklp"

    # 未知API
    else:
        响应 = "未知GET请求" + API

    # 返回请求
    return 响应

# 处理POST请求
@LAPI.route('/', methods=['POST'])
def POST():
    API = request.get_json()
    # 返回请求
    return "API POST"

# 处理update
@LAPI.route('/update', methods=['POST'])
def update():
    API = request.get_json()
    # 处理update
    if API["update"] == "nfcBOX":
        响应 = 获取版本("nfcBOX")
    elif API["update"] == "CVM":
        响应 = 获取版本("CVM")
    else:
        响应 = "n"
    # 返回请求
    return 响应

# 处理systemInfo
@LAPI.route('/systemInfo', methods=['POST'])
def systemInfo():
    API = request.get_json()
    # 系统信息
    if API["systemInfo"] == "OSname":
        响应 = platform.system()
    elif API["systemInfo"] == "OSVersion":
        响应 = platform.release()
    # CPU信息
    elif API["systemInfo"] == "CPU":
        响应 = subprocess.getoutput("cat /proc/cpuinfo")
    elif API["systemInfo"] == "CPUusage":
        响应 = psutil.cpu_percent(interval=1)
    # 内存信息
    elif API["systemInfo"] == "MEMtotal":
        内存信息 = psutil.virtual_memory()
        响应 = 内存信息.total // (1024**2)
    elif API["systemInfo"] == "MEMused":
        内存信息 = psutil.virtual_memory()
        响应 = 内存信息.used // (1024**2)
    elif API["systemInfo"] == "MEMpercent":
        内存信息 = psutil.virtual_memory()
        响应 = 内存信息.percent // (1024**2)
    # 硬盘信息
    elif API["systemInfo"] == "DISKtotal":
        硬盘信息 = psutil.disk_usage('/')
        响应 = 硬盘信息.total // (1024**3)
    elif API["systemInfo"] == "DISKused":
        硬盘信息 = psutil.disk_usage('/')
        响应 = 硬盘信息.used
    # 网络信息
    elif API["systemInfo"] == "CPU":
        响应 = subprocess.getoutput("cat /proc/cpuinfo")
    # 未知API
    else:
        响应 = "未知POST请求" + API
    # 返回请求
    return 响应

LAPI.run()