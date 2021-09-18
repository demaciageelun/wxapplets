# 获取数据接口
from datetime import datetime

import flask, json
from flask import request
from produce import producePlan,in_Storge

'''
flask： web框架，通过flask提供的装饰器@server.route()将普通函数转换为服务
登录接口，需要传url、username、passwd
'''
# 创建一个服务，把当前这个python文件当做一个服务
server = flask.Flask(__name__)


# @server.route()可以将普通函数转变为服务 登录接口的路径、请求方式
@server.route('/yDGoods', methods=['get', 'post'])
def yDGoods():
    datas = request.get_data().decode('utf8')
    jsondata = json.loads(datas)
    proPlanInfo = producePlan.getProPlanInfo(jsondata)
    resu = {"success": "True"}
    return json.dumps(proPlanInfo, ensure_ascii=False)


@server.route('/inStorge', methods=['get', 'post'])
def inStorge():
    datas = request.get_data().decode('utf8')
    jsondata = json.loads(datas)
    print(jsondata)
    year = str(datetime.now().year)
    month = str(datetime.now().month).zfill(2)
    day = str(datetime.now().day).zfill(2)
    times = year + "-" + month + "-" + day
    folt = year + month + day
    ins = {
        "Creator": "",
        "IsEntryBatchFill": "true",
        "ValidateFlag": "true",
        "NumberSearch": "true",
        "IsAutoSubmitAndAudit": "true",
        "Model": {
            "FBillType": {  # 单据类型
                "FNUMBER": "SCRKD01_SYS"
            },
            "FDate": times,  # 日期
            "FStockOrgId": {  # 入库组织
                "FNumber": "101"
            },
            "FPrdOrgId": {  # 生产组织
                "FNumber": "101.02"
            },
            "FOwnerId0": {  # 货主
                "FNumber": "101.02"
            },
            "FEntity": [{
                "FEntryID": 0,
                "FSrcEntryId": int(jsondata["id11"]),  # 源单分录内码
                "FIsNew": "false",
                "FMaterialId": {  # 物料代码
                    "FNumber": jsondata["id2"]
                },
                "FInStockType": "1",  # 入库类型
                "FStockId": {  # 仓库
                    "FNumber": "CK022"
                },
                "FProductType": "1",
                "FUnitID": {  # 单位
                    "FNumber": "jian"
                },
                "FMustQty": float(jsondata["id7"]),  # 应收数量
                "FRealQty": float(jsondata["id8"]),  # 实收数量
                "FBaseUnitId": {  # 单位
                    "FNumber": "jian"
                },
                "FOwnerTypeId": "BD_OwnerOrg",  # 货主类型
                "FOwnerId": {  # 货主
                    "FNumber": "101.02"
                },
                "FLot": {  # 批号
                    "FNumber": folt
                },
                "FMoBillNo": jsondata["id5"],  # 生产订单编号
                "FMoId": int(jsondata["id12"]),  # 生产订单内码
                "FMoEntryId": int(jsondata["id13"]),  # 生产订单分录内码
                "FMoEntrySeq": int(jsondata["id14"]),  # 生产订单行号
                "FStockStatusId": {  # 库存状态
                    "FNumber": "KCZT01_SYS"
                },
                "FKeeperTypeId": "BD_KeeperOrg",  # 保管者类型
                "FKeeperId": {  # 保管者
                    "FNumber": "101"
                },
                "FSrcBillType": "SFC_OperationReport",  # 源单类型
                "FSrcBillNo": jsondata["id16"],  # 源单编码
                "FSrcEntrySeq": int(jsondata["id15"]),
                "FSrcInterId ": int(jsondata["id10"]),  # 源单内码
                "FEntity_Link": [{
                    "FEntity_Link_FRuleId": "SFC_OPTRPT2INSTOCK",  # 转换规则（根据bos里的标识）
                    "FEntity_Link_FSBillId": int(jsondata["id10"]),  # 工序汇报单的源单内码或者工序转移单的源单内码
                    "FEntity_Link_FSTableName": "T_SFC_OPTRPTENTRY",  # 源单（明细表）表名
                    "FEntity_Link_FSId": int(jsondata["id11"])  # 工序汇报单的分录内码或者工序转移单的分录内码
                }]
            }]
        }

    }
    print(ins)
    in_Storge.save(ins)
    # 根据前台传来的数据，调用inStorge，生产生产入库单
    resu = {"success": "True"}
    return json.dumps(resu, ensure_ascii=False)


if __name__ == '__main__':
    server.run(debug=True, port=37214, host='0.0.0.0')  # 指定端口、host,0.0.0.0代表不管几个网卡，任何ip都可以访问
