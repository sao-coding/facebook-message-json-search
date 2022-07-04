import json
import datetime
import time
import os

stop = False
file = []
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
        if scan <= 0:
            print('------------------------')
            print("搜尋範圍超出範圍\n請重新輸入")
            print('------------------------')
        else:
            os.system('cls')

    print("代號",view,"第"+str(keywords[view])+"則訊息的前後搜尋結果:")

    for i in range(history*2+1):

        print("第"+str(scan)+"則訊息\n"+name[scan-1],date[scan-1]+"\n\n"+chat[scan-1]+"\n")
        print('------------------------')
        scan += 1
    os.system("pause")


def choose_chat(keywords):
    try:
        print("重新搜尋請在代號輸入0")
        view = int(input("要檢視的代號?:"))
        if view != 0:
            history = int(input("要檢視前後幾則訊息?:"))
            if view in keywords:
                scan = keywords[view]-history
                print(view,history,scan)
                
            else:
                print('------------------------')
                print("沒有此代號\n請重新輸入")
                print('------------------------')
                view,history,scan = choose_chat(keywords)
        else:
            menu()
    except:
        print('------------------------')
        print("輸入錯誤\n請重新輸入")
        print('------------------------')
        choose_chat(keywords)
    return view,history,scan

def menu():
    global stop
    # os.system('cls')
    input("請按Enter鍵開始搜尋")
    os.system('cls')
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
            stop = True
        else:
            print("輸入錯誤\n請重新輸入")
            time.sleep(1)
    except:
        print("輸入錯誤\n請重新輸入")
        menu()


for files in os.listdir("./messenger"):
    if files.endswith(".json"):
        file.append(files)
file.sort(key=lambda x: int(x.split('.')[0][8:]))

for _ in file:
    with open("./messenger/"+_, encoding="utf-8") as f:
        # 讀取 JSON 檔案
        messenger = json.load(f)
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
f.close()
while stop != True:
    menu()
exit("程式結束")
