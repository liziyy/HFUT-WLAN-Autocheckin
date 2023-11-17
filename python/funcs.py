# encoding:utf-8

import requests
import random
from urllib.parse import urlparse, parse_qs
import winreg
import os
import sys
import pywifi
from pywifi import const
import time
import subprocess
import msvcrt
import hashlib
import rsa
from bs4 import BeautifulSoup as bs

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

def get_userinfo():
    user_dir = os.path.expanduser("~")
    path_root = user_dir + "\\AppData\\Local\\HFUT-wlan-autocheckin\\"

    if os.path.exists(path=path_root):
        print(begin_color1 + "\n                     HFUT - WLAN - Autocheckin 程序启动                  \n" + end_color)

    else:
        print(begin_color1 + "检测到第一次启动程序. \n\n已自动创建 " + path_root + "文件夹. \n\n" + end_color + begin_color2 + "后续自动登录需要该文件夹及其文件, 文件重要, 不要误删!\n" + end_color)
        os.mkdir(path=path_root)

    path = path_root + "personalinfo1"
    exist = not(os.path.isfile(path=path))
    # print(exist)
    if exist:
        user_account = input(begin_color3 + "请输入你的校园网账号:\n" + end_color)
        confirm = input(begin_color4 + "请二次检查是否无误？ 无误请输入 1 \n" + end_color)
        while confirm != "1":
            user_account = input(begin_color3 + "请输入你的校园网账号:\n" + end_color)
            confirm = input(begin_color4 + "请二次检查是否无误？ 无误请输入 1 \n" + end_color)

        user_password = input(begin_color3 + "请输入你的账户密码:\n" + end_color)
        confirm = input(begin_color4 + "请二次检查是否无误？ 无误请输入 1 \n" + end_color)
        while confirm != "1":
            user_password = input(begin_color3 + "请输入你的账户密码:\n" + end_color)
            confirm = input(begin_color4 + "请二次检查是否无误？ 无误请输入 1 \n" + end_color)

        option = input(begin_color2 + "是否储存账户密码至" + path_root + "\n账号密码将使用RSA加密算法进行存储, 是自动化登录的必要步骤. \n项目已开源请放心使用. \n注意: 该操作需要管理员权限." + end_color + begin_color3 + "\n请输入: yes/no      默认为yes\n" +end_color)
        if option == "yes":
            (keypair_public,keypair_private) = rsa.newkeys(1024)
            pub = keypair_public.save_pkcs1()
            pri = keypair_private.save_pkcs1()
            with open(path_root + "personalinfo1",'wb+') as wfile1:
                wfile1 = wfile1.write(pub)
            with open(path_root + "personalinfo2",'wb+') as wfile2:
                wfile2 = wfile2.write(pri)

            account = rsa.encrypt(user_account.encode('utf8'),keypair_public)
            password = rsa.encrypt(user_password.encode('utf8'),keypair_public)
            
            with open(path_root + "personalinfo3",'wb+') as wfile3:
                wfile3 = wfile3.write(account)
            with open(path_root + "personalinfo4",'wb+') as wfile4:
                wfile4 = wfile4.write(password)
            print(begin_color2 + "请妥善保管好 " + path_root + " 该目录下的所有文件" + end_color)
            time.sleep(3)
            account = user_account
            password = user_password
        else:
            os.rmdir(path=path_root)
            print(begin_color2 + "保证操作流程纯净, 已清除建立的 " + path_root + "该目录及该目录下的所有文件\n\n" + end_color)
            print(begin_color1 + "如有需要自动登录需求,可以重启程序选择储存账号密码. \n\n开始使用输入的账户密码进行网络认证\n\n" + end_color)
            account = user_account
            password = user_password
    else:
        # with open(path_root + "personalinfo1",'rb') as wfile1:
        #     keypair_public = wfile1.read()
        with open(path_root + "personalinfo2",'rb') as wfile2:
            keypair_private = wfile2.read()
        with open(path_root + "personalinfo3",'rb') as wfile3:
            account = wfile3.read()
        with open(path_root + "personalinfo4",'rb') as wfile4:
            password = wfile4.read()
        # keypair_public = rsa.PublicKey.load_pkcs1(keypair_public)
        keypair_private = rsa.PrivateKey.load_pkcs1(keypair_private)
        account = rsa.decrypt(account,keypair_private).decode()
        password = rsa.decrypt(password,keypair_private).decode()
    return {"account": account, "password": password}

