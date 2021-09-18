# 查询表单数据

import json
import requests

login_url = "http://58.208.85.67/k3cloud/Kingdee.BOS.WebApi.ServicesStub.AuthService.ValidateUser.common.kdsvc"
query_url = "http://58.208.85.67/k3cloud/Kingdee.BOS.WebApi.ServicesStub.DynamicFormService.ExecuteBillQuery.common.kdsvc"
login_data = {"acctid": "608d3f72088e8d", "username": "周为", "password": "372169zw..", "lcid": 2052}


def login():  # 定义登录函数
    login_response = requests.post(url=login_url, data=login_data)
    return login_response.cookies


def getdata(obj, fks, filters, limit, sr):
    # 返回cookies,方便下次访问时携带
    post_data = {"data": json.dumps({"FormId": obj,
                                     "FieldKeys": fks,
                                     "FilterString": filters,
                                     "Limit": limit,
                                     "StartRow": sr})}
    response = requests.post(url=query_url, data=post_data, cookies=login())
    resp_data = json.loads(response.text)
    # print(resp_data)
    return resp_data
