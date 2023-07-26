# -------------------------------------------------------------
# cal/calculation.py
# 计算器功能实现函数
# -------------------------------------------------------------
from io import BytesIO

import numpy as np
import pandas as pd
from django.http import HttpResponse
from django.utils.encoding import escape_uri_path


def calculate_mass(entries1, entries2, entries3, entries4, entries5, entries6, entries7, entries8, entries9, entries10,
                entries11, entries12, entries13, entries14, entries15, entries16, entries17, entries18):

    big_array = np.array(
        [entries1, entries2, entries3, entries4, entries5, entries6, entries7, entries8, entries9, entries10,
                entries11, entries12, entries13, entries14, entries15, entries16, entries17, entries18])
    # a = 原始数组
    # b = 将百分比转换成实地数据 # 这个数组考虑转成碳排放再汇总
    # c = 分物料汇成一个大总物料
    # d = b+c
    # e = B+C+大总物料各组分百分比
    # f = 计算各组分对应碳排放
    # g2 = 将各组分碳排放汇总成一股料

    # 求出燃料气组分百分比数组-质量分数
    b = [big_array[0]]

    for i in big_array[1:, ]:
        new = big_array[0] * i * 0.01
        b.append(new)

    b = np.array(b)

    c = []
    for i in b:
        c.append(np.sum(i))
    D = np.insert(b, 0, c, axis=1)

    list_percent = []
    for i in D[:, 0]:
        single_percent = i / D[:, 0][0]
        list_percent.append(single_percent)
    list_percent = np.array(list_percent)
    E = np.insert(D, 0, list_percent, axis=1)

    row_E = range(1, big_array.shape[-1] + 1)
    row_index_material = ["汇总物料百分比%", "汇总物料含量"]
    row_index_material_C = ["汇总物料碳排放"]
    row_index_material_HH = ["汇总物料高位热值"]
    row_index_material_LH = ["汇总物料低位热值"]

    for i in range(1, big_array.shape[-1] + 1):
        row_index_material.append("物料" + str(i))
        row_index_material_C.append("物料" + str(i) + "碳排放")
        row_index_material_HH.append("物料" + str(i) + "高位热值")
        row_index_material_LH.append("物料" + str(i) + "低位热值")
    row_whole = row_index_material + row_index_material_C
    # print(row_whole)
    B = np.array(b)

    column_index_material = np.array(
        ["Total", "甲烷", "乙烷", "乙烯", "乙炔", "丙烷", "丙烯", "IC4", "NC4", "丁烯", "戊烷", "戊烯", "H2", "H2O", "H2S", "N2",
         "CO", "CO2"])
    row_index_material = np.array(row_index_material)
    row_index_material_C = np.array(row_index_material_C)
    row_index_material_HH = np.array(row_index_material_HH)
    row_index_material_LH = np.array(row_index_material_LH)

    count = 0
    middle = 0
    H_heat_middle = 0
    L_heat_middle = 0
    F = []
    H_heat = []
    L_heat = []
    for i in B[1:, ]:
        count += 1
        if count == 1:  # 甲烷
            middle = i * (44 / 16)
            H_heat_middle = i * 13256  # kCal/kg
            L_heat_middle = i * 11909  # kCal/kg
        if count == 2:  # 乙烷
            middle = i * (44 / 30)
            H_heat_middle = i * 12391  # kCal/kg
            L_heat_middle = i * 11312  # kCal/kg
        if count == 3:  # 乙烯
            middle = i * (44 / 28)
            H_heat_middle = i * 12113  # kCal/kg
            L_heat_middle = i * 11341  # kCal/kg
        if count == 4:  # 乙炔
            middle = i * (44 / 26)
            H_heat_middle = i * 12014  # kCal/kg
            L_heat_middle = i * 11600  # kCal/kg
        if count == 5:  # 丙烷
            middle = i * (44 / 44)
            H_heat_middle = i * 12025  # kCal/kg
            L_heat_middle = i * 11045  # kCal/kg
        if count == 6:  # 丙烯
            middle = i * (44 / 42)
            H_heat_middle = i * 11756  # kCal/kg
            L_heat_middle = i * 10986  # kCal/kg
        if count == 7:  # IC4
            middle = i * (44 / 58)
            H_heat_middle = i * 11829  # kCal/kg
            L_heat_middle = i * 10900  # kCal/kg
        if count == 8:  # NC4
            middle = i * (44 / 58)
            H_heat_middle = i * 11829  # kCal/kg
            L_heat_middle = i * 10900  # kCal/kg
        if count == 9:  # 丁烯
            middle = i * (44 / 56)
            H_heat_middle = i * 11614  # kCal/kg
            L_heat_middle = i * 10844  # kCal/kg
        if count == 10:  # 戊烷
            middle = i * (44 / 71)
            H_heat_middle = i * 11709  # kCal/kg
            L_heat_middle = i * 10810  # kCal/kg
        if count == 11:  # 戊烯
            middle = i * (44 / 70)
            H_heat_middle = i * 11328  # kCal/kg
            L_heat_middle = i * 10556  # kCal/kg
        if count == 12:  # H2
            middle = i * 0
            H_heat_middle = i * 33942  # kCal/kg
            L_heat_middle = i * 28575  # kCal/kg
        if count == 13:  # H2O
            middle = i * 0
            H_heat_middle = i * 0  # kCal/kg
            L_heat_middle = i * 0  # kCal/kg
        if count == 14:  # H2S
            middle = i * 0
            H_heat_middle = i * 1.313 * 6054  # kCal/kg
            L_heat_middle = i * 1.313 * 5581  # kCal/kg
        if count == 15:  # N2
            middle = i * 0
            H_heat_middle = i * 0
            L_heat_middle = i * 0
        if count == 16:  # CO
            middle = i * 0
            H_heat_middle = i * 2414  # kCal/kg
            L_heat_middle = i * 2414  # kCal/kg
        if count == 17:  # CO2
            middle = i * 0
            H_heat_middle = i * 0
            L_heat_middle = i * 0
        F.append(middle)
        H_heat.append(H_heat_middle)
        L_heat.append(L_heat_middle)
    sum_H_heat_column = np.sum(np.array(H_heat), axis=1)
    sum_L_heat_column = np.sum(np.array(L_heat), axis=1)

    HMV_x = np.concatenate((sum_H_heat_column.reshape(-1, 1), np.array(H_heat)), axis=1)
    LMV_x = np.concatenate((sum_L_heat_column.reshape(-1, 1), np.array(L_heat)), axis=1)

    HMV_row = np.sum(np.array(HMV_x), axis=0)
    LMV_row = np.sum(np.array(LMV_x), axis=0)

    HMV_labelr_labelc = np.concatenate((HMV_row.reshape(1, -1), np.array(HMV_x)), axis=0)
    LMV_labelr_labelc = np.concatenate((LMV_row.reshape(1, -1), np.array(LMV_x)), axis=0)

    F = np.array(F)
    row_sums = np.sum(F, axis=1)
    G = np.concatenate((row_sums.reshape(-1, 1), F), axis=1)
    column_sums = np.sum(G, axis=0)
    G2 = np.row_stack((column_sums, G))

    H = np.concatenate((E, G2), axis=1)

    data = H
    data2 = HMV_labelr_labelc
    data3 = LMV_labelr_labelc

    data_df = pd.DataFrame(data)
    data_df.columns = [row_whole]

    data_df.index = [column_index_material]

    data_df2 = pd.DataFrame(data=data2)
    data_df2.columns = [row_index_material_HH]
    data_df2.index = [column_index_material]

    data_df3 = pd.DataFrame(data=data3)
    data_df3.columns = [row_index_material_LH]
    data_df3.index = [column_index_material]

    output = BytesIO()  # 转二进制流
    writer = pd.ExcelWriter(output, engine='openpyxl')
    data_df.to_excel(writer, "碳排放", float_format='%.2f')
    data_df2.to_excel(writer, "高热值", float_format='%.2f')
    data_df3.to_excel(writer, "低热值", float_format='%.2f')

    writer.save()
    output.seek(0)  # 重新定位到开始
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = "attachment;filename=%s" % escape_uri_path('1-MassFraction.xlsx')
    response.write(output.getvalue())
    output.close()

    return response


