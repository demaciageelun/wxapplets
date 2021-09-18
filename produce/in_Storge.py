# 向erp中新建数据
# 第一步、获取erp采购价目表数据，并通过接口传给云之家的互联控件
# 第二步、获取云之家接口数据
# 第三步、将数据写入到erp中
# 第四步、提交审核数据

import json, requests
import submitData, auditData

login_url = "http://58.208.85.67/k3cloud/Kingdee.BOS.WebApi.ServicesStub.AuthService.ValidateUser.common.kdsvc"
save_url = "http://58.208.85.67/k3cloud/Kingdee.BOS.WebApi.ServicesStub.DynamicFormService.save.common.kdsvc"
login_data = {"acctid": "608d3f72088e8d", "username": "周为", "password": "372169zw..", "lcid": 2052}


def login():  # 定义登录函数
    login_response = requests.post(url=login_url, data=login_data)
    return login_response.cookies

    # 返回cookies,方便下次访问时携带


def save(data):
    # 获取表名和数据，写入erp
    # ins = {
    #     "Model": {
    #         "FBillType": {  # 单据类型
    #             "FNUMBER": "SCRKD01_SYS"
    #         },
    #         "FDate": "2021-08-25",  # 日期
    #         "FStockOrgId": {  # 入库组织
    #             "FNumber": "101"
    #         },
    #         "FPrdOrgId": {  # 生产组织
    #             "FNumber": "101.02"
    #         },
    #         "FOwnerId0": {  # 货主
    #             "FNumber": "101.02"
    #         },
    #         "FEntity": [{
    #             "FSrcEntryId": 450490,  # 源单分录内码
    #             "FIsNew": "true",
    #             "FMaterialId": {  # 物料代码
    #                 "FNumber": "D1205002008"
    #             },
    #             "FInStockType": "1",  # 入库类型
    #             "FUnitID": {  # 单位
    #                 "FNumber": "jian"
    #             },
    #             "FBaseUnitId": {  # 单位
    #                 "FNumber": "jian"
    #             },
    #             "FMustQty": 1,  # 应收数量
    #             "FRealQty": 1,  # 实收数量
    #             "FOwnerTypeId": "BD_OwnerOrg",  # 货主类型
    #             "FOwnerId": {  # 货主
    #                 "FNumber": "101.02"
    #             },
    #             "FStockId": {  # 仓库
    #                 "FNumber": "CK022"
    #             },
    #             "FLot": {  # 批号
    #                 "FNumber": "20210825"
    #             },
    #             "FMoBillNo": "MO005188",  # 生产订单编号
    #             "FMoId": 263236,  # 生产订单内码
    #             "FMoEntryId": 365859,  # 生产订单分录内码
    #             "FStockStatusId": {  # 库存状态
    #                 "FNumber": "KCZT01_SYS"
    #             },
    #             "FKeeperTypeId": "BD_KeeperOrg",  # 保管者类型
    #             "FKeeperId": {  # 保管者
    #                 "FNumber": "101"
    #             },
    #             "FSrcBillType": "SFC_OperationReport",  # 源单类型
    #             "FSrcBillNo": "GXHB245251",  # 源单编码
    #             "FSrcEntrySeq": 1,
    #             "FSrcInterId ": 399081,  # 源单内码
    #             "FEntity_Link": [{
    #                 "FEntity_Link_FRuleId": "SFC_OPTRPT2INSTOCK",  # 转换规则（根据bos里的标识）
    #                 "FEntity_Link_FSBillId": 399081,  # 工序汇报单的源单内码或者工序转移单的源单内码
    #                 "FEntity_Link_FSTableName": "T_SFC_OPTRPTENTRY",  # 源单（明细表）表名
    #                 "FEntity_Link_FSId": 450490  # 工序汇报单的分录内码或者工序转移单的分录内码
    #             }]
    #         }]
    #     }
    # }

    data = {"FormID": "PRD_INSTOCK", "Data": json.dumps(data)}
    response = requests.post(url=save_url, data=data, cookies=login())
    resp_data = json.loads(response.text)
    # try:
    #     fnumber = resp_data["Result"]["Number"]
    #     subdata = {"Numbers": fnumber}
    #     submitData.submitToErp("STK_OutStockApply", subdata)
    #     auditData.auditToErp("STK_OutStockApply", subdata)
    # except Exception as s:
    #     print(s)
    print(response.text)

# if __name__ == '__main__':
#     save()