def get_v():
    return str(random.randint(500,10500))

def get_phpid():
    session = requests.Session()
    v = random.randint(500,10500)

    url = 'http://xxx.xx.xxx.xxx:801/eportal/?c=Portal&a=page_type_data&callback=dr1001&v=' + str(v)
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"
    headers = {
        "User_Agent": user_agent,
        "Host": "xxx.xx.xxx.xxx:801",
        "Refer": "http://xxx.xx.xxx.xxx/",
        "Connection": "keep-alive"
    }
    response = session.get(url=url,headers=headers)
    phpid = response.cookies["PHPSESSID"]
    return phpid

def get_authinfo():
    baseurl = "http://x.x.x.x/?cmd=redirect&arubalp=12345"

    session = requests.Session()
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"
    headers = {
        "User-Agent": user_agent,
        "Host": "x.x.x.x",
        "Connection": "keep-alive",
        "Referer": "http://x.x.x.x/",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
    }

    response = session.get(url=baseurl,headers=headers)
    reurl = response.url
    # print(reurl)

    parsed_url = urlparse(reurl)
    query_paramaters = parse_qs(parsed_url.query)

    swithchip = query_paramaters.get('switchip',[''])[0]
    mac = query_paramaters.get('mac',[''])[0]
    ip = query_paramaters.get('ip',[''])[0]

    # print('swithchip:',swithchip)
    # print('mac:',mac)
    # print('ip:',ip)
    return {'switchip': swithchip, 'mac': mac, 'ip': ip, 'url': reurl}

def exe_startup():
    get_userinfo()
    pwd = os.getcwd()
    src_file = pwd + '\\main.exe'
    user_dir = os.path.expanduser("~")
    path_root = user_dir + "\\AppData\\Local\\HFUT-wlan-autocheckin\\"
    dst_file = path_root + 'hfut-wlan.exe'
    os.system('cp {} {}'.format(src_file,dst_file))
    pwd = dst_file

    # key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run',0,winreg.KEY_ALL_ACCESS)
    # reged = winreg.QueryValueEx(key,"HFUT-wlan-autocheckin")
    # print(reged)

    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run',0,winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(key,"HFUT-wlan-autocheckin",0,winreg.REG_SZ, pwd)
    winreg.CloseKey(key)
    return 0

def test_conn():
    url = 'http://baidu.com'
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"
    headers = {
        "User-Agent": user_agent
    }
    response = requests.get(url=url, headers=headers)
    time.sleep(1)
    # print(response.status_code)
    if "aruba" in response.text or response.status_code != 200:
        # print("\033[2;35;47m联网失败, 请将问题反馈给开发者 \033[0;0m")
        output = "ok"
        return output
    else:
        # print("\033[2;35;47m联网成功\033[0;0m\n")
        output = "exit"
        return output

def test_stren():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()
    time.sleep(3)
    results = iface.scan_results()
    # print(results)
    for result in results:
        print(f"\033[2;32;40mWiFi名称: {result.ssid}                     信号强度: {result.signal} \033[0;0m") 

def wifi_connect():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    # print(iface.status())
    while iface.status() == const.IFACE_DISCONNECTED:
        print("\033[2;32;40mWiFi Disconnected! 请手动打开电脑WiFi连接再进行下一步操作!\n\033[0;0m")
        time.sleep(5)
        profile = pywifi.Profile()
        profile.ssid = "HFUT-WiFi"
        tem_profile = iface.add_network_profile(profile)
        iface.connect(tem_profile)
        time.sleep(1)
        # print(iface.status())
    
    out = subprocess.Popen("netsh wlan show interfaces",stdin=subprocess.PIPE,stdout=subprocess.PIPE,shell=True)
    out = out.stdout.read()
    # print(out)
    sign = "HFUT-WiFi".encode() in out
    # print(sign)
    output = "ok"

    while not(sign):
        # if not(iface.status() in [const.IFACE_CONNECTED,const.IFACE_INACTIVE]):
        #     profile = pywifi.Profile()
        #     profile.ssid = "HFUT-WiFi"
        #     tem_profile = iface.add_network_profile(profile)
        #     iface.connect(tem_profile)
        #     time.sleep(1)
        # else:
        time.sleep(2)
        out = subprocess.Popen("netsh wlan show interfaces",stdin=subprocess.PIPE,stdout=subprocess.PIPE,shell=True)
        out = out.stdout.read()
        # print(out)
        sign = "HFUT-WiFi".encode() in out

        if sign:
            output = "ok"
        else:
            confirm = input("\033[2;32;40m电脑自动连接至其它WiFi, 是否切换至HFUT-WiFi, 是(请输入1)\n\n\033[0;0m")
            if confirm == "1":
                iface.disconnect()
                time.sleep(5)   
                profile = pywifi.Profile()
                profile.ssid = "HFUT-WiFi"
                tem_profile = iface.add_network_profile(profile)
                iface.connect(tem_profile)
                time.sleep(1)

                out = subprocess.Popen("netsh wlan show interfaces",stdin=subprocess.PIPE,stdout=subprocess.PIPE,shell=True)
                out = out.stdout.read()
                # print(out)
                sign = "HFUT-WiFi".encode() in out
                if sign: 
                    print("\033[2;32;40m\n已连接HFUT-WiFi\n\033[0;0m")
                    output = "ok"
            else:
                confirm = input("\033[2;32;40m再次确认放弃自动登录校园网, 确认(再次输入1)\n\033[0;0m")
                if confirm: sys.exit()
    return output
    
