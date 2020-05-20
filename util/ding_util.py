# 丁丁机器人测试
import json
import requests


# reminders 提醒
def send_msg(url, msg):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data = {
        "msgtype": "text",
        "text": {
            "content": msg
        }
    }
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.text
