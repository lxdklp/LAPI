from flask import Flask, request
import requests
import json

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
def handle_post():
    API = request.get_json()
    API = json.loads(API)

    # 处理update
    if API["update"] == "update":
        if API["project"] == "nfcBOX":
            响应 = 获取版本("nfcBOX")
        elif API["project"] == "CVM":
            响应 = 获取版本("CVM")
        else:
            响应 = "未知项目" + API

    # 未知API
    else:
        响应 = "未知POST请求" + API
    # 返回请求
    return 响应

LAPI.run()