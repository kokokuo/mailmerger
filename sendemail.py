#!/usr/bin/python
# -*- coding: utf-8 -*-
import io
import os
from apps.mailagent import MailAgent
import smtplib
import pandas as pd


"""
信件排版可以用 http://htmlformatter.com/
不建議使用 https://codebeautify.org/htmlviewer/ 會跑版
"""


def parse_excel(filepath):
    # sheet_name = raw_input("請輸入要讀取的 Sheet >> ").strip().decode("utf8")

    sheet_name = "sheet1"
    print("您要讀取的為 {} 試算表".format(sheet_name))
    excel = pd.ExcelFile(filepath)

    if sheet_name not in excel.sheet_names:
        raise Exception("不存在此試算表...")

    # 建立寄送信件的類別
    agent = MailAgent("email_naomi_tpe.html")

    sheet_df = excel.parse(sheet_name)
    # 顯示指定的 column 的所有資料
    # 要找出的 key 值
    df_name_email_rows = sheet_df[["hotel_name", "email"]]
    num = 1
    for tup in df_name_email_rows.itertuples():
        # tup[0] 為 dataframe 索引
        print("編號: " + str(num))
        print("準備寄送的資料是: ", tup[1], tup[2])
        print("過濾掉地址...")
        if "(" in tup[1]:
            clean_data = tup[1][:tup[1].index("(")]
        else:
            clean_data = tup[1]
        print(clean_data)
        row = {
            "hotel_name": clean_data,
            "email": tup[2],
        }
        if num > 21:
            break
        else:
            num += 1
        agent.send_mapped_data_email(row)


def main():
    # fifilepath = u"臺南市所有旅宿統計資料(new).xlsx"lepath = raw_input("請輸入檔案的路徑名稱 >> ").strip()
    filepath = "app/Naomi台北表單.xlsx"
    if os.path.isfile(filepath):
        print("檔案存在，開始讀取...")
        parse_excel(filepath)
    else:
        print("不存在該檔案名稱...")


if __name__ == "__main__":
    main()
