import json
import datetime
count = 0
sum = 0
date = []
name = []
chat = []
search = input("輸入想搜尋的關鍵字:")
print()
# 開啟 JSON 檔案
for _ in range(1,11):
    with open("/home/coder/project/messenger/message_"+str(_)+".json") as f:

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
chat.reverse()
for z in range(len(chat)):
    count += 1
    if search in chat[z]:
        sum += 1
        print("代號",sum,"第"+str(count)+"則訊息\n"+name[z],date[z]+"\n\n"+chat[z]+"\n")
        print('------------------------')
print("總共搜尋到",sum,"結果")

view = int(input("要檢視的代號?:"))
history = int(input("要檢視前後幾則訊息"))
