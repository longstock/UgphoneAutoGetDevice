import requests
from colorama import init, Fore, Back, Style
import json

ascii = r"""                              /$$                         /$$
                            | $$                        | $$
 /$$   /$$  /$$$$$$        /$$$$$$    /$$$$$$   /$$$$$$ | $$
| $$  | $$ /$$__  $$      |_  $$_/   /$$__  $$ /$$__  $$| $$
| $$  | $$| $$  \ $$        | $$    | $$  \ $$| $$  \ $$| $$
| $$  | $$| $$  | $$        | $$ /$$| $$  | $$| $$  | $$| $$
|  $$$$$$/|  $$$$$$$        |  $$$$/|  $$$$$$/|  $$$$$$/| $$
 \______/  \____  $$         \___/   \______/  \______/ |__/
           /$$  \ $$                                        
          |  $$$$$$/                                        
           \______/                                         """


print(ascii)

print('Created by withstock / github.com/longstock')


localstorage_input = input(Fore.YELLOW + "Enter your ugphone local storage: ")
localstorage = json.loads(localstorage_input)
accesstoken = localstorage["UGPHONE-Token"]
loginind = localstorage["UGPHONE-ID"]







print(Fore.BLUE + "💎 Getting gems")




headers = {
    'accept': 'application/json, text/plain, /',
    'accept-language': 'en-US,en;q=0.9',
    'access-token': accesstoken,
    'content-type': 'application/json;charset=UTF-8',
    'lang': 'en',
    'login-id': loginind,
    'origin': 'https://www.ugphone.com/',
    'priority': 'u=1, i',
    'referer': 'https://www.ugphone.com/toc-portal/',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'terminal': 'web',
    #'update-date': '20250218',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
    
    
}

json_data = {}

response = requests.post('https://www.ugphone.com/api/apiv1/fee/newPackage', headers=headers, json=json_data)
print(Fore.BLUE + "💎 Get gems successful")

cf_response = requests.get('https://www.ugphone.com/api/apiv1/info/configList2', headers=headers)
cf_data = cf_response.json()




uvip_config_id = None

for item in cf_data["data"]["list"]:
    if item["config_name"] == "UVIP":
        uvip_config_id = item["android_version"][0]["config_id"]
        break



json_data = {
    'config_id': uvip_config_id,
}

network_id = requests.post('https://www.ugphone.com/api/apiv1/info/mealList', headers=headers, json=json_data)

network_dat = network_id.json()
network_id = network_dat["data"]["list"]["subscription"][0]["network_id"]



json_data = {
    'order_type': 'newpay',
    'period_time': '4',
    'unit': 'hour',
    'resource_type': 'cloudphone',
    'resource_param': {
        'pay_mode': 'subscription',
        'config_id': uvip_config_id,
        'network_id': network_id,
        'count': 1,
        'use_points': 3,
        'points': 250,
    },
}

getammount = requests.post(
    'https://www.ugphone.com/api/apiv1/fee/queryResourcePrice',
    
    headers=headers,
    
    json=json_data,
)

am_json = getammount.json()

amount_id = am_json["data"]["amount_id"]
print(Fore.GREEN + f"✅ Get amount id: {amount_id}")


json_data = {
    'amount_id': amount_id,
    'pay_channel': 'free',
}

order_response = requests.post('https://www.ugphone.com/api/apiv1/fee/payment',  headers=headers, json=json_data)
order_mes = order_response.json()
orid = order_mes["data"]["order_id"]
print(Fore.GREEN + f"✅ Ordered successful, Order ID: {orid}")
exit()
