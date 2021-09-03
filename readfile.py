import requests
import json

def start_read(name):
    global accounts,data
    with open("configs/{}".format(name)) as file:
        data = json.load(file)
    with open("accounts.txt") as file:
        accounts = file.read().splitlines()
    start()
def start():
    headers = data["request_1"]["headers"]
    send_data = data["request_1"]["data"]
    request_type = data["request_1"]["type"]
    url = data["request_1"]["url"]
    if request_type == "POST":
        requests.post(url,data=send_data,headers=headers)
    else:
        requests.get(url,data=send_data,headers=headers)