def appendix():
    print(begin_color3 + "\n程序其他功能(无操作5s后关闭):\n\n\n1.开启开机自动连接WiFi\n\n2.测试网络是否连通\n\n3.测网速\n\n4.测试当前WiFi信号强度\n\n5.访问软件仓库, 查看源代码, 为开发者点亮一颗小星星\n\n6.一键自动注销本次登录\n\n7.软件存在其他问题? 欢迎向我们反馈\n\n*.关闭窗口(回车)\n" + end_color)
    start_time = time.time()
    while True:
        if msvcrt.kbhit():
            user_input = msvcrt.getch().decode()
            if user_input: return user_input
        if time.time() - start_time >5:
            sys.exit()
    # start_time = time.time()
    # while True:
    #     if time.time() - start_time >=5:
    #         exit() 
    #     confirm = input(begin_color3 + "\n软件还有其他功能(无操作5s后关闭):\n1.开启开机自动连接WiFi\n2.测试网络是否连通\n3.测网速\n4.测试当前WiFi信号强度\n5.访问软件仓库, 查看源代码, 为开发者点亮一颗小星星\n6.一键自动注销本次登录\n7.软件存在其他问题? 欢迎向我们反馈\n*.关闭窗口(回车)\n" + end_color)

    #     if confirm: return confirm 
    #     else:return 0 

def manage_auth():
    url = "http://xxx.xx.xxx.xxx/Self/login/?302=LI"
    headers = {
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Host": "xxx.xx.xxx.xxx",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"
    }
    session = requests.Session()
    reposonse = session.get(url=url,headers=headers)
    jsessionid = reposonse.cookies["JSESSIONID"]
    # print(jsessionid)
    cookies = {"JSESSIONID": jsessionid}

    reposonse = session.get(url=url,headers=headers,cookies=cookies)
    html = str(reposonse.text)
    soup = bs(html,'html.parser')
    checkcode = soup.find('input',type='hidden')
    # print(checkcode)
    checkcode = str(checkcode['value'])
    # print(checkcode)


    info = get_userinfo()
    account = info["account"]
    password = info["password"]
    password_md5 = hashlib.md5(password.encode())
    password = str(password_md5.hexdigest())
     
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Referer": "http://xxx.xx.xxx.xxx/Self/login/?302=LI",
        "Origin": "http://xxx.xx.xxx.xxx",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Host": "xxx.xx.xxx.xxx",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"
    }
    data = {
        "foo": " ",
        "bar": " ",
        "checkcode": checkcode,
        "account": account,
        "password": password,
        "code": " "
    }
    # print(data)
    session.post(url="http://xxx.xx.xxx.xxx/Self/login/verify",cookies=cookies,headers=headers,data=data)
    headers = {
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Host": "xxx.xx.xxx.xxx",
        "Connection": "keep-alive",
        "Referer": "http://xxx.xx.xxx.xxx/Self/login/?302=LI",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"
    }
    reposonse = session.get(url="http://xxx.xx.xxx.xxx/Self/dashboard",cookies=cookies,headers=headers)
    # print(reposonse.url)

        
# if __name__ == "__main__":
    # print(get_phpid())
    # userpath = exe_startup()
    # print(userpath)
    # test_stren()
    # wifi_connect()
    # test_conn()
    # manage_auth()