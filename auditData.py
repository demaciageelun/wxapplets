# 审核数据

import json, requests

login_url = "http://58.208.85.67/k3cloud/Kingdee.BOS.WebApi.ServicesStub.AuthService.ValidateUser.common.kdsvc"
audit_url = "http://58.208.85.67/k3cloud/Kingdee.BOS.WebApi.ServicesStub.DynamicFormService.Audit.common.kdsvc"
login_data = {"acctid": "608d3f72088e8d", "username": "周为", "password": "372169zw..", "lcid": 2052}


def login():  # 定义登录函数
    login_response = requests.post(url=login_url, data=login_data)
    return login_response.cookies

    # 返回cookies,方便下次访问时携带


# 获取表名和数据，写入erp
# data 格式{"Numbers": ["id"]
def auditToErp(formId, data):
    data = {"FormID": formId, "Data": json.dumps(data)}
    response = requests.post(url=audit_url, data=data, cookies=login())
    print(response.text)