def calculate_volume(entries1, entries2, entries3, entries4, entries5, entries6, entries7, entries8, entries9, entries10,
                entries11, entries12, entries13, entries14, entries15, entries16, entries17, entries18):
    big_array = np.array(
        [entries1, entries2, entries3, entries4, entries5, entries6, entries7, entries8, entries9, entries10,
                entries11, entries12, entries13, entries14, entries15, entries16, entries17, entries18])
    # a = 原始数组
    # b = 将百分比转换成实地数据 # 这个数组考虑转成碳排放再汇总
    # c = 分物料汇成一个大总物料
    # d = b+c
    # e = B+C+大总物料各组分百分比
    # f = 计算各组分对应碳排放
    # g2 = 将各组分碳排放汇总成一股料

    # 求出燃料气组分百分比数组-质量分数
    b = [big_array[0]]

    for i in big_array[1:, ]:
        new = big_array[0] * i * 0.01
        b.append(new)

    b = np.array(b)

    c = []
    for i in b:
        c.append(np.sum(i))
    D = np.insert(b, 0, c, axis=1)

    list_percent = []
    for i in D[:, 0]:
        single_percent = i / D[:, 0][0]
        list_percent.append(single_percent)
    list_percent = np.array(list_percent)
    E = np.insert(D, 0, list_percent, axis=1)

    row_E = range(1, big_array.shape[-1] + 1)
    row_index_material = ["汇总物料百分比%", "汇总物料含量"]
    row_index_material_C = ["汇总物料碳排放"]
    row_index_material_HH = ["汇总物料高位热值"]
    row_index_material_LH = ["汇总物料低位热值"]

    for i in range(1, big_array.shape[-1] + 1):
        row_index_material.append("物料" + str(i))
        row_index_material_C.append("物料" + str(i) + "碳排放")
        row_index_material_HH.append("物料" + str(i) + "高位热值")
        row_index_material_LH.append("物料" + str(i) + "低位热值")
    row_whole = row_index_material + row_index_material_C
    # print(row_whole)
    B = np.array(b)

    column_index_material = np.array(
        ["Total", "甲烷", "乙烷", "乙烯", "乙炔", "丙烷", "丙烯", "IC4", "NC4", "丁烯", "戊烷", "戊烯", "H2", "H2O", "H2S", "N2",
         "CO", "CO2"])
    row_index_material = np.array(row_index_material)
    row_index_material_C = np.array(row_index_material_C)
    row_index_material_HH = np.array(row_index_material_HH)
    row_index_material_LH = np.array(row_index_material_LH)

    count = 0
    middle = 0
    H_heat_middle = 0
    L_heat_middle = 0
    F = []
    H_heat = []
    L_heat = []
    for i in B[1:, ]:
        count += 1
        if count == 1:  # 甲烷
            middle = i * (44 / 16)
            H_heat_middle = i * 13256  # kCal/kg
            L_heat_middle = i * 11909  # kCal/kg
        if count == 2:  # 乙烷
            middle = i * (44 / 30)
            H_heat_middle = i * 12391  # kCal/kg
            L_heat_middle = i * 11312  # kCal/kg
        if count == 3:  # 乙烯
            middle = i * (44 / 28)
            H_heat_middle = i * 12113  # kCal/kg
            L_heat_middle = i * 11341  # kCal/kg
        if count == 4:  # 乙炔
            middle = i * (44 / 26)
            H_heat_middle = i * 12014  # kCal/kg
            L_heat_middle = i * 11600  # kCal/kg
        if count == 5:  # 丙烷
            middle = i * (44 / 44)
            H_heat_middle = i * 12025  # kCal/kg
            L_heat_middle = i * 11045  # kCal/kg
        if count == 6:  # 丙烯
            middle = i * (44 / 42)
            H_heat_middle = i * 11756  # kCal/kg
            L_heat_middle = i * 10986  # kCal/kg
        if count == 7:  # IC4
            middle = i * (44 / 58)
            H_heat_middle = i * 11829  # kCal/kg
            L_heat_middle = i * 10900  # kCal/kg
        if count == 8:  # NC4
            middle = i * (44 / 58)
            H_heat_middle = i * 11829  # kCal/kg
            L_heat_middle = i * 10900  # kCal/kg
        if count == 9:  # 丁烯
            middle = i * (44 / 56)
            H_heat_middle = i * 11614  # kCal/kg
            L_heat_middle = i * 10844  # kCal/kg
        if count == 10:  # 戊烷
            middle = i * (44 / 71)
            H_heat_middle = i * 11709  # kCal/kg
            L_heat_middle = i * 10810  # kCal/kg
        if count == 11:  # 戊烯
            middle = i * (44 / 70)
            H_heat_middle = i * 11328  # kCal/kg
            L_heat_middle = i * 10556  # kCal/kg
        if count == 12:  # H2
            middle = i * 0
            H_heat_middle = i * 33942  # kCal/kg
            L_heat_middle = i * 28575  # kCal/kg
        if count == 13:  # H2O
            middle = i * 0
            H_heat_middle = i * 0  # kCal/kg
            L_heat_middle = i * 0  # kCal/kg
        if count == 14:  # H2S
            middle = i * 0
            H_heat_middle = i * 1.313 * 6054  # kCal/kg
            L_heat_middle = i * 1.313 * 5581  # kCal/kg
        if count == 15:  # N2
            middle = i * 0
            H_heat_middle = i * 0
            L_heat_middle = i * 0
        if count == 16:  # CO
            middle = i * 0
            H_heat_middle = i * 2414  # kCal/kg
            L_heat_middle = i * 2414  # kCal/kg
        if count == 17:  # CO2
            middle = i * 0
            H_heat_middle = i * 0
            L_heat_middle = i * 0
        F.append(middle)
        H_heat.append(H_heat_middle)
        L_heat.append(L_heat_middle)
    sum_H_heat_column = np.sum(np.array(H_heat), axis=1)
    sum_L_heat_column = np.sum(np.array(L_heat), axis=1)

    HMV_x = np.concatenate((sum_H_heat_column.reshape(-1, 1), np.array(H_heat)), axis=1)
    LMV_x = np.concatenate((sum_L_heat_column.reshape(-1, 1), np.array(L_heat)), axis=1)

    HMV_row = np.sum(np.array(HMV_x), axis=0)
    LMV_row = np.sum(np.array(LMV_x), axis=0)

    HMV_labelr_labelc = np.concatenate((HMV_row.reshape(1, -1), np.array(HMV_x)), axis=0)
    LMV_labelr_labelc = np.concatenate((LMV_row.reshape(1, -1), np.array(LMV_x)), axis=0)

    F = np.array(F)
    row_sums = np.sum(F, axis=1)
    G = np.concatenate((row_sums.reshape(-1, 1), F), axis=1)
    column_sums = np.sum(G, axis=0)
    G2 = np.row_stack((column_sums, G))

    H = np.concatenate((E, G2), axis=1)

    data = H
    data2 = HMV_labelr_labelc
    data3 = LMV_labelr_labelc

    data_df = pd.DataFrame(data)
    data_df.columns = [row_whole]

    data_df.index = [column_index_material]

    data_df2 = pd.DataFrame(data=data2)
    data_df2.columns = [row_index_material_HH]
    data_df2.index = [column_index_material]

    data_df3 = pd.DataFrame(data=data3)
    data_df3.columns = [row_index_material_LH]
    data_df3.index = [column_index_material]

    output = BytesIO()  # 转二进制流
    writer = pd.ExcelWriter(output, engine='openpyxl')
    data_df.to_excel(writer, "碳排放", float_format='%.2f')
    data_df2.to_excel(writer, "高热值", float_format='%.2f')
    data_df3.to_excel(writer, "低热值", float_format='%.2f')

    writer.save()
    output.seek(0)  # 重新定位到开始
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = "attachment;filename=%s" % escape_uri_path('2-VolumeFraction.xlsx')
    response.write(output.getvalue())
    output.close()

    return response