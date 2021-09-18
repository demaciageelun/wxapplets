# 根据id查询物料接口,获取物料的物料代码
import json, requests

login_url = "http://58.208.85.67/k3cloud/Kingdee.BOS.WebApi.ServicesStub.AuthService.ValidateUser.common.kdsvc"
view_url = "http://58.208.85.67/k3cloud/Kingdee.BOS.WebApi.ServicesStub.DynamicFormService.View.common.kdsvc"
login_data = {"acctid": "608d3f72088e8d", "username": "周为", "password": "372169zw..", "lcid": 2052}


def login():  # 定义登录函数
    login_response = requests.post(url=login_url, data=login_data)
    return login_response.cookies


def getPkIds(formId, data):
    # type区分根据id获取编码（number）和根据编码获取id
    data = {"FormId": formId, "Data": json.dumps(data)}
    response = requests.post(url=view_url, data=data, cookies=login())
    response_data = json.loads(response.text)
    print(response_data["Result"]["Result"]["Number"])
    return response_data["Result"]["Result"]["Number"]
