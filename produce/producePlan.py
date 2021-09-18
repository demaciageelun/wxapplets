# 1、工序计划查询，看当前工序是否为委外
# 2.1、如果是委外，查询委外转移单的信息（根据转入工序计划号和转入工序号查询）
# 2.2、如果不是委外，查询工序汇报单的信息
import searchdata, interface


# 判断当前工序是否为委外
def getProPlanInfo(data):
    fBillNo = data['Content']
    fOperNumber = data['GXH']
    filterProPlan = "FBillNo = '" + fBillNo + "' and fOperNumber = '" + fOperNumber + "'"
    isOutSrc = searchdata.getdata("SFC_OperationPlanning", "FIsOutSrc", filterProPlan, 2000, 0)
    print(isOutSrc)
    try:
        isOutSrcs = isOutSrc[0][0]
        if isOutSrcs == True:
            return getOperaTrans(fBillNo, fOperNumber)
        else:
            return getOperaReport(fBillNo, fOperNumber)
    except Exception as e:
        print(e)


# 是委外，查询工序转移单
def getOperaTrans(fFInOPBillNo, fInOperNumber):
    filterOperaTrans = "FInOPBillNo = '" + fFInOPBillNo + "' and FInOperNumber = '" + fInOperNumber + "' and FOperQualifiedQty - FQuaInStockQty > 0"
    operaTransInfo = searchdata.getdata("SFC_OperationTransfer",
                                        "FProductId,FProductName,FProSpecification,FMOBillNo,FBillNo,FOperQualifiedQty,FQuaInStockQty,FID",
                                        filterOperaTrans, 2000, 0)
    try:
        final_data = {}
        final_data["type"] = "委外"
        final_data["materId"] = interface.getPkIds("BD_MATERIAL", {"CreateOrgId": 1382935, "Id": operaTransInfo[0][0]})
        final_data["materName"] = operaTransInfo[0][1]
        final_data["materMode"] = operaTransInfo[0][2]
        final_data["produId"] = operaTransInfo[0][3]
        final_data["data"] = []
        i = 0
        for dt in operaTransInfo:
            array_data = {}
            array_data["id"] = i
            array_data["fBillNo"] = dt[4]
            array_data["fNumber"] = dt[5] - dt[6]
            i = i + 1
        final_data["data"].append(array_data)
        print(final_data)
        return final_data
    except Exception as e:
        final_data = {}
        final_data["success"] = False
        return final_data
        print(e)


# 不是委外，查询工序汇报单
def getOperaReport(fOptPlanNo, fOperNumber):
    filterOperaReport = "FOptPlanNo = '" + fOptPlanNo + "' and FOperNumber = '" + fOperNumber + "' and FQuaQty - FStockInQuaAuxQty >0"
    operaReportInfo = searchdata.getdata("SFC_OperationReport",
                                         "FMaterialId,FMaterialName,FSpecification,FMoNumber,FBillNo,FQuaQty,FStockInQuaAuxQty,FID,FEntity_FENTRYID,FMoId,FMoEntryId,FMoRowNumber,FSrcEntrySeq",
                                         filterOperaReport, 2000, 0)
    try:
        print(operaReportInfo)
        final_data = {}
        final_data["success"] = True
        final_data["type"] = "工序汇报"
        final_data["materId"] = interface.getPkIds("BD_MATERIAL", {"CreateOrgId": 1382935, "Id": operaReportInfo[0][0]})
        final_data["materName"] = operaReportInfo[0][1]
        final_data["materMode"] = operaReportInfo[0][2]
        final_data["produId"] = operaReportInfo[0][3]
        final_data["data"] = []
        i = 0
        for dt in operaReportInfo:
            array_data = {}
            array_data["id"] = i
            array_data["fBillNo"] = dt[4]
            array_data["fNumber"] = dt[5] - dt[6]
            array_data["fid"] = dt[7]  # 工序汇报内码
            array_data["fsid"] = dt[8]  # 工序汇报明细行内码
            array_data["fmoid"] = dt[9]  # 生产订单内码
            array_data["fsmoid"] = dt[10]  # 生产订单明细行内码
            array_data["morownumber"] = dt[11]  # 生产订单行号
            array_data["frownumber"] = dt[12]  # 工序汇报行号

            i = i + 1
        final_data["data"].append(array_data)
        print(final_data)
        return final_data
    except Exception as e:
        final_data = {}
        final_data["success"] = False
        return final_data
        print(e)
