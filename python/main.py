# encoding:utf-8

import requests
from funcs import get_authinfo
from funcs import get_v
from funcs import get_phpid
from funcs import exe_startup
from funcs import test_conn
from funcs import test_stren
from funcs import appendix
from funcs import wifi_connect
from funcs import get_userinfo
import time 
import os
import webbrowser

os.system("")
end_color = "\033[0;0m"
# 黑配绿高亮输出带下划线
begin_color1 = "\033[1;31;40m"
# 红配黄高亮输出
begin_color2 = "\033[1;33;40m"
# 红配白闪烁输出
begin_color3 = "\033[1;36;40m"
# 紫配白闪烁输出
begin_color4 = "\033[1;37;40m"

outset = r'''██╗    ██╗      ██████╗ ██╗   ██╗███████╗    ██╗  ██╗███████╗██╗   ██╗████████╗
██║    ██║     ██╔═══██╗██║   ██║██╔════╝    ██║  ██║██╔════╝██║   ██║╚══██╔══╝
██║    ██║     ██║   ██║██║   ██║█████╗      ███████║█████╗  ██║   ██║   ██║   
██║    ██║     ██║   ██║╚██╗ ██╔╝██╔══╝      ██╔══██║██╔══╝  ██║   ██║   ██║   
██║    ███████╗╚██████╔╝ ╚████╔╝ ███████╗    ██║  ██║██║     ╚██████╔╝   ██║   
╚═╝    ╚══════╝ ╚═════╝   ╚═══╝  ╚══════╝    ╚═╝  ╚═╝╚═╝      ╚═════╝    ╚═╝   '''
print("\033[2;32;40m" + outset + "\n\033[0;0m")
outset = r'''     _           _    _                      _      _       _               
    / \   _   _ | |_ | |__    ___   _ __  _ | |    (_) ____(_) _   _  _   _ 
   / _ \ | | | || __|| '_ \  / _ \ | '__|(_)| |    | ||_  /| || | | || | | |
  / ___ \| |_| || |_ | | | || (_) || |    _ | |___ | | / / | || |_| || |_| |
 /_/   \_\\__,_| \__||_| |_| \___/ |_|   (_)|_____||_|/___||_| \__, | \__, |
                                                               |___/  |___/ '''
print("\033[1;35;40m" + outset + "\n\033[0;0m")
print(begin_color1 + "                     HWA - 让校园网像自家WiFi一样用的舒心                   \n" + end_color)

output = wifi_connect()
time.sleep(1)
# print(output)
if output == "ok":
    output = test_conn()
    time.sleep(1)
    # print(output)
    if output == "exit":
        print(begin_color4 + "                               检测到已联网成功!                            " + end_color)
    else:
        info = get_userinfo()
        account = info["account"]
        password = info["password"]
        v = get_v()
        phpsessid = get_phpid()
        cookies = {"PHPSESSID":phpsessid}
        info = get_authinfo()
        ip = info["ip"]
        switchip = info["switchip"]
        mac = info["mac"]
        mac = mac.replace(":","")
        url = "http://xxx.xx.xxx.xxx:xxx/eportal/"

        params = {
            "c": "Portal",
            "a": "login",
            "callback": "dr1003",
            "login_method": "8",
            "user_account": account,
            "user_password": password,
            "wlan_user_ip": ip,
            "wlan_user_mac": mac,
            "wlan_ac_ip": switchip,
            "jsVersion": "3.3.2",
            "v": v
        }
        headers = {
            "Host": "xxx.xx.xxx.xxx:xxx",
            "Connection": "keep-alive",
            "Referer": "http://xxx.xx.xxx.xxx/",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Accept-Encoding": "gzip, deflate"
        }
        session = requests.Session()
        # print(params)
        response = session.get(url=url,headers=headers,cookies=cookies,params=params)

        # RSA解密正常
        # print(account)
        # print(password)
        sign = str(response.text)
        if "1" in sign:
            print(begin_color1 + "\n                     登录成功, 可以开始愉快的网上冲浪了！                \n" + end_color)

while True:
    confirm = appendix()
    if confirm == "1":
        confirmt = input(begin_color4 + "请确认是否需要开机自启自动连接 HFUT-WiFi \n是(1)/否(回车)\n" + end_color)
        if confirmt == "1":
            exe_startup()
            print(begin_color2 + "为实现开机自动认证, 已修改注册表 SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run 的键值, 新增一项 HFUT-wlan-autocheckin\n\n" + end_color)
        else: continue
    else:
        if confirm == "2":
            out = test_conn()
            if out == "ok": 
                print(begin_color3 + "联网失败, 请将问题反馈给开发者" + end_color)
                webbrowser.open("https://github.com/liziyy/HFUT-WLAN-Autocheckin/issues")
            else: print(begin_color4 + "联网成功！" + end_color)
            time.sleep(5)
            confirm = appendix()
        elif confirm == "3":
            webbrowser.open("https://www.speedtest.cn/")
            time.sleep(5)
            confirm = appendix()
        elif confirm == "4":
            test_stren()
            time.sleep(5)
            confirm = appendix()
        elif confirm == "5":
            webbrowser.open("https://github.com/liziyy/HFUT-WLAN-Autocheckin")
            time.sleep(5)
            confirm = appendix()
        elif confirm == "6":
            print(begin_color4 + "还在开发, 别着急" + end_color)
            time.sleep(5)
            confirm = appendix()
        elif confirm == "7":
            print(begin_color4 + "\n欢迎反馈任何有关问题和提出相关建议.\n" + end_color)
            webbrowser.open("https://github.com/liziyy/HFUT-WLAN-Autocheckin/issues")
            time.sleep(5)
            confirm = appendix()
        else:
            exit()
exit()