import json
import datetime
import time
import os

date = []
name = []
chat = []

# 開啟 JSON 檔案

def all_history():
    count = 0
    for i in range(len(chat)):
        count += 1
        print("第"+str(count)+"則訊息\n"+name[i],date[i]+"\n\n"+chat[i]+"\n")
        print('------------------------')
    os.system("pause")

def search_date(date_input):
    count = 0
    print("搜尋日期",date_input)
    for i in range(len(chat)):
        count += 1
        if date_input in date[i]:
            print("第"+str(count)+"則訊息\n"+name[i],date[i]+"\n\n"+chat[i]+"\n")
            print('------------------------')
    os.system("pause")

def search_chat(search):
    count = 0
    number = 0
    scan = -1
    keywords = {}
    print("搜尋訊息",search)
    for i in range(len(chat)):
        count += 1
        if search in chat[i]:
            number += 1
            keywords[number] = count
            print("代號",number,"第"+str(count)+"則訊息\n"+name[i],date[i]+"\n\n"+chat[i]+"\n")
            print('------------------------')
    print("總共搜尋到",number,"結果")
    print('------------------------')

    while scan <= 0:
        view,history,scan = choose_chat(keywords)
    #     if view in keywords:
    #         scan = keywords[view]-history
    #     else:
    #         print('------------------------')
    #         print("沒有此代號\n請重新輸入")
    #         print('------------------------')
    #         view,history = choose_chat()
        if scan <= 0:
            print('------------------------')
            print("搜尋範圍超出範圍\n請重新輸入")
            print('------------------------')
        else:
            os.system('clear')

    print("代號",view,"第"+str(keywords[view])+"則訊息的前後搜尋結果:")
    # print(keywords)
    for i in range(history*2+1):

        print("第"+str(scan)+"則訊息\n"+name[scan-1],date[scan-1]+"\n\n"+chat[scan-1]+"\n")
        print('------------------------')
        scan += 1
    os.system("pause")

def choose_chat(keywords):
    try:
        view = int(input("要檢視的代號?:"))
        history = int(input("要檢視前後幾則訊息?:"))
        if view in keywords:
            scan = keywords[view]-history
        else:
            print('------------------------')
            print("沒有此代號\n請重新輸入")
            print('------------------------')
            view,history,scan = choose_chat(keywords)
    except:
        print("輸入錯誤\n請重新輸入")
        view,history,scan = choose_chat(keywords)
    return view,history,scan

for _ in range(1,11):
    with open("./messenger/message_"+str(_)+".json", encoding="utf-8") as f:

        # 讀取 JSON 檔案
        messenger = json.load(f)
        # .encode('latin1').decode('utf8')

        for item in messenger["messages"]:
            try:
                date.append(str(datetime.datetime.fromtimestamp(item["timestamp_ms"]/1000,datetime.timezone(datetime.timedelta(hours=8))))[:19])
                name.append(item["sender_name"].encode('latin1').decode('utf8'))
                chat.append(item["content"].encode('latin1').decode('utf8'))
            except:
                chat.append("已收回")
date.reverse()
name.reverse()
chat.reverse()

while True:
    os.system('clear')
    input("請按Enter鍵開始搜尋")
    os.system('clear')
    try:
        print("輸入完請按Enter鍵繼續")
        # 1. 顯示完整聊天紀錄 2. 顯示某一天的聊天紀錄 3. 搜尋關鍵字訊息 4. 離開程式
        mode = int(input("1. 顯示完整聊天紀錄\n2. 顯示某一天的聊天紀錄\n3. 搜尋關鍵字訊息\n4. 離開程式\n"))

        if mode == 1:
            all_history()
        elif mode == 2:
            date_input = input("輸入想查詢的日期(格式:YYYY-MM-DD):")
            search_date(date_input)

        elif mode == 3:
            search = input("輸入想搜尋的關鍵字:")
            print()
            print('------------------------')
            search_chat(search)
        elif mode == 4:
            print("程式結束")
            os.system("pause")
            exit()
        else:
            print("輸入錯誤\n請重新輸入")
            time.sleep(1)
    except:
        print("輸入錯誤\n請重新輸入")
        continue
