# -*- coding: utf-8 -*-
import os
import random
import string
import uuid
import requests
import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import requests
import json
import sys
import os
import platform
import re
purple = "\033[1;35m"
violet_chu = "\033[1;35m"
darkblue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
skyblue = "\033[1;36m"
blue = "\033[1;34m"
lightblue = "\033[38;5;81m"
hotpink = "\033[38;5;197m"
light_magenta = "\033[38;5;174m"
white = "\033[1;37m"
lavender = "\033[38;5;189m"
rasp = "\033[38;5;22m"
darkblue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
skyblue = "\033[1;36m"
blue = "\033[1;34m"
lightblue = "\033[38;5;81m"
white = "\033[1;37m"
def clear_screen():
    if 'termux' in platform.system().lower():
        os.system('clear')
    elif platform.system().lower() == 'windows':
        os.system('cls')
    else:
        os.system('clear')

import re
import re
import requests

def get_combined_data(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        'cache-control': "max-age=0",
        'dpr': "2",
        'viewport-width': "980",
        'sec-ch-ua': "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        'sec-ch-ua-mobile': "?0",
        'sec-ch-ua-platform': "\"Linux\"",
        'sec-ch-ua-platform-version': "\"\"",
        'sec-ch-ua-model': "\"\"",
        'sec-ch-ua-full-version-list': "\"Google Chrome\";v=\"131.0.6778.104\", \"Chromium\";v=\"131.0.6778.104\", \"Not_A Brand\";v=\"24.0.0.0\"",
        'sec-ch-prefers-color-scheme': "light",
        'upgrade-insecure-requests': "1",
        'sec-fetch-site': "same-origin",
        'sec-fetch-mode': "navigate",
        'sec-fetch-user': "?1",
        'sec-fetch-dest': "document",
        'accept-language': "en-US,en;q=0.9",
        'priority': "u=0, i",
        'Cookie': "sb=fuZTZ8Zyl9dXj5TFodlxDrGD; dpr=2; wd=980x1628; datr=fuZTZxL-gtbBjTkfeBq-VVDZ"
    }
    try:
        response = requests.get(url, headers=headers).text
        actrs_match = re.search(r'"actrs\\":\\"(\d+)\\"', response)
        actrs_number = actrs_match.group(1) if actrs_match else None
        post_id_match = response.split('"post_id":"')[1].split('"')[0] if '"post_id":"' in response else None
        if actrs_number and post_id_match:
            return f"{actrs_number}_{post_id_match}"
        elif not actrs_number:
            return "actrs number not found!"
        elif not post_id_match:
            return "post_id not found!"
    except Exception as e:
        return f"An error occurred: {str(e)}"

def extract_facebook_video_id(url):
    pattern = r'facebook\.com/(\d+)/videos/(\d+)/'
    match = re.search(pattern, url)    
    if match:
        user_id, video_id = match.groups()
        return f"{user_id}_{video_id}"
    else:
        return None

def extract_ids(url):
    group_pattern = r'groups/(\d+)/permalink/(\d+)/'
    post_pattern = r'(\d+)/posts/(\d+)/'
    photo_pattern = r'fbid=(\d+)'
    group_match = re.search(group_pattern, url)
    post_match = re.search(post_pattern, url)
    photo_match = re.search(photo_pattern, url)
    if group_match:
        group_id, post_id = group_match.groups()
        return f"{group_id}_{post_id}"
    elif post_match:
        group_id, post_id = post_match.groups()
        return f"{group_id}_{post_id}"
    elif photo_match:
        photo_id = photo_match.group(1)
        return photo_id
    else:
        return None 
    
def bryxpogii():
    adrkz = "\033[34m"
    print(f"""
{blue}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m
              {blue}███████╗██████╗░██████╗░░█████╗░██████╗░
              {blue}██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
              {blue}█████╗░░██████╔╝██████╔╝██║░░██║██████╔╝
              {blue}██╔══╝░░██╔══██╗██╔══██╗██║░░██║██╔══██╗
              {blue}███████╗██║░░██║██║░░██║╚█████╔╝██║░░██║
              {blue}╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝ {red}MAKER {green}: {blue}BRIAN CRUZ 
{blue}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m

{yellow}PATH: 6 {blue}: {red}[69K901010@Brian]           {yellow}KEY  {blue}: {red}352923863892
                                                                                  
{green}DEVELOPER     {blue}: {green}BRIAN
{green}FACEBOOK      {blue}: {green}https://www.facebook.com/BrianCruzPogi
{green}TOOL/STATUS   {blue}: {green}PAID/AUTO BOOSTING-BRIAN POGI
{green}VERSION       {blue}: {green}V/0.6
{blue}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m""")

def W_ueragnt():
    chrome_version = random.randint(80, 99)
    webkit_version = random.randint(500, 599)
    safari_version = random.randint(400, 499)
    windows_version = random.randint(8, 10)
    is_win64 = random.choice([
        True,
        False])
    if is_win64:
        if not 'WOW64;':
            user_agent = f'''Mozilla/5.0 (Windows NT {windows_version}.{''}Win64; x64) AppleWebKit/{webkit_version}.0 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Safari/{safari_version}.0'''
            return user_agent

import os
import uuid
import random
import requests
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
import string
import os
import requests
import threading
from concurrent.futures import ThreadPoolExecutor
import random
import time
import sys
import os
import platform
import random
import string

purple = "\033[1;35m"
blue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
white = "\033[1;37m"

def clear_screen():
    if 'termux' in platform.system().lower():
        os.system('clear')
    elif platform.system().lower() == 'windows':
        os.system('cls')
    else:
        os.system('clear')

def generate_user_agent():
    fbav = f"{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}"
    fbbv = str(random.randint(111111111, 999999999))
    fbrv = '0'
    random_seed = random.Random()
    adid = ''.join(random_seed.choices(string.hexdigits, k=16))
    device = random.choice(["HUAWEI MAR-LX1M", "Samsung SM-G960F", "OnePlus GM1913"])
    fbav_version = str(random.randint(49, 150))
    fbbv_version = str(random.randint(11111111, 77777777))
    carrier = random.choice(["Ooredoo TN", "Orange", "Vodafone", "T-Mobile"])
    ua_bgraph = f'[FBAN/FB4A;FBAV/{fbav_version}.0.0.{random.randrange(20, 49)}.{random.randint(11, 99)};FBBV/{fbbv_version};' \
                f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};FBDM/{{density=3.0,width=1080,height=2107}};FBLC/fr_FR;' \
                f'FBRV/{fbrv};FBCR/{carrier};FBMF/{device.split(" ")[0]};FBBD/{device.split(" ")[0]};' \
                f'FBPN/com.facebook.katana;FBDV/{device};FBSV/9;FBOP/1;FBCA/arm64-v8a:]'   
    return ua_bgraph

ua_bgraph = generate_user_agent()

import requests
import random
import concurrent.futures as thread
import os
import string

def bgraph(uid, pw, path_file, extract_type, success_count, existing_uids):
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
    fbav = f'{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'
    fbbv = str(random.randint(111111111, 999999999))
    fbrv = '0'
    random_seed = random.Random()
    adid = ''.join(random_seed.choices(string.hexdigits, k=16))
    ua_bgraph = '[FBAN/FB4A;FBAV/' + str(random.randint(49, 66)) + '.0.0.' + str(random.randrange(20, 49)) + str(random.randint(11, 99)) + ';FBBV/' + str(random.randint(11111111, 77777777)) + ';' + '[FBAN/FB4A;FBAV/' + fbav + ';FBBV/' + fbbv + ';FBDM/{density=3.0,width=1080,height=2107};FBLC/fr_FR;FBRV/' + fbrv + ';FBCR/Ooredoo TN;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1M;FBSV/9;FBOP/1;FBCA/arm64-v8a:]'
    data = {
        'adid': f'{uuid.uuid4()}',
        'format': 'json',
        'device_id': f'{uuid.uuid4()}',
        'cpl': 'true',
        'family_device_id': f'{uuid.uuid4()}',
        'credentials_type': 'device_based_login_password',
        'error_detail_type': 'button_with_disabled',
        'source': 'device_based_login',
        'email': uid,
        'password': pw,
        'access_token': accessToken,
        'generate_session_cookies': '1',
        'meta_inf_fbmeta': '',
        'advertiser_id': f'{uuid.uuid4()}',
        'currently_logged_in_userid': '0',
        'locale': 'en_US',
        'client_country_code': 'US',
        'method': 'auth.login',
        'fb_api_req_friendly_name': 'authenticate',
        'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
    }
    headers = {
        'User-Agent': ua_bgraph,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'graph.facebook.com',
        'X-FB-Net-HNI': str(random.randint(10000, 99999)),
        'X-FB-SIM-HNI': str(random.randint(10000, 99999)),
        'X-FB-Connection-Type': 'MOBILE.LTE',
        'X-Tigon-Is-Retry': 'False',
        'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
        'x-fb-device-group': str(random.randint(1000, 9999)),
        'X-FB-Friendly-Name': 'ViewerReactionsMutation',
        'X-FB-Request-Analytics-Tags': 'graphservice',
        'X-FB-HTTP-Engine': 'Liger',
        'X-FB-Client-IP': 'True',
        'X-FB-Connection-Bandwidth': str(random.randint(20000000, 30000000)),
        'X-FB-Server-Cluster': 'True',
        'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'
    }
    url = 'https://graph.facebook.com/auth/login'
    try:
        if uid in existing_uids:
            print(f"     {yellow}[INFO] {red}ACCOUNT --> {white}{uid} {red}ALREADY EXISTS.")
            print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
            return
        response = requests.post(url,headers=headers,data=data).json()
        print(response)
        if 'access_token' in response:
            token = response['access_token']
            with open(path_file, 'a') as f:
                f.write(f"{uid}|{token}\n")
            print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
            print(f"     \033[32m[SUCCESS]\033[0m: EXTRACTED ACCOUNT ─────> {uid}.")
            print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
            success_count.append(uid)
        else:
            print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
            print(f"     \033[31m[FAILED]\033[0m: TO EXTRACT ACCOUNT ─────> {uid}.")
            print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    except Exception as e:
        print(f"     \033[1;31m ERROR EXTRACTING ACCOUNT: {uid}. REASON: {str(e)}\033[0m\n")

def proz(accounts_file, token_output_path, extract_type):
    success_count = []
    existing_uids = set()
    if os.path.exists(token_output_path):
        with open(token_output_path, 'r') as f:
            existing_uids = {line.split('|')[0] for line in f.readlines()}
    try:
        with open(accounts_file, 'r') as file:
            accounts = file.readlines()
        accounts = [line.strip() for line in accounts if '|' in line.strip()]
        if not accounts:
            print(f"NO VALID ACCOUNTS FOUND IN {accounts_file}.")
            return
        with thread.ThreadPoolExecutor(max_workers=30) as executor:
            futures = [executor.submit(bgraph, uid, pw, token_output_path, extract_type, success_count, existing_uids)
                       for uid, pw in [account.split('|') for account in accounts]]
            for future in futures:
                future.result()
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        print(f"     \033[1;34m[SUCCESS]\033[0m: {len(success_count)} {extract_type}(s) SUCCESSFULLY EXTRACTED.")
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    except FileNotFoundError:
        print(f"FILE NOT FOUND: {accounts_file}")
        return

import requests
import random
import concurrent.futures as thread
import os
import string

def load_existing_tokens(path_file):
    if os.path.exists(path_file):
        with open(path_file, 'r') as f:
            return {line.split('|')[0] for line in f.readlines()}
    return set()

def bgraph_page(uid, pw, path_file, extract_type, success_count, existing_tokens):
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
    fbav = f'''{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'''
    fbbv = str(random.randint(111111111, 999999999))
    fbrv = '0'
    random_seed = random.Random()
    adid = ''.join(random_seed.choices(string.hexdigits, k=16))
    ua_bgraph = '[FBAN/FB4A;FBAV/' + str(random.randint(49, 66)) + '.0.0.' + str(random.randrange(20, 49)) + str(random.randint(11, 99)) + ';FBBV/' + str(random.randint(11111111, 77777777)) + ';' + '[FBAN/FB4A;FBAV/' + fbav + ';FBBV/' + fbbv + ';FBDM/{density=3.0,width=1080,height=2107};FBLC/fr_FR;FBRV/' + fbrv + ';FBCR/Ooredoo TN;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1M;FBSV/9;FBOP/1;FBCA/arm64-v8a:]'
    data = {
        'adid': f'{uuid.uuid4()}',
        'format': 'json',
        'device_id': f'{uuid.uuid4()}',
        'cpl': 'true',
        'family_device_id': f'{uuid.uuid4()}',
        'credentials_type': 'device_based_login_password',
        'error_detail_type': 'button_with_disabled',
        'source': 'device_based_login',
        'email': uid,
        'password': pw,
        'access_token': accessToken,
        'generate_session_cookies': '1',
        'meta_inf_fbmeta': '',
        'advertiser_id': f'{uuid.uuid4()}',
        'currently_logged_in_userid': '0',
        'locale': 'en_US',
        'client_country_code': 'US',
        'method': 'auth.login',
        'fb_api_req_friendly_name': 'authenticate',
        'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
    }
    headers = {
        'User-Agent': ua_bgraph,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'graph.facebook.com',
        'X-FB-Net-HNI': str(random.randint(10000, 99999)),
        'X-FB-SIM-HNI': str(random.randint(10000, 99999)),
        'X-FB-Connection-Type': 'MOBILE.LTE',
        'X-Tigon-Is-Retry': 'False',
        'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
        'x-fb-device-group': str(random.randint(1000, 9999)),
        'X-FB-Friendly-Name': 'ViewerReactionsMutation',
        'X-FB-Request-Analytics-Tags': 'graphservice',
        'X-FB-HTTP-Engine': 'Liger',
        'X-FB-Client-IP': 'True',
        'X-FB-Connection-Bandwidth': str(random.randint(20000000, 30000000)),
        'X-FB-Server-Cluster': 'True',
        'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'
    }
    url = 'https://graph.facebook.com/auth/login'
    try:
        if uid in existing_uids:
            print(f"     {white}ACCOUNT ─────> {red}{uid} {green}ALREADY EXISTS")
            print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
            return 
        response = requests.post(url,headers=headers,data=data).json()
        if 'access_token' in response:
            token = response['access_token']
            pages = extract_fb_pages(token)
            if pages:
                for page in pages:
                    page_id = page['id']
                    if page_id not in existing_tokens:
                        with open(path_file, 'a') as f:
                            f.write(f"{page_id}|{page['accessToken']}\n")
                        print(f"{white}{uid}  ─────> {green}PAGE ID: {red}{page_id} {yellow}EXTRACTED SUCCESSFULLY")
                        existing_tokens.add(page_id)
                    else:
                        print(f"{white}ID:  {page_id} ─────> {green}ALREADY EXISTS ! ")
            else:
                print(f"{white}{uid} ─────> {red}DOESN'T HAVE PAGES !")
            success_count.append(uid)
        else:
            print(f"{white}{uid}  ─────> {red}FAILED TO EXTRACT ! ")
    except Exception as e:
        print(f"ERROR EXTRACTING ACCOUNT: {uid}. REASON: {str(e)}")

def extract_fb_pages(token):
    url = 'https://graph.facebook.com/v18.0/me/accounts'
    headers = {
        'Authorization': f'Bearer {token}'
    }   
    pages_data = [] 
    while url:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f'ERROR: {response.text}')
            return None
        data = response.json()
        for page in data.get('data', []):
            pages_data.append({
                'id': page.get('id'),
                'accessToken': page.get('access_token')
            })
        url = data.get('paging', {}).get('next')
    return pages_data

def prozc(accounts_file, token_output_path, extract_type):
    success_count = []
    existing_tokens = load_existing_tokens(token_output_path)
    try:
        with open(accounts_file, 'r') as file:
            accounts = file.readlines()
        accounts = [line.strip() for line in accounts if '|' in line.strip()]
        if not accounts:
            print(f"NO VALID ACCOUNTS FOUND IN {accounts_file}.")
            return
        with thread.ThreadPoolExecutor(max_workers=30) as executor:
            futures = [executor.submit(bgraph_page, uid, pw, token_output_path, extract_type, success_count, existing_tokens)
                       for uid, pw in [account.split('|') for account in accounts]]
            for future in futures:
                future.result()
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        print(f"     \033[1;34m[SUCCESS]\033[0m: {len(success_count)} {extract_type}(s) SUCCESSFULLY EXTRACTED.")
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    except FileNotFoundError:
        print(f"FILE NOT FOUND: {accounts_file}")

def extraction():
    clear_screen()
    bryxpogii()
    print(f"     {white}[1] {yellow}EXTRACT {red}ACCOUNT")
    print(f"     {white}[2] {yellow}EXTRACT {red}PAGES")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    choice = input(f"    {green}Enter your choice: ").strip()
    if choice == '1':
        axl1()
    elif choice == '2':
        axl2()
    else:
        print(f"     {red}INVALID CHOICE")

def axl2():
    clear_screen()
    bryxpogii()
    folder_path = "/sdcard/boostphere"
    print(f"     {yellow}[01] {blue}FRA EXTRACT ACCOUNT")
    print(f"     {yellow}[02] {blue}FRA EXTRACT PAGES")
    print(f"     {yellow}[03] {blue}RPW EXTRACT ACCOUNT")
    print(f"     {yellow}[04] {blue}RPW EXTRACT PAGES")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    save_choice = input(f"    {green}Enter your choice: ").strip()
    if save_choice == '1':
        account_file = os.path.join(folder_path, "FRAACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '2':
        account_file = os.path.join(folder_path, "FRAPAGES.txt")
        extract_type = 'page'
    elif save_choice == '3':
        account_file = os.path.join(folder_path, "RPWACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '4':
        account_file = os.path.join(folder_path, "RPWPAGES.txt")
        extract_type = 'page'
    else:
        print("INVALID CHOICE. EXITING.")
        return
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    print(f"     \033[33mTHE FORMAT SHOULD BE \033[31muid|pass")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    file_path = input(f"     \033[33mPATH: ").strip()
    prozc(file_path, account_file, extract_type)

def axl1():
    clear_screen()
    bryxpogii()
    folder_path = "/sdcard/boostphere"
    print(f"     {yellow}[01] {blue}FRA EXTRACT ACCOUNT")
    print(f"     {yellow}[02] {blue}FRA EXTRACT PAGES")
    print(f"     {yellow}[03] {blue}RPW EXTRACT ACCOUNT")
    print(f"     {yellow}[04] {blue}RPW EXTRACT PAGES")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    save_choice = input(f"    {green}Enter your choice: ").strip()
    if save_choice == '1':
        account_file = os.path.join(folder_path, "FRAACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '2':
        account_file = os.path.join(folder_path, "FRAPAGES.txt")
        extract_type = 'page'
    elif save_choice == '3':
        account_file = os.path.join(folder_path, "RPWACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '4':
        account_file = os.path.join(folder_path, "RPWPAGES.txt")
        extract_type = 'page'
    else:
        print("INVALID CHOICE. EXITING.")
        return
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    print(f"     \033[33mTHE FORMAT SHOULD BE \033[31muid|pass")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    file_path = input(f"     \033[33mPATH: ").strip()
    token_output_path = account_file
    proz(file_path, token_output_path, extract_type)

folder_name = "/sdcard/boostphere"
file_names = ["FRAACCOUNT.txt", "FRAPAGES.txt", "RPWACCOUNT.txt", "RPWPAGES.txt","generated_code.txt","auto_create_ok.txt"]
if not os.path.exists(folder_name):
    try:
          os.makedirs(folder_name)
    except Exception:
              pass
    for file_name in file_names:
        file_path = os.path.join(folder_name, file_name)
        if not os.path.exists(file_path):
            try:
                with open(file_path, 'w') as file:
                    pass  
            except Exception:
                pass  

def count_tokens(accounts_file, pages_file):
    total_accounts = 0
    total_pages = 0
    try:
        with open(accounts_file, 'r') as af:
            total_accounts = sum(1 for line in af if line.strip())
    except FileNotFoundError:
        print(f"ACCOUNT FILE NOT FOUND: {accounts_file}")
    try:
        with open(pages_file, 'r') as pf:
            total_pages = sum(1 for line in pf if line.strip())
    except FileNotFoundError:
        print(f"PAGE FILE NOT FOUND: {pages_file}")
    return total_accounts, total_pages

import os
import requests
import random
import string
import uuid
import random

def user_agint():
    fbcr_values = ["AT&T", "Orange France", "Telia Sweden","Vodafone Italy", "Sky Mobile","Proximus Belgium", "Movistar Spain", "Tele2 Netherlands", "Vodafone Spain", "Telekom Deutschland","Eir Ireland", "KPN Netherlands", "Three Ireland", "Telekom Austria", "Telia Sweden","Vodafone Italy", "Sky Mobile", "Proximus Belgium", "Movistar Spain", "Tele2 Netherlands","Vodafone Spain", "Telekom Deutschland", "Eir Ireland", "KPN Netherlands", "Three Ireland","Telekom Austria", "Telia Sweden", "Vodafone Italy", "Sky Mobile", "Proximus Belgium","Movistar Spain", "Tele2 Netherlands","Vodafone Spain", "Telekom Deutschland", "Eir Ireland","KPN Netherlands", "Three Ireland", "Telekom Austria", "China Mobile", "NTT Docomo", "KT Corporation", "Singtel","AIS Thailand", "Viettel", "Smart Communications", "PTCL Pakistan", "Grameenphone Bangladesh","Nepal Telecom", "MTN Nigeria", "T-Mobile USA", "Verizon Wireless", "Rogers Canada","O2 United Kingdom", "Telstra Australia", "TIM Brazil", "Vivo India", "Telenor Norway","Mobilink Pakistan", "Bell Canada", "Etisalat UAE", "Claro Mexico", "Orange Spain","Vodafone Portugal", "Telkomsel Indonesia","Beeline Russia", "MTS Russia", "Optus Australia","SK Telecom South Korea", "Entel Chile", "MTNL India", "Tigo Ghana", "Idea India","DTAC Thailand", "Zong Pakistan", "Orange Romania", "EE United Kingdom", "Digi Malaysia","Koodo Canada", "Yoigo Spain", "Airtel Nigeria", "Airtel Kenya", "Telekom Malaysia","Cosmote Greece", "Digicel Jamaica", "LIME Caribbean", "Telus Canada", "Sprint USA","Movistar Mexico", "Vodafone Germany", "Optus Australia","Vivo Brazil", "Singtel Singapore", "Airtel India", "Ncell Nepal", "Telenor Sweden","MEO Portugal", "Claro Argentina", "EE Estonia", "Telkom South Africa", "Telenor Norway","Yoigo Spain", "Giffgaff United Kingdom", "Lycamobile France", "A1 Telekom Austria", "Telenor Hungary","Vodafone Greece", "Cosmote Romania", "Telenor Serbia", "Vodafone New Zealand", "Telekom Croatia","Orange Belgium", "Telkomsel Indonesia", "Vivacom Bulgaria", "Orange Poland", "Rogers Canada","Telkom South Africa", "Lycamobile Germany", "M1 Singapore", "DT Mobile Austria", "Claro Colombia","Telkomsel Indonesia", "Tele2 Norway", "Telia Estonia", "Telenor Denmark","Rakuten Mobile Japan","Ooredoo Qatar","Movistar Argentina", "T-Mobile Netherlands", "Telekom Hungary", "Vodafone Romania","NOS Portugal", "Digicel Haiti", "Three Hong Kong", "Airtel Bangladesh", "Telcel Mexico","Orange Moldova", "Telkomsel Indonesia", "Telenor Bulgaria","Vodafone Ukraine", "Cosmote Greece","T-Mobile Czech Republic", "NetOne Zimbabwe", "Glo Nigeria", "MTS Belarus", "Cell C South Africa","Maxis Malaysia", "Fido Canada", "Zain Saudi Arabia", "Telenor Serbia", "Beeline Uzbekistan","A1 Telekom Austria", "Zong Pakistan", "Jazz Pakistan", "Vodafone Portugal", "Telstra Australia","Vodafone Ireland", "Orange Slovakia", "Claro Peru", "Vivo Brazil", "Vodafone Czech Republic","Telenor Montenegro", "Digi Malaysia", "Etisalat Egypt", "Tigo Rwanda", "Robi Bangladesh","MTC Namibia", "AIS Thailand", "Vodafone Greece", "Orange Romania", "T-Mobile Poland","Telenor Hungary", "Telia Latvia", "Ooredoo Oman", "Optus Australia", "Orange Belgium","Telenor Norway", "Lycamobile France", "EE Estonia", "Yoigo Spain", "Giffgaff United Kingdom","Sprint USA", "Telus Canada", "Vodafone Germany", "Movistar Mexico", "Telkomsel Indonesia","Vivo India", "Airtel India", "Ncell Nepal", "Telenor Sweden", "MEO Portugal","Claro Argentina", "Telekom Croatia", "Cosmote Romania", "Orange Poland", "Telenor Serbia","Vodafone New Zealand", "Vivacom Bulgaria", "Telenor Denmark", "T-Mobile Netherlands", "NOS Portugal","Telkomsel Indonesia", "Tele2 Norway", "Telia Estonia", "Telenor Denmark", "Rakuten Mobile Japan","Ooredoo Qatar", "Movistar Argentina", "T-Mobile Netherlands", "Telekom Hungary", "Vodafone Romania","Digicel Haiti", "Three Hong Kong", "Airtel Bangladesh", "Telcel Mexico", "Orange Moldova","Telkomsel Indonesia", "O2 Germany", "Airtel Nigeria", "Orange Kenya","Digicel Jamaica","Unitel Angola", "MobiFone Vietnam", "TMN Portugal", "Grameenphone Bangladesh", "Movitel Mozambique","Telkom South Africa", "Globacom Nigeria", "Nawras Oman", "Vodafone Ghana", "Telenor Pakistan","Yoigo Spain", "SFR France", "Tigo Colombia", "Vodafone Qatar", "Etisalat UAE","Telenor Norway", "Telia Finland", "LIME Caribbean", "EE United Kingdom", "Koodo Canada","TIM Italy", "Telekom Romania", "Jio India", "Ooredoo Kuwait", "Orange Switzerland","Bouygues Telecom France", "Entel Bolivia", "A1 Telekom Austria", "MTN South Africa", "Vodafone Hungary","Zain Jordan", "Ncell Nepal", "Zain Kuwait", "Djezzy Algeria", "Smart Philippines","Telenor Bulgaria", "Cosmote Greece", "Vodafone Portugal", "Telstra Australia", "Three Ireland","Rogers Canada", "Safaricom Kenya", "Orange Luxembourg", "Elisa Finland", "Vodafone Netherlands","KPN Netherlands", "Telia Lithuania", "Vodafone Iceland", "Tigo Ghana", "Idea India","Tata Docomo India", "Aircel India", "Claro Chile", "Movistar Peru", "T-Mobile Croatia","Telkomsel Indonesia", "O2 Czech Republic", "Smartfren Indonesia", "Axiata Malaysia", "Digicel Caribbean","Beeline Kazakhstan", "Moldcell Moldova", "Djezzy Algeria", "Tigo Rwanda", "Vodafone Egypt","COSMOTE Cyprus", "Bell Mobility Canada", "Telenor Sweden", "3 Sweden", "DNA Finland","Zain Bahrain", "Ooredoo Tunisia", "Orange Morocco", "Vivacom Bulgaria", "VIPnet Croatia","Vodafone Greece", "Orange Romania", "T-Mobile Poland", "Telenor Hungary", "AIS Thailand","TrueMove Thailand", "Vodafone Czech Republic", "Digi Malaysia", "XL Axiata Indonesia", "Dialog Sri Lanka","MTN Uganda", "Airtel Bangladesh", "Viva Kuwait", "Wind Italy", "LMT Latvia","Yoigo Spain", "Maroc Telecom Morocco", "Orange Ivory Coast", "Airtel Malawi", "Airtel Zambia", "DITO", "Globe", "GOMO", "TNT", "TM"]
    fbmf_fbdv_dict = {
    "asus": ["ZenFone 8", "ROG Phone 5", "ZenFone 7", "ROG Phone 3", "ZenFone 6", "ROG Phone II", "ZenFone 5Z", "ZenFone 5", "ZenFone 4 Pro", "ZenFone 4", "ZenFone 3 Deluxe", "ZenFone 3", "ZenFone 2 Laser", "ZenFone 2", "ZenFone", "ZenFone 6Z", "ZenFone Max Pro (M2)", "ZenFone Max Pro (M1)", "ZenFone 6Z", "ZenFone Max Plus (M2)", "ZenFone Max (M2)", "ZenFone Max (M1)", "ZenFone Live", "ZenFone Zoom", "ZenFone Selfie", "ASUS_Z01RD", "ASUS_Z01QD", "ASUS_I01WD", "ASUS_I01BD", "ASUS_I01HDA"],
    "lenovo": ["Legion Phone Duel 2", "Legion Phone Duel", "K12 Note", "K10 Note", "Z6 Pro", "Z5 Pro", "Lenovo Z6 Pro", "Lenovo Z6 Youth", "Lenovo Z5s", "Lenovo Z5 Pro GT", "Lenovo Z5 Pro", "Lenovo Z5", "Lenovo K9", "Lenovo A5", "Lenovo K320t", "Lenovo K8 Note", "Lenovo K6 Note", "Lenovo Vibe K5 Note", "Lenovo Vibe K5", "Lenovo Vibe P1", "Lenovo Vibe X3", "Lenovo Vibe Z2 Pro", "Lenovo Vibe Z2", "Lenovo Vibe Z","A6000", "A6000 Plus", "A7000", "A7000 Turbo", "A2010", "A2010-a", "K3 Note", "Vibe K4 Note", "Vibe K5 Note", "Vibe K5 Plus", "Vibe K5", "Vibe K5 Lite", "Vibe K5 Power", "Vibe K5 S", "Vibe X2", "Vibe X3", "Vibe Z2 Pro", "K6 Power", "K6 Note", "K6", "K6 Plus", "K6 Turbo", "Vibe C", "Vibe C2", "Vibe C2 Power", "Vibe C2 K10a40", "Vibe C2 K10a40C", "Vibe B", "Vibe B A2016a40", "Vibe B A2016b30", "Vibe B A2016b31", "Vibe B A2016b31C", "Vibe B A2016b30A", "Vibe B A2016b30B", "Vibe B A2016b30C", "Vibe B A2016b30D", "Vibe B A2016b30E", "Vibe B A2016b30G", "Vibe B A2016b30J", "Vibe B A2016b30K", "Vibe B A2016b30L", "Vibe B A2016b30M", "Vibe B A2016b30N", "Vibe B A2016b30O", "Vibe B A2016b30Q", "Vibe B A2016b30R", "Vibe B A2016b30T", "Vibe B A2016b30W", "Vibe B A2016b30Y", "Vibe B A2016b31A", "Vibe B A2016b31B", "Vibe B A2016b31C", "Vibe B A2016b31E", "Vibe B A2016b31F", "Vibe B A2016b31G", "Vibe B A2016b31H", "Vibe B A2016b31K", "Vibe B A2016b31L", "Vibe B A2016b31M", "Vibe B A2016b31N", "Vibe B A2016b31O", "Vibe B A2016b31P", "Vibe B A2016b31Q", "Vibe B A2016b31R", "Vibe B A2016b31S", "Vibe B A2016b31T", "Vibe B A2016b31U", "Vibe B A2016b31V", "Vibe B A2016b31W", "Vibe B A2016b31X", "Vibe B A2016b31Y", "Vibe B A2016b31Z", "Vibe B A2016b31AA", "Vibe B A2016b31AB", "Vibe B A2016b31AC", "Vibe B A2016b31AD", "Vibe B A2016b31AE", "Vibe B A2016b31AF", "Vibe B A2016b31AG", "Vibe B A2016b31AH", "Vibe B A2016b31AI", "Vibe B A2016b31AJ", "Vibe B A2016b31AK", "Vibe B A2016b31AL", "Vibe B A2016b31AM", "Vibe B A2016b31AN", "Vibe B A2016b31AO", "Vibe B A2016b31AP", "Vibe B A2016b31AQ", "Vibe B A2016b31AR", "Vibe B A2016b31AS", "Vibe B A2016b31AT", "Vibe B A2016b31AU", "Vibe B A2016b31AV", "Vibe B A2016b31AW", "Vibe B A2016b31AX", "Vibe B A2016b31AY", "Vibe B A2016b31AZ", "Vibe B A2016b31BA", "Vibe B A2016b31BB", "Vibe B A2016b31BC", "Vibe B A2016b31BD", "Vibe B A2016b31BE", "Vibe B A2016b31BF", "Vibe B A2016b31BG", "Vibe B A2016b31BH", "Vibe B A2016b31BI", "Vibe B A2016b31BJ", "Vibe B A2016b31BK", "Vibe B A2016b31BL", "Vibe B A2016b31BM", "Vibe B A2016b31BN", "Vibe B A2016b31BO", "Vibe B A2016b31BP", "Vibe B A2016b31BQ", "Vibe B A2016b31BR", "Vibe B A2016b31BS"],
    "sony": ["Xperia 5 III", "Xperia 10 II", "Xperia 1 II", "Xperia 10 Plus", "Xperia 1", "Xperia XZ3", "Xperia 1 III", "Xperia 1 II", "Xperia 1", "Xperia 5 III", "Xperia 5 II", "Xperia 5", "Xperia 10 III", "Xperia 10 II", "Xperia 10", "Xperia Pro", "Xperia L4", "Xperia L3", "Xperia XZ3", "Xperia XZ2 Premium", "Xperia XZ2", "Xperia XZ1 Compact", "Xperia XZ1", "Xperia XZ Premium", "Xperia XZ", "Xperia XA2 Ultra", "Xperia XA2", "Xperia XA1 Ultra", "Xperia XA1 Plus", "Xperia XA1", "Xperia X Compact","C6603", "D6503", "F5121", "F8331", "G3116", "H3113", "J9210", "XQ-AS52", "XQ-AD52", "XQ-BT52", "XQ-BS52", "XQ-AT51", "XQ-AT52", "XQ-AD52", "XQ-AT52", "XQ-AT42", "XQ-AT41", "XQ-AD51", "XQ-BT51", "XQ-BS41", "XQ-BS52", "XQ-BT52", "XQ-AD51", "XQ-BT51", "XQ-BS41", "XQ-AT41", "XQ-BS52", "XQ-BT52", "XQ-AS42", "XQ-BS42", "XQ-AT42", "XQ-BS41", "XQ-AT51", "XQ-AD51", "XQ-AD42", "XQ-AS41", "XQ-BT41", "XQ-BT51", "XQ-BS51", "XQ-BS42", "XQ-AS52", "XQ-AS41", "XQ-BS42", "XQ-BT41", "XQ-AS42", "XQ-AT42", "XQ-AD42", "XQ-BS41", "XQ-AT41", "XQ-BS51", "XQ-BT51", "XQ-AT51", "XQ-AD51", "F8131", "F8132", "G3121", "G3112", "G3123", "G3125", "G8141", "G8142", "G8341", "G8342", "H8216", "H8266", "H8296", "H8416", "H9436", "H9461", "H9436", "H9461", "H9436", "H9493", "H8541", "H8526", "H8116", "H8166", "I4213", "I4293", "I4293", "I4312", "I4332", "I4332", "I4113", "I4193", "I4213", "I4312", "I4332", "I4293", "I4293", "I4213", "I4312", "I4332", "I4312", "I4332", "I4293", "I4293", "I4213", "I4312", "I4332", "I4293", "I4293", "I4213", "I4312", "I4332", "I4312", "I4332", "I4293", "I4293", "I4213", "I4312", "I4332", "I4293", "I4293", "I4213", "I4312", "I4332", "I4312", "I4332", "I4293", "I4293", "I4213", "I4312", "I4332", "I4293", "I4293", "I4213", "I4312", "I4332", "I4312", "I4332", "I4293", "I4293", "I4213", "I4312", "I4332", "I4293", "I4293", "I4213"],
    "htc": ["Wildfire E3", "Desire 21 Pro", "U20 5G", "Desire 20 Pro", "Desire 19+", "U12 Life","HTC U20", "HTC U12+", "HTC U11", "HTC U12+", "HTC U12 Life", "HTC U11+", "HTC U11 Life", "HTC U11", "HTC U Ultra", "HTC 10", "HTC One M9", "HTC One M8", "HTC One (M7)", "HTC Desire 820", "HTC Desire 816", "HTC Desire 610", "HTC Desire 510", "HTC Butterfly S", "HTC One Max", "HTC One Mini", "HTC Desire 600", "HTC First", "HTC One X+","HTC One M8", "HTC One M9", "HTC 10", "HTC U11", "HTC U12+", "HTC U Ultra", "HTC U Play", "HTC Desire 626", "HTC Desire 816", "HTC Desire 610", "HTC Desire 510", "HTC Desire 820", "HTC Desire 626G+", "HTC One X", "HTC One X+", "HTC One S", "HTC One V", "HTC One Mini", "HTC One Mini 2", "HTC One Max", "HTC One E8", "HTC One E9", "HTC One A9", "HTC One E9+", "HTC One M8s", "HTC Desire Eye", "HTC Desire 820s", "HTC Desire 816G", "HTC Desire 626s", "HTC Desire 530", "HTC Desire 828", "HTC 10 Lifestyle", "HTC U11 Life", "HTC U11 Eyes", "HTC U11+"],
    "apple": ["iPhone 13 Pro", "iPhone 13", "iPhone 13 mini", "iPhone 12 Pro", "iPhone 12", "iPhone SE (3rd Gen)", "iPhone 13 Pro Max", "iPhone 13 Pro", "iPhone 13", "iPhone 13 mini", "iPhone 12 Pro Max", "iPhone 12 Pro", "iPhone 12", "iPhone 12 mini", "iPhone SE (2nd generation)", "iPhone 11 Pro Max", "iPhone 11 Pro", "iPhone 11", "iPhone XR", "iPhone XS Max", "iPhone XS", "iPhone X", "iPhone 8 Plus", "iPhone 8", "iPhone 7 Plus", "iPhone 7", "iPhone SE (1st generation)", "iPhone 6s Plus", "iPhone 6s", "iPhone 6 Plus", "iPhone 6", "iPhone 5s", "iPhone 5c", "iPhone 5", "iPhone 4s", "iPhone 4", "iPhone 3GS", "iPhone 3G", "iPhone","A1549", "A1522", "A1586", "A1633", "A1688", "A1699", "A1700", "A1660", "A1778", "A1661", "A1784", "A1863", "A1901", "A1865", "A1902", "A1920", "A1921", "A2101", "A2102", "A2104", "A1984", "A2103", "A1920", "A1921", "A2160", "A2161", "A2215", "A2217", "A2218", "A2220", "A2221", "A2223", "A2111", "A2229", "A2112", "A2131", "A2106", "A2107", "A2108", "A2162", "A2047", "A2048", "A2049", "A2105", "A2014", "A2015", "A2016", "A1867", "A1868", "A1897", "A1898", "A1899", "A1900", "A1903", "A1923", "A2212", "A2200", "A2202", "A2201", "A2301", "A2223", "A2215", "A1866", "A1993", "A1990", "A2013", "A2012", "A1983", "A1954", "A1953", "A2100", "A2005", "A2114", "A2116", "A2110", "A1920", "A1921", "A1985", "A2115", "A2117", "A2118", "A2003", "A2004", "A2160", "A2161", "A2202", "A2298", "A2299", "A2162", "A2270", "A2271", "A2229", "A2272", "A2273", "A2301", "A2304", "A2324", "A2325", "A2340", "A2341", "A2342", "A2375", "A2376", "A2377", "A2378", "A2406", "A2407", "A2408", "A2451", "A2452", "A2453", "A2600", "A2594", "A2503", "A2571", "A2570", "A2410", "A2402", "A2412", "A2399", "A2400", "A2466", "A2478", "A2479", "A2480", "A2522", "A2523", "A2524", "A2602", "A2604", "A2610", "A2612", "A2626", "A2628", "A2633", "A2634", "A2616", "A2617", "A2630", "A2631", "A2632", "A2624", "A2649", "A2646", "A2647", "A2653", "A2656", "A2654", "A2655", "A2657", "A2658", "A2398", "A2399", "A2403", "A2404", "A2405", "A2406", "A2399", "A2407", "A2408", "A2400", "A2466", "A2478", "A2479", "A2480", "A2522", "A2523", "A2524", "A2602", "A2604", "A2610", "A2612", "A2626", "A2628", "A2633", "A2634", "A2616", "A2617", "A2630", "A2631", "A2632", "A2624", "A2649", "A2646", "A2647", "A2653", "A2656", "A2654", "A2655", "A2657", "A2658", "A2398", "A2399", "A2403", "A2404", "A2405", "A2406", "A2399", "A2407", "A2408", "A2400", "A2466", "A2478", "A2479", "A2480", "A2522", "A2523", "A2524", "A2602", "A2604", "A2610", "A2612", "A2626", "A2628", "A2633", "A2634", "A2616", "A2617", "A2630", "A2631", "A2632", "A2624", "A2649", "A2646", "A2647", "A2653", "A2656", "A2654", "A2655", "A2657", "A2658", "A2398", "A2399", "A2403", "A2404", "A2405", "A2406", "A2399", "A2407", "A2408", "A2400", "A2466", "A2478", "A2479", "A2480", "A2522", "A2523", "A2524", "A2602", "A2604", "A2610", "A2612", "A2626", "A2628", "A2633", "A2634", "A2616", "A2617", "A2630", "A2631", "A2632", "A2624", "A2649", "A2646", "A2647", "A2653", "A2656", "A2654", "A2655", "A2657", "A2658", "A2398", "A2399", "A2403", "A2404", "A2405", "A2406", "A2399", "A2407", "A2408", "A2400", "A2466", "A2478", "A2479", "A2480", "A2522", "A2523", "A2524", "A2602"],
    "oppo": ["Reno 7 Pro", "Reno 7", "Reno 6 Pro+", "A95", "A96", "A93", "Oppo Find X3 Pro", "Oppo Find X2 Pro", "Oppo Find X2", "Oppo Reno 6 Pro+", "Oppo Reno 6 Pro", "Oppo Reno 6", "Oppo Reno 5 Pro+", "Oppo Reno 5 Pro", "Oppo Reno 5", "Oppo A94", "Oppo A74", "Oppo F19 Pro+", "Oppo F19 Pro", "Oppo F19", "Oppo A93", "Oppo A53", "Oppo A33", "Oppo A32", "Oppo A72", "Oppo A52", "Oppo A92", "Oppo A12", "Oppo Reno 3 Pro", "Oppo Reno 3", "Oppo Reno 2", "Oppo Reno", "Oppo K7x", "Oppo K7", "Oppo A9 (2020)", "Oppo A5 (2020)", "CPH1903", "CPH1803", "CPH1859", "CPH1969", "CPH1989", "CPH1919", "CPH1941", "CPH1983", "CPH1963", "CPH1879", "CPH1831", "CPH2035", "CPH2069", "CPH1987", "CPH2071", "CPH2083", "CPH2015", "CPH2019", "CPH2173", "CPH2089", "CPH2067", "CPH2017", "CPH2087", "CPH2205", "CPH2251", "CPH2197", "CPH2235", "CPH2347", "CPH2295", "CPH2249", "CPH2243", "CPH2349", "CPH2359", "CPH2383", "CPH2381", "CPH2239", "CPH2213", "CPH2129", "CPH2195", "CPH2227", "CPH2316", "CPH2353", "CPH2261", "CPH2225", "CPH2269", "CPH2073", "CPH2185", "CPH1877", "CPH2013", "CPH2061", "CPH1955", "CPH1871", "CPH1801", "CPH1873", "CPH1901", "CPH1809", "CPH1853", "CPH1923", "CPH1981", "CPH1833", "CPH1917", "CPH1967", "CPH1937", "CPH1893", "CPH1931", "CPH1921", "CPH1823", "CPH2023", "CPH2021", "CPH2103", "CPH2220", "CPH2127", "CPH2059", "CPH2139", "CPH2253", "CPH2267", "CPH2263", "CPH2247", "CPH2241", "CPH2297", "CPH2357", "CPH2255", "CPH2345", "CPH2329", "CPH2209", "CPH2191", "CPH2199", "CPH2289", "CPH2319", "CPH2343", "CPH2363", "CPH2161", "CPH2163", "CPH1979", "CPH1977", "CPH1973", "CPH1965", "CPH1959", "CPH1951", "CPH1913", "CPH1909", "CPH1905", "CPH1861", "CPH1863", "CPH1967", "CPH1933", "CPH1937", "CPH1921", "CPH1923", "CPH1987", "CPH1919", "CPH1897", "CPH1875", "CPH1874", "CPH1872", "CPH1865", "CPH1863", "CPH1862", "CPH1853", "CPH1852", "CPH1851", "CPH1843", "CPH1841", "CPH1835", "CPH1833", "CPH1832", "CPH1831", "CPH1825", "CPH1823", "CPH1821", "CPH1819", "CPH1813", "CPH1812", "CPH1811", "CPH1809", "CPH1808", "CPH1807", "CPH1805", "CPH1803", "CPH1801"],
    "realme": ["Realme GT Master Edition", "Realme 8i", "Realme 8s", "Narzo 30", "Narzo 20", "Realme 7i", "Realme 8", "Realme 7 Pro", "Realme X50 Pro","Realme GT Master Explorer Edition", "Realme GT Master Edition", "Realme GT", "Realme 8 Pro", "Realme 8", "Realme Narzo 30 Pro", "Realme Narzo 30A", "Realme X7 Pro", "Realme X7", "Realme 7 Pro", "Realme 7", "Realme C21", "Realme C20", "Realme C15", "Realme C12", "Realme C11", "Realme 6 Pro", "Realme 6", "Realme X2 Pro", "Realme XT", "Realme 5 Pro", "Realme 5", "Realme 3 Pro", "Realme 3", "Realme 2 Pro", "Realme 2", "Realme 1","RMX2111", "RMX3092", "RMX3161", "RMX3142", "RMX3185", "RMX3186", "RMX3281", "RMX3274", "RMX3361", "RMX3165", "RMX3243", "RMX3242", "RMX3294", "RMX3162", "RMX3241", "RMX3290", "RMX3289", "RMX3270", "RMX3267", "RMX3266", "RMX3263", "RMX3260", "RMX3240", "RMX3280", "RMX3276", "RMX3244", "RMX3121", "RMX3063", "RMX3061", "RMX3090", "RMX3091", "RMX3080", "RMX3211", "RMX3334", "RMX3221", "RMX3295", "RMX3292", "RMX3331", "RMX3383", "RMX3350", "RMX3332", "RMX3300", "RMX3310", "RMX3311", "RMX3385", "RMX3336", "RMX3337", "RMX3338", "RMX3235", "RMX3225", "RMX3124", "RMX3065", "RMX3143", "RMX3201", "RMX3070", "RMX3250", "RMX3246", "RMX3261", "RMX3071", "RMX3150", "RMX3164", "RMX3141", "RMX3063", "RMX3060", "RMX3357", "RMX3223", "RMX3330", "RMX3284", "RMX3362", "RMX3236", "RMX3193", "RMX3191", "RMX3358", "RMX3384", "RMX3262", "RMX3248", "RMX3339", "RMX3283", "RMX3195", "RMX3093", "RMX3098", "RMX3245", "RMX3095", "RMX3064", "RMX3341", "RMX3340", "RMX3365", "RMX3363", "RMX3364", "RMX3366", "RMX3367", "RMX3368", "RMX3369", "RMX3370", "RMX3371", "RMX3372", "RMX3373", "RMX3374", "RMX3375", "RMX3376", "RMX3377", "RMX3378", "RMX3379", "RMX3380", "RMX3381", "RMX3382", "RMX3312", "RMX3249", "RMX3094", "RMX3116", "RMX3187", "RMX3096", "RMX3097", "RMX3171", "RMX3152", "RMX3115", "RMX3081", "RMX3272", "RMX3273", "RMX3264", "RMX3265", "RMX3269", "RMX3268", "RMX3082", "RMX3083", "RMX3084", "RMX3085", "RMX3086", "RMX3087", "RMX3088", "RMX3089", "RMX3099", "RMX309A", "RMX309B", "RMX309C", "RMX309D", "RMX309E", "RMX309F", "RMX309G", "RMX309H", "RMX309I", "RMX309J", "RMX309K", "RMX309L", "RMX309M", "RMX309N", "RMX309O", "RMX309P", "RMX309Q", "RMX309R", "RMX309S", "RMX309T", "RMX309U", "RMX309V", "RMX309W", "RMX309X", "RMX309Y", "RMX309Z", "RMX31ZM", "RMX31ZN", "RMX31ZS", "RMX31ZT", "RMX31ZW", "RMX31ZV", "RMX31ZR", "RMX31ZQ", "RMX31ZP", "RMX31ZO", "RMX31ZN", "RMX31ZM", "RMX31ZL", "RMX31ZK", "RMX31ZJ", "RMX31ZI", "RMX31ZH", "RMX31ZG", "RMX31ZF", "RMX31ZE", "RMX31ZD", "RMX31ZC"],
    "motorola": ["Moto G100", "Moto G60", "Moto G40 Fusion", "Moto G30", "Moto G9 Power", "Moto G8", "Moto G Power 2022", "Moto G7", "Moto G Stylus 2022", "Motorola Edge 20 Pro", "Motorola Edge 20", "Motorola Edge 20 Lite", "Motorola Moto G Stylus (2021)", "Motorola Moto G Power (2021)", "Motorola Moto G Play (2021)", "Motorola Moto G9 Plus", "Motorola Moto G9", "Motorola Moto G8 Plus", "Motorola Moto G8 Power", "Motorola Moto G8", "Motorola Moto G7 Plus", "Motorola Moto G7 Power", "Motorola Moto G7 Play", "Motorola Moto G7", "Motorola Moto G6 Plus", "Motorola Moto G6", "Motorola Moto G5S Plus", "Motorola Moto G5 Plus", "Motorola Moto G5", "Motorola Moto G4 Plus", "Motorola Moto G4", "Motorola Moto X4", "Motorola Moto X (2nd Gen)", "Motorola Moto X", "Motorola Moto Z3 Play", "Motorola Moto Z2 Play", "Motorola Moto Z", "Motorola Moto E7 Plus", "Motorola Moto E6 Plus", "Motorola Moto E5 Plus", "Motorola Moto E4 Plus", "Motorola Moto E (2nd Gen)", "Motorola Moto E", "XT2127-2", "XT2127-4", "XT2127-5", "XT2127-6", "XT2127-7", "XT2127-8", "XT2127-10", "XT2127-11", "XT2127-12", "XT2127-13", "XT2127-14", "XT2127-15", "XT2127-16", "XT2127-17", "XT2127-18", "XT2127-19", "XT2127-20", "XT2127-21", "XT2127-22", "XT2127-23", "XT2127-24", "XT2127-25", "XT2127-26", "XT2127-27", "XT2127-28", "XT2127-29", "XT2127-30", "XT2127-31", "XT2127-32", "XT2127-33", "XT2127-34", "XT2127-35", "XT2127-36", "XT2127-37", "XT2127-38", "XT2127-39", "XT2127-40", "XT2127-41", "XT2127-42", "XT2127-43", "XT2127-44", "XT2127-45", "XT2127-46", "XT2127-47", "XT2127-48", "XT2127-49", "XT2127-50", "XT2127-51", "XT2127-52", "XT2127-53", "XT2127-54", "XT2127-55", "XT2127-56", "XT2127-57", "XT2127-58", "XT2127-59", "XT2127-60", "XT2127-61", "XT2127-62", "XT2127-63", "XT2127-64", "XT2127-65", "XT2127-66", "XT2127-67", "XT2127-68", "XT2127-69", "XT2127-70", "XT2127-71", "XT2127-72", "XT2127-73", "XT2127-74", "XT2127-75", "XT2127-76", "XT2127-77", "XT2127-78", "XT2127-79", "XT2127-80", "XT2127-81", "XT2127-82", "XT2127-83", "XT2127-84", "XT2127-85", "XT2127-86", "XT2127-87", "XT2127-88", "XT2127-89", "XT2127-90", "XT2127-91", "XT2127-92", "XT2127-93", "XT2127-94", "XT2127-95", "XT2127-96", "XT2127-97", "XT2127-98", "XT2127-99", "XT2127-100", "XT2127-101", "XT2127-102", "XT2127-103", "XT2127-104", "XT2127-105", "XT2127-106", "XT2127-107", "XT2127-108", "XT2127-109", "XT2127-110", "XT2127-111", "XT2127-112", "XT2127-113", "XT2127-114", "XT2127-115", "XT2127-116", "XT2127-117", "XT2127-118", "XT2127-119", "XT2127-120", "XT2127-121", "XT2127-122", "XT2127-123", "XT2127-124", "XT2127-125", "XT2127-126", "XT2127-127", "XT2127-128", "XT2127-129", "XT2127-130", "XT2127-131", "XT2127-132", "XT2127-133", "XT2127-134", "XT2127-135", "XT2127-136", "XT2127-137", "XT2127-138", "XT2127-139", "XT2127-140", "XT2127-141", "XT2127-142", "XT2127-143", "XT2127-144", "XT2127-145", "XT2127-146", "XT2127-147", "XT2127-148", "XT2127-149", "XT2127-150", "XT2127-151", "XT2127-152", "XT2127-153"],
    "nokia": ["Nokia X20", "Nokia X10", "Nokia G20", "Nokia G10", "Nokia 8.3 5G", "Nokia 5.4", "Nokia 3.4", "Nokia 2.4", "Nokia 8.1", "Nokia 7.2", "Nokia 6.2", "Nokia 4.2", "Nokia 3.2", "Nokia 2.2", "Nokia 9 PureView", "Nokia 8 Sirocco", "Nokia 8", "Nokia 7 Plus", "Nokia 7.1", "Nokia 6.1 Plus", "Nokia 6.1", "Nokia 5.1 Plus", "Nokia 5.1", "Nokia 4.1", "Nokia 3.1 Plus", "Nokia 3.1", "Nokia 2.1", "Nokia 1", "TA-1337", "TA-1380", "TA-1395", "TA-1208", "TA-1208", "TA-1334", "TA-1336", "TA-1230", "TA-1239", "TA-1283", "TA-1335", "TA-1234", "TA-1347", "TA-1353", "TA-1340", "TA-1233", "TA-1338", "TA-1386", "TA-1307", "TA-1296", "TA-1281", "TA-1333", "TA-1244", "TA-1235", "TA-1357", "TA-1236", "TA-1339", "TA-1316", "TA-1329", "TA-1343", "TA-1354", "TA-1300", "TA-1303", "TA-1289", "TA-1315", "TA-1287", "TA-1342", "TA-1351", "TA-1331", "TA-1325", "TA-1295", "TA-1240", "TA-1286", "TA-1328", "TA-1284", "TA-1293", "TA-1341", "TA-1292", "TA-1327", "TA-1298", "TA-1323", "TA-1238", "TA-1291", "TA-1345", "TA-1309", "TA-1344", "TA-1324", "TA-1346", "TA-1326", "TA-1304", "TA-1320", "TA-1348", "TA-1318", "TA-1330", "TA-1280", "TA-1246", "TA-1248", "TA-1317", "TA-1299", "TA-1310", "TA-1350", "TA-1332", "TA-1242", "TA-1206", "TA-1294", "TA-1313", "TA-1249", "TA-1241", "TA-1216", "TA-1297", "TA-1285", "TA-1319", "TA-1243", "TA-1356"],   
    "xiaomi": ["Mi 11", "Mi 10 Pro", "Mi 9T","M2101K7AG","M2003J15SC","M2004J19C","M2006C3LG","M2007J20CG","M2010J19CG","M2011K2C","M2012K11AG","M2101K7BG","M2101K9G","M2102J20SG","M2102K1G","M2012K11C","Redmi 6A","M2003J15SC","MI MAX 2","AT&amp;amp-T","Redmi Note 4","Redmi Note 5", "Redmi 4X","Redmi Note 8","Redmi Note 8 Pro","Xiaomi Mi 11 Ultra", "Xiaomi Mi 11 Pro", "Xiaomi Mi 11", "Xiaomi Mi 10 Ultra", "Xiaomi Mi 10 Pro", "Xiaomi Mi 10", "Xiaomi Mi 10T Pro", "Xiaomi Mi 10T", "Xiaomi Mi 9T Pro", "Xiaomi Mi 9T", "Xiaomi Mi 9 Pro 5G", "Xiaomi Mi 9", "Xiaomi Mi 8 Pro", "Xiaomi Mi 8", "Xiaomi Mi 8 Lite", "Xiaomi Mi 8 SE", "Xiaomi Mi Mix 3", "Xiaomi Mi Mix 2S", "Xiaomi Mi Mix 2", "Xiaomi Mi Mix", "Xiaomi Redmi Note 11 Pro+", "Xiaomi Redmi Note 11 Pro", "Xiaomi Redmi Note 11", "Xiaomi Redmi Note 10 Pro", "Xiaomi Redmi Note 10", "Xiaomi Redmi Note 9 Pro", "Xiaomi Redmi Note 9", "Xiaomi Redmi Note 8 Pro", "Xiaomi Redmi Note 8", "Xiaomi Redmi Note 7 Pro", "Xiaomi Redmi Note 7", "Xiaomi Redmi K40 Pro", "Xiaomi Redmi K40", "Xiaomi Redmi K30 Pro", "Xiaomi Redmi K30", "Xiaomi Redmi K20 Pro", "Xiaomi Redmi K20", "Xiaomi Poco X3 Pro", "Xiaomi Poco X3", "Xiaomi Poco X2", "Xiaomi Poco F3", "Xiaomi Poco F2 Pro", "Xiaomi Poco F1"],
    "samsung": ["Galaxy S21", "Galaxy A52", "Galaxy S20","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935F","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820","SPH-L720","SM-S906E", "Samsung Galaxy S21 Ultra", "Samsung Galaxy S21+", "Samsung Galaxy S21", "Samsung Galaxy Note 20 Ultra", "Samsung Galaxy Note 20", "Samsung Galaxy S20 Ultra", "Samsung Galaxy S20+", "Samsung Galaxy S20", "Samsung Galaxy Note 10+", "Samsung Galaxy Note 10", "Samsung Galaxy S10+", "Samsung Galaxy S10", "Samsung Galaxy Note 9", "Samsung Galaxy S9+", "Samsung Galaxy S9", "Samsung Galaxy Note 8", "Samsung Galaxy S8+", "Samsung Galaxy S8", "Samsung Galaxy Note 7", "Samsung Galaxy S7 Edge", "Samsung Galaxy S7", "Samsung Galaxy Note 5", "Samsung Galaxy S6 Edge+", "Samsung Galaxy S6 Edge", "Samsung Galaxy S6", "Samsung Galaxy Note 4", "Samsung Galaxy S5", "Samsung Galaxy S4", "Samsung Galaxy S3", "Samsung Galaxy Note 3", "SM-G991", "SM-G981", "SM-G973", "SM-G960", "SM-G950", "SM-G930", "SM-G920", "SM-G900", "GT-I9500", "GT-I9300", "GT-I9100", "GT-I9000", "SM-N981", "SM-N970", "SM-N960", "SM-N950", "SM-N920", "SM-N910", "SM-N900", "GT-N7100", "GT-N7000", "SM-G991", "SM-G981", "SM-G973", "SM-G960", "SM-G950", "SM-G930", "SM-G920", "SM-G900", "GT-I9500", "GT-I9300", "GT-I9100", "GT-I9000", "SM-N981", "SM-N970", "SM-N960", "SM-N950", "SM-N920", "SM-N910", "SM-N900", "GT-N7100", "GT-N7000", "SM-A526B", "SM-A516B", "SM-A516N", "SM-A526U", "SM-A716U", "SM-A716V", "SM-A5260", "SM-A526W", "SM-A126U", "SM-A126V", "SM-A016G", "SM-A016B", "SM-A016M", "SM-A025M", "SM-A025F", "SM-A217F", "SM-A217M", "SM-A207F", "SM-A207M", "SM-A102U", "SM-A102U1", "SM-A102W", "SM-A102N", "SM-A1020", "SM-A105F", "SM-A105G", "SM-A105M", "SM-A202F", "SM-A202G", "SM-A202M", "SM-A125U", "SM-A125V", "SM-A022G", "SM-A022M", "SM-A027G", "SM-A027M", "SM-A2170", "SM-A115M", "SM-A107M", "SM-A107F", "SM-A107M", "SM-A0220", "SM-A115F", "SM-A102F", "SM-A1050"],
    "vivo": ["Vivo_X60_Pro", "Vivo_X50_Pro", "Vivo_X30_Pro", "Vivo_X27", "Vivo_X23", "Vivo_X21", "Vivo_V21", "Vivo_V17", "Vivo_V15", "Vivo_V11", "Vivo_V9", "Vivo_Y95", "Vivo_Y91", "Vivo_Y81", "Vivo_Y71", "Vivo_S1", "V2056", "V2112A", "V2112", "V2122A", "V2120A", "V2120", "V2116A", "V2114A", "V2112A", "V2010A", "V2019A", "V2010", "V2003A", "V2002A", "V2002", "V1932A", "V1932T", "V1932", "V1929A", "V1928A", "V1928T", "V1928", "V1927A", "V1926A", "V1925A", "V1925", "V1924A", "V1922A", "V1921A", "V1921", "V1920A", "V1919A", "V1916A", "V1916", "V1912A", "V1911A", "V1910A", "V1910", "V1909A", "V1907A", "V1905", "V1903A", "V1901A", "V1901T", "V1901", "V1836", "V1824A", "V1824T", "V1824", "V1818A", "V1818T", "V1813A", "V1813T", "V1813", "V1812A", "V1811A", "V1811T", "V1811", "V1808A", "V1808T", "V1808", "V1801A", "V1801T", "V1801", "V1730T", "V1730F", "V1730A", "V1730", "V1724A", "V1723A", "V1723", "V1721A", "V1720A", "V1720T", "V1720", "V1716A", "V1715A", "V1715", "V1713A", "V1713", "V1712A", "V1712", "V1711T", "V1711A", "V1711", "V1709A", "V1709T", "V1709", "V1708A", "V1708T", "V1707A", "V1707T", "V1706T", "V1706", "V1703A", "V1701A", "V1701", "V1624A", "V1623A", "V1622A", "V1622", "V1621A", "V1619", "V1618A", "V1617A", "V1616", "V1615T", "V1614T", "V1613", "V1611T", "V1611", "V1608A", "V1609", "V1605", "V1604", "V1603", "V1601", "V1570", "V1562", "V1561", "V1550", "V1548", "V1546", "V1543", "V1542", "V1540", "V1530", "V1520", "V1510", "V1500", "V1420", "V1400", "V1310", "V1320"],
    "zte": ["ZTE_Axon_10_Pro", "ZTE_Axon_9", "ZTE_Axon_7", "ZTE_Axon_7_Mini", "ZTE_Blade_20", "ZTE_Blade_10", "ZTE_Blade_V10", "ZTE_Blade_V9", "ZTE_Blade_X", "ZTE_Blade_A7", "ZTE_Nubia_Red_Magic", "ZTE_Nubia_Z20", "ZTE_Nubia_X", "ZTE_Nubia_Z18", "ZTE_Nubia_Z17","Axon_10_Pro", "Axon_9", "Axon_7", "Axon_7_Mini", "Blade_20", "Blade_10", "Blade_V10", "Blade_V9", "Blade_X", "Blade_A7", "Nubia_Red_Magic", "Nubia_Z20", "Nubia_X", "Nubia_Z18", "Nubia_Z17"],
    "lg": ["LG_G8", "LG_V50", "LG_V40", "LG_G7", "LG_V30", "LG_G6", "LG_V20", "LG_G5", "LG_V10", "LG_G4", "LG_G3", "LG_G2", "LG_G_Flex"],
    "huawei": ["Huawei_P40", "Huawei_P30", "Huawei_P20", "Huawei_Mate_30", "Huawei_Mate_20", "Huawei_Mate_10", "Huawei_Nova_5", "Huawei_Nova_4", "Huawei_Nova_3", "Huawei_P10", "Huawei_P9", "Huawei_Honor_9", "Huawei_Honor_8", "Huawei_Y9", "Huawei_Y8"],
    "oneplus": ["OnePlus_9_Pro", "OnePlus_9", "OnePlus_8T", "OnePlus_8_Pro", "OnePlus_8", "OnePlus_7T_Pro", "OnePlus_7T", "OnePlus_7_Pro", "OnePlus_7", "OnePlus_6T", "OnePlus_6", "OnePlus_5T", "OnePlus_5", "OnePlus_3T", "OnePlus_3"]}
    fbcr = random.choice(fbcr_values)
    fbmf = random.choice(list(fbmf_fbdv_dict.keys()))
    fbdv = random.choice(fbmf_fbdv_dict[fbmf])
    color = random.choice(['\033[91m','\033[92m','\033[93m','\033[94m','\033[95m','\033[96m','\033[97m'])
    user_agent = f"[FBAN/FB4A;FBAV/"+str(random.randint(199,399))+".0.0."+str(random.randint(1,9))+"."+str(random.randint(99,199))+";FBBV/"+str(random.randint(111111111,999999999))+";FBDM/{density="+str(random.randint(2,3))+"."+str(random.randint(0,5))+",width=1080,height="+str(random.randint(1400,1499))+"};FBLC/en_US;FBRV/"+str(random.randint(199,399))+".0.0."+str(random.randint(1,9))+"."+str(random.randint(99,199))+";FBCR/"+fbcr+";FBMF/"+fbmf+";FBBD/"+fbmf+";FBPN/com.facebook.katana;FBDV/"+fbdv+";FBSV/"+str(random.randint(9,12))+";FBOP/1;FBCA/arm64-v8a:]"
    return user_agent

import random
import string

def generate_user_agent():
    fbav = f"{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}"
    fbbv = str(random.randint(111111111, 999999999))
    fbrv = '0'
    random_seed = random.Random()
    adid = ''.join(random_seed.choices(string.hexdigits, k=16))
    device = random.choice(["HUAWEI MAR-LX1M", "Samsung SM-G960F", "OnePlus GM1913"])
    fbav_version = str(random.randint(49, 150))
    fbbv_version = str(random.randint(11111111, 77777777))
    carrier = random.choice(["Ooredoo TN", "Orange", "Vodafone", "T-Mobile"])
    ua_bgraph = f'[FBAN/FB4A;FBAV/{fbav_version}.0.0.{random.randrange(20, 49)}.{random.randint(11, 99)};FBBV/{fbbv_version};' \
                f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};FBDM/{{density=3.0,width=1080,height=2107}};FBLC/fr_FR;' \
                f'FBRV/{fbrv};FBCR/{carrier};FBMF/{device.split(" ")[0]};FBBD/{device.split(" ")[0]};' \
                f'FBPN/com.facebook.katana;FBDV/{device};FBSV/9;FBOP/1;FBCA/arm64-v8a:]'
    return ua_bgraph

ua_bgraph = generate_user_agent()

import requests
import random
import concurrent.futures as thread
import os
import string

def bgraph(uid, pw, path_file, extract_type, success_count, existing_uids):
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
    fbav = f'{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'
    fbbv = str(random.randint(111111111, 999999999))
    fbrv = '0'
    random_seed = random.Random()
    adid = ''.join(random_seed.choices(string.hexdigits, k=16))
    ua_bgraph = '[FBAN/FB4A;FBAV/' + str(random.randint(49, 66)) + '.0.0.' + str(random.randrange(20, 49)) + str(random.randint(11, 99)) + ';FBBV/' + str(random.randint(11111111, 77777777)) + ';' + '[FBAN/FB4A;FBAV/' + fbav + ';FBBV/' + fbbv + ';FBDM/{density=3.0,width=1080,height=2107};FBLC/fr_FR;FBRV/' + fbrv + ';FBCR/Ooredoo TN;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1M;FBSV/9;FBOP/1;FBCA/arm64-v8a:]'
    data = {
        'adid': f'{uuid.uuid4()}',
        'format': 'json',
        'device_id': f'{uuid.uuid4()}',
        'cpl': 'true',
        'family_device_id': f'{uuid.uuid4()}',
        'credentials_type': 'device_based_login_password',
        'error_detail_type': 'button_with_disabled',
        'source': 'device_based_login',
        'email': uid,
        'password': pw,
        'access_token': accessToken,
        'generate_session_cookies': '1',
        'meta_inf_fbmeta': '',
        'advertiser_id': f'{uuid.uuid4()}',
        'currently_logged_in_userid': '0',
        'locale': 'en_US',
        'client_country_code': 'US',
        'method': 'auth.login',
        'fb_api_req_friendly_name': 'authenticate',
        'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
    }
    headers = {
        'User-Agent': ua_bgraph,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'graph.facebook.com',
        'X-FB-Net-HNI': str(random.randint(10000, 99999)),
        'X-FB-SIM-HNI': str(random.randint(10000, 99999)),
        'X-FB-Connection-Type': 'MOBILE.LTE',
        'X-Tigon-Is-Retry': 'False',
        'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
        'x-fb-device-group': str(random.randint(1000, 9999)),
        'X-FB-Friendly-Name': 'ViewerReactionsMutation',
        'X-FB-Request-Analytics-Tags': 'graphservice',
        'X-FB-HTTP-Engine': 'Liger',
        'X-FB-Client-IP': 'True',
        'X-FB-Connection-Bandwidth': str(random.randint(20000000, 30000000)),
        'X-FB-Server-Cluster': 'True',
        'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'
    }
    url = 'https://graph.facebook.com/auth/login'
    try:
        if uid in existing_uids:
            print(f"     {yellow}[INFO] {red}ACCOUNT --> {white}{uid} {red}ALREADY EXISTS.")
            print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
            return
        response = requests.post(url,headers=headers,data=data).json()
        print(response)
        if 'access_token' in response:
            token = response['access_token']
            with open(path_file, 'a') as f:
                f.write(f"{uid}|{token}\n")
            print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
            print(f"     \033[32m[SUCCESS]\033[0m: EXTRACTED ACCOUNT ─────> {uid}.")
            print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
            success_count.append(uid)
        else:
            print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
            print(f"     \033[31m[FAILED]\033[0m: TO EXTRACT ACCOUNT ─────> {uid}.")
            print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    except Exception as e:
        print(f"     \033[1;31m ERROR EXTRACTING ACCOUNT: {uid}. Reason: {str(e)}\033[0m\n")

def proz(accounts_file, token_output_path, extract_type):
    success_count = []
    existing_uids = set()
    if os.path.exists(token_output_path):
        with open(token_output_path, 'r') as f:
            existing_uids = {line.split('|')[0] for line in f.readlines()}
    try:
        with open(accounts_file, 'r') as file:
            accounts = file.readlines()
        accounts = [line.strip() for line in accounts if '|' in line.strip()]
        if not accounts:
            print(f"NO VALID ACCOUNTS FOUND IN {accounts_file}.")
            return
        with thread.ThreadPoolExecutor(max_workers=30) as executor:
            futures = [executor.submit(bgraph, uid, pw, token_output_path, extract_type, success_count, existing_uids)
                       for uid, pw in [account.split('|') for account in accounts]]
            for future in futures:
                future.result()
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        print(f"     \033[1;34m[SUCCESS]\033[0m: {len(success_count)} {extract_type}(s) SUCCESSFULLY EXTRACTED.")
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    except FileNotFoundError:
        print(f"FILE NOT FOUND: {accounts_file}")
        return

def axl1():
    clear_screen()
    bryxpogii()
    folder_path = "/sdcard/boostphere"
    print(f"     {yellow}[01] {blue}FRA EXTRACT ACCOUNT")
    print(f"     {yellow}[02] {blue}FRA EXTRACT PAGES")
    print(f"     {yellow}[03] {blue}RPW EXTRACT ACCOUNT")
    print(f"     {yellow}[04] {blue}RPW EXTRACT PAGES")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    save_choice = input(f"    {green}Enter your choice: ").strip()
    if save_choice == '1':
        account_file = os.path.join(folder_path, "FRAACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '2':
        account_file = os.path.join(folder_path, "FRAPAGES.txt")
        extract_type = 'page'
    elif save_choice == '3':
        account_file = os.path.join(folder_path, "RPWACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '4':
        account_file = os.path.join(folder_path, "RPWPAGES.txt")
        extract_type = 'page'
    else:
        print("INVALID CHOICE. EXITING.")
        return
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    print(f"     \033[33mTHE FORMAT SHOULD BE \033[31muid|pass")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    file_path = input(f"     \033[33mPATH: ").strip()
    token_output_path = account_file
    proz(file_path, token_output_path, extract_type)

import requests
import random
import concurrent.futures as thread
import os
import string

def load_existing_tokens(path_file):
    if os.path.exists(path_file):
        with open(path_file, 'r') as f:
            return {line.split('|')[0] for line in f.readlines()}
    return set()

def bgraph_page(uid, pw, path_file, extract_type, success_count, existing_tokens):
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
    fbav = f'''{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'''
    fbbv = str(random.randint(111111111, 999999999))
    fbrv = '0'
    random_seed = random.Random()
    adid = ''.join(random_seed.choices(string.hexdigits, k=16))
    ua_bgraph = '[FBAN/FB4A;FBAV/' + str(random.randint(49, 66)) + '.0.0.' + str(random.randrange(20, 49)) + str(random.randint(11, 99)) + ';FBBV/' + str(random.randint(11111111, 77777777)) + ';' + '[FBAN/FB4A;FBAV/' + fbav + ';FBBV/' + fbbv + ';FBDM/{density=3.0,width=1080,height=2107};FBLC/fr_FR;FBRV/' + fbrv + ';FBCR/Ooredoo TN;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1M;FBSV/9;FBOP/1;FBCA/arm64-v8a:]'
    data = {
        'adid': f'{uuid.uuid4()}',
        'format': 'json',
        'device_id': f'{uuid.uuid4()}',
        'cpl': 'true',
        'family_device_id': f'{uuid.uuid4()}',
        'credentials_type': 'device_based_login_password',
        'error_detail_type': 'button_with_disabled',
        'source': 'device_based_login',
        'email': uid,
        'password': pw,
        'access_token': accessToken,
        'generate_session_cookies': '1',
        'meta_inf_fbmeta': '',
        'advertiser_id': f'{uuid.uuid4()}',
        'currently_logged_in_userid': '0',
        'locale': 'en_US',
        'client_country_code': 'US',
        'method': 'auth.login',
        'fb_api_req_friendly_name': 'authenticate',
        'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
    }
    headers = {
        'User-Agent': ua_bgraph,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'graph.facebook.com',
        'X-FB-Net-HNI': str(random.randint(10000, 99999)),
        'X-FB-SIM-HNI': str(random.randint(10000, 99999)),
        'X-FB-Connection-Type': 'MOBILE.LTE',
        'X-Tigon-Is-Retry': 'False',
        'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
        'x-fb-device-group': str(random.randint(1000, 9999)),
        'X-FB-Friendly-Name': 'ViewerReactionsMutation',
        'X-FB-Request-Analytics-Tags': 'graphservice',
        'X-FB-HTTP-Engine': 'Liger',
        'X-FB-Client-IP': 'True',
        'X-FB-Connection-Bandwidth': str(random.randint(20000000, 30000000)),
        'X-FB-Server-Cluster': 'True',
        'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'
    }
    url = 'https://graph.facebook.com/auth/login'
    try:
        if uid in existing_uids:
            print(f"     {white}ACCOUNT ─────> {red}{uid} {green}ALREADY EXISTS")
            print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
            return
        response = requests.post(url,headers=headers,data=data).json()
        if 'access_token' in response:
            token = response['access_token']
            pages = extract_fb_pages(token)
            if pages:
                for page in pages:
                    page_id = page['id']
                    if page_id not in existing_tokens:
                        with open(path_file, 'a') as f:
                            f.write(f"{page_id}|{page['accessToken']}\n")
                        print(f"{white}{uid}  ─────> {green}PAGE ID: {red}{page_id} {yellow}EXTRACTED SUCCESSFULLY")
                        existing_tokens.add(page_id)
                    else:
                        print(f"{white}ID:  {page_id} ─────> {green}ALREADY EXISTS ! ")
            else:
                print(f"{white}{uid} ─────> {red}DOESN'T HAVE PAGES !")
            success_count.append(uid)
        else:
            print(f"{white}{uid}  ─────> {red}FAILED TO EXTRACT ! ")
    except Exception as e:
        print(f"ERROR EXTRACTING ACCOUNT: {uid}. REASON: {str(e)}")

def extract_fb_pages(token):
    url = 'https://graph.facebook.com/v18.0/me/accounts'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    pages_data = []
    while url:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f'ERROR: {response.text}')
            return None
        data = response.json()
        for page in data.get('data', []):
            pages_data.append({
                'id': page.get('id'),
                'accessToken': page.get('access_token')
            })
        url = data.get('paging', {}).get('next')
    return pages_data

def prozc(accounts_file, token_output_path, extract_type):
    success_count = []
    existing_tokens = load_existing_tokens(token_output_path)
    try:
        with open(accounts_file, 'r') as file:
            accounts = file.readlines()
        accounts = [line.strip() for line in accounts if '|' in line.strip()]
        if not accounts:
            print(f"NO VALID ACCOUNTS FOUND IN {accounts_file}.")
            return
        with thread.ThreadPoolExecutor(max_workers=30) as executor:
            futures = [executor.submit(bgraph_page, uid, pw, token_output_path, extract_type, success_count, existing_tokens)
                       for uid, pw in [account.split('|') for account in accounts]]
            for future in futures:
                future.result()
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        print(f"     \033[1;34m[SUCCESS]\033[0m: {len(success_count)} {extract_type}(s) SUCCESSFULLY EXTRACTED.")
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    except FileNotFoundError:
        print(f"FILE NOT FOUND: {accounts_file}")

def axl2():
    clear_screen()
    bryxpogii()
    folder_path = "/sdcard/boostphere"  
    print(f"     {yellow}[01] {blue}FRA EXTRACT ACCOUNT")
    print(f"     {yellow}[02] {blue}FRA EXTRACT PAGES")
    print(f"     {yellow}[03] {blue}RPW EXTRACT ACCOUNT")
    print(f"     {yellow}[04] {blue}RPW EXTRACT PAGES")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    save_choice = input(f"    {green}Enter your choice: ").strip()
    if save_choice == '1':
        account_file = os.path.join(folder_path, "FRAACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '2':
        account_file = os.path.join(folder_path, "FRAPAGES.txt")
        extract_type = 'page'
    elif save_choice == '3':
        account_file = os.path.join(folder_path, "RPWACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '4':
        account_file = os.path.join(folder_path, "RPWPAGES.txt")
        extract_type = 'page'
    else:
        print("INVALID CHOICE. EXITING.")
        return
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    print(f"     \033[33mTHE FORMAT SHOULD BE \033[31muid|pass")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    file_path = input(f"     \033[33mPATH: ").strip()
    prozc(file_path, account_file, extract_type)

def remove_duplicates():
    clear_screen()
    bryxpogii()
    file_paths = {
        "1": "/sdcard/boostphere/FRAACCOUNT.txt",
        "2": "/sdcard/boostphere/FRAPAGES.txt",
        "3": "/sdcard/boostphere/RPWACCOUNT.txt",
        "4": "/sdcard/boostphere/RPWPAGES.txt"
    }
    print(f"     {blue}CHOOSE WHICH FILE TO REMOVE DUPLICATES FROM:")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    print(f"     {yellow}[1]  {blue}FRA ACCOUNT")
    print(f"     {yellow}[2]  {blue}FRA PAGES")
    print(f"     {yellow}[3]  {blue}RPW ACCOUNT")
    print(f"     {yellow}[4]  {blue}RPW PAGES")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    choice = input(f"    {green}Enter your choice: ").strip()
    if choice not in file_paths:
        print("INVALID CHOICE. PLEASE TRY AGAIN.")
        return
    file_path = file_paths[choice]
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        seen_uids = set()
        unique_lines = []
        for line in lines:
            if '|' in line:
                uid, password = line.split('|', 1)
                if uid not in seen_uids:
                    unique_lines.append(line)
                    seen_uids.add(uid)
        with open(file_path, 'w') as file:
            file.writelines(unique_lines)
        print(f"     {green}SUCCESSFULLY REMOVED DUPLICATES FROM: {file_path}")
    except Exception as e:
        print(f"ERROR PROCESSING {file_path}: {str(e)}")

import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def perform_reaction_vid(token, uid_url, reaction_type, reactions_count):
    access_token = token.split('|')[1]
    auto_react_url = f'https://graph.facebook.com/{uid_url}/reactions?type={reaction_type}&access_token={access_token}'
    try:
        response = requests.post(auto_react_url)
        return access_token, response.status_code, response.text
    except requests.exceptions.RequestException as e:
        return access_token, None, str(e)

def clear_text_files():
    clear_screen()
    bryxpogii()
    file_paths = {
        "1": "/sdcard/boostphere/FRAACCOUNT.txt",
        "2": "/sdcard/boostphere/FRAPAGES.txt",
        "3": "/sdcard/boostphere/RPWACCOUNT.txt",
        "4": "/sdcard/boostphere/RPWPAGES.txt"
    }
    print(f"     {blue}CHOOSE FILE TO RESET:")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    print(f"     {yellow}[01]  {blue}FRA ACCOUNT")
    print(f"     {yellow}[02]  {blue}FRA PAGES")
    print(f"     {yellow}[03]  {blue}RPW ACCOUNT")
    print(f"     {yellow}[04]  {blue}RPW PAGES")
    print(f"     {yellow}[05]  {blue}ALL FILES")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    user_choice = input(f"    {green}Enter your choice: ").strip()
    if user_choice == '5':
        for file_path in file_paths.values():
            try:
                with open(file_path, 'w') as file:
                    file.truncate(0)
                print(f"SUCCESSFULLY CLEARED: {file_path}")
            except Exception as e:
                print(f"ERROR CLEARING {file_path}: {str(e)}")
        return
    selected_file = file_paths.get(user_choice)
    if selected_file:
        try:
            with open(selected_file, 'w') as file:
                file.truncate(0)
            print(f"SUCCESSFULLY CLEARED: {selected_file}")
        except Exception as e:
            print(f"ERROR CLEARING {selected_file}: {str(e)}")
    else:
        print("INVALID CHOICE. PLEASE ENTER A VALID NUMBER.")

def perform_reaction_fast_vid():
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    bryxpogii()
    print(f"""     {blue}CHOOSE TYPE OF REACTORS: 
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m
     {yellow}[01] {blue}FRA ACCOUNT 
     {yellow}[02] {blue}FRA PAGES
     {yellow}[03] {blue}RPW ACCOUNT
     {yellow}[04] {blue}RPW PAGES
     {red}[0]  {red}EXIT 
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m""")
    try:
        file_choice = int(input(f"    {green}Enter your choice: ").strip())
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        if file_choice not in file_options:
            print("INVALID CHOICE.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("PLEASE ENTER A VALID NUMBER.")
        return
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print("FILE NOT FOUND.")
        return
    except Exception as e:
        print(f"ERROR LOADING TOKENS: {e}")
        return
    available_tokens = len(tokens)
    if available_tokens == 0:
        print("NO TOKENS AVAILABLE FROM THE SELECTED FILE.")
        return
    try:
        start_line = int(input(f"    {green}Enter the starting line {red}(1 to {available_tokens}{red}): "))
        if start_line < 1 or start_line > available_tokens:
            print(f"PLEASE ENTER A VALID LINE NUMBER BETWEEN 1 AND {available_tokens}.")
            return
    except ValueError:
        print("PLEASE ENTER A VALID NUMBER.")
        return
    tokens = tokens[start_line - 1:]
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    print(f"    {green}FORMAT {yellow}: {red}https://www.facebook.com/100078043222260/videos/539673715119122/?mibextid=rS40aB7S9Ucbxw6v")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    post_link = input(f"   {green}Enter the post link or ID: ")
    uid_url = extract_facebook_video_id(post_link)
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    print(f"""    {blue}CHOOSE THE REACTION TYPE:
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m
     {yellow}[1] {blue}LIKE
     {yellow}[2] {blue}LOVE
     {yellow}[3] {blue}WOW
     {yellow}[4] {blue}SAD
     {yellow}[5] {blue}ANGRY
     {yellow}[6] {blue}HAHA
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m""")
    try:
        reaction_choice = int(input(f"    {green}Enter your choice: ").strip())
        reaction_map = {
            1: "LIKE",
            2: "LOVE",
            3: "WOW",
            4: "SAD",
            5: "ANGRY",
            6: "HAHA"
        }
        reaction_type = reaction_map.get(reaction_choice, None)
        if reaction_type is None:
            print("INVALID REACTION CHOICE.")
            return
    except ValueError:
        print("PLEASE ENTER A VALID NUMBER.")
        return
    try:
        num_reactions = int(input(f"     {yellow}Enter the number of reactions: "))
    except ValueError:
        print(f"PLEASE ENTER A VALID NUMBER FOR REACTIONS.")
        return
    if num_reactions > len(tokens):
        print(f"{red}ENTER AGAIN NOT EXCEEDING {len(tokens)}")
        return
    reactions_count = 0
    max_workers = 15
    while reactions_count < num_reactions and tokens:
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_token = {executor.submit(perform_reaction_vid, token, uid_url, reaction_type): token for token in tokens}
            for future in as_completed(future_to_token):
                token = future_to_token[future]
                try:
                    access_token, status_code, response_text = future.result()
                    if status_code == 200:
                        reactions_count += 1
                        print(f"   {green}[SUCCESS] SUCCESSFULLY REACTED TO {white}───────> {red}{uid_url}")
                        if reactions_count >= num_reactions:
                            break
                    else:
                        print(f"   {green}[FAILED] FAILED TO SEND REACTION  {white}───────> {red}{uid_url}")
                except Exception as e:
                    print(f"ERROR PROCESSING TOKEN {token}: {str(e)}")
        tokens = tokens[len(future_to_token):]
    print(f"REACTIONS COMPLETE! {reactions_count} REACTIONS WERE SUCCESSFULLY SENT.")
    print(f"TOTAL REACTIONS SENT: {reactions_count} OUT OF {num_reactions}")

import requests

def fetch_account_info(file_options):
    clear_screen()
    bryxpogii()
    print(f"     {blue}CHOOSE WHICH FILE YOU WANT TO CHECK:")
    print(f"\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    for key, value in file_options.items():
        print(f"     {red}[{key}] {yellow}{value.split('/')[-1]}")
    print(f"\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    file_choice = int(input(f"    {green}Enter your choice: ").strip())
    accounts_file = file_options.get(file_choice)
    if accounts_file is None:
        print("INVALID CHOICE. EXITING.")
        return
    try:
        with open(accounts_file, 'r') as file:
            accounts = file.readlines()
        for account in accounts:
            uid, token = account.strip().split('|')
            account_info = get_account_info(token)
            if account_info:
                account_name = account_info.get('name', 'No name available')
                print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
                print(f"     {yellow}ACCOUNT NAME {red}: {green}{account_name}")
                pages = extract_fb_pages(token)
                if pages:
                    print()
                    print(f"          {yellow}PAGES ASSOCIATED WITH {white}: {red}{account_name}")
                    for page in pages:
                        print()
                        print(f"       👉 {yellow}{page['name']} {white}= {green}PAGE ID: {red}{page['id']}")
                        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
                else:
                    print(f"     {red}NO PAGES ASSOCIATED WITH THIS ACCOUNT ! .")
            else:
                print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
                print(f"     {yellow}FAILED TO FETCH ACCOUNT INFORMATION ! {white}= {red}{uid}")
    except FileNotFoundError:
        print(f"FILE NOT FOUND: {accounts_file}")
    except Exception as e:
        print(f"ERROR {str(e)}")

def get_account_info(token):
    url = 'https://graph.facebook.com/v18.0/me'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            pass
            return None
    except Exception as e:
        print(f"ERROR FETCHING ACCOUNT INFO: {str(e)}")
        return None

def extract_fb_pages(token):
    url = 'https://graph.facebook.com/v18.0/me/accounts'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    pages_data = []
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            for page in data.get('data', []):
                pages_data.append({
                    'id': page.get('id'),
                    'name': page.get('name'),
                    'accessToken': page.get('access_token')
                })
            return pages_data
        else:
            print(f"FAILED TO FETCH PAGES: {response.text}")
            return None
    except Exception as e:
        print(f"ERROR FETCHING PAGES: {str(e)}")
        return None

file_options = {
    1: "/sdcard/boostphere/FRAACCOUNT.txt",
    2: "/sdcard/boostphere/FRAPAGES.txt",
    3: "/sdcard/boostphere/RPWACCOUNT.txt",
    4: "/sdcard/boostphere/RPWPAGES.txt"
}

import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def perform_reaction(token, uid_url, reaction_type):
    access_token = token.split('|')[1]
    auto_react = f'https://graph.facebook.com/{uid_url}/reactions?type={reaction_type}&access_token={access_token}'
    headers_ = {
        'User-Agent': W_ueragnt()
    }
    try:
        response = requests.post(auto_react, headers=headers_)
        return access_token, response.status_code, response.text
    except requests.exceptions.RequestException as e:
        return access_token, None, str(e)

def perform_reaction_fast():
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    bryxpogii()
    print(f"""     {blue}CHOOSE TYPE OF REACTORS: 
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m
     {yellow}[1] {blue}FRA ACCOUNT 
     {blue}[2] {blue}FRA PAGES
     {blue}[3] {blue}RPW ACCOUNT
     {blue}[4] {blue}RPW PAGES
     {red}[0]  {red}EXIT 
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m""")
    try:
        file_choice = int(input(f"    {green}Enter your choice: ").strip())
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        if file_choice not in file_options:
            print("INVALID CHOICE.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("PLEASE ENTER A VALID NUMBER.")
        return
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print("FILE NOT FOUND.")
        return
    except Exception as e:
        print(f"ERROR LOADING TOKENS: {e}")
        return
    available_tokens = len(tokens)
    if available_tokens == 0:
        print("NO TOKENS AVAILABLE FROM THE SELECTED FILE.")
        return
    try:
        start_line = int(input(f"    {green}Enter the starting line {red}(1 to {available_tokens}{red}): "))
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        if start_line < 1 or start_line > available_tokens:
            print(f"PLEASE ENTER A VALID LINE NUMBER BETWEEN 1 AND {available_tokens}.")
            return
    except ValueError:
        print("PLEASE ENTER A VALID NUMBER.")
        return
    tokens = tokens[start_line - 1:]
    print(f"    {green}FORMAT {yellow}: {red}https://www.facebook.com/100078043222260/posts/110105688267538/?mibextid=rS40aB7S9Ucbxw6v")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    z = input(f"   {green}Enter the post link or ID: ")
    post_id = extract_ids(z)
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    uid_url = post_id
    print(f"""    {blue}CHOOSE THE REACTION TYPE:
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m
     {yellow}[1] {blue}LIKE
     {yellow}[2] {blue}LOVE
     {yellow}[3] {blue}WOW
     {yellow}[4] {blue}SAD
     {yellow}[5] {blue}ANGRY
     {yellow}[6] {blue}HAHA
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m""")
    try:
        reaction_choice = int(input(f"    {green}Enter your choice: ").strip())
        reaction_map = {
            1: "LIKE",
            2: "LOVE",
            3: "WOW",
            4: "SAD",
            5: "ANGRY",
            6: "HAHA"
        }
        reaction_type = reaction_map.get(reaction_choice, None)
        if reaction_type is None:
            print("INVALID REACTION CHOICE.")
            return
    except ValueError:
        print("PLEASE ENTER A VALID NUMBER.")
        return
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    try:
        num_reactions = int(input(f"     {yellow}Enter the number of reactions: "))
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    except ValueError:
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        print("PLEASE ENTER A VALID NUMBER FOR REACTIONS.")
        return
    max_workers = 15
    reactions_count = 0
    total_successful_reactions = 0
    results = []
    tokens_used = 0
    while total_successful_reactions < num_reactions and tokens_used < available_tokens:
        remaining_tokens = tokens[tokens_used:]
        tokens_batch = remaining_tokens[:num_reactions - total_successful_reactions]
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_token = {executor.submit(perform_reaction, token, uid_url, reaction_type): token for token in tokens_batch}
            for future in as_completed(future_to_token):
                token = future_to_token[future]
                uid = token.split('|')[0]
                try:
                    access_token, status_code, response_text = future.result()
                    if status_code == 200:
                        reactions_count += 1
                        total_successful_reactions += 1
                        print(f"     {red}[REACTOR] {yellow}{uid}  {blue}───────> {green}SUCCESSFULLY REACTED!")
                        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
                    else:
                        print(f"     {red}[REACTOR] {yellow}{uid}  {blue}───────> {red}FAILED TO REACT!")
                        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
                except Exception as e:
                    print(f"ERROR PROCESSING TOKEN {token}: {e}")
        tokens_used += len(tokens_batch)
        if tokens_used >= available_tokens:
            print("NO MORE TOKENS AVAILABLE.")
            break            
    print(f"\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    print(f"{green}TOTAL SUCCESSFUL REACTIONS: {total_successful_ractions}")

import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def perform_reaction(token, uid_url, reaction_type):
    access_token = token.split('|')[1]
    auto_react = f'https://graph.facebook.com/{uid_url}/reactions?type={reaction_type}&access_token={access_token}'
    headers_ = {
        'User-Agent': W_ueragnt()
    }
    try:
        response = requests.post(auto_react, headers=headers_)
        return access_token, response.status_code, response.text
    except requests.exceptions.RequestException as e:
        return access_token, None, str(e)

def live_react():
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    bryxpogii()
    print(f"""     {blue}CHOOSE TYPE OF REACTORS: 
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m
     {yellow}[1] {blue}FRA ACCOUNT 
     {yellow}[2] {blue}FRA PAGES
     {yellow}[3] {blue}RPW ACCOUNT
     {yellow}[4] {blue}RPW PAGES
     {red}[0] {red}EXIT 
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m""")
    try:
        file_choice = int(input(f"    {green}Enter your choice: ").strip())
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        if file_choice not in file_options:
            print("INVALID CHOICE.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("PLEASE ENTER A VALID NUMBER.")
        return
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print("FILE NOT FOUND.")
        return
    except Exception as e:
        print(f"ERROR LOADING TOKENS: {e}")
        return
    available_tokens = len(tokens)
    if available_tokens == 0:
        print("NO TOKENS AVAILABLE FROM THE SELECTED FILE.")
        return
    try:
        start_line = int(input(f"    {green}Enter the starting line {red}(1 to {available_tokens}{red}): "))
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        if start_line < 1 or start_line > available_tokens:
            print(f"PLEASE ENTER A VALID LINE NUMBER BETWEEN 1 AND {available_tokens}.")
            return
    except ValueError:
        print("PLEASE ENTER A VALID NUMBER.")
        return
    tokens = tokens[start_line - 1:]
    print(f"    {green}FORMAT {yellow}: {red}https://www.facebook.com/100078043222260/video/110105688267538/")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    z = input(f"   {green}Enter the post link or ID: ")
    post_id = get_combined_data(z)
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    uid_url = post_id
    print(f"""    {blue}CHOOSE THE REACTION TYPE:
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m
     {yellow}[1] {blue}LIKE
     {yellow}[2] {blue}LOVE
     {yellow}[3] {blue}WOW
     {yellow}[4] {blue}SAD
     {yellow}[5] {blue}ANGRY
     {yellow}[6] {blue}HAHA
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m""")
    try:
        reaction_choice = int(input(f"    {green}Enter your choice: ").strip())
        reaction_map = {
            1: "LIKE",
            2: "LOVE",
            3: "WOW",
            4: "SAD",
            5: "ANGRY",
            6: "HAHA"
        }
        reaction_type = reaction_map.get(reaction_choice, None)
        if reaction_type is None:
            print("INVALID REACTION CHOICE.")
            return
    except ValueError:
        print("PLEASE ENTER A VALID NUMBER.")
        return
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    try:
        num_reactions = int(input(f"     {yellow}Enter the number of reactions: "))
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    except ValueError:
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        print("PLEASE ENTER A VALID NUMBER FOR REACTIONS.")
        return
    max_workers = 10
    reactions_count = 0
    total_successful_reactions = 0
    results = []
    tokens_used = 0
    while total_successful_reactions < num_reactions and tokens_used < available_tokens:
        remaining_tokens = tokens[tokens_used:]
        tokens_batch = remaining_tokens[:num_reactions - total_successful_reactions]
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_token = {executor.submit(perform_reaction, token, uid_url, reaction_type): token for token in tokens_batch}
            for future in as_completed(future_to_token):
                token = future_to_token[future]
                uid = token.split('|')[0]
                try:
                    access_token, status_code, response_text = future.result()
                    if status_code == 200:
                        reactions_count += 1
                        total_successful_reactions += 1
                        print(f"     {red}[REACTOR] {yellow}{uid}  {blue}───────> {green}SUCCESSFULLY REACTED!")
                    else:
                        pass
                except Exception as e:
                    print(f"ERROR PROCESSING TOKEN {token}: {e}")      
        tokens_used += len(tokens_batch)
        if tokens_used >= available_tokens:
            print("NO MORE TOKENS AVAILABLE.")
            break
    print(f"\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    print(f"{green}TOTAL SUCCESSFUL REACTIONS: {total_successful_reactions}")

def vid():
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    bryxpogii()
    print(f"""     {blue}CHOOSE TYPE OF REACTORS: 
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m
     {yellow}[1] {blue}FRA ACCOUNT 
     {yellow}[2] {blue}FRA PAGES
     {yellow}[3] {blue}RPW ACCOUNT
     {yellow}[4] {blue}RPW PAGES
     {red}[0] {red}EXIT 
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m""")
    try:
        file_choice = int(input(f"    {green}Enter your choice: ").strip())
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        if file_choice not in file_options:
            print("INVALID CHOICE.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("PLEASE ENTER A VALID NUMBER.")
        return
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print("FILE NOT FOUND.")
        return
    except Exception as e:
        print(f"ERROR LOADING TOKENS: {e}")
        return
    available_tokens = len(tokens)
    if available_tokens == 0:
        print("NO TOKENS AVAILABLE FROM THE SELECTED FILE.")
        return
    try:
        start_line = int(input(f"    {green}Enter the starting line {red}(1 to {available_tokens}{red}): "))
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        if start_line < 1 or start_line > available_tokens:
            print(f"PLEASE ENTER A VALID LINE NUMBER BETWEEN 1 AND {available_tokens}.")
            return
    except ValueError:
        print("PLEASE ENTER A VALID NUMBER.")
        return
    tokens = tokens[start_line - 1:]
    print(f"    {green}FORMAT {yellow}: {red}https://www.facebook.com/100078043222260/video/110105688267538/?mibextid=rS40aB7S9Ucbxw6v")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    z = input(f"   {green}Enter the post link or ID: ")
    post_id = get_combined_data(z)
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    uid_url = post_id
    print(f"""    {blue}CHOOSE THE REACTION TYPE:
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m
     {yellow}[1] {blue}LIKE
     {yellow}[2] {blue}LOVE
     {yellow}[3] {blue}WOW
     {yellow}[4] {blue}SAD
     {yellow}[5] {blue}ANGRY
     {yellow}[6] {blue}HAHA
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m""")
    try:
        reaction_choice = int(input(f"    {green}Enter your choice: ").strip())
        reaction_map = {
            1: "LIKE",
            2: "LOVE",
            3: "WOW",
            4: "SAD",
            5: "ANGRY",
            6: "HAHA"
        }
        reaction_type = reaction_map.get(reaction_choice, None)
        if reaction_type is None:
            print("INVALID REACTION CHOICE.")
            return
    except ValueError:
        print("PLEASE ENTER A VALID NUMBER.")
        return
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    try:
        num_reactions = int(input(f"     {yellow}Enter the number of reactions: "))
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    except ValueError:
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        print("PLEASE ENTER A VALID NUMBER FOR REACTIONS.")
        return
    max_workers = 10
    reactions_count = 0
    total_successful_reactions = 0
    results = []
    tokens_used = 0
    while total_successful_reactions < num_reactions and tokens_used < available_tokens:
        remaining_tokens = tokens[tokens_used:]
        tokens_batch = remaining_tokens[:num_reactions - total_successful_reactions]
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_token = {executor.submit(perform_reaction, token, uid_url, reaction_type): token for token in tokens_batch}
            for future in as_completed(future_to_token):
                token = future_to_token[future]
                uid = token.split('|')[0]
                try:
                    access_token, status_code, response_text = future.result()
                    if status_code == 200:
                        reactions_count += 1
                        total_successful_reactions += 1
                        print(f"     {red}[REACTOR] {yellow}{uid}  {blue}───────> {green}SUCCESSFULLY REACTED!")
                    else:
                        pass
                except Exception as e:
                    print(f"ERROR PROCESSING TOKEN {token}: {e}")
        tokens_used += len(tokens_batch)
        if tokens_used >= available_tokens:
            print("NO MORE TOKENS AVAILABLE.")
            break
    print(f"\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    print(f"{green}TOTAL SUCCESSFUL REACTIONS: {total_successful_reactions}")

import requests
import json
import time
import uuid
import base64
import re

def extract_reel_id(link):
    pattern = r'/reel/(\d+)'
    match = re.search(pattern, link)
    if match:
        return match.group(1)
    else:
        return None

def react_comment(token, uid_url, reaction_type, reactions_count):
    access_token = token.split('|')[1]
    url = f'https://graph.facebook.com/v18.0/{uid_url}/reactions'
    params = {
        'access_token': access_token,
        'type': reaction_type
    } 
    headers_ = {
        'User-Agent': W_ueragnt()
    }
    try:
        response = requests.post(url, params=params, headers=headers_)
        return access_token, response.status_code, response.text
    except requests.exceptions.RequestException as e:
        return access_token, None, str(e)

def comment_react():
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    bryxpogii()
    print(f"""     {blue}CHOOSE TYPE OF REACTORS: 
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m
     {yellow}[1] {blue}FRA ACCOUNT 
     {yellow}[2] {blue}FRA PAGES
     {yellow}[3] {blue}RPW ACCOUNT
     {yellow}[4] {blue}RPW PAGES
     {red}[0] {red}EXIT 
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m""")
    try:
        file_choice = int(input(f"    {green}Enter your choice: ").strip())
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        if file_choice not in file_options:
            print("INVALID CHOICE.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("PLEASE ENTER A VALID NUMBER.")
        return
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print("FILE NOT FOUND.")
        return
    except Exception as e:
        print(f"ERROR LOADING TOKENS: {e}")
        return
    available_tokens = len(tokens)
    if available_tokens == 0:
        print("NO TOKENS AVAILABLE FROM THE SELECTED FILE.")
        return
    try:
        start_line = int(input(f"    {green}Enter the starting line {red}(1 to {available_tokens}{red}): "))
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        if start_line < 1 or start_line > available_tokens:
            print(f"PLEASE ENTER A VALID LINE NUMBER BETWEEN 1 AND {available_tokens}.")
            return
    except ValueError:
        print("PLEASE ENTER A VALID NUMBER.")
        return
    tokens = tokens[start_line - 1:]
    print(f"    {green}FORMAT {yellow}: {red}https://www.facebook.com/100078043222260/posts/541319968479439/?mibextid=rS40aB7S9Ucbxw6v")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    post_id = input(f"   {green}POST ID: ")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    comment_id = input(f"   {green}COMMENT ID: ")
    uid_url = f"{post_id}_{comment_id}"
    print(f"""    {blue}CHOOSE THE REACTION TYPE:
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m
     {yellow}[1] {blue}LIKE
     {yellow}[2] {blue}LOVE
     {yellow}[3] {blue}WOW
     {yellow}[4] {blue}SAD
     {yellow}[5] {blue}ANGRY
     {yellow}[6] {blue}HAHA
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m""")
    try:
        reaction_choice = int(input(f"    {green}Enter your choice: ").strip())
        reaction_map = {
            1: "LIKE",
            2: "LOVE",
            3: "WOW",
            4: "SAD",
            5: "ANGRY",
            6: "HAHA"
        }
        reaction_type = reaction_map.get(reaction_choice, None)
        if reaction_type is None:
            print("INVALID REACTION CHOICE.")
            return
    except ValueError:
        print("PLEASE ENTER A VALID NUMBER.")
        return
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    try:
        num_reactions = int(input(f"     {yellow}Enter the number of reactions: "))
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    except ValueError:
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        print("PLEASE ENTER A VALID NUMBER FOR REACTIONS.")
        return
    if num_reactions > len(tokens):
        print(f"{red}ENTER AGAIN NOT EXCEEDING {len(tokens)}")
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        return
    reactions_count = 0
    failed_reactions = 0
    target_reactions = num_reactions
    remaining_tokens = tokens[:num_reactions]
    max_workers = 20
    results = []
    while reactions_count < target_reactions and remaining_tokens:
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_token = {executor.submit(react_comment, token, uid_url, reaction_type, reactions_count): token for token in remaining_tokens}
            for future in as_completed(future_to_token):
                token = future_to_token[future]
                uid = token.split('|')[0]
                try:
                    access_token, status_code, response_text = future.result()
                    if status_code == 200:
                        reactions_count += 1
                        print(f"     {red}[REACTOR] {yellow}{uid}  {blue}───────> {green}SUCCESSFULLY REACTED TO COMMENT!")
                        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
                    else:
                        failed_reactions += 1
                        pass
                except Exception as e:
                    print(f"ERROR PROCESSING TOKEN {token}: {e}")
        remaining_tokens = [token for token in remaining_tokens if token not in future_to_token]
        if failed_reactions > 0:
            print(f"{red}RETRYING FAILED REACTIONS...{blue}")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    print(f"{green}TOTAL: {reactions_count} SUCCESSFULLY REACTED")

import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def perform_reaction(token, uid_url, reaction_type):
    access_token = token.split('|')[1]
    auto_react = f'https://graph.facebook.com/{uid_url}/reactions?type={reaction_type}&access_token={access_token}'
    headers_ = {
        'User-Agent': W_ueragnt()
    }
    try:
        response = requests.post(auto_react, headers=headers_)
        return access_token, response.status_code, response.text
    except requests.exceptions.RequestException as e:
        return access_token, None, str(e)

def perform_reaction_fast():
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    bryxpogii()
    print(f"""     {blue}CHOOSE TYPE OF REACTORS: 
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m
     {yellow}[1] {blue}FRA ACCOUNT 
     {yellow}[2] {blue}FRA PAGES
     {yellow}[3] {blue}RPW ACCOUNT
     {yellow}[4] {blue}RPW PAGES
     {red}[0] {red}EXIT 
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m""")
    try:
        file_choice = int(input(f"    {green}Enter your choice: ").strip())
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        if file_choice not in file_options:
            print("INVALID CHOICE.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("PLEASE ENTER A VALID NUMBER.")
        return
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print("FILE NOT FOUND.")
        return
    except Exception as e:
        print(f"ERROR LOADING TOKENS: {e}")
        return
    available_tokens = len(tokens)
    if available_tokens == 0:
        print("NO TOKENS AVAILABLE FROM THE SELECTED FILE.")
        return
    try:
        start_line = int(input(f"    {green}Enter the starting line {red}(1 to {available_tokens}{red}): "))
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        if start_line < 1 or start_line > available_tokens:
            print(f"PLEASE ENTER A VALID LINE NUMBER BETWEEN 1 AND {available_tokens}.")
            return
    except ValueError:
        print("PLEASE ENTER A VALID NUMBER.")
        return
    tokens = tokens[start_line - 1:]
    print(f"    {green}FORMAT {yellow}: {red}https://www.facebook.com/100078043222260/posts/110105688267538/?mibextid=rS40aB7S9Ucbxw6v")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    z = input(f"   {green}Enter the post link or ID: ")
    post_id = get_combined_data(z)
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    uid_url = post_id
    print(f"""    {blue}CHOOSE THE REACTION TYPE:
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m
     {yellow}[1] {blue}LIKE
     {yellow}[2] {blue}LOVE
     {yellow}[3] {blue}WOW
     {yellow}[4] {blue}SAD
     {yellow}[5] {blue}ANGRY
     {yellow}[6] {blue}HAHA
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m""")
    try:
        reaction_choice = int(input(f"    {green}Enter your choice: ").strip())
        reaction_map = {
            1: "LIKE",
            2: "LOVE",
            3: "WOW",
            4: "SAD",
            5: "ANGRY",
            6: "HAHA"
        }
        reaction_type = reaction_map.get(reaction_choice, None)
        if reaction_type is None:
            print("INVALID REACTION CHOICE.")
            return
    except ValueError:
        print("PLEASE ENTER A VALID NUMBER.")
        return
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    try:
        num_reactions = int(input(f"     {yellow}Enter the number of reactions: "))
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    except ValueError:
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        print("PLEASE ENTER A VALID NUMBER FOR REACTIONS.")
        return
    max_workers = 10
    reactions_count = 0
    total_successful_reactions = 0
    results = []
    tokens_used = 0
    while total_successful_reactions < num_reactions and tokens_used < available_tokens:
        remaining_tokens = tokens[tokens_used:]
        tokens_batch = remaining_tokens[:num_reactions - total_successful_reactions]
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_token = {executor.submit(perform_reaction, token, uid_url, reaction_type): token for token in tokens_batch}
            for future in as_completed(future_to_token):
                token = future_to_token[future]
                uid = token.split('|')[0]
                try:
                    access_token, status_code, response_text = future.result()
                    if status_code == 200:
                        reactions_count += 1
                        total_successful_reactions += 1
                        print(f"     {red}[REACTOR] {yellow}{uid}  {blue}───────> {green}SUCCESSFULLY REACTED!")
                        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
                    else:
                        pass
                except Exception as e:
                    print(f"ERROR PROCESSING TOKEN {token}: {e}")
        tokens_used += len(tokens_batch)
        if tokens_used >= available_tokens:
            print("NO MORE TOKENS AVAILABLE.")
            break
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    print(f"{green}TOTAL SUCCESSFUL REACTIONS: {total_successful_reactions}")

import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def perform_reaction(token, uid_url, reaction_type):
    access_token = token.split('|')[1]
    auto_react = f'https://graph.facebook.com/{uid_url}/reactions?type={reaction_type}&access_token={access_token}'
    headers_ = {
        'User-Agent': W_ueragnt()
    }   
    try:
        response = requests.post(auto_react, headers=headers_)
        return access_token, response.status_code, response.text
    except requests.exceptions.RequestException as e:
        return access_token, None, str(e)

def reels():
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    bryxpogii()
    print(f"""     {blue}CHOOSE TYPE OF REACTORS:
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m
     {yellow}[1] {blue}FRA ACCOUNT 
     {yellow}[2] {blue}FRA PAGES
     {yellow}[3] {blue}RPW ACCOUNT
     {yellow}[4] {blue}RPW PAGES
     {red}[0] {red}EXIT 
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m""")   
    try:
        file_choice = int(input(f"    {green}Enter your choice: ").strip())
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        if file_choice not in file_options:
            print("INVALID CHOICE.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("PLEASE ENTER A VALID NUMBER.")
        return
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print("FILE NOT FOUND.")
        return
    except Exception as e:
        print(f"ERROR LOADING TOKENS: {e}")
        return
    available_tokens = len(tokens)
    if available_tokens == 0:
        print("NO TOKENS AVAILABLE FROM THE SELECTED FILE.")
        return
    try:
        start_line = int(input(f"    {green}Enter the starting line {red}(1 to {available_tokens}{red}): "))
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        if start_line < 1 or start_line > available_tokens:
            print(f"PLEASE ENTER A VALID LINE NUMBER BETWEEN 1 AND {available_tokens}.")
            return
    except ValueError:
        print("PLEASE ENTER A VALID NUMBER.")
        return
    tokens = tokens[start_line - 1:]
    print(f"    {green}FORMAT {yellow}: {red}https://www.facebook.com/reel/26674343208847358?mibextid=rS40aB7S9Ucbxw6v")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    z = input(f"   {green}Enter the post link or ID: ")
    post_id = get_combined_data(z)
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    uid_url = post_id
    print(f"""    {blue}CHOOSE THE REACTION TYPE:
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m
     {yellow}[1] {blue}LIKE
     {yellow}[2] {blue}LOVE
     {yellow}[3] {blue}WOW
     {yellow}[4] {blue}SAD
     {yellow}[5] {blue}ANGRY
     {yellow}[6] {blue}HAHA
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m""")
    try:
        reaction_choice = int(input(f"    {green}Enter your choice: ").strip())
        reaction_map = {
            1: "LIKE",
            2: "LOVE",
            3: "WOW",
            4: "SAD",
            5: "ANGRY",
            6: "HAHA"
        }
        reaction_type = reaction_map.get(reaction_choice, None)
        if reaction_type is None:
            print("INVALID REACTION CHOICE.")
            return
    except ValueError:
        print("PLEASE ENTER A VALID NUMBER.")
        return
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")   
    try:
        num_reactions = int(input(f"     {yellow}Enter the number of reactions: "))
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    except ValueError:
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        print("PLEASE ENTER A VALID NUMBER FOR REACTIONS.")
        return
    max_workers = 10
    reactions_count = 0
    total_successful_reactions = 0
    results = []
    tokens_used = 0
    while total_successful_reactions < num_reactions and tokens_used < available_tokens:
        remaining_tokens = tokens[tokens_used:]
        tokens_batch = remaining_tokens[:num_reactions - total_successful_reactions]
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_token = {executor.submit(perform_reaction, token, uid_url, reaction_type): token for token in tokens_batch}
            for future in as_completed(future_to_token):
                token = future_to_token[future]
                uid = token.split('|')[0]
                try:
                    access_token, status_code, response_text = future.result()
                    if status_code == 200:
                        reactions_count += 1
                        total_successful_reactions += 1
                        print(f"     {red}[REACTOR] {yellow}{uid}  {blue}───────> {green}SUCCESSFULLY REACTED!")
                    else:
                        pass
                except Exception as e:
                    print(f"ERROR PROCESSING TOKEN {token}: {e}")       
        tokens_used += len(tokens_batch)
        if tokens_used >= available_tokens:
            print("NO MORE TOKENS AVAILABLE.")
            break
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    print(f"{green}TOTAL SUCCESSFUL REACTIONS: {total_successful_reactions}")

from concurrent.futures import ThreadPoolExecutor
import re
import requests

def extract_user_id_prof(url):
    pattern = r'id=(\d+)|profile\.php\?id=(\d+)'
    match = re.search(pattern, url)
    if match:
        return match.group(1) or match.group(2)
    return None

def follow_account(page_access_token, account_id):
    headers_ = {
        'User-Agent': W_ueragnt()
    }
    headers = {
        'Authorization': f'Bearer {page_access_token}',
        **headers_
    }
    try:
        response = requests.post(
            f'https://graph.facebook.com/v18.0/{account_id}/subscribers',
            headers=headers
        )
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        print(f"REQUEST FAILED FOR TOKEN {page_access_token}: {e}")
        return False

def auto_follow_fast():
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    bryxpogii()
    print(f"""     {white}CHOOSE TYPE OF REACTORS: 
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m
     {yellow}[1] {blue}FRA ACCOUNT 
     {yellow}[2] {blue}FRA PAGES
     {yellow}[3] {blue}RPW ACCOUNT
     {yellow}[4] {blue}RPW PAGES
     {red}[0] {red}EXIT 
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m""")
    file_choice = int(input(f"    {green}Enter your choice: ").strip())
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    file_path = file_options.get(file_choice)
    if not file_path:
        print("INVALID CHOICE.")
        return
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print("FILE NOT FOUND.")
        return
    if len(tokens) == 0:
        print("NO TOKENS FOUND IN THE SELECTED FILE.")
        return
    start_line = int(input(f"    {yellow}Enter the starting line (1 to {len(tokens)}): "))
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    tokens = tokens[start_line - 1:]
    account_id = extract_user_id_prof(input(f"   {yellow}Enter the target account URL: "))
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    if not account_id:
        print(f"INVALID ACCOUNT ID.")
        return
    try:        
        follow_limit = int(input(f'    {red}LIMIT: '))
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    except ValueError:
        print("INVALID NUMBER FOR FOLLOW LIMIT.")
        return
    follow_count = 0
    failed_count = 0
    current_index = 0
    with ThreadPoolExecutor(max_workers=10) as executor:
        while follow_count < follow_limit and current_index < len(tokens):
            token = tokens[current_index]
            page_access_token = token.split('|')[1]
            uid = token.split('|')[0]
            future = executor.submit(follow_account, page_access_token, account_id)
            success = future.result()
            if success:
                follow_count += 1
                print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
                print(f"     {green}[REACTOR] {yellow}{uid}  {blue}───────> {green}SUCCESSFULLY FOLLOWED!")
            else:
                failed_count += 1
                print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
                print(f"   {red}[REACTOR] {yellow}{uid}  {blue}───────> {red}FAILED TO FOLLOW!")
            current_index += 1
            if current_index >= len(tokens) and follow_count < follow_limit:
                pass
                current_index = 0
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    print(f'     {green}SUCCESS: {follow_count}')
    print(f'     {red}FAILED: {failed_count}')

import requests
from bs4 import BeautifulSoup as bs
import time
from concurrent.futures import ThreadPoolExecutor

def p_like():
    clear_screen()
    bryxpogii()
    ses = requests.Session()
    cokix = input(f"     {green} Cookie: ")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    ids_coki = input(f"     \033[33mPATH: ").strip()
    try:
        with open(ids_coki, "r") as file:
            page_id = file.read().splitlines()
    except FileNotFoundError:
        print("FILE NOT FOUND.")
        time.sleep(3)
        return
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m") 
    page_ids = input(f"{yellow}  Input Target Page ID : {green}")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    try:
        limitx = int(input(f"{yellow}  QUANTITY : {green}"))
    except ValueError:
        print(f"{red}  INVALID QUANTITY! MUST BE A NUMBER.")
        return
    headersccc = {'user-agent': W_ueragnt()}
    mbasic_url = f"https://mbasic.facebook.com/{page_ids}"
    try:
        response = ses.get(mbasic_url, headers=headersccc, cookies={'cookie': cokix})
        response.raise_for_status()
        reqx = bs(response.content, 'html.parser')
    except requests.RequestException as e:
        print(f"{red}  FAILED TO FETCH PAGE: {e}")
        return
    reqxx = reqx.find_all('a', string='Message')
    if not reqxx:
        print(f"{red}  COULD NOT FIND MESSAGE LINK ON PAGE.")
        return
    try:
        d_pa_id = str(reqxx).split('href="/messages/thread/')[1].split('/')[0]
    except IndexError:
        print(f"{red}  FAILED TO EXTRACT MESSAGE THREAD ID.")
        return
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    print(f"{yellow}  TOTAL PAGES : {green}{len(page_id)}")
    print(f"{yellow}  TARGET     : {green}{page_ids}")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    with ThreadPoolExecutor(max_workers=30) as executor:
        for i in range(min(len(page_id), limitx)):
            pageid = page_id[i]
            cookies_page = {'cookie': cokix + f"; i_user={pageid}"}
            executor.submit(likepage, cookies_page, pageid, page_ids, d_pa_id)
    print(f"{red}  PROCESS COMPLETED.")

import requests
import re
from bs4 import BeautifulSoup as bs

done = []

def likepage(cookies_page, pageid, page_ids, d_pa_id):
    global headers
    ses = requests.Session()
    headers['user-agent'] = W_ueragnt()
    web_url = f'https://www.facebook.com/profile.php?id={page_ids}'
    try:
        response = ses.get(web_url, headers=headers, cookies=cookies_page)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"FAILED TO FETCH PROFILE PAGE: {e}")
        return
    req = bs(response.content, 'html.parser')
    page_html = str(req)
    try:
        uidx = re.search(r'__user=(\d+)', page_html).group(1)
        dpr = re.search(r'"pr":([\d.]+),', page_html).group(1)
        fb_dtsg = re.search(r'"DTSGInitialData",\[\],{"token":"(.*?)"}', page_html).group(1)
        jazoest = re.search(r'&jazoest=(\d+)', page_html).group(1)
        lsd = re.search(r'"LSD",\[\],{"token":"(.*?)"}', page_html).group(1)
    except AttributeError:
        print("Failed to extract required parameters. The page structure may have changed.")
        return
    data_post = {
        'av': uidx,
        'dpr': dpr,
        'fb_dtsg': fb_dtsg,
        'jazoest': jazoest,
        'lsd': lsd,
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'CometProfilePlusLikeMutation',
        'variables': f'''{{"input":{{"is_tracking_encrypted":false,"page_id":"{d_pa_id}","source":null,"tracking":null,"actor_id":"{uidx}","client_mutation_id":"1"}},"scale":1}}''',
        'server_timestamps': 'true',
        'doc_id': '6716077648448761'
    }
    headers['user-agent'] = W_ueragnt()
    try:
        response = ses.post('https://www.facebook.com/api/graphql/', cookies=cookies_page, headers=headers, data=data_post)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        print(f"FAILED TO SEND LIKE REQUEST: {e}")
        return
    except ValueError:
        print("FAILED TO PARSE JSON RESPONSE.")
        return
    if 'data' in data and 'page_like' in data['data'] and 'page' in data['data']['page_like']:
        subscribe_status = data['data']['page_like']['page'].get('subscribe_status', 'UNKNOWN')
        done.append(pageid)
        print(f"[{len(done)}] PAGE LIKE AND FOLLOW DONE: {pageid} (Status: {subscribe_status})")
    else:
        print("LIKE REQUEST FAILED. RESPONSE STRUCTURE UNEXPECTED.")

import re

def extract_fbid_dp(url):
    pattern = r'fbid=(\d+)'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None

import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def perform_reaction(token, uid_url, reaction_type):
    access_token = token.split('|')[1]
    auto_react = f'https://graph.facebook.com/{uid_url}/reactions?type={reaction_type}&access_token={access_token}'
    try:
        response = requests.post(auto_react)
        return access_token, response.status_code, response.text
    except requests.exceptions.RequestException as e:
        return access_token, None, str(e)

def perform_reaction_fast_dp():
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    bryxpogii()
    print(f"""     {white}CHOOSE TYPE OF REACTORS: 
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m
     {blue}[1] {green}FRA ACCOUNT 
     {blue}[2] {green}FRA PAGES
     {blue}[3] {green}RPW ACCOUNT
     {blue}[4] {green}RPW PAGES
     {red}[0] {red}EXIT 
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m""")
    try:
        file_choice = int(input(f"    {green}Enter your choice: ").strip())
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        if file_choice not in file_options:
            print("INVALID CHOICE.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("PLEASE ENTER A VALID NUMBER.")
        return
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]  # Ensure no empty lines
    except FileNotFoundError:
        print("FILE NOT FOUND.")
        return
    except Exception as e:
        print(f"ERROR LOADING TOKENS: {e}")
        return
    available_tokens = len(tokens)
    if available_tokens == 0:
        print("NO TOKENS AVAILABLE FROM THE SELECTED FILE.")
        return
    try:
        start_line = int(input(f"    {green}Enter the starting line {red}(1 to {available_tokens}{red}): "))
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        if start_line < 1 or start_line > available_tokens:
            print(f"PLEASE ENTER A VALID LINE NUMBER BETWEEN 1 AND {available_tokens}.")
            return
    except ValueError:
        print("PLEASE ENTER A VALID NUMBER.")
        return
    tokens = tokens[start_line - 1:]  
    print(f"    {green}FORMAT {yellow}: {red}https://www.facebook.com/photo.php?fbid=541361691808600")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    z = input(f"   {green}Enter the post link or ID: ")
    post_id = get_combined_data(z)
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    uid_url = post_id
    print(f"""    {blue}Choose the reaction type:
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m
     {yellow}[1] {blue}LIKE
     {yellow}[2] {blue}LOVE
     {yellow}[3] {blue}WOW
     {yellow}[4] {blue}SAD
     {yellow}[5] {blue}ANGRY
     {yellow}[6] {blue}HAHA
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m""")  
    try:
        reaction_choice = int(input(f"    {green}Enter your choice: ").strip())
        reaction_map = {
            1: "LIKE",
            2: "LOVE",
            3: "WOW",
            4: "SAD",
            5: "ANGRY",
            6: "HAHA"
        }
        reaction_type = reaction_map.get(reaction_choice, None)
        if reaction_type is None:
            print("INVALID REACTION CHOICE.")
            return
    except ValueError:
        print("PLEASE ENTER A VALID NUMBER.")
        return
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    try:
        num_reactions = int(input(f"     {yellow}Enter the number of reactions: "))
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    except ValueError:
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        print("PLEASE ENTER A VALID NUMBER FOR REACTIONS.")
        return
    if num_reactions > len(tokens):
        print(f"{red}ENTER AGAIN NOT EXCEEDING {len(tokens)}")
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        return
    reactions_count = 0
    max_workers = 10
    results = []  
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_token = {executor.submit(perform_reaction, token, uid_url, reaction_type): token for token in tokens[:num_reactions]}
        while reactions_count < num_reactions:
            for future in as_completed(future_to_token):
                token = future_to_token[future]
                uid = token.split('|')[0]
                try:
                    access_token, status_code, response_text = future.result()
                    if status_code == 200:
                        reactions_count += 1
                        print(f"     {red}[REACTOR] {yellow}{uid}  {blue}───────> {green}SUCCESSFULLY REACTED!")
                        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
                    else:
                        pass
                    if reactions_count >= num_reactions:
                        print(f"\n{green}SUCCESSFULLY REACHED {reactions_count} REACTIONS! EXITING...")
                        return
                except Exception as e:
                    print(f"ERROR PROCESSING TOKEN {token}: {e}")
            remaining_tokens = tokens[num_reactions: num_reactions + 5]
            if remaining_tokens:
                future_to_token = {executor.submit(perform_reaction, token, uid_url, reaction_type): token for token in remaining_tokens}
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    print(f"{green}TOTAL: {reactions_count}")

import random
import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def rep(post_id, comment, access_token):
    if '|' in access_token:
        _, access_token = access_token.split('|', 1)
    if not access_token.startswith(("EA", "EAA")):
        return f"INVALID TOKEN: {access_token}"
    try:
        converted_link = post_id
        auto_comment_url = f'https://graph.facebook.com/v13.0/{converted_link}/comments'
        params = {
            'message': comment,
            'access_token': access_token
        }
        time.sleep(1)
        headers = {
            'user-agent': W_ueragnt()
        }
        response = requests.post(auto_comment_url, params=params, headers=headers)
        if response.status_code == 200:
            return f"\033[1;31m[SUCCESS]\033[1;31m \033[1;32mSUCCESSFULLY COMMENTED: {green}{comment}\033[1;32m"
        else:
            return f"\033[1;31m[FAILED]\033[1;31m FAILED TO COMMENT: {green}{comment} "
    except requests.exceptions.RequestException as e:
        return f"REQUEST FAILED: {str(e)}"

def reply():
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    bryxpogii()
    print(f"""     {blue}CHOOSE TYPE OF REACTORS: 
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m
     {yellow}[1] {blue}FRA ACCOUNT 
     {yellow}[2] {blue}FRA PAGES
     {yellow}[3] {blue}RPW ACCOUNT
     {yellow}[4] {blue}RPW PAGES
     {red}[0] {red}EXIT 
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m""")
    try:
        file_choice = int(input(f"    {green}Enter your choice: ").strip())
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        if file_choice not in file_options:
            print("INVALID CHOICE.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("PLEASE ENTER A VALID NUMBER.")
        return
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]  # Ensure no empty lines
    except FileNotFoundError:
        print("FILE NOT FOUND.")
        return
    except Exception as e:
        print(f"ERROR LOADING TOKENS: {e}")
        return
    available_tokens = len(tokens)
    if available_tokens == 0:
        print("NO TOKENS AVAILABLE FROM THE SELECTED FILE.")
        return
    try:
        start_line = int(input(f"    {green}Enter the starting line {red}(1 to {available_tokens}): "))
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        if start_line < 1 or start_line > available_tokens:
            print(f"PLEASE ENTER A VALID LINE NUMBER BETWEEN 1 AND {available_tokens}.")
            return
    except ValueError:
        print("PLEASE ENTER A VALID NUMBER.")
        return
    tokens = tokens[start_line - 1:]
    a = input(f"    {green}Enter the post ID: ")
    b = input(f"    {green}Enter the comment ID: ")
    result = f"{a}_{b}"
    post_id = result
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    try:
        num_comments = int(input(f"    {red}Enter the number of comments: "))
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        if num_comments <= 0:
            print("NUMBER OF COMMENTS MUST BE GREATER THAN 0.")
            return
    except ValueError:
        print("PLEASE ENTER A VALID NUMBER.")
        return
    comments_list = []
    for i in range(num_comments):
        comment = input(f"    {green}Enter comment {i + 1}: ")
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        comments_list.append(comment)
    try:
        num_accounts = int(input(f"   {green}Enter the number of accounts to use for commenting (1 to {len(tokens)}): "))
        if num_accounts > len(tokens) or num_accounts <= 0:
            print(f"PLEASE ENTER A VALID NUMBER BETWEEN 1 AND {len(tokens)}.")
            return
    except ValueError:
        print("PLEASE ENTER A VALID NUMBER.")
        return
    results = []
    comments_count = 0
    max_workers = 10
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_token = {}
        for i, token in enumerate(tokens[:num_accounts]):
            comment = random.choice(comments_list)
            future = executor.submit(rep, post_id, comment, token)
            future_to_token[future] = token
        for future in as_completed(future_to_token):
            try:
                result = future.result()
                print(result)
                if "SUCCESSFULLY" in result:
                    comments_count += 1
            except Exception as e:
                print(f"ERROR PROCESSING TOKEN: {e}")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    print(f"TOTAL COMMENTS MADE: {comments_count}")

def comment_with_token(post_id, comment, access_token):
    if '|' in access_token:
        _, access_token = access_token.split('|', 1)
    if not access_token.startswith(("EA", "EAA")):
        return f"INVALID TOKEN: {access_token}"    
    try:
        converted_link = post_id
        auto_comment_url = f'https://graph.facebook.com/v13.0/{converted_link}/comments'
        params = {
            'message': comment,
            'access_token': access_token
        }
        time.sleep(1)
        headers = {
            'user-agent': W_ueragnt()
        }
        response = requests.post(auto_comment_url, params=params, headers=headers)
        pass
        if response.status_code == 200:
            return f"\033[1;31m[SUCCESS]\033[1;31m \033[1;32mSUCCESSFULLY COMMENTED: {green}{comment}\033[1;32m"
        else:
            pass
    except requests.exceptions.RequestException as e:
        pass

def perform_comment_fast():
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    bryxpogii()
    print(f"""     {blue}CHOOSE TYPE OF REACTORS: 
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m
     {yellow}[1] {blue}FRA ACCOUNT 
     {yellow}[2] {blue}FRA PAGES
     {yellow}[3] {blue}RPW ACCOUNT
     {yellow}[4] {blue}RPW PAGES
     {red}[0] {red}EXIT 
    {blue}───────────────────────────────────────────────────────────────\033[0m""")
    try:
        file_choice = int(input(f"    {green}Enter your choice: ").strip())
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        if file_choice not in file_options:
            print("INVALID CHOICE.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("PLEASE ENTER A VALID NUMBER.")
        return
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print("FILE NOT FOUND.")
        return
    except Exception as e:
        pass
        return
    available_tokens = len(tokens)
    if available_tokens == 0:
        print("NO TOKENS AVAILABLE FROM THE SELECTED FILE.")
        return
    try:
        start_line = int(input(f"    {green}Enter the starting line {red}(1 to {available_tokens}): "))
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        if start_line < 1 or start_line > available_tokens:
            print(f"PLEASE ENTER A VALID LINE NUMBER BETWEEN 1 AND {available_tokens}.")
            return
    except ValueError:
        print("PLEASE ENTER A VALID NUMBER.")
        return
    tokens = tokens[start_line - 1:]
    a = input(f"    {green}Enter the post ID: ")
    post_id = get_combined_data(a)
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    try:
        num_comments = int(input(f"    {red}Enter the number of comments: "))
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        if num_comments <= 0:
            print("NUMBER OF COMMENTS MUST BE GREATER THAN 0.")
            return
    except ValueError:
        print("PLEASE ENTER A VALID NUMBER.")
        return
    comments_list = []
    for i in range(num_comments):
        comment = input(f"    {green}Enter comment {i + 1}: ")
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        comments_list.append(comment)
    try:
        num_accounts = int(input(f"   {green}Enter the number of accounts to successfully comment (1 to {len(tokens)}): "))
        if num_accounts > len(tokens) or num_accounts <= 0:
            print(f"PLEASE ENTER A VALID NUMBER BETWEEN 1 AND {len(tokens)}.")
            return
    except ValueError:
        print("PLEASE ENTER A VALID NUMBER.")
        return
    successful_comments = 0
    max_workers =  2
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        while successful_comments < num_accounts and tokens:
            token = tokens.pop(0)
            comment = random.choice(comments_list)
            future = executor.submit(comment_with_token, post_id, comment, token)
            try:
                result = future.result()
                print(result)
                if "SUCCESSFULLY" in result:
                    successful_comments += 1
                    print(f"{successful_comments}/{num_accounts} COMMENTS SUCCESSFUL.")
            except Exception as e:
                pass
    if successful_comments == num_accounts:
        print(f"ALL {num_accounts} COMMENTS WERE SUCCESSFULLY MADE!")
    else:
        print(f"ONLY {successful_comments}/{num_accounts} COMMENTS WERE SUCCESSFUL. NO MORE TOKENS AVAILABLE.")

def live_comment():
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    bryxpogii()
    print(f"""     {blue}CHOOSE TYPE OF REACTORS: 
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m
     {yellow}[1] {blue}FRA ACCOUNT 
     {yellow}[2] {blue}FRA PAGES
     {yellow}[3] {blue}RPW ACCOUNT
     {yellow}[4] {blue}RPW PAGES
     {red}[0] {red}EXIT 
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m""") 
    try:
        file_choice = int(input(f"    {green}Enter your choice: ").strip())
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        if file_choice not in file_options:
            print("INVALID CHOICE.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("PLEASE ENTER A VALID NUMBER.")
        return
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print("FILE NOT FOUND.")
        return
    except Exception as e:
        print(f"ERROR LOADING TOKENS: {e}")
        return
    available_tokens = len(tokens)
    if available_tokens == 0:
        print("NO TOKENS AVAILABLE FROM THE SELECTED FILE.")
        return
    try:
        start_line = int(input(f"    {green}Enter the starting line {red}(1 to {available_tokens}): "))
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        if start_line < 1 or start_line > available_tokens:
            print(f"PLEASE ENTER A VALID LINE NUMBER BETWEEN 1 AND {available_tokens}.")
            return
    except ValueError:
        print("PLEASE ENTER A VALID NUMBER.")
        return
    tokens = tokens[start_line - 1:]
    a = input(f"    {green}Enter the post ID: ")
    post_id = get_combined_data(a)
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    try:
        num_comments = int(input(f"    {red}Enter the number of comments: "))
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        if num_comments <= 0:
            print("NUMBER OF COMMENTS MUST BE GREATER THAN 0.")
            return
    except ValueError:
        print("PLEASE ENTER A VALID NUMBER.")
        return
    comments_list = []
    for i in range(num_comments):
        comment = input(f"    {green}Enter comment {i + 1}: ")
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        comments_list.append(comment)
    try:
        num_accounts = int(input(f"   {green}Enter the number of accounts to use for commenting (1 to {len(tokens)}): "))
        if num_accounts > len(tokens) or num_accounts <= 0:
            print(f"PLEASE ENTER A VALID NUMBER BETWEEN 1 AND {len(tokens)}.")
            return
    except ValueError:
        print("PLEASE ENTER A VALID NUMBER.")
        return
    results = []
    comments_count = 0
    max_workers = 2
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_token = {}
        for i, token in enumerate(tokens[:num_accounts]):
            comment = random.choice(comments_list)
            future = executor.submit(comment_with_token, post_id, comment, token)
            future_to_token[future] = token
        for future in as_completed(future_to_token):
            try:
                result = future.result()
                print(result)
                if "SUCCESSFULLY" in result:
                    comments_count += 1
            except Exception as e:
                print(f"ERROR PROCESSING TOKEN: {e}")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    print(f"TOTAL COMMENTS MADE: {comments_count}")

import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def load_tokens(file_path):
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]
        return tokens
    except FileNotFoundError:
        print("FILE NOT FOUND.")
        return []
    except Exception as e:
        print(f"ERROR LOADING TOKENS: {e}")
        return []

def follow_and_like_facebook_page(uid, access_token):
    follow_url = f"https://graph.facebook.com/v20.0/{uid}/subscribers"
    headers = {'Authorization': f'Bearer {access_token}'}
    follow_response = make_http_request('POST', follow_url, headers=headers)
    if follow_response and 'error' in follow_response:
        print(f"ERROR FOLLOWING PAGE WITH UID {uid}: {follow_response['error']['message']}")
    elif follow_response:
        print(f"\033[1;32m[SUCCESSFULLY] FOLLOWED THE PAGE/PROFILE WITH UID {uid}\033[0m")
    like_url = f"https://graph.facebook.com/v20.0/{uid}/likes"
    like_response = make_http_request('POST', like_url, headers=headers)
    if like_response and 'error' in like_response:
        print(f"ERROR LIKING PAGE WITH UID {uid}: {like_response['error']['message']}")
    else:
        print(f"\033[1;32m[SUCCESSFULLY] LIKED THE PAGE/PROFILE WITH UID {uid}\033[0m")

def make_http_request(method, url, headers=None, data=None):
    try:
        if method.upper() == 'POST':
            response = requests.post(url, headers=headers, data=data)
        elif method.upper() == 'GET':
            response = requests.get(url, headers=headers)
        else:
            print(f"UNSUPPORTED HTTP METHOD: {method}")
            return None
        if response.status_code == 200:
            return response.json()
        else:
            print(f"HTTP REQUEST FAILED WITH STATUS CODE: {response.status_code}")
            return response.json()
    except Exception as e:
        print(f"AN ERROR OCCURRED DURING THE HTTP REQUEST: {str(e)}")
        return None

def perform_actions_from_file():
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    bryxpogii()
    print(f"""     {blue}CHOOSE TYPE OF REACTORS: 
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m
     {yellow}[1] {blue}FRA ACCOUNT 
     {yellow}[2] {blue}FRA PAGES
     {yellow}[3] {blue}RPW ACCOUNT
     {yellow}[4] {blue}RPW PAGES
     {red}[0] {red}EXIT 
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m""")    
    try:
        file_choice = int(input(f"    {green}Enter your choice: ").strip())
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        if file_choice not in file_options:
            print("INVALID CHOICE.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("PLEASE ENTER A VALID NUMBER.")
        return
    tokens = load_tokens(file_path)
    total_tokens = len(tokens)
    if total_tokens == 0:
        print("NO TOKENS AVAILABLE FROM THE SELECTED FILE.")
        return
    try:
        start_line = int(input(f"    {green}Enter the starting line {red}(1 to {total_tokens}{red}): "))
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        if start_line < 1 or start_line > total_tokens:
            print(f"PLEASE ENTER A VALID LINE NUMBER BETWEEN 1 AND {total_tokens}.")
            return
    except ValueError:
        print("PLEASE ENTER A VALID NUMBER.")
        return
    tokens = tokens[start_line - 1:]
    uid = input(f"    {green}Enter the Page/Profile UID: ").strip()
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    if not uid.isdigit():
        print("INVALID UID. PLEASE ENSURE YOU ENTERED A CORRECT NUMERIC UID.")
        return
    try:
        num_actions = int(input(f"    {green}LIMIT {red}(not exceeding {total_tokens}): ").strip())
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        if num_actions > total_tokens:
            print(f"IT EXCEEDS THE LIMIT OF {total_tokens}.")
            return
    except ValueError:
        print("INVALID INPUT. PLEASE ENTER A VALID NUMBER FOR THE ACTIONS.")
        return
    action_count = 0
    tasks = []
    with ThreadPoolExecutor(max_workers=2) as executor:
        for token in tokens[:num_actions]:
            future = executor.submit(follow_and_like_facebook_page, uid, token.split('|')[1])
            tasks.append(future)
            action_count += 1
        for task in as_completed(tasks):
            y = token.split('|')[0]
            try:
                task.result()
            except Exception as e:
                print(f"AN ERROR OCCURRED DURING EXECUTION: {str(e)}")
    print(f"     {red}ID {white}: {blue}{y} | {green}\nSUCCESSFULLY FOLLOWED AND LIKED | ID:", uid)
    print(f"COMPLETED {action_count} REQUESTED ACTIONS.")

import requests
import sys
import time
from concurrent.futures import ThreadPoolExecutor

gome_token = []

def tokz(input_cookies):
    for cookie in input_cookies:
        header_ = {
            'authority': 'business.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'cache-control': 'max-age=0',
            'cookie': cookie,
            'referer': 'https://www.facebook.com/',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
        }
        try:
            home_business = requests.get('https://business.facebook.com/content_management', headers=header_).text
            token = home_business.split('EAAG')[1].split('","')[0]
            cookie_token = f'{cookie}|EAAG{token}'
            gome_token.append(cookie_token)
        except:
            pass
    return gome_token

def share(tach, id_share):
    cookie = tach.split('|')[0]
    token = tach.split('|')[1]
    he = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate',
        'connection': 'keep-alive',
        'content-length': '0',
        'cookie': cookie,
        'host': 'graph.facebook.com'
    }
    try:
        requests.post(f'https://graph.facebook.com/me/feed?link=https://m.facebook.com/{id_share}&published=0&access_token={token}', headers=he).json()
    except:
        pass

def shar():
    clear_screen()
    bryxpogii()
    input_cookies = input(f"     {green}Enter Cookie: ").split(',')
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    id_share = input(f"     {green}Enter Post ID: ")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    total_share = int(input(f"    {green}How Many Share: "))
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    delay = int(input(f"    {green} Delay Share: "))
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    print(f'    {green} Waiting...', end='\r')
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    all = tokz(input_cookies)
    total_live = len(all)
    print(f'    {green} Live: {total_live} Cookies')
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    if total_live == 0:
        sys.exit()
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    stt = 0
    with ThreadPoolExecutor(max_workers=2000) as executor:
        futures = []
        while True:
            for tach in all:
                if stt >= total_share:
                    break
                futures.append(executor.submit(share, tach, id_share))
                stt += 1
                print(f'    {green} Share: {stt}', end='\r')
                time.sleep(delay)
            if stt >= total_share:
                break
    gome_token.clear()
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")

import os
import requests
import uuid
import random
from requests import post as pt
from rich import print as rp
from rich.panel import Panel as pan
import os
import requests
import uuid
import random
from requests import post as pt
from rich import print as rp
from rich.panel import Panel as pan
import platform
import os
import random
import uuid

darkblue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
skyblue = "\033[1;36m"
blue = "\033[1;34m"
lightblue = "\033[38;5;81m"
white = "\033[1;37m"
R = "\033[31m"  # Red
G = "\033[32m"  # Green
Y = "\033[33m"  # Yellow
B = "\033[34m"  # Blue
M = "\033[35m"  # Magenta
P = "\033[36m"  # Cyan
C = "\033[37m"  # White

def clear_screen():
    if 'termux' in platform.system().lower():
        os.system('clear')
    elif platform.system().lower() == 'windows':
        os.system('cls')
    else:
        os.system('clear')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_file_path():
    clear_screen()
    bryxpogii()
    return input(f"     {green}{C}Enter path to file with email and password: ")
print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")

def get_cookie_storage_path():
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    return input(f"     {yellow}{C}Enter path to store cookies: ")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")

def read_credentials(file_path):
    credentials = []
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        for line in lines:
            line = line.strip()
            if '|' in line:
                uid, password = line.split('|', 1)
                credentials.append((uid.strip(), password.strip()))
            elif line:
                print(f"WARNING: SKIPPING INVALID LINE FORMAT: {line}")
    except FileNotFoundError as e:
        print(f"ERROR: FILE NOT FOUND {file_path}: {str(e)}")
    return credentials

def cuser(user, passw):
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
    data = {
        'adid': f'{uuid.uuid4()}',
        'format': 'json',
        'device_id': f'{uuid.uuid4()}',
        'cpl': 'true',
        'family_device_id': f'{uuid.uuid4()}',
        'credentials_type': 'device_based_login_password',
        'error_detail_type': 'button_with_disabled',
        'source': 'device_based_login',
        'email': user,
        'password': passw,
        'access_token': accessToken,
        'generate_session_cookies': '1',
        'meta_inf_fbmeta': '',
        'advertiser_id': f'{uuid.uuid4()}',
        'currently_logged_in_userid': '0',
        'locale': 'en_US',
        'client_country_code': 'US',
        'method': 'auth.login',
        'fb_api_req_friendly_name': 'authenticate',
        'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
    }
    headers = {
        'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/en_US;FBBV/135374479;FBCR/SMART;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'graph.facebook.com',
        'X-FB-Net-HNI': str(random.randint(10000, 99999)),
        'X-FB-SIM-HNI': str(random.randint(10000, 99999)),
        'X-FB-Connection-Type': 'MOBILE.LTE',
        'X-Tigon-Is-Retry': 'False',
        'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
        'x-fb-device-group': str(random.randint(1000, 9999)),
        'X-FB-Friendly-Name': 'ViewerReactionsMutation',
        'X-FB-Request-Analytics-Tags': 'graphservice',
        'X-FB-HTTP-Engine': 'Liger',
        'X-FB-Client-IP': 'True',
        'X-FB-Connection-Bandwidth': str(random.randint(20000000, 30000000)),
        'X-FB-Server-Cluster': 'True',
        'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'
    }
    response = pt("https://b-graph.facebook.com/auth/login", headers=headers, data=data, allow_redirects=False)
    return response.json()

def runing():
    clear_screen()
    bryxpogii()
    file_path = get_file_path()
    storage_path = get_cookie_storage_path()
    credentials = read_credentials(file_path)
    if not credentials:
        print(f"{R}NO CREDENTIALS FOUND IN THE FILE.")
        return
    print(f"      {red}FOUND {len(credentials)} {green}CREDENTIALS !...")
    for user, passw in credentials:
        response = cuser(user, passw)
        if "session_key" in response:
            clear()
            cookie_str = '; '.join(f'{i["name"]}={i["value"]}' for i in response.get('session_cookies', []))
            clear_screen()
            bryxpogii()
            print(f"     {red}COOKIE {yellow}: {white}{C}{cookie_str}")
            with open(storage_path, 'a') as f:
                f.write(cookie_str + '\n')
        else:
            print(f"{R}INVALID/CHECKPOINT FOR USER ID: {C}{user}")
    print(f"{G}PROCESSING COMPLETE. ALL CREDENTIALS HAVE BEEN PROCESSED.")

def bitz():
    clear_screen()
    bryxpogii()
    print(f"     {yellow}[1] {green}GET COOKIE")
    print(f"     {yellow}[2] {green}AUTO CREATE PAGE")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    num_reactions = int(input(f'     {red}Enter Option: '))
    if num_reactions == 1:
        runing()
    elif num_reactions == 2:
        hackezr()
    else:
        print(f"{R}INVALID OPTION SELECTED.")

import random
import requests
from colorama import init, Fore, Style
import os

init()

class RegPro5:
    def __init__(self, cookies) -> None:
        self.cookies = cookies
        self.id_acc = self.cookies.split('c_user=')[1].split(';')[0]
        headers = {
            'authority': 'www.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'vi',
            'cookie': self.cookies,
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'viewport-width': '1366',
        }       
        url_profile = requests.get('https://www.facebook.com/me', headers=headers).url
        profile = requests.get(url_profile, headers=headers).text
        self.fb_dtsg = None
        patterns = [
            '{"name":"fb_dtsg","value":"',
            ',"f":"',
        ]
        for pattern in patterns:
            try:
                self.fb_dtsg = profile.split(pattern)[1].split('"},')[0]
                break
            except IndexError:
                continue
        if not self.fb_dtsg:
            kolor("ERROR: FB_DTSG NOT FOUND IN PROFILE DATA.", 'red')

import requests
import threading
from concurrent.futures import ThreadPoolExecutor
import random
import time
import sys
import os
import platform
import random
import string

purple = "\033[1;35m"
blue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
white = "\033[1;37m"

def clear_screen():
    if 'termux' in platform.system().lower():
        os.system('clear')
    elif platform.system().lower() == 'windows':
        os.system('cls')
    else:
        os.system('clear')

def generate_user_agent():
    fbav = f"{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}"
    fbbv = str(random.randint(111111111, 999999999))
    fbrv = '0'
    random_seed = random.Random()
    adid = ''.join(random_seed.choices(string.hexdigits, k=16))
    device = random.choice(["HUAWEI MAR-LX1M", "Samsung SM-G960F", "OnePlus GM1913"])
    fbav_version = str(random.randint(49, 150))
    fbbv_version = str(random.randint(11111111, 77777777))
    carrier = random.choice(["Ooredoo TN", "Orange", "Vodafone", "T-Mobile"])
    ua_bgraph = f'[FBAN/FB4A;FBAV/{fbav_version}.0.0.{random.randrange(20, 49)}.{random.randint(11, 99)};FBBV/{fbbv_version};' \
                f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};FBDM/{{density=3.0,width=1080,height=2107}};FBLC/fr_FR;' \
                f'FBRV/{fbrv};FBCR/{carrier};FBMF/{device.split(" ")[0]};FBBD/{device.split(" ")[0]};' \
                f'FBPN/com.facebook.katana;FBDV/{device};FBSV/9;FBOP/1;FBCA/arm64-v8a:]'
    return ua_bgraph

ua_bgraph = generate_user_agent()

import requests
import random
import concurrent.futures as thread
import os
import string

def bgraph(uid, pw, path_file, extract_type, success_count, existing_uids):
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'  # Example token
    fbav = f'{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'
    fbbv = str(random.randint(111111111, 999999999))
    fbrv = '0'
    random_seed = random.Random()
    adid = ''.join(random_seed.choices(string.hexdigits, k=16))
    ua_bgraph = '[FBAN/FB4A;FBAV/' + str(random.randint(49, 66)) + '.0.0.' + str(random.randrange(20, 49)) + str(random.randint(11, 99)) + ';FBBV/' + str(random.randint(11111111, 77777777)) + ';' + '[FBAN/FB4A;FBAV/' + fbav + ';FBBV/' + fbbv + ';FBDM/{density=3.0,width=1080,height=2107};FBLC/fr_FR;FBRV/' + fbrv + ';FBCR/Ooredoo TN;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1M;FBSV/9;FBOP/1;FBCA/arm64-v8a:]'
    data = {
        'adid': f'{uuid.uuid4()}',
        'format': 'json',
        'device_id': f'{uuid.uuid4()}',
        'cpl': 'true',
        'family_device_id': f'{uuid.uuid4()}',
        'credentials_type': 'device_based_login_password',
        'error_detail_type': 'button_with_disabled',
        'source': 'device_based_login',
        'email': uid,
        'password': pw,
        'access_token': accessToken,
        'generate_session_cookies': '1',
        'meta_inf_fbmeta': '',
        'advertiser_id': f'{uuid.uuid4()}',
        'currently_logged_in_userid': '0',
        'locale': 'en_US',
        'client_country_code': 'US',
        'method': 'auth.login',
        'fb_api_req_friendly_name': 'authenticate',
        'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
    }
    headers = {
        'User-Agent': ua_bgraph,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'graph.facebook.com',
        'X-FB-Net-HNI': str(random.randint(10000, 99999)),
        'X-FB-SIM-HNI': str(random.randint(10000, 99999)),
        'X-FB-Connection-Type': 'MOBILE.LTE',
        'X-Tigon-Is-Retry': 'False',
        'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
        'x-fb-device-group': str(random.randint(1000, 9999)),
        'X-FB-Friendly-Name': 'ViewerReactionsMutation',
        'X-FB-Request-Analytics-Tags': 'graphservice',
        'X-FB-HTTP-Engine': 'Liger',
        'X-FB-Client-IP': 'True',
        'X-FB-Connection-Bandwidth': str(random.randint(20000000, 30000000)),
        'X-FB-Server-Cluster': 'True',
        'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'
    }
    url = 'https://graph.facebook.com/auth/login'
    try:
        if uid in existing_uids:
            print(f"     {yellow}[INFO] {red}ACCOUNT --> {white}{uid} {red}already exists.")
            print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
            return
        response = requests.post(url,headers=headers,data=data).json()
        print(response)
        if 'access_token' in response:
            token = response['access_token']
            with open(path_file, 'a') as f:
                f.write(f"{uid}|{token}\n")
            print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
            print(f"     \033[32m[SUCCESS]\033[0m: EXTRACTED ACCOUNT ─────> {uid}.")
            print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
            success_count.append(uid)
        else:
            print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
            print(f"     \033[31m[FAILED]\033[0m: TO EXTRACT ACCOUNT ─────> {uid}.")
            print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    except Exception as e:
        print(f"     \033[1;31m ERROR EXTRACTING ACCOUNT: {uid}. REASON: {str(e)}\033[0m\n")

def proz(accounts_file, token_output_path, extract_type):
    success_count = []
    existing_uids = set()
    if os.path.exists(token_output_path):
        with open(token_output_path, 'r') as f:
            existing_uids = {line.split('|')[0] for line in f.readlines()}
    try:
        with open(accounts_file, 'r') as file:
            accounts = file.readlines()
        accounts = [line.strip() for line in accounts if '|' in line.strip()]
        if not accounts:
            print(f"NO VALID ACCOUNTS FOUND IN {accounts_file}.")
            return
        with thread.ThreadPoolExecutor(max_workers=30) as executor:
            futures = [executor.submit(bgraph, uid, pw, token_output_path, extract_type, success_count, existing_uids)
                       for uid, pw in [account.split('|') for account in accounts]]
            for future in futures:
                future.result()
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        print(f"     \033[1;34m[SUCCESS]\033[0m: {len(success_count)} {extract_type}(s) SUCCESSFULLY EXTRACTED.")
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    except FileNotFoundError:
        print(f"FILE NOT FOUND: {accounts_file}")
        return

import requests
import random
import concurrent.futures as thread
import os
import string

def load_existing_tokens(path_file):
    if os.path.exists(path_file):
        with open(path_file, 'r') as f:
            return {line.split('|')[0] for line in f.readlines()}
    return set()

def bgraph_page(uid, pw, path_file, extract_type, success_count, existing_tokens):
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
    fbav = f'''{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'''
    fbbv = str(random.randint(111111111, 999999999))
    fbrv = '0'
    random_seed = random.Random()
    adid = ''.join(random_seed.choices(string.hexdigits, k=16))
    ua_bgraph = '[FBAN/FB4A;FBAV/' + str(random.randint(49, 66)) + '.0.0.' + str(random.randrange(20, 49)) + str(random.randint(11, 99)) + ';FBBV/' + str(random.randint(11111111, 77777777)) + ';' + '[FBAN/FB4A;FBAV/' + fbav + ';FBBV/' + fbbv + ';FBDM/{density=3.0,width=1080,height=2107};FBLC/fr_FR;FBRV/' + fbrv + ';FBCR/Ooredoo TN;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1M;FBSV/9;FBOP/1;FBCA/arm64-v8a:]'
    data = {
        'adid': f'{uuid.uuid4()}',
        'format': 'json',
        'device_id': f'{uuid.uuid4()}',
        'cpl': 'true',
        'family_device_id': f'{uuid.uuid4()}',
        'credentials_type': 'device_based_login_password',
        'error_detail_type': 'button_with_disabled',
        'source': 'device_based_login',
        'email': uid,
        'password': pw,
        'access_token': accessToken,
        'generate_session_cookies': '1',
        'meta_inf_fbmeta': '',
        'advertiser_id': f'{uuid.uuid4()}',
        'currently_logged_in_userid': '0',
        'locale': 'en_US',
        'client_country_code': 'US',
        'method': 'auth.login',
        'fb_api_req_friendly_name': 'authenticate',
        'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
    }
    headers = {
        'User-Agent': ua_bgraph,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'graph.facebook.com',
        'X-FB-Net-HNI': str(random.randint(10000, 99999)),
        'X-FB-SIM-HNI': str(random.randint(10000, 99999)),
        'X-FB-Connection-Type': 'MOBILE.LTE',
        'X-Tigon-Is-Retry': 'False',
        'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
        'x-fb-device-group': str(random.randint(1000, 9999)),
        'X-FB-Friendly-Name': 'ViewerReactionsMutation',
        'X-FB-Request-Analytics-Tags': 'graphservice',
        'X-FB-HTTP-Engine': 'Liger',
        'X-FB-Client-IP': 'True',
        'X-FB-Connection-Bandwidth': str(random.randint(20000000, 30000000)),
        'X-FB-Server-Cluster': 'True',
        'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'
    }
    url = 'https://graph.facebook.com/auth/login'
    try:
        if uid in existing_uids:
            print(f"     {white}ACCOUNT ─────> {red}{uid} {green}ALREADY EXISTS")
            print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
            return
        response = requests.post(url,headers=headers,data=data).json()
        if 'access_token' in response:
            token = response['access_token']
            pages = extract_fb_pages(token)
            if pages:
                for page in pages:
                    page_id = page['id']
                    if page_id not in existing_tokens:
                        with open(path_file, 'a') as f:
                            f.write(f"{page_id}|{page['accessToken']}\n")
                        print(f"{white}{uid}  ─────> {green}PAGE ID: {red}{page_id} {yellow}EXTRACTED SUCCESSFULLY")
                        existing_tokens.add(page_id)
                    else:
                        print(f"{white}ID:  {page_id} ─────> {green}ALREADY EXISTS ! ")
            else:
                print(f"{white}{uid} ─────> {red}DOESN'T HAVE PAGES !")
            success_count.append(uid)
        else:
            print(f"{white}{uid}  ─────> {red}FAILED TO EXTRACT ! ")
    except Exception as e:
        print(f"ERROR EXTRACTING ACCOUNT: {uid}. REASON: {str(e)}")

def extract_fb_pages(token):
    url = 'https://graph.facebook.com/v18.0/me/accounts'
    headers = {
        'Authorization': f'Bearer {token}'
    }   
    pages_data = []    
    while url:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f'Error: {response.text}')
            return None
        data = response.json()
        for page in data.get('data', []):
            pages_data.append({
                'id': page.get('id'),
                'accessToken': page.get('access_token')
            })
        url = data.get('paging', {}).get('next')
    return pages_data

def prozc(accounts_file, token_output_path, extract_type):
    success_count = []
    existing_tokens = load_existing_tokens(token_output_path)
    try:
        with open(accounts_file, 'r') as file:
            accounts = file.readlines()
        accounts = [line.strip() for line in accounts if '|' in line.strip()]
        if not accounts:
            print(f"NO VALID ACCOUNTS FOUND IN {accounts_file}.")
            return
        with thread.ThreadPoolExecutor(max_workers=30) as executor:
            futures = [executor.submit(bgraph_page, uid, pw, token_output_path, extract_type, success_count, existing_tokens)
                       for uid, pw in [account.split('|') for account in accounts]]
            for future in futures:
                future.result()
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        print(f"     \033[1;34m[SUCCESS]\033[0m: {len(success_count)} {extract_type}(s) successfully extracted.")
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    except FileNotFoundError:
        print(f"FILE NOT FOUND: {accounts_file}")

def extraction():
    clear_screen()
    bryxpogii()
    print(f"     {white}[1] {yellow}EXTRACT {red}ACCOUNT")
    print(f"     {white}[2] {yellow}EXTRACT {red}PAGES")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    choice = input(f"    {green}Enter your choice: ").strip()
    if choice == '1':
        axl1()
    elif choice == '2':
        axl2()
    else:
        print(f"     {red}INVALID CHOICE")

def axl2():
    clear_screen()
    bryxpogii()
    folder_path = "/sdcard/boostphere"
    print(f"     {yellow}[01] {blue}FRA EXTRACT ACCOUNT")
    print(f"     {yellow}[02] {blue}FRA EXTRACT PAGES")
    print(f"     {yellow}[03] {blue}RPW EXTRACT ACCOUNT")
    print(f"     {yellow}[04] {blue}RPW EXTRACT PAGES")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    save_choice = input(f"    {green}Enter your choice: ").strip()
    if save_choice == '1':
        account_file = os.path.join(folder_path, "FRAACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '2':
        account_file = os.path.join(folder_path, "FRAPAGES.txt")
        extract_type = 'page'
    elif save_choice == '3':
        account_file = os.path.join(folder_path, "RPWACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '4':
        account_file = os.path.join(folder_path, "RPWPAGES.txt")
        extract_type = 'page'
    else:
        print("INVALID CHOICE. EXITING.")
        return
    
    print(f"     \033[33mTHE FORMAT SHOULD BE \033[31muid|pass")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    file_path = input(f"     \033[33mPATH: ").strip()
    prozc(file_path, account_file, extract_type)

def axl1():
    clear_screen()
    bryxpogii()
    folder_path = "/sdcard/boostphere"
    print(f"     {yellow}[01] {blue}FRA EXTRACT ACCOUNT")
    print(f"     {yellow}[02] {blue}FRA EXTRACT PAGES")
    print(f"     {yellow}[03] {blue}RPW EXTRACT ACCOUNT")
    print(f"     {yellow}[04] {blue}RPW EXTRACT PAGES")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    save_choice = input(f"    {green}Enter your choice: ").strip()
    if save_choice == '1':
        account_file = os.path.join(folder_path, "FRAACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '2':
        account_file = os.path.join(folder_path, "FRAPAGES.txt")
        extract_type = 'page'
    elif save_choice == '3':
        account_file = os.path.join(folder_path, "RPWACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '4':
        account_file = os.path.join(folder_path, "RPWPAGES.txt")
        extract_type = 'page'
    else:
        print("INVALID CHOICE. EXITING.")
        return
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    print(f"     \033[33mTHE FORMAT SHOULD BE \033[31muid|pass")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    file_path = input(f"     \033[33mPATH: ").strip()
    token_output_path = account_file
    proz(file_path, token_output_path, extract_type)

def get_token_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        tokens = [line.strip().split('|')[1] for line in lines if '|' in line]
    return random.choice(tokens)

class FacebookPoster:
    def __init__(self, link):
        self.link = link
    def share_post(self, token):
        url = "https://graph.facebook.com/v13.0/me/feed"
        payload = {
            'link': self.link,
            'published': '0',
            'privacy': '{"value":"SELF"}',
            'access_token': token
        }
        try:
            response = requests.post(url, data=payload)
            print(response)
            if response.status_code == 200:
                print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
                print(f"{green}      Successfully Shared")
                return True
            else:
                return False
        except requests.exceptions.RequestException as e:
            print(f"AN ERROR OCCURRED: {e}")
            return False

def share_in_threads(link, file_path, num_shares):
    start_all = time.time()
    def worker():
        success = False
        while not success:
            token = get_token_from_file(file_path)
            fb_poster = FacebookPoster(link)
            success = fb_poster.share_post(token)
    max_workers = 40
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        for _ in range(num_shares):
            executor.submit(worker)
    end_all = time.time()
    duration = end_all - start_all
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    print(f"\n  {yellow}SHARING STARTED: {start_all}")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    print(f"     {yellow}SHARING ENDED: {end_all}")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    print(f"    {yellow}TOTAL DURATION: {duration:.2f} SECONDS\033[0m")

def count_tokens(accounts_file, pages_file):
    total_accounts = 0
    total_pages = 0
    try:
        with open(accounts_file, 'r') as af:
            total_accounts = sum(1 for line in af if line.strip())
    except FileNotFoundError:
        print(f"ACCOUNT FILE NOT FOUND: {accounts_file}")
    try:
        with open(pages_file, 'r') as pf:
            total_pages = sum(1 for line in pf if line.strip())
    except FileNotFoundError:
        print(f"PAGE FILE NOT FOUND: {pages_file}")
    return total_accounts, total_pages

def share():
    clear_screen()
    bryxpogii()
    print(f"""     {blue}CHOOSE TYPE OF ACCOUNTS TO AUTO SHARE: 
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m
     {yellow}[1] {blue}FRA ACCOUNT 
     {yellow}[2] {blue}FRA PAGES
     {yellow}[3] {blue}RPW ACCOUNT
     {yellow}[4] {blue}RPW PAGES
     {red}[0] {red}EXIT 
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m""")
    choice = input(f"    {green}Enter your choice: ").strip()
    file_map = {
        '1': '/sdcard/boostphere/FRAACCOUNT.txt',
        '2': '/sdcard/boostphere/FRAPAGES.txt',
        '3': '/sdcard/boostphere/RPWACCOUNT.txt',
        '4': '/sdcard/boostphere/RPWACCOUNT.txt'
    }
    file_path = file_map.get(choice)
    if not file_path:
        print("INVALID CHOICE. EXITING.")
        return
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    post_id = input(f"   {yellow}Enter the post link to share: ")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    num_shares = int(input(f"   {blue}Limit Share: "))
    link = f"https://www.facebook.com/{post_id}"
    share_in_threads(link, file_path, num_shares)

def main2(): 
    fraaccounts_file = '/sdcard/boostphere/FRAACCOUNT.txt'
    frapages_file = '/sdcard/boostphere/FRAPAGES.txt'
    rpwaccounts = '/sdcard/boostphere/RPWACCOUNT.txt'
    rpwpages = '/sdcard/boostphere/RPWPAGES.txt'
    total_accounts, total_pages = count_tokens(fraaccounts_file, frapages_file)
    total_account_rpw, total_pages_rpw = count_tokens(rpwaccounts,rpwpages)
    clear_screen()
    bryxpogii()
    print(f"""                 {yellow}OVERVIEW OF STORED ACCOUNT & PAGES💫
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m
                      {blue}FRA ACCOUNT{yellow} : {green}{total_accounts}
                      {blue}FRA PAGES  {yellow} : {green}{total_pages}
                      {blue}RPW ACCOUNT{yellow} : {green}{total_account_rpw}
                      {blue}RPW PAGES  {yellow} : {green}{total_pages_rpw}
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m""")
    print(f"     {blue}[1] {yellow}EXTRACT ACCOUNT")
    print(f"     {blue}[2] {yellow}AUTO SPAM SHARE ")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    choice = input(f"    {green}Enter your choice: ").strip()
    if choice == '1': 
        extraction()
    if choice == '2': 
        share()

import os,sys,re,time,json,pytz,uuid
import requests,bs4,string
import faker,random
from faker import Faker
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as bs
from datetime import datetime
from time import sleep
from time import sleep as jeda
from time import strftime
from bs4 import BeautifulSoup as sop
from rich import print as rich_print
from rich.panel import Panel

bulan = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10': 'October', '11': 'November', '12': 'December'}
tgl = datetime.now().day
bln = bulan[(str(datetime.now().month))]
thn = datetime.now().year
tanggal = (str(tgl)+' '+str(bln)+' '+str(thn))
waktu = strftime('%H:%M:%S')
hari = datetime.now().strftime("%A")

waktuu = datetime.now(pytz.timezone('Asia/Manila')).strftime("%d-%m-%Y %H:%M:%S")

from fake_useragent import UserAgent
ua = UserAgent()
def ugenX():
    ualist = [ua.random for _ in range(50)]
    return str(random.choice(ualist))

def fake_name():
    first = Faker().first_name()
    last = Faker().last_name()
    return first,last

def fake_password():
    name = " ".join(fake_name()).replace(' ', '')
    jam = str(datetime.now().strftime("%X")).replace(':','')
    namepassword = f'{name}.{jam}.{str(random.randrange(1000,10000))}'
    return namepassword

def useragent_facebook():
        htc = ["HTC One M8", "HTC One M9", "HTC 10", "HTC U11", "HTC U12+", "HTC Desire 626", "HTC Sensation", "HTC EVO 4G", "HTC One X", "HTC Desire Eye", "HTC One A9", "HTC U Ultra", "HTC Butterfly", "HTC Desire 820", "HTC Wildfire", "HTC HD2", "HTC Evo Shift 4G", "HTC Desire 610", "HTC One Mini", "HTC ThunderBolt", "HTC Droid DNA", "HTC Desire 816", "HTC Legend", "HTC Sensation XL", "HTC Incredible S", "HTC One S", "HTC Rhyme", "HTC Desire HD", "HTC Evo 3D", "HTC Touch Pro 2"]
        nexus = ['Galaxy Nexus', 'Nexus 10', 'Nexus 2', 'Nexus 4', 'Nexus 4', 'Nexus 4', 'Nexus 4', 'Nexus 4', 'Nexus 4', 'Nexus 5', 'phone/Nexus 5', 'Nexus 5X', 'Nexus 6', 'Nexus 7', 'Nexus 9', 'Nexus One', 'Nexus One', 'Nexus One', 'Nexus One', 'Nexus One', 'Nexus One', 'Nexus Player', 'Nexus Player', 'Nexus S', 'Nexus S', 'Nexus S 4G', 'nexus S', 'Nexus S', 'Nexus s', 'Nexus S', 'Nexus S', 'Nexus S', 'Nexus S', 'Nexus S']
        pixel = ["Pixel 5a", "Pixel 4a 5G", "Pixel 2 XL", "Pixel 6 Pro", "Pixel 4 XL", "Pixel 5", "Pixel 3", "Pixel 3 XL", "Pixel 4a", "Pixel 4", "Pixel 3a","Pixel 5 XL","Pixel 7a","Pixel 6 XL","Pixel 4a","Pixel 6a","Pixel 3a","Pixel 7 XL"]
        micromax = ['Micromax 10', 'Micromax 1J', 'Micromax 86519', 'Micromax A064', 'Micromax_A064', 'Micromax A065', 'Micromax_A065', 'Micromax A066', 'Micromax_A066', 'Micromax A067', 'Micromax_A067', 'MICROMAX_A068', 'MICROMAX A068', 'Micromax A068', 'Micromax A069', 'Micromax_A069', 'Micromax A075', 'Micromax A082', 'Micromax_A082', 'Micromax A089', 'Micromax_A089', 'Micromax A091', 'Micromax A092', 'Micromax_A092', 'Micromax A093', 'Micromax_A093', 'Micromax A095', 'Micromax A096', 'Micromax_A101', 'Micromax A102', 'Micromax_A102', 'Micromax A104', 'Micromax a104', 'Micromax A105', 'Micromax_A105', 'Micromax A106', 'Micromax-A106', 'Micromax A108', 'Micromax_A109', 'Micromax A109', 'Micromax A110', 'Micromax_A110', 'Micromax A110Q', 'Micromax_A110Q', 'Micromax A111', 'Micromax A114', 'Micromax A114R', 'Micromax_A114R', 'Micromax A115', 'Micromax_A115', 'Micromax A116', 'Micromax_A116', 'Micromax A116i', 'Micromax_A116i', 'Micromax A117', 'Micromax_A117', 'Micromax A118R', 'Micromax A119', 'Micromax A120', 'Micromax A121', 'Micromax_A121', 'Micromax A15', 'Micromax A177', 'Micromax A190', 'Micromax_A190', 'Micromax A200', 'Micromax_A200', 'Micromax A21', 'Micromax A210', 'Micromax A24', 'Micromax_A24', 'Micromax A25 Smarty', 'Micromax A250', 'Micromax A255', 'Micromax_A255', 'Micromax A26', 'Micromax_A26', 'Micromax_A27', 'Micromax A27', 'Micromax_A28', 'Micromax A28/GRI40', 'Micromax A28', 'Micromax A290', 'Micromax A30', 'Micromax A300', 'Micromax A310', 'Micromax A311', 'Micromax A315', 'Micromax_A315', 'Micromax_A316', 'Micromax A316', 'Micromax_A34', 'Micromax A34', 'Micromax_A35', 'Micromax A35', 'Micromax A350', 'Micromax_A36', 'Micromax A36', 'Micromax_A37', 'Micromax A37', 'Micromax A37B', 'Micromax_A37B', 'Micromax A40', 'Micromax_A40', 'Micromax A46', 'Micromax_A46', 'Micromax A47', 'MicromaxA47', 'Micromax_A50', 'Micromax A50', 'Micromax A51', 'Micromax A52', 'Micromax A54', 'Micromax A56', 'Micromax_A57', 'Micromax A57', 'Micromax A58', 'Micromax_A58', 'Micromax A59', 'Micromax A60', 'Micromax A61', 'Micromax A62', 'Micromax_A62', 'Micromax A63', 'Micromax_A63', 'Micromax_A65', 'Micromax A65', 'Micromax_A66', 'Micromax A66', 'Micromax A67', 'Micromax A68', 'Micromax A69', 'Micromax_A69', 'Micromax_A70', 'Micromax A700', 'Micromax A71', 'Micromax_A71', 'Micromax A72', 'Micromax_A72', 'Micromax A73', 'Micromax_A74', 'Micromax A74', 'Micromax A75', 'Micromax_A76', 'Micromax A76', 'Micromax A77', 'Micromax A78', 'Micromax A79', 'en_us Micromax A80', 'Micromax A80', 'Micromax A82', 'Micromax_A82', 'Micromax A84', 'Micromax A85', 'Micromax A86', 'Micromax_A86', 'Micromax_A87', 'Micromax A87', 'Micromax A87 . Ninja 4.0', 'Micromax A88', 'Micromax_A88', 'Micromax A89', 'Micromax A90', 'Micromax A90s', 'MIcromax_A90s', 'Micromax A90S', 'Micromax A91', 'Micromax_A91', 'Micromax_A92', 'Micromax A92', 'MicromaxA93', 'Micromax A93', 'Micromax A94', 'Micromax_A94', 'Micromax A96', 'Micromax_A96', 'Micromax A97', 'Micromax_A99', 'Micromax A99', 'Micromax_AD3520', 'Micromax AD3520', 'Micromax AD3550', 'Micromax AD4500', 'Micromax_AD4500', 'Micromax AE90', 'Micromax AO5510', 'Micromax AQ5000', 'Micromax B4A', 'Micromax B5 Pro', 'B5Pro', 'Micromax_Bharat_5_Plus', 'Micromax Q402Plus', 'Micromax Q440', 'Micromax Bharat 5', 'Micromax Q4204', 'Micromax Bharat 5 Plus', 'Micromax Bharat 5 Pro', 'Micromax Bolt 3425', 'Micromax Bolt 2', 'Micromax Q402+', 'Micromax Q306', 'Micromax Q3001', 'Micromax Q301', 'Micromax Q303', 'Micromax Q324', 'Micromax Q326', 'Q327', 'Micromax Q327', 'Micromax Q3301', 'Micromax Q333', 'Micromax_Q333', 'Micromax Q338', 'Micromax Q346', 'Micromax Q354', 'Micromax Q357', 'Micromax Q383', 'Micromax_S302', 'Micromax S302', 'Micromax Q424', 'Micromax Q352', 'Micromax Q4101', 'Micromax C2A', 'Micromax C9', 'Micromax C1', 'Micromax C1A', 'Micromax C2APLS', 'Micromax Q4310', 'Micromax E4815', 'arm_64 Micromax E481', 'Micromax E481', 'Micromax E4816', 'Micromax Q462', 'Micromax Q463', 'Micromax E485', 'Micromax E484', 'Micromax AQ4501', 'Micromax AQ4502', 'A240', 'Micromax A240', 'Micromax Q391', 'Micromax E453', 'Micromax A107', 'Micromax HS2', 'Micromax HS1', 'Micromax_HS3', 'en Micromax_HS3', 'AQ5001', 'Micromax AQ5001', 'AQ5001 Canvas Power', 'Micromax Q392', 'Micromax Q465', 'Micromax Q461', 'Micromax Q350R', 'Micromax Q421', 'Micromax Q417', 'Micromax Q426', 'Micromax Q4260', 'Micromax E311', 'Micromax E352', 'Micromax E455', 'Micromax Q415', 'Micromax Q355', 'Micromax Q469', 'Micromax E451', 'Micromax E451', 'Micromax Q340', 'Micromax Q349', 'Micromax Q345', 'Micromax Q450', 'Micromax Q480', 'arm_64 Micromax Q480', 'Micromax Q380', 'Micromax Q3502', 'Micromax Q351', 'Micromax Q385', 'P70221', 'Micromax P681', 'MicromaxP802', 'Micromax Q427', 'Micromax_Q427', 'Micromax Q413', 'Micromax E313', 'Micromax D2', 'Micromax D200', 'Micromax_D200', 'Micromax D303', 'Micromax D304', 'Micromax_D304', 'Micromax D305', 'Micromax D306', 'Micromax D320', 'Micromax D321', 'Micromax D333', 'Micromax D340', 'Micromax D7517', 'Micromax DM5003', 'Micromax E353', 'Micromax E457', 'Micromax E458', 'Micromax E460', 'Micromax E471', 'Micromax E4817', 'Micromax E482', 'Micromax E483', 'Micromax E5018M', 'Micromax EG111', 'Micromax EG116', 'micromax F', 'micromax F189', 'Micromax F601', 'MicromaxF666', 'Micromax IN', 'Micromax E7533', 'Micromax E6523', 'IN_2b', 'IN_Note1', 'MICROMAX IN1', 'N8216', 'N8301', 'ione note', 'MICROMAX ione note', 'Micromax N4120', 'Micromax N8202', 'Micromax Ninja', 'Micromax Nitro', 'Micromax Note 1+', 'Micromax Note 5', 'Micromax Note3', 'Micromax NX', 'Micromax P001', 'Micromax P250(Funbook)', 'Micromax P255', 'Micromax P256', 'xx Micromax P275', 'Micromax_P275', 'Micromax P275', 'Micromax P280', 'Micromax P290', 'Micromax P310', 'Micromax P350', 'xx Micromax P350', 'Micromax P360', 'Micromax P362', 'Micromax P365', 'Micromax P410', 'Micromax P410i', 'Micromax_P410i', 'Micromax P420', 'Micromax P469', 'Micromax P470', 'MicromaxP480', 'Micromax P500(Funbook)', 'Micromax P560', 'Micromax P580', 'Micromax P580i', 'Micromax P600', 'Micromax P650', 'Micromax P650E', 'Micromax P660', 'Micromax P660', 'Micromax_P666', 'Micromax P666', 'MicromaxP680', 'Micromax P690', 'Micromax P701', 'MicromaxP702', 'Micromax P810', 'en Micromax Q300', 'Micromax_Q300', 'Micromax Q323', 'Micromax_Q323', 'Micromax Q325', 'Micromax_Q325', 'Micromax Q331', 'Micromax_Q331', 'Micromax Q332', 'Micromax_Q332', 'Micromax Q334', 'Micromax Q335', 'Micromax_Q335', 'Micromax Q336', 'Micromax_Q336', 'Micromax Q341', 'Micromax Q343', 'Micromax Q348', 'Micromax_Q353', 'en Micromax_Q353', 'Micromax_Q353P', 'Micromax Q3551', 'Micromax Q3555', 'Micromax Q361', 'Micromax Q370', 'Micromax_Q370', 'Micromax Q371', 'Micromax_Q371', 'Micromax Q375', 'Micromax_Q375', 'Micromax Q379', 'Micromax Q381', 'Micromax Q382', 'Micromax Q386', 'Micromax Q394', 'Micromax_Q394', 'Micromax Q395', 'Micromax Q397', 'Micromax Q398', 'arm Micromax Q398', 'Micromax Q400', 'Micromax_Q400', 'Micromax Q4002', 'en Micromax Q4002', 'Micromax Q401', 'Micromax Q402', 'Micromax Q402 Ultra', 'Micromax Q404', 'Micromax Q411', 'Micromax_Q411', 'Micromax Q412', 'Micromax Q414', 'Micromax Q416', 'Micromax Q419', 'Micromax Q4201', 'Micromax Q422', 'Micromax Q4220', 'Micromax Q423', 'Micromax Q428', 'Micromax_Q428', 'Micromax Q429', '720X1280 Micromax Q4309', 'Micromax Q4312', 'en_US Micromax Q437', 'Micromax Q440Plus', 'Micromax Q454', 'Micromax Q470', 'Micromax Q479', 'Micromax Q491', 'Micromax_Q491', 'Micromax Q502+', 'Micromax Q666', 'Micromax Q67', 'micromax Q68', 'micromax Q78', 'Micromax S300', 'Micromax_S300', 'Micromax S301', 'Micromax_S301', 'Micromax Q4311', 'Micromax Q4601', 'Micromax Q409A', 'Micromax Q409', 'Micromax Q452', 'Micromax Unite 3', 'Micromax Unite 2', 'Micromax Unite 2 A106', 'Micromax Q372', 'Micromax V89', 'Micromax Q4001', 'Micromax Q4202', 'Micromax Q4251', 'arm Micromax Q4251', 'Micromax W5509', 'Micromax X5098', 'Micromax-Xzoom A52', 'YU5530', 'YU5040', 'Micromax YU5900', 'YU5012', 'Micromax Z59']
        mz_plus = ['MZ-m1 note','MZ-m2 note','MZ-M3s','MZ-M3','MZ-M5s','MZ-M3 Max','MZ-m3 note','MZ-MX4','MZ-U20','MZ-MX4 Pro','MZ-PRO 5','MZ-U10','MZ-M5c','MZ-meizu M8 lite','MZ-mmm52','MZ-Meizu S6','MZ-M3 Max','MZ-M1 E','MZ-meizu note9','MZ-16 X','MZ-16th Plus','MZ-15 Plus','MZ-16T','MZ-M6','MZ-PRO 7 Plus','MZ-m1 metal','MZ-16s Pro','MZ-M5 Note','MZ-Meizu 6T','MZ-16 X','MZ-16th','MZ-MEIZU 18X','MZ-MEIZU 18s','MZ-M1822','MZ-meizu 17','MZ-meizu 17 Pro','MZ-MEIZU 18 Pro','MZ-TYH212U','MZ-MEIZU 20','MZ-MEIZU 20 Pro','Meizu C3','MZ-ZTE T660','ZTE BLADE 8']
        vivo = ['vivo 1002T', 'Vivo 1605', 'vivo 1730', 'vivo 1809', 'vivo_1820', 'vivo 1835', 'vivo 1914', 'vivo 2010', 'vivo 2019', 'vivo 2019', 'vivo 2019', 'vivo 2023', 'vivo 2027', 'vivo 3969', 'VIVO 5', 'Vivo 6', 'Vivo 7 Pro', 'Vivo 8', 'Vivo 93K Prime', 'vivo A5 ', 'vivo a54', 'Vivo A54', 'vivo a57', 'Vivo A87', 'VIVO A94', 'VIVO AIR', 'VIVO C8818', 'vivo E1', 'vivo E3', 'vivo E3', 'vivo E5', 'Vivo EGO', 'V1962BA', 'vivo h5', 'V1824A', 'V1824A', 'V1824BA', 'V2217A', 'V2217A', 'V2218A', 'V2218A', 'V2218A', 'V2243A', 'V1955A', 'I1927', 'I1928', 'V2024A', 'V2025A', 'V2025A', 'V2049A', 'V2049A', 'I2009', 'I2012', 'I2012', 'V2136A', 'V2136A', 'V2141A', 'V2171A', 'I2017', 'V2172A', 'V2172A', 'I2022', 'I2019', 'I2019', 'I2201', 'V1914A', 'V1914A', 'V1981A', 'V2055A', 'V2118A', 'V2157A', 'V2157A', 'V2154A', 'V2196A', 'V2196A', 'V2199A', 'V2231A', 'V2238A', 'V1936AL', 'V1936A', 'V1922A', 'V1922A', 'V1922A ', 'V1916A', 'V2023A', 'V2023A', 'VIVO V2023A', 'V2065A', 'V2061A', 'V2061A', 'V2143A', 'V2106A', 'V2165A', 'V2165A', 'V2180GA', 'V1986A', 'V2012A', 'V2012A', 'V2073A', 'V2073A', 'I2011', 'V2148A', 'I2018', 'V1919A', 'V2131A', 'V2220A', 'I2202', 'I2206', 'I2203', 'I2202', 'I2127', 'I2202', 'I2208', 'I2208', 'I2126', 'I2126', 'I2126', 'V2164KA', 'V2164KA', 'VIVO IV', 'VIVO IV', 'VIVO IV', 'VIVO IV', 'Vivo J5', 'vivo 1805', 'vivo 1805', 'vivo NEX', 'V1923A', 'vivo 1912', 'V1923A', 'vivo 1912', 'vivo 1913', 'V1924A', 'V1924A', 'vivo 1913', 'V1950A', 'V1950A', 'vivo NEX A', 'vivo NEX A', 'vivo 1813', 'V1821A', 'V1821A', 'vivo NEX S', 'vivo NEX S', 'Vivo ONE', 'Vivo ONE', 'PA2170', 'vivo PD1628F_EX', 'vivo PD1709', 'vivo PD1709F_EX', 'vivo PD1709F_EX', 'vivo PD1728', 'vivo PD1728', 'vivo PD1832F_EX', 'vivo PD2046F_EX', 'vivo PD2050F_EX', 'vivo PD2055F_EX', 'vivo PD2059F_EX', 'Vivo S', 'V1831A', 'V1831A', 'VIVO S1', 'Vivo S1 Prime', 'V1832A', 'V1832T', 'V2121A', 'V2121A', 'V2130A', 'V2130A', 'Vivo S11', 'Vivo S11 ', 'vivo S11t', 'vivo S11t', 'vivo S11t', 'vivo S11t', 'vivo S12', 'V2162A', 'Vivo S13', 'V2203A', 'V2207A', 'V2190A', 'V2244A', 'vivo S1Pro', 'Vivo S20 ', 'Vivo S21 ', 'Vivo S31', 'Vivo S4', 'Vivo S40', 'Vivo S41 /MMB439M', 'V1932A', 'vivo S6', 'V1962A', 'vivo S6T', 'V2020CA', 'V2020A', 'Vivo S76', 'V2031EA', 'vivo S7i(t)', 'vivo S7i(t)', 'vivo S7i(t)', 'V2080A', 'vivo S7t', 'vivo_S7t', 'vivo S7t', 'S7t 5G', 'vivo S7w', 'vivo S8', 'vivo S9', 'vivo S9', 'vivo S9', 'V2072A', 'V2048A', 'vivo S9t', 'V2168', 'V2168', 'V2153', 'V2153', 'V2150', 'V2151', 'V2151', 'V2151', 'V2143', 'vivo TD1602_EX', 'vivo U1', 'vivo 1916', 'vivo 1916', 'vivo 1921', 'V1941A', 'V1941A', 'V1928A', 'vivo V1', 'vivo V1', 'vivo V10', 'Vivo V10', 'VIVO V11', 'Vivo V11', 'vivo 1804', 'vivo 1804', 'vivo 1806', 'vivo 1806', 'vivo v11pro', 'vivo 1819', 'vivo 1818', 'vivo 1818', 'vivo 1920', 'vivo 1919', 'vivo 1907', 'vivo 1907', 'vivo 1907_19', 'vivo 1910', 'vivo 1909', 'vivo 1910', 'vivo 1933', 'vivo 1933', 'vivo V1907', 'vivo v19neo', 'vivo V1Max', 'vivo V1Max', 'vivo V2', 'V2040', 'vivo 2018', 'vivo 2018', 'V2022', 'Vivo V20A', 'Vivo V20G', 'V2066', 'V2108', 'V2050', 'V2050', 'V2050', 'V2061', 'V2055', 'Vivo V21S', 'V2130', 'V2132A', 'V2116', 'V2115', 'V2116', 'V2116', 'V2126', 'V2126', 'V2228', 'V2228', 'V2158', 'V2158', 'V2202', 'V2202', 'V2201', 'V2246', 'V2230', 'V2230', 'V2237', 'vivo V3', 'vivo V3', 'vivo V3Max A', 'vivo V3Max L', 'vivo v30', 'vivo v31', 'vivo V3L', 'vivo V3L', 'vivo V3L', 'vivo V3L', 'vivo V3M A', 'vivo V3M A', 'vivo V3MA', 'vivo_V3Max', 'vivo v45', 'vivo 1601', 'vivo V5', 'vivo 1609', 'vivo 1611', 'Vivo V51', 'Vivo V54', 'vivo 1612', 'vivo 1713', 'vivo V5S A', 'vivo 1718', 'vivo 1716', 'vivo Y79A', 'vivo Y79A', 'V2166BA', 'Vivo V8', 'vivo 1723', 'vivo V9 mini', 'vivo 1851', 'VIVO V9Pro', 'vivo 1851', 'vivo 1727', 'Vivo X', 'V2178A', 'V2229A', 'V2170A', 'V2170A', 'vivo Xplay3S', 'vivo Xplay3S', 'vivo Xplay3S', 'vivo Xplay5A', 'vivo Xplay5A', 'vivo Xplay5A', 'vivo Xplay5S', 'vivo Xplay5S', 'vivo Xplay6', 'vivo Xplay6L', 'vivo Xplay6', 'vivo Xplay6', 'vivo X710L', 'vivo X710L', 'vivo X710L', 'vivo X710L', 'vivo X1', 'vivo X1', 'vivo X1', 'vivo X1', 'Vivo X11', 'vivo X1S', 'vivo X1S', 'vivo X1S', 'vivo X1St', 'vivo X1St', 'vivo X1St', 'vivo X1St', 'vivo X1St', 'vivo X1W', 'vivo X1w', 'VIVO X2', 'VIVO X2', 'VIVO_X2', 'vivo X20', 'vivo X20A', 'vivo X20Plus A', 'vivo 1720', 'vivo X20Plus UD', 'vivo X20Plus UD', 'vivo X21', 'vivo X21A', 'vivo X21UD A', 'vivo X21i', 'vivo X21i A', 'vivo X21i', 'vivo X21i A ', 'V1814A', 'V1814T', 'V1814T', 'V1814A', 'V1809A', 'V1809A', 'V1816A', 'V1809T', 'V1816T', 'V1829A', 'V1838A', 'V1838T', 'V1829T', 'V1836A', 'V1836A', 'V1836T', 'vivo X27Pro', 'V1938CT', 'V1938T', 'V1938T', 'vivo X3F', 'vivo X3F', 'vivo X3F', 'vivo X3L', 'vivo X3L', 'vivo X3S', 'vivo X3S', 'vivo X3S', 'vivo X3S', 'vivo X3S', 'vivo X3S', 'vivo X3S W', 'vivo X3S W', 'vivo X3S W', 'vivo X3S W', 'vivo X3t', 'vivo X3t', 'vivo X3t', 'vivo X3t', 'vivo X3V', 'vivo X3V', 'vivo X3V', 'vivo X3V', 'Vivo X40', 'vivo X5L', 'vivo X5', 'vivo X5L', 'vivo X5Pro D', 'vivo X5Pro L', 'vivo X5Pro V', 'vivo X5Pro D', 'vivo X5Pro D', 'V2001A', 'V2001A', 'vivo 2004', 'vivo 2005', 'vivo 2005', 'V1937', 'vivo 1937', 'V1937', 'V1937', 'vivo 2006', 'vivo 2006', 'V2005A', 'V2011A', 'X50 Pro+', 'V1930', 'V1930', 'vivo X510t', 'vivo X510t', 'vivo X510t', 'vivo X510t', 'vivo X510t', 'vivo X520L', 'vivo X5F', 'vivo X5M', 'vivo X5M', 'vivo X5M', 'vivo X5Max ', 'vivo X5Max L', 'vivo X5Max L', 'vivo X5Max S', 'vivo X5Max V', 'vivo X5S L', 'vivo X5S L', 'vivo X5V', 'vivo X5V', 'vivo X5V', 'vivo X6D', 'vivo X6A', 'vivo X6Plus D', 'vivo X6Plus A', 'vivo X6Plus L', 'vivo X6Plus D', 'vivo X6Plus A', 'vivo X6Plus D', 'vivo X6Plus L', 'V2046A', 'V2059A', 'V2046A', 'V2045', 'V2046', 'V2047A', 'V2056A', 'V2085A', 'vivo X6S A', 'vivo X6S A', 'vivo X6S A', 'vivo X6S A', 'vivo X6SPlus D', 'vivo X6SPlus D', 'vivo X6SPlus D', 'vivo X6SPlus D', 'vivo X6SPlus A', 'vivo X7L', 'vivo X7Plus', 'vivo X7Plus', 'V2133A', 'V2104', 'V2104', 'V2105', 'V2134A', 'V2105', 'V2145A', 'V2114', 'V2145A', 'vivo X710F', 'vivo X710F', 'vivo X710F', 'vivo X710F', 'V2144', 'V2183A', 'V2144', 'V2208', 'V2185A', 'V2145', 'V2185A', 'Vivo X83', 'vivo X9', 'vivo X9L', 'vivo X9', 'vivo X9', 'vivo X9Plus', 'vivo X9Plus L', 'V2241A', 'V2242A', 'V2242A', 'V2227A', 'vivo X9i', 'vivo X9i', 'vivo X9i', 'vivo X9s', 'vivo X9s L', 'vivo X9s Plus', 'vivo X9s Plus', 'vivo X9s Plus L', 'vivo X9s Plus', 'VIVO XL', 'vivo Xplay', 'vivo Xshot', 'vivo Xshot', 'vivo Xshot', 'vivo Xshot', 'V2203', 'V2221', 'Vivo y1', 'Vivo Y1', 'V2168A', 'V2168A', 'vivo 1906', 'V2028', 'vivo Y11t', 'vivo Y11t', 'vivo Y11t', 'vivo 1904', 'V2163A', 'V2102', 'V2102', 'vivo 2007', 'vivo 2007', 'Vivo Y12I Pro', 'V2026', 'V2042', 'V2033', 'V2039', 'V2069', 'V2026_21', 'vivo Y13L', 'vivo Y13', 'vivo Y13L', 'vivo Y13L', 'vivo Y13i', 'vivo_Y13i', 'vivo Y13iL', 'vivo Y13iL', 'vivo Y13T', 'vivo Y13T', 'vivo 1901', 'vivo Y15T', 'vivo Y15T', 'V2134', 'V2147', 'V2147', 'V2212', 'V2120', 'V2204', 'V2214', 'V2204', 'vivo 1902', 'vivo 1902_19', 'VIVO 1902', 'vivo Y17T', 'vivo Y17T', 'vivo_Y17T', 'vivo Y17T', 'vivo Y17W', 'vivo Y17W', 'vivo Y17W', 'vivo Y18L', 'vivo Y18L', 'vivo Y18L', 'vivo 1915', 'vivo Y19t', 'vivo Y19t', 'vivo Y19t', 'vivo Y19t', 'Vivo Y1i', 'vivo 2015', 'vivo 2015', 'V2029', 'V2027', 'V2043_21', 'V2101', 'V2070', 'V2054', 'V2052', 'V2037', 'V2032', 'V2038', 'V2038', 'V2129', 'V2129', 'V2111', 'V2149', 'V2140', 'V2140', 'V2152', 'V2152', 'V2110', 'V2110', 'V2131', 'V2135', 'V2207', 'vivo Y22iL', 'vivo Y22iL', 'V2206', 'V2206', 'vivo Y23L', 'vivo Y23L', 'vivo y23l', 'vivo Y23L', 'vivo Y23L', 'vivo Y23L', 'vivo 1613', 'vivo Y27', 'vivo Y27L', 'vivo Y27', 'vivo Y28', 'vivo Y28', 'vivo Y28L', 'vivo Y28L', 'vivo Y29L', 'vivo Y29L', 'vivo Y29L', 'V1901A', 'V1901A', 'V1901A', 'V1901T', 'V1930A', 'vivo 1938', 'V2034A', 'V2036A', 'V2099A', 'V2099A', 'V2160', 'V2160', 'V2160', 'V2066BA', 'V2066A', 'Y30g', 'Vivo Y30S', 'vivo Y31L', 'V2068', 'V2054A', 'V2068A', 'V2068', 'V2158A', 'Vivo Y32', 'V2180A', 'V2057', 'V2109', 'V2166A', 'V2166A', 'V2146', 'V2205', 'V2205', 'vivo Y37A', 'vivo Y37', 'V2044', 'vivo Y3t', 'vivo Y3t', 'vivo Y3t', 'vivo y41', 'vivo Y5 ', 'Vivo Y5', 'vivo 1935', 'VIVO Y50(2021)', 'V2023EA', 'Y50t', 'V2035', 'vivo Y51L', 'vivo Y51A', 'V2030', 'vivo 1707', 'V2031_21', 'vivo Y51t L', 'vivo Y51t L', 'vivo Y51t L', 'V2053', 'V2057A', 'vivo Y53', 'vivo 1606A', 'vivo Y53n', 'V2058', 'V2123A', 'V2069A', 'V2045A', 'V2045A', 'vivo Y55A', 'V2127', 'V2127', 'vivo 1603', 'vivo Y55n', 'vivo 1610', 'V2164A', 'V2164A', 'V1934A', 'V2006', 'vivo Y613', 'vivo Y613', 'vivo Y613F', 'vivo Y622', 'vivo Y622', 'vivo Y622', 'vivo Y622', 'vivo Y622', 'vivo Y623', 'vivo Y623', 'vivo Y627', 'vivo Y627', 'vivo Y627', 'vivo Y627', 'vivo Y628', 'vivo Y628', 'vivo 1719', 'vivo Y66', 'vivo Y66L', 'vivo Y66i A', 'vivo Y67', 'vivo Y67A', 'vivo Y67L', 'vivo Y685', 'vivo 1714', 'vivo Y69A', 'V2002A', 'V2002A', 'vivo Y71A', 'vivo 1724', 'vivo Y71A', 'vivo 1801', 'V2041', 'V2060', 'V2102A', 'V1731CA', 'vivo Y73', 'Vivo Y73 /MMB239M', 'V2059', 'V2031A', 'V2164PA', 'V2117', 'vivo Y75A', 'V2142', 'V2142', 'vivo Y75s', 'vivo Y75s', 'vivo Y75S', 'vivo Y75s', 'V2124', 'V2156A', 'V2219A', 'V2219A', 'V2169', 'V2169', 'V1913A', 'vivo 1808i', 'vivo 1803', 'vivo 1803', 'vivo 1812', 'vivo Y81S', 'V1732A', 'V1732T', 'vivo Y83A', 'vivo 1802', 'vivo Y83A', 'vivo Y83A', 'vivo 1726', 'Vivo Y83I', 'vivo Y85A', 'vivo Y85', 'Vivo Y85i', 'Vivo Y86', 'V1730EA', 'vivo v1730ea', 'vivo 1908', 'vivo 1823', 'vivo 1908_19', 'vivo 1817', 'vivo 1811', 'vivo Y913', 'vivo Y913', 'vivo Y91C', 'vivo 1820', 'vivo 1816', 'vivo Y923', 'vivo Y923', 'vivo Y927', 'vivo Y927', 'vivo Y928', 'vivo Y928', 'vivo Y928', 'vivo 1814', 'V1818A', 'V1818A', 'vivo 1814', 'vivo Y937', 'vivo Y937', 'vivo Y937', 'V1818CT', 'V1818CA', 'vivo 1807', 'vivo Y95', 'V1813A', 'V1813T', 'V1813A', 'vivo Y97', 'V1945A', 'V1801A0', 'vivo Z1', 'vivo 1918', 'vivo 1951', 'vivo 1951', 'VIVO Z1Pro', 'vivo 1918', 'vivo 1918 Flow', 'Vivo Z10', 'vivo Z1i', 'V1730DA', 'V1730DT', 'vivo Z1i', 'vivo_1951', 'vivo 1917', 'V1813BA', 'V1813BT', 'V1813BT', 'Vivo Z34', 'vivo Z3x', 'V1730GA', 'vivo Z3x', 'vivo Z3x', 'V1921A', 'V1911A', 'V1911A', 'V1911A', 'V1990A', 'V1990A', 'V1963A', 'V1963A']
        vivo2 = ["vivo/iQOO 5 Pro", "vivo/iQOO 7", "vivo/iQOO Z5", "vivo/iQOO U3", "vivo/iQOO U1x", "vivo/iQOO Neo 3", "vivo/iQOO U1", "vivo/iQOO 8", "vivo/iQOO 9", "vivo/iQOO Z3", "vivo/iQOO Z6", "vivo/iQOO Z7", "vivo/iQOO U5", "vivo/iQOO U3x", "vivo/iQOO 6", "vivo/iQOO 10", "vivo/iQOO Z1", "vivo/iQOO 11", "vivo/iQOO Z2", "vivo/iQOO 12", "vivo/iQOO Z4", "vivo/iQOO 13", "vivo/iQOO Z8", "vivo/iQOO 14", "vivo/iQOO Z9", "vivo/iQOO 15", "vivo/iQOO Z10", "vivo/iQOO 16", "vivo/iQOO Z11", "vivo/iQOO 17", "vivo/iQOO Z12"]
        oneplus = ['NE2213', 'NE2217', 'NE2215', 'NE2210', 'NE2210', 'CPH2423', 'CPH2411', 'CPH2417', 'CPH2413', 'CPH2415', 'CPH2449', 'CPH2487', 'ONE A2003', 'ONE A2003', 'ONE A2001', 'ONE A2005', 'ONEPLUS A3003', 'ONEPLUS A3000', 'ONEPLUS A3010', 'ONEPLUS A5000', 'ONEPLUS A5000', 'ONEPLUS A5010', 'ONEPLUS A5010', 'ONEPLUS A5010', 'ONEPLUS A5010', 'ONEPLUS A5010', 'ONEPLUS A6003', 'ONEPLUS A6000', 'ONEPLUS A6010', 'ONEPLUS A6013', 'ONEPLUS A6010', 'GM1900', 'GM1901', 'GM1903', 'GM1917', 'GM1913', 'GM1911', 'GM1910', 'GM1915', 'GM1910', 'HD1901', 'HD1903', 'HD1900 Flow', 'HD1905', 'HD1900', 'HD1907', 'HD1911', 'HD1913', 'HD1910', 'GM1925', 'HD1925', 'GM1920', 'IN2013', 'IN2015', 'IN2010', 'IN2010', 'IN2017', 'IN2019', 'IN2023', 'IN2025', 'IN2020', 'OnePlus8Pro', 'KB2005', 'KB2001', 'KB2007', 'KB2003', 'KB2000', 'OnePlus 8T 5G', 'LE2115', 'LE2113', 'LE2111', 'LE2110', 'LE2120', 'LE2125', 'LE2123', 'LE2121', 'LE2127', 'OnePlus9Pro', 'LE2101', 'LE2100', 'MT2111', 'MT2110', 'ONEPLUS A19677', 'ONEPLUS A2345', 'Oneplus A31', 'Oneplus A3331', 'ONEPLUS A35904', 'ONEPLUS A37000', 'ONEPLUS A3EVB', 'ONEPLUS A62322', 'ONEPLUS A64794', 'ONEPLUS A65369', 'ONEPLUS A68333', 'ONEPLUS A70458', 'ONEPLUS A70791', 'ONEPLUS A78637', 'ONEPLUS A80828', 'ONEPLUS A83306', 'ONEPLUS A87046', 'ONEPLUS A90641', 'Oneplus A99831', 'PGKM10', 'PGKM10', 'PHK110', 'PHK110', 'PGP110', 'PGP110', 'PGZ110', 'ONEPLUS KB2023', 'OnePlus Nord', 'Oneplus Nord 2', 'DN2103', 'DN2101', 'CPH2399', 'CPH2401', 'AC2001', 'AC2003', 'IV2201', 'CPH2409', 'CPH2381', 'CPH2465', 'EB2103', 'EB2101', 'EB2101', 'BE2025', 'BE2026', 'BE2029', 'Nord N10 5G', 'BE2028', 'BE2013', 'BE2011', 'BE2012', 'CPH2459', 'GN2200', 'CPH2469', 'DE2118', 'DE2117', 'A0001', 'ONE E1001', 'ONE E1003', 'ONE E1001', 'ONE E1005']
        oppo = ["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"]
        oppo2 = ["OP4F97", "OP4BA5L1", "OP664D1", "OP5F11L1", "OP2A92", "OP8F17", "OP8F31", "OP4C9E1", "OP5B31", "OP4BA6L1", "OP2B87", "OP6F21", "OP6C8E1", "OP8F11", "OPPOA16", "OPPOA15", "OPPOA11", "OPPOA73", "OPPOA37", "OPPOA53", "OPPOA33", "OPPOA93", "OPPOA35", "OPPOA83", "OPPOA57", "OPPOA71", "OPPOA39", "OPPOA3", "OPPOA51", "OPPOA27", "OPPOA79"]
        poco = ['M2006C3MI', '211033MI', '22031116AI', '220333QPG', '220333QPG', 'POCO C40', 'POCO C40', 'POCO F2 Pro', 'POCO F2 Pro', 'M2012K11AG', 'M2104K10I', '22021211RG', '22021211RI', 'POCO F4', 'POCO F4', 'POCO F4', '21121210G', 'POCO F4 GT', 'POCO F4 GT', '23049PCD8G', '23013PC75G', 'M2004J19PI', 'POCO M2 Pro', 'POCO M2 Pro', 'M2010J19CI', 'M2010J19CG', 'POCO M3', 'POCO M3 Pro', 'POCO M3 Pro', 'M2103K19PG', 'POCO M3 Pro 5G', '22041219PG', '22041219PI', 'POCO M4 5G', '2201117PG', '21091116AG', 'POCO M4 Pro 5G', 'POCO M4 Pro 5G', 'POCO M4 Pro 5G', 'POCO M4 Pro 5G', '22071219CG', 'POCO M5', 'POCO M5', '22071219CI', '2207117BPG', 'POCO M5s', 'POCO X2', 'M2007J20CI', 'M2007J20CI', '21061110AG', 'M2007J20CG', 'M2102J20SG', 'M2102J20SI', '22041216G', 'POCO X4 GT', '22041216G', 'POCO X4 GT', 'POCO X4 GT', 'POCO X4 GT', '2201116PG', 'POCO X4 Pro 5G', '2201116PG', '2201116PI', '22111317PG', 'POCO X5 5G', 'POCO X5 5G', '22101320G', 'POCO X5 Pro 5G', 'POCO X5 Pro 5G', 'POCO X5 Pro 5G', '22101320G']
        dpi = str(random.choice(['320dpi','640dpi','213dpi','480dpi','420dpi','240dpi','280dpi','160dpi','560dpi','540dpi','272dpi','360dpi','720dpi','270dpi','450dpi','600dpi','279dpi','210dpi','180dpi','510dpi','300dpi','454dpi','314dpi','288dpi','401dpi','153dpi','267dpi','345dpi','493dpi','340dpi','604dpi','465dpi','680dpi','256dpi','290dpi','432dpi','273dpi','120dpi','200dpi','367dpi','419dpi','306dpi','303dpi','411dpi','195dpi','518dpi','230dpi','384dpi','315dpi','293dpi','274dpi','235dpi']))
        pxl = str(random.choice(['720x1280','1440x2560','1440x2768','1280x720','1280x800','1080x1920','540x960','1080x2076','1080x2094','1080x2220','480x800','768x1024','1440x2792','1200x1920','720x1384','1920x1080','720x1369','800x1280','720x1440','1080x2058','600x1024','720x1396','2792x1440','1920x1200','2560x1440','1536x2048','720x1382','1080x2113','1080x2198','1080x2131','720x1423','1080x2069','720x1481','1080x2047','1080x2110','1080x2181','1080x2209','1080x2180','1080x2020','1080x2095','1440x2723','1080x2175','720x1365','1440x2699','1080x2218','2699x1440','1440x2907','1080x2257','720x1370','1080x2042','720x1372','1080x2200','1080x2186','720x1361','1080x2024','1080x2006','720x1402','1440x2831','720x1454','1080x2064','1440x2933','720x1411','720x1450','1440x2730','1080x2046','2094x1080','540x888','1440x2759','1080x2274','1080x2178','1440x2706','720x1356','720x1466','1440x2900','2560x1600','1080x2038','1600x2452','1080x2129','720x1422','720x1381','1080x2183','1080x2285','800x1216','1080x2216','1080x2168','1080x2119','1080x2128','1080x2273','2274x1080','1080x2162','1080x2164','2076x1080','1024x768','1080x2173','1440x2845','1080x2134','720x1379','1440x2838','1080x2139','2131x1080','1440x2744','1080x2192','720x1406','1440x2960','1080x2029','2042x1080','1080x2212','1406x720','1080x2288','2047x1080','1080x2051','720x1398','1280x736','1382x720','720x1353','1080x2050','1080x2028','1080x2256','2711x1440','2175x1080','1080x2281','2560x1492','1440x2923','1200x1845','1080x2189','1080x2002','1440x2711','2110x1080','960x540','1080x2033','2200x1080','720x1452','720x1480','1440x2735','720x1472','1080x2277','1080x2169','2874x1440','1600x2560','1080x2151','2218x1080','1080x2182','720x1468','1440x2898','1080x2011','1080x2201','720x1380','1080x2287','2069x1080','1200x1836','2046x1080','720x1439','2058x1080','2182x1080','720x1399','1080x2282','1440x2721','1080x2324','720x1432','1080x2165','1080x2150','1080x2156','1080x1872','1440x3048','1532x2560','720x1355','720x1390','720x1476','720x1410','1080x2032','720x1437','1440x2682','1440x2921','1080x2270','1080x2160','720x1446','1200x1848','1440x2874','1080x2309','1080x2174','1440x2867','1080x2060','1080x2196','1080x2401','1536x1922','1080x2280','1080x2123','720x1435','1440x2927','1080x2276','720x1448','720x1469','720x1344','1080x2187','540x937','1440x3028','1080x2184','1440x2718','1080x2326','840x1834','1440x2935','1440x2880','1440x2892','2048x2048','1080x2195','1080x2322','720x1419','987x1450','1080x2092','1440x3047','720x1358','1080x2136','720x1357','1080x2093','720x1477','1080x2312','1080x2361','720x1341','720x1507','1080x2172','720x1337','1080x2177','1080x2125','1440x2891','1600x2434','720x1394','1080x2159','720x1387','1080x2166','1080x2154','1080x2147','1440x2747','1080x2105','1440x2911','720x1473','1080x2055','1080x2265','720x1436','1080x2190','1600x2526','720x1373','720x1415','1080x2249','1080x2254','720x1455','1440x3040','1080x2149','720x1385','1440x3036','1080x2111','1440x2904','720x1442','720x1377','1080x2307','1080x2327','1080x2141','1080x2025','720x1430','720x1375','1080x2283','1440x2779','1080x2321','1080x2268','1440x2758','1752x2698','1080x2267','1200x1856','1440x2756','720x1464','1080x2234','1080x2171','1080x2155','720x1463','1080x2122','720x1467','1080x2264','720x1349','1440x2999','720x1458','1080x2015','720x1431','1242x2208','1080x2185','1080x2148','1080x2163','1440x2780','720x1445','1080x2146','1200x1916','720x1502','1200x1928','720x1506','720x1424','720x1465','720x1420','1080x2176','720x1521','1080x2315','1080x2400','720x1471','1080x2157','1600x2458','1080x2067','1080x2191','1080x2271','720x1407','800x1208','1080x2087','1080x2199','578x1028','720x1485','540x879','1080x2179','720x1555','810x1598','720x1378','1200x1897','720x1395','720x1459','900x1600','1080x2275','1440x2733']))
        mt_qcom = str(random.choice(["qcom","mt6769", "qcom", "mt6768", "qcom","mt6767", "qcom","mt6765", "qcom","mt6763", "qcom","mt6757", "qcom","mt6755", "qcom","mt6753", "qcom","mt6739", "qcom","mt6737", "qcom","mt6735", "qcom","mt6595", "qcom","mt6582", "qcom","mt6572", "mt6571", "qcom","mt6570", "qcom","mt8563", "qcom","mt8167", "qcom","mt8163", "mt8135", "qcom","mt8127", "qcom","mt8125", "qcom","mt7623", "qcom","mt6797", "qcom","mt6592", "qcom","mt6590", "qcom","mt6580", "qcom","mt6573", "qcom","mt6575", "qcom","mt6260", "qcom","mt6236"]))
        device_android = str(random.choice(["27/9","27/10","27/11","27/12","27/12","27/13","28/9","28/10","28/11","28/12","28/12","28/13","29/9","29/10","29/11","29/12","29/12","29/13","27/9","30/10","30/11","30/12","30/12","30/13","31/9","31/10","31/11","31/12","31/12","31/13","32/9","32/10","32/11","32/12","32/12","32/13","33/9","33/10","33/11","33/12","33/12","33/13"]))
        kode = str(random.choice(['145652090','206670917','185203686','192992561','183982986','206670927','150338061','183982962','127049016','175574603','155374054','205858247','135374896','206670920','169474958','206670926','160497905','161478672','192992578','206670929','131223243','206670916','142841919','187682681','171727795','151414277','206670922','160497915','207505137','165030898','208061741','208061688','208180365','208061674','197825052','147375133','208061744','196643798','208061725','122338247','157536430','208061728','209143963','208727155','209143726','205280539','209143903','209143970','181496409','208061739','209143957','210180522','210180512','209143881','209143712','180322805','210180521','195435561','210370119','210180523','210180493','175574596','210180510','210180480','210180513','210180517','176649504','177770663','210180479','211114117','210908379','206670921','211114134','183982943','211399345','211399342','211399332','201775962','211574187','211574249','210180519','167338559','185203649','124583960','211399337','211399335','197825163','166149717','211399336','212063371','211399329','209143954','210180482','168361634','212214017','209143867','211399341','211399340','212214027','195435510','122338243','139237670','152367502','212676872','212676898','212676875','212676895','212676901','209823384','212676869','196643822','212676878','213367980','213368005','212676886','213558743','209143913','212214039','158441917','174081672','213558750','201775966','188791681','185203705','143631575','161478664','214245350','161478663','212676881','213558770','214245346','138226752','214245221','214245182','214245206','214245218','214245354','214245295','214245199','214245304','214245280','214446313','214245187','214245288','214139002','202766605','214245319','214646783','158441914','215246048','195435544','208061677','215464400','128676146','215464389','215464385','215464390','215464398','182747397','215464393','216233197','201775791','216817344','215464395','216817286','185203642','164094529','216817305','215464401','162439029','215464382','216817280','216817331','214330969','216817299','216817357','217948981','217948980','217948956','217948959','217948968','216817296','217948952','217948982','216817269','219308759','219308726','182747387','219308721','219308754','219308763','176649435','183982982','219909486','127049038','219308730','221134012','221134032','221134009','221134037','194383426','221134029','221134005','221134018','145652093','225283632','165031108','225283625','224652582','139906580','225283628','225283624','226142579','225283634','225283631','226493211','225283623','185203672','156514151','218793478','225283621','227299063','225283627','227299064','227299021','227299027','227544546','227299041','227299060','227299012','228970707','228970705','227299005','228970687','228970683','228970694','228970710','228970689','160497904','195435540','129611419','229783842','230291708','228970681','148324047','230877709','231192211','230877674','230877705','230877678','211399328','209143896','230877713','194383428','230877689','221134002','231457747','208061721','230877671','230877668','232868027','232088496','185203706','232868005','232867964','232868001','232868015','232868031','232867959','232868009','164094526','232867941','234041364','182747399','232868024','232867949','234847239','234847238','234847234','162439040','234847229','234847230','181496427','234847240','232867993','195435558','232867967','232867997','234847227','235871830','221133998','236572344','236572377','153386780','236572337','236572349','236572372','234847226','236572383','237507050','238093993','238093948','238093954','238093999','238093982','239490565','239490555','238093946','238093966','239490563','239490550','239974660','240726416','239490568','240726484','240726452','239490551','239490548','240726426','240726476','240726491','240726471','241043882','241114613','236572331','241267273','240726407','241456456','241267278','241267269','241114619','241456445','241456451','242168941','242168928','242168931','242168939','242168925','240726436','242375239','144722090','242168935','242290370','157405369','242168933','242290355','242703240','242807362','242168923','242168943','242991209','243646252','243646269','242991200','243711120','243646267','243711093','243975802','243646263','243646248','243646255','244167578','128676156','194383413','243975835','244390417','244390338','245196084','245196061','240726392','245196055','243646273','245196082','245196063','245196070','245666450','245466705','245870319','245870301','245870347','245196087','246889064','246889072','246889073','246889074','246889065','247146500','246889063','245870262','247370962','247146481','246889068','246889062','247541884','247541831','247370955','247370942','247720736','247720751','248310216','248310220','248310208','247720744','248399342','248310210','247720747','248310206','248717751','248310212','248310221','248823392','248583561','248310205','248899028','248955251','248955247','249178904','248955244','249507608','249507582','249507588','249507585','248955240','249507607','249507592','249810008','249966137','249507610','249966081','249966100','249507599','249966140','249810004','123790722','250188776','249628096','250188788','250742103','250742113','250742102','250877984','250742105','250742111','251048681','250742107','250742115','251048695','251304696','251304682','251524431','251530710','251304689','251524420','251524409','251524390','250742101','251048673','252055918','252055945','251920416','252055944','252055925','252239038','252055936','252055915','252055948','252390568','252390583','252580134','252740497','252740485','252740490','253120615','253325372','253325384','253325385','253447816','253146263','253120607','253325374','253120598','253325371','253447808','253447809','253325378','253447814','253447807','253447811','253447817','253447813','181496411','253447806','255191971','255013798','255777478','255777471','255777474','255777472','255959637','255777477','255959614','255959635','256099199','256099204','150338064','256099153','256099205','256099156','255983744','256107300','255777470','126223536','256203326','256099190','256099151','256324061','256324047','256203339','256966628','256966589','256966626','256966590','124584015','257456576','256966593','257456590','256966629','256966587','256966592','257456586','257456539','259829115','259829104','259829113','260037038','259829105','259829109','260037030','260149625','259829103','260149621','260465044','259829116','260724710','179155058','261079769','261079761','261079768','261079762','261079771','261276939','157405370','135374885','261079765','261393056','261393062','261079760','181496406','182747360','261504698','261690888','261504706','169474957','262218766','262290715','262290774','262372432','262372425','262372431','262886993','262886995','262372426','262886987','261079764','262886986','262886988','262886990','262372433','262886996','263652962','264009049','264009019','264009030','264009021','264009023','264009052','264009024','261763534','174081651','169474965','232867942','264009013','255959606','264009028','267397344','267397322','267925737','267397343','267925708','267397327','267397321','267925714','267258517','267925705','268773287','267925733','268773233','267925702','268773286','159526770','268773239','268773272','269790795','269285030','269790805','269790803','269790792','268773227','269849047','270426177','270426174','271182277','269790789','271182270','268773290','271182266','271182276','269790798','271182279','271182265','271182267','269790807','271823819','272382110','272382111','272382106','272693584','272382095','272382093','272382098','272382100','272382103','273728833','273371577','273728832','273728798','273907093','273907111','273907108','238093987','273907112','273907103','274774869','274774891','274774908','273907087','274774904','274774875','274774914','275292626','276027938','276028040','276027963','276028037','276028020','276028017','274774862','276028013','249507580','276028029','273907098','277249238','277249248','277249249','276028033','277249250','277249226','275292623','277249214','277249242','277249237','277249240','278625447','278002558','278625420','278625431','278625423','117539687','278625416','278625444','277249213','278625451','279469964','279996068','279996060','279996067','279996058','280194220','279996065','279996063','279996061','279996059','280894196','273728787','271182262','281579032','281579023','276514494','281579021','281579027','281579033','268773274','283072590','281579025','283072571','282619332','283489774','283072587','283072567','281579031','283072580','283072574','284459213','284459224','179155089','256966583','284459214','283072585','284459218','284459223','284459225','285338607','275113919','284459221','284459212','284459215','285855793','285855800','285855803','285855791','285855802','285855804','285855795','286809973','287420974','287421023','287420968','287420979','287421017','287421005','287421019','287421012','277249241','288682406','287421026','288682405','288682397','288682407','261079772','288682398','288682401','288205409','289692198','287420997','289692186']))
        kode2 = (f'{random.randint(211111111,399999999)}')
        locale = str(random.choice((["id_ID","en_GB", "en_US", "ar_LY", "fr_FR", "es_ES", "de_DE", "it_IT", "pt_BR", "tr_TR","ru_RU","in_ID"])))
        #versi_facebook = random.choice(("70.0.0.15.98, 80.0.0.20.101,60.0.0.10.76, 85.0.0.25.100,75.0.0.22.99,72.0.0.18.94, 68.0.0.16.84,78.0.0.14.97, 63.0.0.20.81,81.0.0.24.105,73.0.0.16.96,67.0.0.18.88,84.0.0.21.110,74.0.0.18.100,71.0.0.15.92,79.0.0.14.103,62.0.0.18.80,87.0.0.22.115,76.0.0.20.102,83.0.0.18.10,66.0.0.16.87,88.0.0.24.118,77.0.0.22.103,64.0.0.18.82,82.0.0.20.107,69.0.0.14.92,89.0.0.20.123,61.0.0.14.76,86.0.0.18.112,65.0.0.12.86").split(","))
        versi_facebook = (f'{random.randint(299,399)}.{random.randint(1,10)}.0.{random.randint(20,35)}.{random.randint(90,120)}')
        asus = ['ASUS_A002','ASUS_A002A','ASUS_A002_1','ASUS_A002_2','ASUS_AI2201','ASUS_AI2201_B','QTI SM8475','ASUS_I001_1','ASUS_I001D','ASUS_I002D','ASUS_I003_1','ASUS_I003D','ASUS_I004D','ASUS_I005_1','ASUS_I005D','ASUS_I006D','ASUS_I006D','ASUS_I007_1','ASUS_I007D','ASUS_I01WD','ASUS_Z01QD_1','ASUS_Z01QD']
        iphn = random.choice(["11,8", "12,1", "9,2", "13,3", "10,5", "12,8", "10,4", "13,1", "9,1", "11,2"])
        ios = random.choice(["iOS 14_4_1", "iOS 15_0", "iOS 12_1_3", "iOS 15_0_1", "iOS 14_7_1", "iOS 14_6", "iOS 13_5", "iOS 14_0_1", "iOS 11_2_6", "iOS 15_1"])
        scale = random.choice(["2.00", "3.00", "2.61", "2.00", "2.61", "2.00", "3.00", "2.00", "2.61", "3.00"])
        gamut = random.choice(["display", "P3", "display", "wide", "P3", "display", "wide"])
        return(random.choice([
              f'Barcelona {versi_facebook} Android ({device_android}; {dpi}; {pxl}; ASUS MOBILITY LIMITED/asus; {str(random.choice(asus))}; {str(random.choice(asus))}; qcom; in_ID; {kode2})',
              f'Barcelona {versi_facebook} Android ({device_android}; {dpi}; {pxl}; OPPO MOBILITY LIMITED/oppo; {str(random.choice(oppo2))}; {str(random.choice(oppo))}; qcom; in_ID; {kode2})',
              f'Barcelona {versi_facebook} Android ({device_android}; {dpi}; {pxl}; MICROMAX MOBILITY LIMITED/micromax; {str(random.choice(micromax))}; {str(random.choice(micromax))}; qcom; in_ID; {kode2})',
              f'Barcelona {versi_facebook} Android ({device_android}; {dpi}; {pxl}; ONEPLUS MOBILITY LIMITED/oneplus; {str(random.choice(oneplus))}; {str(random.choice(oneplus))}; qcom; in_ID; {kode2})',
              f'Barcelona {versi_facebook} Android ({device_android}; {dpi}; {pxl}; VIVO MOBILITY LIMITED/vivo; {str(random.choice(vivo2))}; {str(random.choice(vivo))}; qcom; in_ID; {kode2})',
              f'Barcelona {versi_facebook} Android ({device_android}; {dpi}; {pxl}; POCO MOBILITY LIMITED/poco; {str(random.choice(poco))}; {str(random.choice(poco))}; qcom; in_ID; {kode2})',
              f"Barcelona {versi_facebook} (iPhone{iphn}; {ios}; in_ID; in_ID; scale={scale}; gamut={gamut}; {pxl}; {kode2})"  
       ])) 
def useragent_facebook2():
        htc = ["HTC One M8", "HTC One M9", "HTC 10", "HTC U11", "HTC U12+", "HTC Desire 626", "HTC Sensation", "HTC EVO 4G", "HTC One X", "HTC Desire Eye", "HTC One A9", "HTC U Ultra", "HTC Butterfly", "HTC Desire 820", "HTC Wildfire", "HTC HD2", "HTC Evo Shift 4G", "HTC Desire 610", "HTC One Mini", "HTC ThunderBolt", "HTC Droid DNA", "HTC Desire 816", "HTC Legend", "HTC Sensation XL", "HTC Incredible S", "HTC One S", "HTC Rhyme", "HTC Desire HD", "HTC Evo 3D", "HTC Touch Pro 2"]
        nexus = ['Galaxy Nexus', 'Nexus 10', 'Nexus 2', 'Nexus 4', 'Nexus 4', 'Nexus 4', 'Nexus 4', 'Nexus 4', 'Nexus 4', 'Nexus 5', 'phone/Nexus 5', 'Nexus 5X', 'Nexus 6', 'Nexus 7', 'Nexus 9', 'Nexus One', 'Nexus One', 'Nexus One', 'Nexus One', 'Nexus One', 'Nexus One', 'Nexus Player', 'Nexus Player', 'Nexus S', 'Nexus S', 'Nexus S 4G', 'nexus S', 'Nexus S', 'Nexus s', 'Nexus S', 'Nexus S', 'Nexus S', 'Nexus S', 'Nexus S']
        pixel = ["Pixel 5a", "Pixel 4a 5G", "Pixel 2 XL", "Pixel 6 Pro", "Pixel 4 XL", "Pixel 5", "Pixel 3", "Pixel 3 XL", "Pixel 4a", "Pixel 4", "Pixel 3a","Pixel 5 XL","Pixel 7a","Pixel 6 XL","Pixel 4a","Pixel 6a","Pixel 3a","Pixel 7 XL"]
        micromax = ['Micromax 10', 'Micromax 1J', 'Micromax 86519', 'Micromax A064', 'Micromax_A064', 'Micromax A065', 'Micromax_A065', 'Micromax A066', 'Micromax_A066', 'Micromax A067', 'Micromax_A067', 'MICROMAX_A068', 'MICROMAX A068', 'Micromax A068', 'Micromax A069', 'Micromax_A069', 'Micromax A075', 'Micromax A082', 'Micromax_A082', 'Micromax A089', 'Micromax_A089', 'Micromax A091', 'Micromax A092', 'Micromax_A092', 'Micromax A093', 'Micromax_A093', 'Micromax A095', 'Micromax A096', 'Micromax_A101', 'Micromax A102', 'Micromax_A102', 'Micromax A104', 'Micromax a104', 'Micromax A105', 'Micromax_A105', 'Micromax A106', 'Micromax-A106', 'Micromax A108', 'Micromax_A109', 'Micromax A109', 'Micromax A110', 'Micromax_A110', 'Micromax A110Q', 'Micromax_A110Q', 'Micromax A111', 'Micromax A114', 'Micromax A114R', 'Micromax_A114R', 'Micromax A115', 'Micromax_A115', 'Micromax A116', 'Micromax_A116', 'Micromax A116i', 'Micromax_A116i', 'Micromax A117', 'Micromax_A117', 'Micromax A118R', 'Micromax A119', 'Micromax A120', 'Micromax A121', 'Micromax_A121', 'Micromax A15', 'Micromax A177', 'Micromax A190', 'Micromax_A190', 'Micromax A200', 'Micromax_A200', 'Micromax A21', 'Micromax A210', 'Micromax A24', 'Micromax_A24', 'Micromax A25 Smarty', 'Micromax A250', 'Micromax A255', 'Micromax_A255', 'Micromax A26', 'Micromax_A26', 'Micromax_A27', 'Micromax A27', 'Micromax_A28', 'Micromax A28/GRI40', 'Micromax A28', 'Micromax A290', 'Micromax A30', 'Micromax A300', 'Micromax A310', 'Micromax A311', 'Micromax A315', 'Micromax_A315', 'Micromax_A316', 'Micromax A316', 'Micromax_A34', 'Micromax A34', 'Micromax_A35', 'Micromax A35', 'Micromax A350', 'Micromax_A36', 'Micromax A36', 'Micromax_A37', 'Micromax A37', 'Micromax A37B', 'Micromax_A37B', 'Micromax A40', 'Micromax_A40', 'Micromax A46', 'Micromax_A46', 'Micromax A47', 'MicromaxA47', 'Micromax_A50', 'Micromax A50', 'Micromax A51', 'Micromax A52', 'Micromax A54', 'Micromax A56', 'Micromax_A57', 'Micromax A57', 'Micromax A58', 'Micromax_A58', 'Micromax A59', 'Micromax A60', 'Micromax A61', 'Micromax A62', 'Micromax_A62', 'Micromax A63', 'Micromax_A63', 'Micromax_A65', 'Micromax A65', 'Micromax_A66', 'Micromax A66', 'Micromax A67', 'Micromax A68', 'Micromax A69', 'Micromax_A69', 'Micromax_A70', 'Micromax A700', 'Micromax A71', 'Micromax_A71', 'Micromax A72', 'Micromax_A72', 'Micromax A73', 'Micromax_A74', 'Micromax A74', 'Micromax A75', 'Micromax_A76', 'Micromax A76', 'Micromax A77', 'Micromax A78', 'Micromax A79', 'en_us Micromax A80', 'Micromax A80', 'Micromax A82', 'Micromax_A82', 'Micromax A84', 'Micromax A85', 'Micromax A86', 'Micromax_A86', 'Micromax_A87', 'Micromax A87', 'Micromax A87 . Ninja 4.0', 'Micromax A88', 'Micromax_A88', 'Micromax A89', 'Micromax A90', 'Micromax A90s', 'MIcromax_A90s', 'Micromax A90S', 'Micromax A91', 'Micromax_A91', 'Micromax_A92', 'Micromax A92', 'MicromaxA93', 'Micromax A93', 'Micromax A94', 'Micromax_A94', 'Micromax A96', 'Micromax_A96', 'Micromax A97', 'Micromax_A99', 'Micromax A99', 'Micromax_AD3520', 'Micromax AD3520', 'Micromax AD3550', 'Micromax AD4500', 'Micromax_AD4500', 'Micromax AE90', 'Micromax AO5510', 'Micromax AQ5000', 'Micromax B4A', 'Micromax B5 Pro', 'B5Pro', 'Micromax_Bharat_5_Plus', 'Micromax Q402Plus', 'Micromax Q440', 'Micromax Bharat 5', 'Micromax Q4204', 'Micromax Bharat 5 Plus', 'Micromax Bharat 5 Pro', 'Micromax Bolt 3425', 'Micromax Bolt 2', 'Micromax Q402+', 'Micromax Q306', 'Micromax Q3001', 'Micromax Q301', 'Micromax Q303', 'Micromax Q324', 'Micromax Q326', 'Q327', 'Micromax Q327', 'Micromax Q3301', 'Micromax Q333', 'Micromax_Q333', 'Micromax Q338', 'Micromax Q346', 'Micromax Q354', 'Micromax Q357', 'Micromax Q383', 'Micromax_S302', 'Micromax S302', 'Micromax Q424', 'Micromax Q352', 'Micromax Q4101', 'Micromax C2A', 'Micromax C9', 'Micromax C1', 'Micromax C1A', 'Micromax C2APLS', 'Micromax Q4310', 'Micromax E4815', 'arm_64 Micromax E481', 'Micromax E481', 'Micromax E4816', 'Micromax Q462', 'Micromax Q463', 'Micromax E485', 'Micromax E484', 'Micromax AQ4501', 'Micromax AQ4502', 'A240', 'Micromax A240', 'Micromax Q391', 'Micromax E453', 'Micromax A107', 'Micromax HS2', 'Micromax HS1', 'Micromax_HS3', 'en Micromax_HS3', 'AQ5001', 'Micromax AQ5001', 'AQ5001 Canvas Power', 'Micromax Q392', 'Micromax Q465', 'Micromax Q461', 'Micromax Q350R', 'Micromax Q421', 'Micromax Q417', 'Micromax Q426', 'Micromax Q4260', 'Micromax E311', 'Micromax E352', 'Micromax E455', 'Micromax Q415', 'Micromax Q355', 'Micromax Q469', 'Micromax E451', 'Micromax E451', 'Micromax Q340', 'Micromax Q349', 'Micromax Q345', 'Micromax Q450', 'Micromax Q480', 'arm_64 Micromax Q480', 'Micromax Q380', 'Micromax Q3502', 'Micromax Q351', 'Micromax Q385', 'P70221', 'Micromax P681', 'MicromaxP802', 'Micromax Q427', 'Micromax_Q427', 'Micromax Q413', 'Micromax E313', 'Micromax D2', 'Micromax D200', 'Micromax_D200', 'Micromax D303', 'Micromax D304', 'Micromax_D304', 'Micromax D305', 'Micromax D306', 'Micromax D320', 'Micromax D321', 'Micromax D333', 'Micromax D340', 'Micromax D7517', 'Micromax DM5003', 'Micromax E353', 'Micromax E457', 'Micromax E458', 'Micromax E460', 'Micromax E471', 'Micromax E4817', 'Micromax E482', 'Micromax E483', 'Micromax E5018M', 'Micromax EG111', 'Micromax EG116', 'micromax F', 'micromax F189', 'Micromax F601', 'MicromaxF666', 'Micromax IN', 'Micromax E7533', 'Micromax E6523', 'IN_2b', 'IN_Note1', 'MICROMAX IN1', 'N8216', 'N8301', 'ione note', 'MICROMAX ione note', 'Micromax N4120', 'Micromax N8202', 'Micromax Ninja', 'Micromax Nitro', 'Micromax Note 1+', 'Micromax Note 5', 'Micromax Note3', 'Micromax NX', 'Micromax P001', 'Micromax P250(Funbook)', 'Micromax P255', 'Micromax P256', 'xx Micromax P275', 'Micromax_P275', 'Micromax P275', 'Micromax P280', 'Micromax P290', 'Micromax P310', 'Micromax P350', 'xx Micromax P350', 'Micromax P360', 'Micromax P362', 'Micromax P365', 'Micromax P410', 'Micromax P410i', 'Micromax_P410i', 'Micromax P420', 'Micromax P469', 'Micromax P470', 'MicromaxP480', 'Micromax P500(Funbook)', 'Micromax P560', 'Micromax P580', 'Micromax P580i', 'Micromax P600', 'Micromax P650', 'Micromax P650E', 'Micromax P660', 'Micromax P660', 'Micromax_P666', 'Micromax P666', 'MicromaxP680', 'Micromax P690', 'Micromax P701', 'MicromaxP702', 'Micromax P810', 'en Micromax Q300', 'Micromax_Q300', 'Micromax Q323', 'Micromax_Q323', 'Micromax Q325', 'Micromax_Q325', 'Micromax Q331', 'Micromax_Q331', 'Micromax Q332', 'Micromax_Q332', 'Micromax Q334', 'Micromax Q335', 'Micromax_Q335', 'Micromax Q336', 'Micromax_Q336', 'Micromax Q341', 'Micromax Q343', 'Micromax Q348', 'Micromax_Q353', 'en Micromax_Q353', 'Micromax_Q353P', 'Micromax Q3551', 'Micromax Q3555', 'Micromax Q361', 'Micromax Q370', 'Micromax_Q370', 'Micromax Q371', 'Micromax_Q371', 'Micromax Q375', 'Micromax_Q375', 'Micromax Q379', 'Micromax Q381', 'Micromax Q382', 'Micromax Q386', 'Micromax Q394', 'Micromax_Q394', 'Micromax Q395', 'Micromax Q397', 'Micromax Q398', 'arm Micromax Q398', 'Micromax Q400', 'Micromax_Q400', 'Micromax Q4002', 'en Micromax Q4002', 'Micromax Q401', 'Micromax Q402', 'Micromax Q402 Ultra', 'Micromax Q404', 'Micromax Q411', 'Micromax_Q411', 'Micromax Q412', 'Micromax Q414', 'Micromax Q416', 'Micromax Q419', 'Micromax Q4201', 'Micromax Q422', 'Micromax Q4220', 'Micromax Q423', 'Micromax Q428', 'Micromax_Q428', 'Micromax Q429', '720X1280 Micromax Q4309', 'Micromax Q4312', 'en_US Micromax Q437', 'Micromax Q440Plus', 'Micromax Q454', 'Micromax Q470', 'Micromax Q479', 'Micromax Q491', 'Micromax_Q491', 'Micromax Q502+', 'Micromax Q666', 'Micromax Q67', 'micromax Q68', 'micromax Q78', 'Micromax S300', 'Micromax_S300', 'Micromax S301', 'Micromax_S301', 'Micromax Q4311', 'Micromax Q4601', 'Micromax Q409A', 'Micromax Q409', 'Micromax Q452', 'Micromax Unite 3', 'Micromax Unite 2', 'Micromax Unite 2 A106', 'Micromax Q372', 'Micromax V89', 'Micromax Q4001', 'Micromax Q4202', 'Micromax Q4251', 'arm Micromax Q4251', 'Micromax W5509', 'Micromax X5098', 'Micromax-Xzoom A52', 'YU5530', 'YU5040', 'Micromax YU5900', 'YU5012', 'Micromax Z59']
        mz_plus = ['MZ-m1 note','MZ-m2 note','MZ-M3s','MZ-M3','MZ-M5s','MZ-M3 Max','MZ-m3 note','MZ-MX4','MZ-U20','MZ-MX4 Pro','MZ-PRO 5','MZ-U10','MZ-M5c','MZ-meizu M8 lite','MZ-mmm52','MZ-Meizu S6','MZ-M3 Max','MZ-M1 E','MZ-meizu note9','MZ-16 X','MZ-16th Plus','MZ-15 Plus','MZ-16T','MZ-M6','MZ-PRO 7 Plus','MZ-m1 metal','MZ-16s Pro','MZ-M5 Note','MZ-Meizu 6T','MZ-16 X','MZ-16th','MZ-MEIZU 18X','MZ-MEIZU 18s','MZ-M1822','MZ-meizu 17','MZ-meizu 17 Pro','MZ-MEIZU 18 Pro','MZ-TYH212U','MZ-MEIZU 20','MZ-MEIZU 20 Pro','Meizu C3','MZ-ZTE T660','ZTE BLADE 8']
        vivo = ['vivo 1002T', 'Vivo 1605', 'vivo 1730', 'vivo 1809', 'vivo_1820', 'vivo 1835', 'vivo 1914', 'vivo 2010', 'vivo 2019', 'vivo 2019', 'vivo 2019', 'vivo 2023', 'vivo 2027', 'vivo 3969', 'VIVO 5', 'Vivo 6', 'Vivo 7 Pro', 'Vivo 8', 'Vivo 93K Prime', 'vivo A5 ', 'vivo a54', 'Vivo A54', 'vivo a57', 'Vivo A87', 'VIVO A94', 'VIVO AIR', 'VIVO C8818', 'vivo E1', 'vivo E3', 'vivo E3', 'vivo E5', 'Vivo EGO', 'V1962BA', 'vivo h5', 'V1824A', 'V1824A', 'V1824BA', 'V2217A', 'V2217A', 'V2218A', 'V2218A', 'V2218A', 'V2243A', 'V1955A', 'I1927', 'I1928', 'V2024A', 'V2025A', 'V2025A', 'V2049A', 'V2049A', 'I2009', 'I2012', 'I2012', 'V2136A', 'V2136A', 'V2141A', 'V2171A', 'I2017', 'V2172A', 'V2172A', 'I2022', 'I2019', 'I2019', 'I2201', 'V1914A', 'V1914A', 'V1981A', 'V2055A', 'V2118A', 'V2157A', 'V2157A', 'V2154A', 'V2196A', 'V2196A', 'V2199A', 'V2231A', 'V2238A', 'V1936AL', 'V1936A', 'V1922A', 'V1922A', 'V1922A ', 'V1916A', 'V2023A', 'V2023A', 'VIVO V2023A', 'V2065A', 'V2061A', 'V2061A', 'V2143A', 'V2106A', 'V2165A', 'V2165A', 'V2180GA', 'V1986A', 'V2012A', 'V2012A', 'V2073A', 'V2073A', 'I2011', 'V2148A', 'I2018', 'V1919A', 'V2131A', 'V2220A', 'I2202', 'I2206', 'I2203', 'I2202', 'I2127', 'I2202', 'I2208', 'I2208', 'I2126', 'I2126', 'I2126', 'V2164KA', 'V2164KA', 'VIVO IV', 'VIVO IV', 'VIVO IV', 'VIVO IV', 'Vivo J5', 'vivo 1805', 'vivo 1805', 'vivo NEX', 'V1923A', 'vivo 1912', 'V1923A', 'vivo 1912', 'vivo 1913', 'V1924A', 'V1924A', 'vivo 1913', 'V1950A', 'V1950A', 'vivo NEX A', 'vivo NEX A', 'vivo 1813', 'V1821A', 'V1821A', 'vivo NEX S', 'vivo NEX S', 'Vivo ONE', 'Vivo ONE', 'PA2170', 'vivo PD1628F_EX', 'vivo PD1709', 'vivo PD1709F_EX', 'vivo PD1709F_EX', 'vivo PD1728', 'vivo PD1728', 'vivo PD1832F_EX', 'vivo PD2046F_EX', 'vivo PD2050F_EX', 'vivo PD2055F_EX', 'vivo PD2059F_EX', 'Vivo S', 'V1831A', 'V1831A', 'VIVO S1', 'Vivo S1 Prime', 'V1832A', 'V1832T', 'V2121A', 'V2121A', 'V2130A', 'V2130A', 'Vivo S11', 'Vivo S11 ', 'vivo S11t', 'vivo S11t', 'vivo S11t', 'vivo S11t', 'vivo S12', 'V2162A', 'Vivo S13', 'V2203A', 'V2207A', 'V2190A', 'V2244A', 'vivo S1Pro', 'Vivo S20 ', 'Vivo S21 ', 'Vivo S31', 'Vivo S4', 'Vivo S40', 'Vivo S41 /MMB439M', 'V1932A', 'vivo S6', 'V1962A', 'vivo S6T', 'V2020CA', 'V2020A', 'Vivo S76', 'V2031EA', 'vivo S7i(t)', 'vivo S7i(t)', 'vivo S7i(t)', 'V2080A', 'vivo S7t', 'vivo_S7t', 'vivo S7t', 'S7t 5G', 'vivo S7w', 'vivo S8', 'vivo S9', 'vivo S9', 'vivo S9', 'V2072A', 'V2048A', 'vivo S9t', 'V2168', 'V2168', 'V2153', 'V2153', 'V2150', 'V2151', 'V2151', 'V2151', 'V2143', 'vivo TD1602_EX', 'vivo U1', 'vivo 1916', 'vivo 1916', 'vivo 1921', 'V1941A', 'V1941A', 'V1928A', 'vivo V1', 'vivo V1', 'vivo V10', 'Vivo V10', 'VIVO V11', 'Vivo V11', 'vivo 1804', 'vivo 1804', 'vivo 1806', 'vivo 1806', 'vivo v11pro', 'vivo 1819', 'vivo 1818', 'vivo 1818', 'vivo 1920', 'vivo 1919', 'vivo 1907', 'vivo 1907', 'vivo 1907_19', 'vivo 1910', 'vivo 1909', 'vivo 1910', 'vivo 1933', 'vivo 1933', 'vivo V1907', 'vivo v19neo', 'vivo V1Max', 'vivo V1Max', 'vivo V2', 'V2040', 'vivo 2018', 'vivo 2018', 'V2022', 'Vivo V20A', 'Vivo V20G', 'V2066', 'V2108', 'V2050', 'V2050', 'V2050', 'V2061', 'V2055', 'Vivo V21S', 'V2130', 'V2132A', 'V2116', 'V2115', 'V2116', 'V2116', 'V2126', 'V2126', 'V2228', 'V2228', 'V2158', 'V2158', 'V2202', 'V2202', 'V2201', 'V2246', 'V2230', 'V2230', 'V2237', 'vivo V3', 'vivo V3', 'vivo V3Max A', 'vivo V3Max L', 'vivo v30', 'vivo v31', 'vivo V3L', 'vivo V3L', 'vivo V3L', 'vivo V3L', 'vivo V3M A', 'vivo V3M A', 'vivo V3MA', 'vivo_V3Max', 'vivo v45', 'vivo 1601', 'vivo V5', 'vivo 1609', 'vivo 1611', 'Vivo V51', 'Vivo V54', 'vivo 1612', 'vivo 1713', 'vivo V5S A', 'vivo 1718', 'vivo 1716', 'vivo Y79A', 'vivo Y79A', 'V2166BA', 'Vivo V8', 'vivo 1723', 'vivo V9 mini', 'vivo 1851', 'VIVO V9Pro', 'vivo 1851', 'vivo 1727', 'Vivo X', 'V2178A', 'V2229A', 'V2170A', 'V2170A', 'vivo Xplay3S', 'vivo Xplay3S', 'vivo Xplay3S', 'vivo Xplay5A', 'vivo Xplay5A', 'vivo Xplay5A', 'vivo Xplay5S', 'vivo Xplay5S', 'vivo Xplay6', 'vivo Xplay6L', 'vivo Xplay6', 'vivo Xplay6', 'vivo X710L', 'vivo X710L', 'vivo X710L', 'vivo X710L', 'vivo X1', 'vivo X1', 'vivo X1', 'vivo X1', 'Vivo X11', 'vivo X1S', 'vivo X1S', 'vivo X1S', 'vivo X1St', 'vivo X1St', 'vivo X1St', 'vivo X1St', 'vivo X1St', 'vivo X1W', 'vivo X1w', 'VIVO X2', 'VIVO X2', 'VIVO_X2', 'vivo X20', 'vivo X20A', 'vivo X20Plus A', 'vivo 1720', 'vivo X20Plus UD', 'vivo X20Plus UD', 'vivo X21', 'vivo X21A', 'vivo X21UD A', 'vivo X21i', 'vivo X21i A', 'vivo X21i', 'vivo X21i A ', 'V1814A', 'V1814T', 'V1814T', 'V1814A', 'V1809A', 'V1809A', 'V1816A', 'V1809T', 'V1816T', 'V1829A', 'V1838A', 'V1838T', 'V1829T', 'V1836A', 'V1836A', 'V1836T', 'vivo X27Pro', 'V1938CT', 'V1938T', 'V1938T', 'vivo X3F', 'vivo X3F', 'vivo X3F', 'vivo X3L', 'vivo X3L', 'vivo X3S', 'vivo X3S', 'vivo X3S', 'vivo X3S', 'vivo X3S', 'vivo X3S', 'vivo X3S W', 'vivo X3S W', 'vivo X3S W', 'vivo X3S W', 'vivo X3t', 'vivo X3t', 'vivo X3t', 'vivo X3t', 'vivo X3V', 'vivo X3V', 'vivo X3V', 'vivo X3V', 'Vivo X40', 'vivo X5L', 'vivo X5', 'vivo X5L', 'vivo X5Pro D', 'vivo X5Pro L', 'vivo X5Pro V', 'vivo X5Pro D', 'vivo X5Pro D', 'V2001A', 'V2001A', 'vivo 2004', 'vivo 2005', 'vivo 2005', 'V1937', 'vivo 1937', 'V1937', 'V1937', 'vivo 2006', 'vivo 2006', 'V2005A', 'V2011A', 'X50 Pro+', 'V1930', 'V1930', 'vivo X510t', 'vivo X510t', 'vivo X510t', 'vivo X510t', 'vivo X510t', 'vivo X520L', 'vivo X5F', 'vivo X5M', 'vivo X5M', 'vivo X5M', 'vivo X5Max ', 'vivo X5Max L', 'vivo X5Max L', 'vivo X5Max S', 'vivo X5Max V', 'vivo X5S L', 'vivo X5S L', 'vivo X5V', 'vivo X5V', 'vivo X5V', 'vivo X6D', 'vivo X6A', 'vivo X6Plus D', 'vivo X6Plus A', 'vivo X6Plus L', 'vivo X6Plus D', 'vivo X6Plus A', 'vivo X6Plus D', 'vivo X6Plus L', 'V2046A', 'V2059A', 'V2046A', 'V2045', 'V2046', 'V2047A', 'V2056A', 'V2085A', 'vivo X6S A', 'vivo X6S A', 'vivo X6S A', 'vivo X6S A', 'vivo X6SPlus D', 'vivo X6SPlus D', 'vivo X6SPlus D', 'vivo X6SPlus D', 'vivo X6SPlus A', 'vivo X7L', 'vivo X7Plus', 'vivo X7Plus', 'V2133A', 'V2104', 'V2104', 'V2105', 'V2134A', 'V2105', 'V2145A', 'V2114', 'V2145A', 'vivo X710F', 'vivo X710F', 'vivo X710F', 'vivo X710F', 'V2144', 'V2183A', 'V2144', 'V2208', 'V2185A', 'V2145', 'V2185A', 'Vivo X83', 'vivo X9', 'vivo X9L', 'vivo X9', 'vivo X9', 'vivo X9Plus', 'vivo X9Plus L', 'V2241A', 'V2242A', 'V2242A', 'V2227A', 'vivo X9i', 'vivo X9i', 'vivo X9i', 'vivo X9s', 'vivo X9s L', 'vivo X9s Plus', 'vivo X9s Plus', 'vivo X9s Plus L', 'vivo X9s Plus', 'VIVO XL', 'vivo Xplay', 'vivo Xshot', 'vivo Xshot', 'vivo Xshot', 'vivo Xshot', 'V2203', 'V2221', 'Vivo y1', 'Vivo Y1', 'V2168A', 'V2168A', 'vivo 1906', 'V2028', 'vivo Y11t', 'vivo Y11t', 'vivo Y11t', 'vivo 1904', 'V2163A', 'V2102', 'V2102', 'vivo 2007', 'vivo 2007', 'Vivo Y12I Pro', 'V2026', 'V2042', 'V2033', 'V2039', 'V2069', 'V2026_21', 'vivo Y13L', 'vivo Y13', 'vivo Y13L', 'vivo Y13L', 'vivo Y13i', 'vivo_Y13i', 'vivo Y13iL', 'vivo Y13iL', 'vivo Y13T', 'vivo Y13T', 'vivo 1901', 'vivo Y15T', 'vivo Y15T', 'V2134', 'V2147', 'V2147', 'V2212', 'V2120', 'V2204', 'V2214', 'V2204', 'vivo 1902', 'vivo 1902_19', 'VIVO 1902', 'vivo Y17T', 'vivo Y17T', 'vivo_Y17T', 'vivo Y17T', 'vivo Y17W', 'vivo Y17W', 'vivo Y17W', 'vivo Y18L', 'vivo Y18L', 'vivo Y18L', 'vivo 1915', 'vivo Y19t', 'vivo Y19t', 'vivo Y19t', 'vivo Y19t', 'Vivo Y1i', 'vivo 2015', 'vivo 2015', 'V2029', 'V2027', 'V2043_21', 'V2101', 'V2070', 'V2054', 'V2052', 'V2037', 'V2032', 'V2038', 'V2038', 'V2129', 'V2129', 'V2111', 'V2149', 'V2140', 'V2140', 'V2152', 'V2152', 'V2110', 'V2110', 'V2131', 'V2135', 'V2207', 'vivo Y22iL', 'vivo Y22iL', 'V2206', 'V2206', 'vivo Y23L', 'vivo Y23L', 'vivo y23l', 'vivo Y23L', 'vivo Y23L', 'vivo Y23L', 'vivo 1613', 'vivo Y27', 'vivo Y27L', 'vivo Y27', 'vivo Y28', 'vivo Y28', 'vivo Y28L', 'vivo Y28L', 'vivo Y29L', 'vivo Y29L', 'vivo Y29L', 'V1901A', 'V1901A', 'V1901A', 'V1901T', 'V1930A', 'vivo 1938', 'V2034A', 'V2036A', 'V2099A', 'V2099A', 'V2160', 'V2160', 'V2160', 'V2066BA', 'V2066A', 'Y30g', 'Vivo Y30S', 'vivo Y31L', 'V2068', 'V2054A', 'V2068A', 'V2068', 'V2158A', 'Vivo Y32', 'V2180A', 'V2057', 'V2109', 'V2166A', 'V2166A', 'V2146', 'V2205', 'V2205', 'vivo Y37A', 'vivo Y37', 'V2044', 'vivo Y3t', 'vivo Y3t', 'vivo Y3t', 'vivo y41', 'vivo Y5 ', 'Vivo Y5', 'vivo 1935', 'VIVO Y50(2021)', 'V2023EA', 'Y50t', 'V2035', 'vivo Y51L', 'vivo Y51A', 'V2030', 'vivo 1707', 'V2031_21', 'vivo Y51t L', 'vivo Y51t L', 'vivo Y51t L', 'V2053', 'V2057A', 'vivo Y53', 'vivo 1606A', 'vivo Y53n', 'V2058', 'V2123A', 'V2069A', 'V2045A', 'V2045A', 'vivo Y55A', 'V2127', 'V2127', 'vivo 1603', 'vivo Y55n', 'vivo 1610', 'V2164A', 'V2164A', 'V1934A', 'V2006', 'vivo Y613', 'vivo Y613', 'vivo Y613F', 'vivo Y622', 'vivo Y622', 'vivo Y622', 'vivo Y622', 'vivo Y622', 'vivo Y623', 'vivo Y623', 'vivo Y627', 'vivo Y627', 'vivo Y627', 'vivo Y627', 'vivo Y628', 'vivo Y628', 'vivo 1719', 'vivo Y66', 'vivo Y66L', 'vivo Y66i A', 'vivo Y67', 'vivo Y67A', 'vivo Y67L', 'vivo Y685', 'vivo 1714', 'vivo Y69A', 'V2002A', 'V2002A', 'vivo Y71A', 'vivo 1724', 'vivo Y71A', 'vivo 1801', 'V2041', 'V2060', 'V2102A', 'V1731CA', 'vivo Y73', 'Vivo Y73 /MMB239M', 'V2059', 'V2031A', 'V2164PA', 'V2117', 'vivo Y75A', 'V2142', 'V2142', 'vivo Y75s', 'vivo Y75s', 'vivo Y75S', 'vivo Y75s', 'V2124', 'V2156A', 'V2219A', 'V2219A', 'V2169', 'V2169', 'V1913A', 'vivo 1808i', 'vivo 1803', 'vivo 1803', 'vivo 1812', 'vivo Y81S', 'V1732A', 'V1732T', 'vivo Y83A', 'vivo 1802', 'vivo Y83A', 'vivo Y83A', 'vivo 1726', 'Vivo Y83I', 'vivo Y85A', 'vivo Y85', 'Vivo Y85i', 'Vivo Y86', 'V1730EA', 'vivo v1730ea', 'vivo 1908', 'vivo 1823', 'vivo 1908_19', 'vivo 1817', 'vivo 1811', 'vivo Y913', 'vivo Y913', 'vivo Y91C', 'vivo 1820', 'vivo 1816', 'vivo Y923', 'vivo Y923', 'vivo Y927', 'vivo Y927', 'vivo Y928', 'vivo Y928', 'vivo Y928', 'vivo 1814', 'V1818A', 'V1818A', 'vivo 1814', 'vivo Y937', 'vivo Y937', 'vivo Y937', 'V1818CT', 'V1818CA', 'vivo 1807', 'vivo Y95', 'V1813A', 'V1813T', 'V1813A', 'vivo Y97', 'V1945A', 'V1801A0', 'vivo Z1', 'vivo 1918', 'vivo 1951', 'vivo 1951', 'VIVO Z1Pro', 'vivo 1918', 'vivo 1918 Flow', 'Vivo Z10', 'vivo Z1i', 'V1730DA', 'V1730DT', 'vivo Z1i', 'vivo_1951', 'vivo 1917', 'V1813BA', 'V1813BT', 'V1813BT', 'Vivo Z34', 'vivo Z3x', 'V1730GA', 'vivo Z3x', 'vivo Z3x', 'V1921A', 'V1911A', 'V1911A', 'V1911A', 'V1990A', 'V1990A', 'V1963A', 'V1963A']
        vivo2 = ["vivo/iQOO 5 Pro", "vivo/iQOO 7", "vivo/iQOO Z5", "vivo/iQOO U3", "vivo/iQOO U1x", "vivo/iQOO Neo 3", "vivo/iQOO U1", "vivo/iQOO 8", "vivo/iQOO 9", "vivo/iQOO Z3", "vivo/iQOO Z6", "vivo/iQOO Z7", "vivo/iQOO U5", "vivo/iQOO U3x", "vivo/iQOO 6", "vivo/iQOO 10", "vivo/iQOO Z1", "vivo/iQOO 11", "vivo/iQOO Z2", "vivo/iQOO 12", "vivo/iQOO Z4", "vivo/iQOO 13", "vivo/iQOO Z8", "vivo/iQOO 14", "vivo/iQOO Z9", "vivo/iQOO 15", "vivo/iQOO Z10", "vivo/iQOO 16", "vivo/iQOO Z11", "vivo/iQOO 17", "vivo/iQOO Z12"]
        oneplus = ['NE2213', 'NE2217', 'NE2215', 'NE2210', 'NE2210', 'CPH2423', 'CPH2411', 'CPH2417', 'CPH2413', 'CPH2415', 'CPH2449', 'CPH2487', 'ONE A2003', 'ONE A2003', 'ONE A2001', 'ONE A2005', 'ONEPLUS A3003', 'ONEPLUS A3000', 'ONEPLUS A3010', 'ONEPLUS A5000', 'ONEPLUS A5000', 'ONEPLUS A5010', 'ONEPLUS A5010', 'ONEPLUS A5010', 'ONEPLUS A5010', 'ONEPLUS A5010', 'ONEPLUS A6003', 'ONEPLUS A6000', 'ONEPLUS A6010', 'ONEPLUS A6013', 'ONEPLUS A6010', 'GM1900', 'GM1901', 'GM1903', 'GM1917', 'GM1913', 'GM1911', 'GM1910', 'GM1915', 'GM1910', 'HD1901', 'HD1903', 'HD1900 Flow', 'HD1905', 'HD1900', 'HD1907', 'HD1911', 'HD1913', 'HD1910', 'GM1925', 'HD1925', 'GM1920', 'IN2013', 'IN2015', 'IN2010', 'IN2010', 'IN2017', 'IN2019', 'IN2023', 'IN2025', 'IN2020', 'OnePlus8Pro', 'KB2005', 'KB2001', 'KB2007', 'KB2003', 'KB2000', 'OnePlus 8T 5G', 'LE2115', 'LE2113', 'LE2111', 'LE2110', 'LE2120', 'LE2125', 'LE2123', 'LE2121', 'LE2127', 'OnePlus9Pro', 'LE2101', 'LE2100', 'MT2111', 'MT2110', 'ONEPLUS A19677', 'ONEPLUS A2345', 'Oneplus A31', 'Oneplus A3331', 'ONEPLUS A35904', 'ONEPLUS A37000', 'ONEPLUS A3EVB', 'ONEPLUS A62322', 'ONEPLUS A64794', 'ONEPLUS A65369', 'ONEPLUS A68333', 'ONEPLUS A70458', 'ONEPLUS A70791', 'ONEPLUS A78637', 'ONEPLUS A80828', 'ONEPLUS A83306', 'ONEPLUS A87046', 'ONEPLUS A90641', 'Oneplus A99831', 'PGKM10', 'PGKM10', 'PHK110', 'PHK110', 'PGP110', 'PGP110', 'PGZ110', 'ONEPLUS KB2023', 'OnePlus Nord', 'Oneplus Nord 2', 'DN2103', 'DN2101', 'CPH2399', 'CPH2401', 'AC2001', 'AC2003', 'IV2201', 'CPH2409', 'CPH2381', 'CPH2465', 'EB2103', 'EB2101', 'EB2101', 'BE2025', 'BE2026', 'BE2029', 'Nord N10 5G', 'BE2028', 'BE2013', 'BE2011', 'BE2012', 'CPH2459', 'GN2200', 'CPH2469', 'DE2118', 'DE2117', 'A0001', 'ONE E1001', 'ONE E1003', 'ONE E1001', 'ONE E1005']
        oppo = ["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"]
        oppo2 = ["OP4F97", "OP4BA5L1", "OP664D1", "OP5F11L1", "OP2A92", "OP8F17", "OP8F31", "OP4C9E1", "OP5B31", "OP4BA6L1", "OP2B87", "OP6F21", "OP6C8E1", "OP8F11", "OPPOA16", "OPPOA15", "OPPOA11", "OPPOA73", "OPPOA37", "OPPOA53", "OPPOA33", "OPPOA93", "OPPOA35", "OPPOA83", "OPPOA57", "OPPOA71", "OPPOA39", "OPPOA3", "OPPOA51", "OPPOA27", "OPPOA79"]
        poco = ['M2006C3MI', '211033MI', '22031116AI', '220333QPG', '220333QPG', 'POCO C40', 'POCO C40', 'POCO F2 Pro', 'POCO F2 Pro', 'M2012K11AG', 'M2104K10I', '22021211RG', '22021211RI', 'POCO F4', 'POCO F4', 'POCO F4', '21121210G', 'POCO F4 GT', 'POCO F4 GT', '23049PCD8G', '23013PC75G', 'M2004J19PI', 'POCO M2 Pro', 'POCO M2 Pro', 'M2010J19CI', 'M2010J19CG', 'POCO M3', 'POCO M3 Pro', 'POCO M3 Pro', 'M2103K19PG', 'POCO M3 Pro 5G', '22041219PG', '22041219PI', 'POCO M4 5G', '2201117PG', '21091116AG', 'POCO M4 Pro 5G', 'POCO M4 Pro 5G', 'POCO M4 Pro 5G', 'POCO M4 Pro 5G', '22071219CG', 'POCO M5', 'POCO M5', '22071219CI', '2207117BPG', 'POCO M5s', 'POCO X2', 'M2007J20CI', 'M2007J20CI', '21061110AG', 'M2007J20CG', 'M2102J20SG', 'M2102J20SI', '22041216G', 'POCO X4 GT', '22041216G', 'POCO X4 GT', 'POCO X4 GT', 'POCO X4 GT', '2201116PG', 'POCO X4 Pro 5G', '2201116PG', '2201116PI', '22111317PG', 'POCO X5 5G', 'POCO X5 5G', '22101320G', 'POCO X5 Pro 5G', 'POCO X5 Pro 5G', 'POCO X5 Pro 5G', '22101320G']
        dpi = str(random.choice(['320dpi','640dpi','213dpi','480dpi','420dpi','240dpi','280dpi','160dpi','560dpi','540dpi','272dpi','360dpi','720dpi','270dpi','450dpi','600dpi','279dpi','210dpi','180dpi','510dpi','300dpi','454dpi','314dpi','288dpi','401dpi','153dpi','267dpi','345dpi','493dpi','340dpi','604dpi','465dpi','680dpi','256dpi','290dpi','432dpi','273dpi','120dpi','200dpi','367dpi','419dpi','306dpi','303dpi','411dpi','195dpi','518dpi','230dpi','384dpi','315dpi','293dpi','274dpi','235dpi']))
        pxl = str(random.choice(['720x1280','1440x2560','1440x2768','1280x720','1280x800','1080x1920','540x960','1080x2076','1080x2094','1080x2220','480x800','768x1024','1440x2792','1200x1920','720x1384','1920x1080','720x1369','800x1280','720x1440','1080x2058','600x1024','720x1396','2792x1440','1920x1200','2560x1440','1536x2048','720x1382','1080x2113','1080x2198','1080x2131','720x1423','1080x2069','720x1481','1080x2047','1080x2110','1080x2181','1080x2209','1080x2180','1080x2020','1080x2095','1440x2723','1080x2175','720x1365','1440x2699','1080x2218','2699x1440','1440x2907','1080x2257','720x1370','1080x2042','720x1372','1080x2200','1080x2186','720x1361','1080x2024','1080x2006','720x1402','1440x2831','720x1454','1080x2064','1440x2933','720x1411','720x1450','1440x2730','1080x2046','2094x1080','540x888','1440x2759','1080x2274','1080x2178','1440x2706','720x1356','720x1466','1440x2900','2560x1600','1080x2038','1600x2452','1080x2129','720x1422','720x1381','1080x2183','1080x2285','800x1216','1080x2216','1080x2168','1080x2119','1080x2128','1080x2273','2274x1080','1080x2162','1080x2164','2076x1080','1024x768','1080x2173','1440x2845','1080x2134','720x1379','1440x2838','1080x2139','2131x1080','1440x2744','1080x2192','720x1406','1440x2960','1080x2029','2042x1080','1080x2212','1406x720','1080x2288','2047x1080','1080x2051','720x1398','1280x736','1382x720','720x1353','1080x2050','1080x2028','1080x2256','2711x1440','2175x1080','1080x2281','2560x1492','1440x2923','1200x1845','1080x2189','1080x2002','1440x2711','2110x1080','960x540','1080x2033','2200x1080','720x1452','720x1480','1440x2735','720x1472','1080x2277','1080x2169','2874x1440','1600x2560','1080x2151','2218x1080','1080x2182','720x1468','1440x2898','1080x2011','1080x2201','720x1380','1080x2287','2069x1080','1200x1836','2046x1080','720x1439','2058x1080','2182x1080','720x1399','1080x2282','1440x2721','1080x2324','720x1432','1080x2165','1080x2150','1080x2156','1080x1872','1440x3048','1532x2560','720x1355','720x1390','720x1476','720x1410','1080x2032','720x1437','1440x2682','1440x2921','1080x2270','1080x2160','720x1446','1200x1848','1440x2874','1080x2309','1080x2174','1440x2867','1080x2060','1080x2196','1080x2401','1536x1922','1080x2280','1080x2123','720x1435','1440x2927','1080x2276','720x1448','720x1469','720x1344','1080x2187','540x937','1440x3028','1080x2184','1440x2718','1080x2326','840x1834','1440x2935','1440x2880','1440x2892','2048x2048','1080x2195','1080x2322','720x1419','987x1450','1080x2092','1440x3047','720x1358','1080x2136','720x1357','1080x2093','720x1477','1080x2312','1080x2361','720x1341','720x1507','1080x2172','720x1337','1080x2177','1080x2125','1440x2891','1600x2434','720x1394','1080x2159','720x1387','1080x2166','1080x2154','1080x2147','1440x2747','1080x2105','1440x2911','720x1473','1080x2055','1080x2265','720x1436','1080x2190','1600x2526','720x1373','720x1415','1080x2249','1080x2254','720x1455','1440x3040','1080x2149','720x1385','1440x3036','1080x2111','1440x2904','720x1442','720x1377','1080x2307','1080x2327','1080x2141','1080x2025','720x1430','720x1375','1080x2283','1440x2779','1080x2321','1080x2268','1440x2758','1752x2698','1080x2267','1200x1856','1440x2756','720x1464','1080x2234','1080x2171','1080x2155','720x1463','1080x2122','720x1467','1080x2264','720x1349','1440x2999','720x1458','1080x2015','720x1431','1242x2208','1080x2185','1080x2148','1080x2163','1440x2780','720x1445','1080x2146','1200x1916','720x1502','1200x1928','720x1506','720x1424','720x1465','720x1420','1080x2176','720x1521','1080x2315','1080x2400','720x1471','1080x2157','1600x2458','1080x2067','1080x2191','1080x2271','720x1407','800x1208','1080x2087','1080x2199','578x1028','720x1485','540x879','1080x2179','720x1555','810x1598','720x1378','1200x1897','720x1395','720x1459','900x1600','1080x2275','1440x2733']))
        mt_qcom = str(random.choice(["qcom","mt6769", "qcom", "mt6768", "qcom","mt6767", "qcom","mt6765", "qcom","mt6763", "qcom","mt6757", "qcom","mt6755", "qcom","mt6753", "qcom","mt6739", "qcom","mt6737", "qcom","mt6735", "qcom","mt6595", "qcom","mt6582", "qcom","mt6572", "mt6571", "qcom","mt6570", "qcom","mt8563", "qcom","mt8167", "qcom","mt8163", "mt8135", "qcom","mt8127", "qcom","mt8125", "qcom","mt7623", "qcom","mt6797", "qcom","mt6592", "qcom","mt6590", "qcom","mt6580", "qcom","mt6573", "qcom","mt6575", "qcom","mt6260", "qcom","mt6236"]))
        device_android = str(random.choice(["27/9","27/10","27/11","27/12","27/12","27/13","28/9","28/10","28/11","28/12","28/12","28/13","29/9","29/10","29/11","29/12","29/12","29/13","27/9","30/10","30/11","30/12","30/12","30/13","31/9","31/10","31/11","31/12","31/12","31/13","32/9","32/10","32/11","32/12","32/12","32/13","33/9","33/10","33/11","33/12","33/12","33/13"]))
        kode = str(random.choice(['145652090','206670917','185203686','192992561','183982986','206670927','150338061','183982962','127049016','175574603','155374054','205858247','135374896','206670920','169474958','206670926','160497905','161478672','192992578','206670929','131223243','206670916','142841919','187682681','171727795','151414277','206670922','160497915','207505137','165030898','208061741','208061688','208180365','208061674','197825052','147375133','208061744','196643798','208061725','122338247','157536430','208061728','209143963','208727155','209143726','205280539','209143903','209143970','181496409','208061739','209143957','210180522','210180512','209143881','209143712','180322805','210180521','195435561','210370119','210180523','210180493','175574596','210180510','210180480','210180513','210180517','176649504','177770663','210180479','211114117','210908379','206670921','211114134','183982943','211399345','211399342','211399332','201775962','211574187','211574249','210180519','167338559','185203649','124583960','211399337','211399335','197825163','166149717','211399336','212063371','211399329','209143954','210180482','168361634','212214017','209143867','211399341','211399340','212214027','195435510','122338243','139237670','152367502','212676872','212676898','212676875','212676895','212676901','209823384','212676869','196643822','212676878','213367980','213368005','212676886','213558743','209143913','212214039','158441917','174081672','213558750','201775966','188791681','185203705','143631575','161478664','214245350','161478663','212676881','213558770','214245346','138226752','214245221','214245182','214245206','214245218','214245354','214245295','214245199','214245304','214245280','214446313','214245187','214245288','214139002','202766605','214245319','214646783','158441914','215246048','195435544','208061677','215464400','128676146','215464389','215464385','215464390','215464398','182747397','215464393','216233197','201775791','216817344','215464395','216817286','185203642','164094529','216817305','215464401','162439029','215464382','216817280','216817331','214330969','216817299','216817357','217948981','217948980','217948956','217948959','217948968','216817296','217948952','217948982','216817269','219308759','219308726','182747387','219308721','219308754','219308763','176649435','183982982','219909486','127049038','219308730','221134012','221134032','221134009','221134037','194383426','221134029','221134005','221134018','145652093','225283632','165031108','225283625','224652582','139906580','225283628','225283624','226142579','225283634','225283631','226493211','225283623','185203672','156514151','218793478','225283621','227299063','225283627','227299064','227299021','227299027','227544546','227299041','227299060','227299012','228970707','228970705','227299005','228970687','228970683','228970694','228970710','228970689','160497904','195435540','129611419','229783842','230291708','228970681','148324047','230877709','231192211','230877674','230877705','230877678','211399328','209143896','230877713','194383428','230877689','221134002','231457747','208061721','230877671','230877668','232868027','232088496','185203706','232868005','232867964','232868001','232868015','232868031','232867959','232868009','164094526','232867941','234041364','182747399','232868024','232867949','234847239','234847238','234847234','162439040','234847229','234847230','181496427','234847240','232867993','195435558','232867967','232867997','234847227','235871830','221133998','236572344','236572377','153386780','236572337','236572349','236572372','234847226','236572383','237507050','238093993','238093948','238093954','238093999','238093982','239490565','239490555','238093946','238093966','239490563','239490550','239974660','240726416','239490568','240726484','240726452','239490551','239490548','240726426','240726476','240726491','240726471','241043882','241114613','236572331','241267273','240726407','241456456','241267278','241267269','241114619','241456445','241456451','242168941','242168928','242168931','242168939','242168925','240726436','242375239','144722090','242168935','242290370','157405369','242168933','242290355','242703240','242807362','242168923','242168943','242991209','243646252','243646269','242991200','243711120','243646267','243711093','243975802','243646263','243646248','243646255','244167578','128676156','194383413','243975835','244390417','244390338','245196084','245196061','240726392','245196055','243646273','245196082','245196063','245196070','245666450','245466705','245870319','245870301','245870347','245196087','246889064','246889072','246889073','246889074','246889065','247146500','246889063','245870262','247370962','247146481','246889068','246889062','247541884','247541831','247370955','247370942','247720736','247720751','248310216','248310220','248310208','247720744','248399342','248310210','247720747','248310206','248717751','248310212','248310221','248823392','248583561','248310205','248899028','248955251','248955247','249178904','248955244','249507608','249507582','249507588','249507585','248955240','249507607','249507592','249810008','249966137','249507610','249966081','249966100','249507599','249966140','249810004','123790722','250188776','249628096','250188788','250742103','250742113','250742102','250877984','250742105','250742111','251048681','250742107','250742115','251048695','251304696','251304682','251524431','251530710','251304689','251524420','251524409','251524390','250742101','251048673','252055918','252055945','251920416','252055944','252055925','252239038','252055936','252055915','252055948','252390568','252390583','252580134','252740497','252740485','252740490','253120615','253325372','253325384','253325385','253447816','253146263','253120607','253325374','253120598','253325371','253447808','253447809','253325378','253447814','253447807','253447811','253447817','253447813','181496411','253447806','255191971','255013798','255777478','255777471','255777474','255777472','255959637','255777477','255959614','255959635','256099199','256099204','150338064','256099153','256099205','256099156','255983744','256107300','255777470','126223536','256203326','256099190','256099151','256324061','256324047','256203339','256966628','256966589','256966626','256966590','124584015','257456576','256966593','257456590','256966629','256966587','256966592','257456586','257456539','259829115','259829104','259829113','260037038','259829105','259829109','260037030','260149625','259829103','260149621','260465044','259829116','260724710','179155058','261079769','261079761','261079768','261079762','261079771','261276939','157405370','135374885','261079765','261393056','261393062','261079760','181496406','182747360','261504698','261690888','261504706','169474957','262218766','262290715','262290774','262372432','262372425','262372431','262886993','262886995','262372426','262886987','261079764','262886986','262886988','262886990','262372433','262886996','263652962','264009049','264009019','264009030','264009021','264009023','264009052','264009024','261763534','174081651','169474965','232867942','264009013','255959606','264009028','267397344','267397322','267925737','267397343','267925708','267397327','267397321','267925714','267258517','267925705','268773287','267925733','268773233','267925702','268773286','159526770','268773239','268773272','269790795','269285030','269790805','269790803','269790792','268773227','269849047','270426177','270426174','271182277','269790789','271182270','268773290','271182266','271182276','269790798','271182279','271182265','271182267','269790807','271823819','272382110','272382111','272382106','272693584','272382095','272382093','272382098','272382100','272382103','273728833','273371577','273728832','273728798','273907093','273907111','273907108','238093987','273907112','273907103','274774869','274774891','274774908','273907087','274774904','274774875','274774914','275292626','276027938','276028040','276027963','276028037','276028020','276028017','274774862','276028013','249507580','276028029','273907098','277249238','277249248','277249249','276028033','277249250','277249226','275292623','277249214','277249242','277249237','277249240','278625447','278002558','278625420','278625431','278625423','117539687','278625416','278625444','277249213','278625451','279469964','279996068','279996060','279996067','279996058','280194220','279996065','279996063','279996061','279996059','280894196','273728787','271182262','281579032','281579023','276514494','281579021','281579027','281579033','268773274','283072590','281579025','283072571','282619332','283489774','283072587','283072567','281579031','283072580','283072574','284459213','284459224','179155089','256966583','284459214','283072585','284459218','284459223','284459225','285338607','275113919','284459221','284459212','284459215','285855793','285855800','285855803','285855791','285855802','285855804','285855795','286809973','287420974','287421023','287420968','287420979','287421017','287421005','287421019','287421012','277249241','288682406','287421026','288682405','288682397','288682407','261079772','288682398','288682401','288205409','289692198','287420997','289692186']))
        kode2 = (f'{random.randint(211111111,399999999)}')
        locale = str(random.choice((["id_ID","en_GB", "en_US", "ar_LY", "fr_FR", "es_ES", "de_DE", "it_IT", "pt_BR", "tr_TR","ru_RU","in_ID"])))
        versi_facebook = random.choice(("70.0.0.15.98, 80.0.0.20.101,60.0.0.10.76, 85.0.0.25.100,75.0.0.22.99,72.0.0.18.94, 68.0.0.16.84,78.0.0.14.97, 63.0.0.20.81,81.0.0.24.105,73.0.0.16.96,67.0.0.18.88,84.0.0.21.110,74.0.0.18.100,71.0.0.15.92,79.0.0.14.103,62.0.0.18.80,87.0.0.22.115,76.0.0.20.102,83.0.0.18.10,66.0.0.16.87,88.0.0.24.118,77.0.0.22.103,64.0.0.18.82,82.0.0.20.107,69.0.0.14.92,89.0.0.20.123,61.0.0.14.76,86.0.0.18.112,65.0.0.12.86").split(","))
        #versi_facebook = (f'{random.randint(299,399)}.{random.randint(1,10)}.0.{random.randint(20,35)}.{random.randint(90,120)}')
        asus = ['ASUS_A002','ASUS_A002A','ASUS_A002_1','ASUS_A002_2','ASUS_AI2201','ASUS_AI2201_B','QTI SM8475','ASUS_I001_1','ASUS_I001D','ASUS_I002D','ASUS_I003_1','ASUS_I003D','ASUS_I004D','ASUS_I005_1','ASUS_I005D','ASUS_I006D','ASUS_I006D','ASUS_I007_1','ASUS_I007D','ASUS_I01WD','ASUS_Z01QD_1','ASUS_Z01QD']
        iphn = random.choice(["11,8", "12,1", "9,2", "13,3", "10,5", "12,8", "10,4", "13,1", "9,1", "11,2"])
        ios = random.choice(["iOS 14_4_1", "iOS 15_0", "iOS 12_1_3", "iOS 15_0_1", "iOS 14_7_1", "iOS 14_6", "iOS 13_5", "iOS 14_0_1", "iOS 11_2_6", "iOS 15_1"])
        scale = random.choice(["2.00", "3.00", "2.61", "2.00", "2.61", "2.00", "3.00", "2.00", "2.61", "3.00"])
        gamut = random.choice(["display", "P3", "display", "wide", "P3", "display", "wide"])
        return(random.choice([
              f'Barcelona {versi_facebook} Android ({device_android}; {dpi}; {pxl}; ASUS MOBILITY LIMITED/asus; {str(random.choice(asus))}; {str(random.choice(asus))}; qcom; in_ID; {kode2})',
              f'Barcelona {versi_facebook} Android ({device_android}; {dpi}; {pxl}; OPPO MOBILITY LIMITED/oppo; {str(random.choice(oppo2))}; {str(random.choice(oppo))}; qcom; in_ID; {kode2})',
              f'Barcelona {versi_facebook} Android ({device_android}; {dpi}; {pxl}; MICROMAX MOBILITY LIMITED/micromax; {str(random.choice(micromax))}; {str(random.choice(micromax))}; qcom; in_ID; {kode2})',
              f'Barcelona {versi_facebook} Android ({device_android}; {dpi}; {pxl}; ONEPLUS MOBILITY LIMITED/oneplus; {str(random.choice(oneplus))}; {str(random.choice(oneplus))}; qcom; in_ID; {kode2})',
              f'Barcelona {versi_facebook} Android ({device_android}; {dpi}; {pxl}; VIVO MOBILITY LIMITED/vivo; {str(random.choice(vivo2))}; {str(random.choice(vivo))}; qcom; in_ID; {kode2})',
              f'Barcelona {versi_facebook} Android ({device_android}; {dpi}; {pxl}; POCO MOBILITY LIMITED/poco; {str(random.choice(poco))}; {str(random.choice(poco))}; qcom; in_ID; {kode2})',
              f"Barcelona {versi_facebook} (iPhone{iphn}; {ios}; in_ID; in_ID; scale={scale}; gamut={gamut}; {pxl}; {kode2})"  
       ]))
def useragent_facebook():
        chrome = (f'{random.choice(["108","128"])}.0.{random.randrange(5111,6999)}.{random.randrange(60, 299)}')
        angka = random.choice(['01','02','03','04','05','06','07','08','09','10'])
        ubuntu = random.choice(['Ubuntu ','Ubuntu/','Ubuntu; ','Ubuntu-'])
        linucx = random.choice(['GoogleApp','YandexSearch','LinuxApp'])
        arm = str(random.randint(32,64))
        windows = random.choice(['WOW64','Win32'])
        tahun = random.choice(['2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023','2024'])
        return(random.choice([
            f'Mozilla/5.0 (X11; {ubuntu}{random.randrange(10,22)}.{angka}; Linux {random.choice(["x86_64","i686"])}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Safari/537.36 {linucx}/{str(random.randint(10,20))}.{str(random.randint(20,40))}.{str(random.randint(20,70))}.{str(random.randint(20,29))}.arm{arm}',
            f'Mozilla/5.0 (Linux; {ubuntu}{random.randrange(10,22)}.{angka}; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Safari/537.36 {linucx}/{str(random.randint(10,20))}.{str(random.randint(20,40))}.{str(random.randint(20,70))}.{str(random.randint(20,29))}.arm{arm}',
            f'Mozilla/5.0 (Compatible; {ubuntu}{random.randrange(10,22)}.{angka}; Windows NT 10.0; {windows}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Safari/537.36 {linucx}/{str(random.randint(10,20))}.{str(random.randint(20,40))}.{str(random.randint(20,70))}.{str(random.randint(20,29))}.arm{arm}',
            f'Mozilla/5.0 (Linux; {ubuntu}{random.randrange(10,22)}.{angka}; Android {random.randint(9,14)}; moto g stylus 5G ({tahun})) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Safari/537.36 {linucx}/{str(random.randint(10,20))}.{str(random.randint(20,40))}.{str(random.randint(20,70))}.{str(random.randint(20,29))}.arm{arm}'
        ]))

def extractor(data):
    try:
        soup = BeautifulSoup(data,"html.parser")
        data = {}
        for inputs in soup.find_all("input"):
            name = inputs.get("name")
            value = inputs.get("value")
            if name:
                data[name] = value
        return data
    except Exception as e:
        return {"error":str(e)}

def dn():
    time.sleep(random.randint(3,7))
    
def dnn():
    time.sleep(random.randint(10,20))

def GetEmail():
    response = requests.post('https://api.internal.temp-mail.io/api/v3/email/new').json()
    return response['email']

def GetPhone():
    na = random.choice(['77', '78', '59'])
    ni = str(random.randrange(1000, 10000))
    nu = str(random.randrange(10000, 100000))
    nope = '+639%s%s%s' % (na, ni, nu)
    return nope

def GetEmails():
    nam1 = random.choice(['eka','dwi','tri','budi','indah','dewi'])
    nam2 = random.choice(['nurhayati','handoko','setiyani','susanto','permata'])
    nam3 = random.choice(['triatmaja','siagian','manopo','jayaningrat','widodo'])
    name = f'{nam1}{nam2}{nam3}'
    domain = random.choice(['gmail.com','yahoo.com','hotmail.com','gonetor.com'])
    nu = str(random.randrange(10000, 100000))
    nope = f'{name}@{domain}'
    return nope

def GetCode(email2):
    try:
        response = requests.get(f'https://api.internal.temp-mail.io/api/v3/email/{email}/messages').text
        code = re.search(r'FB-(\d+)', response).group(1)
        return code
    except:
        return None

def get_temp_plus():
	name = " ".join(fake_name()).replace(' ', '')
	jam = str(datetime.now().strftime("%X")).replace(':','')
	domain = random.choice(['fexbox.org','fexpost.com','fextemp.com','chitthi.in'])
	email = f'{name}.{jam}.{str(random.randrange(1000,10000))}@{domain}'
	return email

def get_code_temp_plus(email):
	mail = requests.Session()
	headers = {
			'User-Agent':'Temp%20Plus/30 CFNetwork/1220.1 Darwin/20.3.0',
			'Content-Type':'application/json',
			'Connection-type': 'wifi'
		}
	headers.update({'cookie': f'email={email}'})
	response = mail.get(f'https://tempmail.plus/api/mails', headers=headers)
	print(response.json())
	if response.status_code == 200:
		req = response.json()
		mail_list = req.get("mail_list", [])
		if mail_list:
			subject = mail_list[0].get('subject', '')
			kode = re.search(r'(\d+)', subject)
			code = kode.group(1) if kode else 'Code not found'
			return code
		else:
			return 'not found'
	return None

cps=[]
oks=[]
uid=[]
tokenku=[]

def progres(current,num_accounts,delay):
		for sleep in range(int(delay), 0, -1):
			sys.stdout.write('\033[1;37m[\033[1;35mBRYX-CREATE\033[1;37m] [\033[1;36m%s\033[1;37m|\033[1;31m%s\033[1;37m] \033[1;32mALIVE\033[0m||\033[1;31mDEAD \033[1;32m%s\033[0m||\033[1;31m%s\033[1;37m\r\r'%(current,num_accounts,len(oks),len(cps)));sys.stdout.flush()
			time.sleep(1)
			if current == num_accounts:
				break

def createfb() -> None:
    clear_screen()
    bryxpogii()
    global web_email,oks,cps,passw,num_accounts,delay
    folder_path = "/sdcard/boostphere"
    num_accounts = int(input("     \033[1;37mHow many acc: "))
    delay = int(input("     \033[1;37mDelay time between requests: "))
    clear_screen()
    bryxpogii()
    print(f"""     {blue}CHOOSE TYPE OF AUTO CREATE EMAIL ADDRESS:
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m
     {yellow}[01] {blue}TEMPMAIL.PLUS
     {yellow}[02] {blue}TEMP-MAIL.IO
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m""")
    web_email = input(f"    {green}Enter your choice: ").strip()
    if web_email == '1':
    	email2 = get_temp_plus()
    	valid = get_code_temp_plus(email2)
    if web_email == '2':
    	email2 = GetEmail()
    	valid = GetCode(email2)
    clear_screen()
    bryxpogii()
    print(f"""     {blue}CHOOSE TYPE OF AUTO CREATE PASSWORD:
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m
     {yellow}[01] {blue}DEFAULT PASSWORD
     {yellow}[02] {blue}CUSTOM PASSWORD
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m""")
    bryxemail = input(f"    {green}Enter your choice: ").strip()
    if bryxemail == '1':
    	passw=fake_password()
    if bryxemail == '2':
    	passw=input(f'     \033[1;37mEnter custom password: ')
    for make in range(int(num_accounts)):
        progres(make+1,num_accounts,delay)
        ses = requests.Session()
        response = ses.get(
            url='https://x.facebook.com/reg',
            params={"_rdc":"1","_rdr":"","wtsid":"rdr_0t3qOXoIHbMS6isLw","refsrc":"deprecated"},
        )
        mts = ses.get("https://x.facebook.com").text
        m_ts = re.search(r'name="m_ts" value="(.*?)"',str(mts)).group(1)
        formula = extractor(response.text)
        phone2 = GetPhone()
        email3 = GetEmails()
        firstname,lastname = fake_name()
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        print()
        print("ACCESSING FACEBOOK")
        dn()
        print("REGISTERING ACCOUNT")
        dn()
        print("FILLING UP CREDENTIALS")
        dn()
        print("CHECKING ACCOUNT LIVE OR NOT")
        dn()
        print("GETTING MAIL & GETTING PHONE")
        dn()
        print(f"DUMMYPHONE ─────> {phone2}")
        dn()
        print(f"DUMMYEMAIL ─────> {email3}")
        dn()
        print(f"NAME ─────> {firstname} {lastname}")
        dn()
        print(f"EMAIL ─────> {email2}")
        dn()
        print(f"FILLING CREDENTIALS \033[1;32mDONE")
        dn()
        payload = {
            'ccp': "2",
            'reg_instance': str(formula["reg_instance"]),
            'submission_request': "true",
            'helper': "",
            'reg_impression_id': str(formula["reg_impression_id"]),
            'ns': "1",
            'zero_header_af_client': "",
            'app_id': "103",
            'logger_id': str(formula["logger_id"]),
            'field_names[0]': "firstname",
            'firstname': firstname,
            'lastname': lastname,
            'field_names[1]': "birthday_wrapper",
            'birthday_day': str(random.randint(1,28)),
            'birthday_month': str(random.randint(1,12)),
            'birthday_year': str(random.randint(1992,2009)),
            'age_step_input': "",
            'did_use_age': "false",
            'field_names[2]': "reg_email__",
            'reg_email__': email3,
            'reg_email__': email2,
            'reg_number__': phone2,
            'field_names[3]': "sex",
            'sex': "2",
            'preferred_pronoun': "",
            'custom_gender': "",
            'field_names[4]': "reg_passwd__",
            'name_suggest_elig': "false",
            'was_shown_name_suggestions': "false",
            'did_use_suggested_name': "false",
            'use_custom_gender': "false",
            'guid': "",
            'pre_form_step': "",
            'encpass': '#PWD_BROWSER:0:{}:{}'.format(str(time.time()).split('.')[0],"Rayhan143"),
            'submit': "Sign Up",
            'fb_dtsg': "NAcMC2x5X2VrJ7jhipS0eIpYv1zLRrDsb5y2wzau2bw3ipw88fbS_9A:0:0",
            'jazoest': str(formula["jazoest"]),
            'lsd': str(formula["lsd"]),
            '__dyn': "1ZaaAG1mxu1oz-l0BBBzEnxG6U4a2i5U4e0C8dEc8uwcC4o2fwcW4o3Bw4Ewk9E4W0pKq0FE6S0x81vohw5Owk8aE36wqEd8dE2YwbK0iC1qw8W0k-0jG3qaw4kwbS1Lw9C0le0ue0QU",
            '__csr': "",
            '__req': "p",
            '__fmt': "1",
            '__a': "AYkiA9jnQluJEy73F8jWiQ3NTzmH7L6RFbnJ_SMT_duZcpo2yLDpuVXfU2doLhZ-H1lSX6ucxsegViw9lLO6uRx31-SpnBlUEDawD_8U7AY4kQ",
            '__user': "0"
        }
        header1 = {
            "Host":"m.facebook.com",
            "Connection":"keep-alive",
            "Upgrade-Insecure-Requests":"1",
            "User-Agent":ugenX(),
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "dnt":"1",
            "X-Requested-With":"mark.via.gp",
            "Sec-Fetch-Site":"none",
            "Sec-Fetch-Mode":"navigate",
            "Sec-Fetch-User":"?1",
            "Sec-Fetch-Dest":"document",
            "dpr":"1.75",
            "viewport-width":"980",
            "sec-ch-ua":"\"Android WebView\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
            "sec-ch-ua-mobile":"?1",
            "sec-ch-ua-platform":"\"Android\"",
            "sec-ch-ua-platform-version":"\"\"",
            "sec-ch-ua-model":"\"\"",
            "sec-ch-ua-full-version-list":"",
            "sec-ch-prefers-color-scheme":"dark",
            "Accept-Encoding":"gzip, deflate, br, zstd",
            "Accept-Language":"en-GB,en-US;q=0.9,en;q=0.8"
        }
        reg_url = "https://www.facebook.com/reg/submit/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzM0NDE0OTk2LCJjYWxsc2l0ZV9pZCI6OTA3OTI0NDAyOTQ4MDU4fQ%3D%3D&multi_step_form=1&skip_suma=0&shouldForceMTouch=1"
        py_submit = ses.post(reg_url, data=payload, headers=header1)
        #print(ses.cookies.get_dict().items())
        if "c_user" in py_submit.cookies:
            first_cok = ses.cookies.get_dict()
            uid = str(first_cok["c_user"])
            header2 = {
                'authority': 'm.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'cache-control': 'max-age=0',
                'dpr': '2',
                'referer': 'https://m.facebook.com/login/save-device/',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="125", "Google Chrome";v="125"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': ugenX(),
                'viewport-width': '980',      
            }
            params = {
                'next': 'https://m.facebook.com/?deoia=1',
                'soft': 'hjk',
            }
            con_sub = ses.get('https://x.facebook.com/confirmemail.php', params=params, headers=header2).text
            if valid:
                print(f"OTP SENT TO MAIL")
                dn()
                print(f"OTP RECEIVED : FB-{valid}")
                dn()
                confirm_id(email2,uid,valid,con_sub,ses)
            else:
                cps.append(uid)
        else:
            cps.append(uid)

def confirm_id(mail,uid,otp,data,ses):
    try:
        url = "https://m.facebook.com/confirmation_cliff/"
        params = {
        'contact': mail,
        'type': "submit",
        'is_soft_cliff': "false",
        'medium': "email",
        'code': otp}
        payload = {
        'fb_dtsg': 'NAcMC2x5X2VrJ7jhipS0eIpYv1zLRrDsb5y2wzau2bw3ipw88fbS_9A:0:0',
        'jazoest': re.search(r'"\d+"', data).group().strip('"'),
        'lsd': re.search(r'"LSD",\[\],{"token":"([^"]+)"}',str(data)).group(1),
        '__dyn': "",
        '__csr': "",
        '__req': "4",
        '__fmt': "1",
        '__a': "",
        '__user': uid}
        headers = {
        'User-Agent': ugenX(),
        'Accept-Encoding': "gzip, deflate, br, zstd",
        'sec-ch-ua-full-version-list': "",
        'sec-ch-ua-platform': "\"Android\"",
        'sec-ch-ua': "\"Android WebView\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        'sec-ch-ua-model': "\"\"",
        'sec-ch-ua-mobile': "?1",
        'x-asbd-id': "129477",
        'x-fb-lsd': "KnpjLz-YdSXR3zBqds98cK",
        'sec-ch-prefers-color-scheme': "light",
        'sec-ch-ua-platform-version': "\"\"",
        'origin': "https://m.facebook.com",
        'x-requested-with': "mark.via.gp",
        'sec-fetch-site': "same-origin",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://m.facebook.com/confirmemail.php?next=https%3A%2F%2Fm.facebook.com%2F%3Fdeoia%3D1&soft=hjk",
        'accept-language': "en-GB,en-US;q=0.9,en;q=0.8",
        'priority': "u=1, i"}
        response = ses.post(url, params=params, data=payload, headers=headers)
        if "checkpoint" in str(response.url):
            cps.append(uid)
        else:
            cookie = (";").join([ "%s=%s" % (key,value) for key,value in ses.cookies.get_dict().items()])
            rich_print(Panel(f"[bold green1] DATE & TIME : [bold green1]{tanggal} {waktu}\n[bold green1] UID         : {uid}\n[bold green1] PASSWORD    : {passw}\n[bold green1] COOKIE      : [bold green1]{cookie}\n[bold green1] USERAGENT   : [bold green1]{useragent_facebook()}",subtitle="[bold yellow] CREATE ",style="bold blue"))
            dn()
            open("/sdcard/boostphere/auto_create_ok.txt","a").write(uid+f"|{passw}|"+cookie+"\n")
    except Exception as e:
        pass

import requests, re, time, urllib.parse, json, os
ses = requests.Session()
capacity = []

class Pinterest:
	def __init__(self):
		self.capacity = []
		clear_screen()
		bryxpogii()
		self.now = str(time.time()).replace('.','')[:-4]
		self.contain = capacity;self.number = 0
		self.search = urllib.parse.quote(input(f"Enter the keywords you are looking for\n\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m\ninput : "));print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
		self.scrol = int(input(f"How many times do you want to scroll down?\n\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m\nNote the less the more accurate\ninput : "));print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
		print(f"Dump started press ctrl+c to stop dump");print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
		self.awal = ses.get('https://id.pinterest.com/resource/UserExperienceResource/get/?source_url=/search/pins/?rs=typed&q='+self.search+'&data={"options":{"placement_ids":[29],"extra_context":{"search_query":"'+urllib.parse.unquote(self.search)+'"}},"context":{}}&_='+self.now).text
		self.head = {"User-Agent": "Mozilla/5.0 (Linux; Android 11; 220333QAG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36", "X-APP-VERSION": "ba6e535", "X-Pinterest-AppState": "active", "X-Pinterest-PWS-Handler": "www/search/[scope].js", "X-Pinterest-Source-Url": "/search/pins/?rs=typed&q="+self.search, "X-Requested-With": "XMLHttpRequest", "Accept":"application/json, text/javascript, */*, q=0.01"}
		try: self.get_source()
		except KeyboardInterrupt: Pinterest().simpan_foto()
		self.simpan_foto()
	
	def simpan_foto(self):
		print("\r"); print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
		if input(f"\rHas been collected in total {len(self.capacity)} photo link\nWant to save as image [Y/N]\nchoose : ") in ["n","N","NO","No","no"]:
			isi = '\n'.join(_ for _ in tampung)
			open(f"/sdcard/boostphere/{urllib.parse.unquote(self.search)}{str(time.time()).replace('.','')[:-4]}.txt","a+").write(isi)
			exit(f"Link saved in internal folder boostphere")
		else:print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
		file = input("Please enter a name for the file\nJust name example 'FotoAbg'\nName  : ");print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
		for foto in self.contain:
			try:
				open(f"/sdcard/boostphere/{file}{str(time.time()).replace('.','')[:-4]}.jpg","wb").write(urllib.request.urlopen(foto).read())
				self.number += 1
				print("\r SUCCESSFUL SAVE {} FROM {} PHOTOS".format(self.number, len(self.contain)), end="", flush=True)
			except: pass	
		
	def get_source(self):
		try:
			link = ses.get('https://id.pinterest.com/resource/BaseSearchResource/get/?source_url=/search/pins/?rs=typed&q='+self.cari+'&data={"options":{"article":"","appliedProductFilters":"---","price_max":null,"price_min":null,"query":"'+urllib.parse.unquote(self.cari)+'","scope":"pins","auto_correction_disabled":"","top_pin_id":"","filters":""},"context":{}}&_='+self.now, headers=self.head).text
			for pin in re.findall(r'"id":"(\d+)"', link):
				if len(pin)==18: self.get_source_pin(pin)
			self.get_source_url(link)
		except Exception as e: pass
	
	def get_source_url(self, link):
		for rozh_bas in range(self.scrol):
			try:
				for pin in re.findall(r'"id":"(\d+)"', link):
					if len(pin)==18: self.get_source_pin(pin)
				for url in re.findall('"url":"(.*?)"', str(link)):
					if "com/736" in str(url):
						if url in self.tampung: pass
						else: print("Link :",url); self.tampung.append(url)
					else: continue
				date = {"data": json.dumps({"options":{"article":"","appliedProductFilters":"---","price_max": "null","price_min": "null","query": urllib.parse.unquote(self.cari),"scope":"pins","auto_correction_disabled":"","top_pin_id":"","filters":"","bookmarks": [re.findall('"bookmark":"(.*?)"', link)[0]]},"context":{}}), "source_url": "/search/pins/?rs=typed&q="+self.cari}
				link = ses.post("https://id.pinterest.com/resource/BaseSearchResource/get/", params=date, headers={**self.head, "X-CSRFToken": ses.cookies["csrftoken"]}).text
			except Exception as e: pass
		
	def get_source_pin(self, pin):
		try:
			link = ses.get('https://id.pinterest.com/resource/RelatedPinFeedResource/get/?source_url=/pin/'+pin+'/&data={"options":{"field_set_key":"unauth_react","page_size":12,"pin":"'+pin+'","source":"search"},"context":{}}&_=1688744498583'+self.now, headers={**self.head, "X-CSRFToken": ses.cookies["csrftoken"], "X-Pinterest-Source-Url": f"/pin/{pin}/"}).text
			for url in re.findall('"url":"(.*?)"', str(link)):
				if "originals" in str(url):
					if url in self.tampung: pass
					else: print("Link :",url); self.tampung.append(url)
				else: continue
			self.get_next_pin(link, pin)
		except Exception as e: pass
		
	def get_next_pin(self, link, pin):
		main_link = 'https://id.pinterest.com/resource/RelatedPinFeedResource/get/?source_url=/pin/'+pin+'/&data={"options":{"field_set_key":"unauth_react","page_size":12,"pin":"'+pin+'","source":"search","bookmarks": ["'+re.findall('"bookmark":"(.*?)"', link)[0]+'"]},"context":{}}&_='+self.now
		for rozh_bas in range(self.scrol):
			try:
				link = ses.get(main_link, headers={**self.head, "X-CSRFToken": ses.cookies["csrftoken"], "X-Pinterest-Source-Url": f"/pin/{pin}/"}).text
				for url in re.findall('"url":"(.*?)"', str(link)):
					if "originals" in str(url):
						if url in self.tampung: pass
						else: print("Link :",url); self.tampung.append(url)
					else: continue
				main_link = 'https://id.pinterest.com/resource/RelatedPinFeedResource/get/?source_url=/pin/'+pin+'/&data={"options":{"field_set_key":"unauth_react","page_size":12,"pin":"'+pin+'","source":"search","bookmarks": ["'+re.findall('"bookmark":"(.*?)"', link)[0]+'"]},"context":{}}&_='+self.now
			except Exception as e: pass

def extraction():
    clear_screen()
    bryxpogii()
    print(f"     {white}[1] {yellow}EXTRACT {red}ACCOUNT")
    print(f"     {white}[2] {yellow}EXTRACT {red}PAGES")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    choice = input(f"    {green}Enter your choice: ").strip()
    if choice == '1':
        axl1()
    elif choice == '2':
        axl2()
    else:
        print(f"     {red}INVALID CHOICE")

    def reg(self, name):
        headers = {
            'authority': 'www.facebook.com',
            'accept': '*/*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'cookie': self.cookies,
            'origin': 'https://www.facebook.com',
            'referer': 'https://www.facebook.com/pages/creation?ref_type=launch_point',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'viewport-width': '979',
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
            'variables': '{"input":{"bio":"","categories":["181475575221097"],"creation_source":"comet","name":"' + name + '","page_referrer":"launch_point","actor_id":"' + self.id_acc + '","client_mutation_id":"1"}}',
            'server_timestamps': 'true',
            'doc_id': '5903223909690825',
        }
        response = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data)
        try:
            result = response.json()
            if 'id' in result:
                page_id = result['id']
                self.set_profile_picture(page_id)
            return result
        except:
            return response.text

    def set_profile_picture(self, page_id):
        picture_path = "/home/spade/Desktop/load data/Profile.jpeg"  # Replace with your actual path to the profile picture
        headers = {
            'authority': 'www.facebook.com',
            'accept': '*/*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'cookie': self.cookies,
            'origin': 'https://www.facebook.com',
            'referer': f'https://www.facebook.com/{page_id}',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'viewport-width': '979',
            'x-fb-friendly-name': 'ProfilePicUpload',
            'x-fb-lsd': 'ZM7FAk6cuRcUp3imwqvHTY',
        }
        files = {
            'source': (os.path.basename(picture_path), open(picture_path, 'rb'), 'image/jpeg')
        }
        data = {
            'av': self.id_acc,
            '__user': self.id_acc,
            'profile_id': page_id,
            'fb_dtsg': self.fb_dtsg,
            'photo_source': '4',
            'composer_entry_time': '0',
            'composer_session_id': 'abc',
            'ref': 'timeline',
            'upload_id': 'profile_pic',
            'upload_type': 'profile',
        }
        response = requests.post('https://www.facebook.com/photos/upload', headers=headers, files=files, data=data)
        try:
            return response.json()
        except:
            return response.text

def kolor(text, color):
    if color == 'green':
        print(Fore.GREEN + text + Style.RESET_ALL)
    elif color == 'red':
        print(Fore.RED + text + Style.RESET_ALL)
    else:
        print(text)

def get_cookies_file_path():
    clear_screen()
    bryxpogii()
    return input("Enter the path to the cookies.txt file: ")

def hackezr():  
    cookies_file = get_cookies_file_path()
    try:
        with open(cookies_file, 'r') as f:
            cookies_list = f.readlines()
    except FileNotFoundError:
        kolor("ERROR: FILE NOT FOUND. PLEASE CHECK THE PATH.", 'red')
        return
    for cookie_line in cookies_list:
        cookie_line = cookie_line.strip()
        cookies = cookie_line
        vietnamese_names = [
"MrsTexasUNIVERSE Dr.MeenakshiRavi",
"Melanii",
"Israt Jahan",
"Md Rubel Kahan",
"Mariya Akthr Sathi",
"Israt Xahan Esha",
"Younietha Wasilah",
"Nusaiba Islam Eva",
"Lx Zoya",
"Tasnia Rahman",
"Mehedi Hasan",
"Roja Islam",
"Esme Johnston",
"Riya Jahan",
"Sinthiya Chowdhury",
"Jannatul Ferdos",
"Aysha Jannat",
"Moinul Islam Shanto",
"Tanveer Rahman",
"Rosabel Mercado Oaing",
"Bnegali Basi",
"Ashlie Allaisa",
"Rapk Miah",
"Saima Akter",
"Md Minar",
"Tahmina Jannat Mim",
"Humaryra Bin Allbihi",
"Sadiya Akter",
"MD Naeem",
"Foysol Khan",
"Md Robiul Sheikh",
"Md Sohel",
"Alex Hels Afridy",
"Ocena Manus",
"Shohag Sheikh",
"Gojo Saturo",
"Shaddat Khan",
"MD Mithun",
"Rakib Ahmmed Foysal",
"Md Oliull Sheikh",
"Md Sabbir Shaike",
"Sk Tushar",
"Vagne Dev",
"MB �m�m",
"Limon Sehk Limon Sehk",
"Md Milan",
"Reyad Islam",
"Md Shobuzpra",
"Md Masum Islam",
"Tanzim Rabby",
"R�bin Here",
"MD Sumon MD Sumon",
"Asif Khan",
"Mis Afia",
"���m�l H�q��",
"Md Shakib Mridha",
"Urzzal Mia",
"Samuel Ramirez",
"Shaddat Khan",
"Shaheen Kanaipur",
"MD Salman Sak",
"MD Amirol",
"Mahedi Islam",
"MD Alhassan Hawlder",
"Anis Osim",
"Raihan Islam",
"Hamida Forid Pur",
"MD Sohel Sheikh",
"Md Emram",
"Md Nijam Uddin Sheikh",
"MD Biplob",
"Md Moyazzem",
"Md Azad",
"BA DH ON",
"Md Rezaul Rezaul",
"Tanjin Molla",
"Md Sumon",
"Obaidul Krim",
"Rabby Khan",
"Jahangir Gazi",
"Md. Tamim",
"Najir Sheikh",
"Abu Bakar Khan",
"Md Alamin",
"Sgush Rsuhe",
"Rabby Sheikh",
        ]
        random_name = random.choice(vietnamese_names)
        reg_instance = RegPro5(cookies)
        result = reg_instance.reg(random_name)
        if 'error' not in result:
            print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
            kolor(f"     {green}[SUCCESS] {red}CREATED PAGE", 'green')
        else:
            print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
            kolor(f"     {red}[UNSUCCESSFUL] {green}CREATED PAGE", 'red')

import requests
import os

class Color:
    END = '\033[0m'
    BOLD = '\033[1m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'

def pzl(username, passwords):
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
    url = 'https://graph.facebook.com/auth/login'
    for password in passwords:
        data = {
            'method': 'auth.login',
            'fb_api_req_friendly_name': 'authenticate',
            'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
            'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
            'email': username,
            'password': password,
            'access_token': accessToken
        }
        try:
            response = requests.post(url, data=data)
            response.raise_for_status()
            responses = response.json()
            if 'access_token' in responses:
                return responses['access_token'], True
            else:
                error_msg = responses.get('error_msg', 'Unknown error')
                print(f"{Color.RED}ERROR FOR {username}: {error_msg}{Color.END}")
        except requests.exceptions.RequestException as e:
            print(f"{Color.RED}ERROR FOR {username}: {str(e)}{Color.END}")   
    return None, False

def sav(tokens_array, token_file_path):
    with open(token_file_path, 'w') as file:
        for token_info in tokens_array:
            uid = token_info['email']
            access_token = token_info['access_token']
            file.write(f"{uid}|{access_token}\n")

def prz(file_path, tokens_array):
    if not os.path.isfile(file_path):
        print(f"{Color.BOLD}FILE {file_path} DOES NOT EXIST.{Color.END}")
        return
    print(f"     {Color.BOLD}PROCESSING FILE: {file_path}{Color.END}")
    with open(file_path, 'r') as file:
        lines = file.readlines()
    if not lines:
        print(f"{Color.BOLD}FILE {file_path} IS EMPTY.{Color.END}")
        return
    account_pairs = [line.strip() for line in lines if '|' in line]
    if not account_pairs:
        print(f"{Color.BOLD}NO VALID UID|PASS PAIRS FOUND IN {file_path}.{Color.END}")
        return
    for account in account_pairs:
        uid, password = account.split('|')
        pass
        token, success = pzl(uid, [password])
        if success:
            tokens_array.append({"email": uid, "access_token": token})
            print(f"{Color.GREEN}SUCCESSFULLY EXTRACTED TOKEN FOR {uid}{Color.END}")
        else:
            print(f"{Color.BOLD}FAILED TO GET TOKEN FOR {uid}.{Color.END}")

def maz():
    clear_screen()
    bryxpogii()
    file_path = input(f"{Color.YELLOW}Enter the path of the text file with accounts and passwords: {Color.END}").strip()
    token_file_path = input(f"{Color.YELLOW}Enter the path of the file where tokens should be stored: {Color.END}").strip()
    tokens_array = []
    prz(file_path, tokens_array)
    if tokens_array:
        pass
        for token_info in tokens_array:
            pass
        sav(tokens_array, token_file_path)
    else:
        print(f"{Color.BOLD}NO TOKENS COLLECTED.{Color.END}")
    print(f"{Color.BLUE}EXITING THE PROGRAM...{Color.END}")

def start():
    clear_screen()
    bryxpogii()
    token_file_path = input("Enter the path to the file containing the tokens: ").strip()
    tokens = rad(token_file_path)
    if not tokens:
        print("NO TOKENS FOUND. EXITING.")
        return
    if not os.path.exists(DIRECTORY):
        print(f"ERROR: DIRECTORY '{DIRECTORY}' DOES NOT EXIST.")
        return
    files_in_directory = os.listdir(DIRECTORY)
    if not files_in_directory:
        print(f"ERROR: NO FILES FOUND IN DIRECTORY '{DIRECTORY}'.")
        return
    for user_token in tokens:
        pages = pigzs(user_token)
        if not pages:
            print(f"NO PAGES FOUND FOR TOKEN {user_token}. Skipping.")
            continue
        for page in pages:
            pass
            page_id = page['id']
            page_access_token = page.get('access_token')
            if not page_access_token:
                print(f"NO ACCESS TOKEN FOUND FOR PAGE {page_id}. Skipping.")
                continue
            if pec(page_id):
                pass
                continue
            file_name = random.choice(files_in_directory)
            file_path = os.path.join(DIRECTORY, file_name)
            result = plod(page_id, page_access_token, file_path)
            print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
            print(f"    {green}SUCCESSFULLY UPLOADED PROFILE PICTURE {page['name']} ──────> {page['id']} ")
            print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
            time.sleep(2)

import requests
import os
import random
import time

BASE_URL = 'https://graph.facebook.com/v18.0'
DIRECTORY = 'Picture'

def pigzs(access_token):
    url = f'{BASE_URL}/me/accounts'
    params = {
        'access_token': access_token
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json().get('data', [])
    except requests.exceptions.RequestException as e:
        print(f"ERROR GETTING PAGES FOR TOKEN {access_token}: {str(e)}")
        return []

def pec(page_id):
    url = f'{BASE_URL}/{page_id}?fields=picture'
    try:
        response = requests.get(url)
        response.raise_for_status()
        picture_data = response.json().get('picture', {})
        return 'data' in picture_data and 'url' in picture_data['data']
    except requests.exceptions.RequestException as e:
        print(f"ERROR CHECKING PROFILE PICTURE FOR PAGE {page_id}: {str(e)}")
        return False

def plod(page_id, page_access_token, file_path):
    try:
        with open(file_path, 'rb') as file:
            files = {
                'source': file
            }
            data = {
                'access_token': page_access_token
            }
            url = f'{BASE_URL}/{page_id}/picture'
            response = requests.post(url, files=files, data=data)
            response.raise_for_status()
            return response.json()
    except requests.exceptions.RequestException as e:
        print(f"ERROR UPLOADING PROFILE PICTURE TO PAGE {page_id}: {str(e)}")
        return {'error': str(e)}
    except FileNotFoundError as e:
        print(f"ERROR: FILE NOT FOUND {file_path}: {str(e)}")
        return {'error': str(e)}

def rad(file_path):
    tokens = []
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if '|' in line:
                    uid, token = line.split('|', 1)
                    tokens.append((uid.strip(), token.strip()))
    except FileNotFoundError as e:
        print(f"ERROR: TOKENS FILE NOT FOUND | PLEASE TRY AGAIN {file_path}: {str(e)}")
    return tokens

def mainzsa():
    clear_screen()
    bryxpogii()
    print(f"     {red}[1] {green}GET TOKEN")
    print(f"     {red}[2] {green}SET PFP")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    choice = input(f"    {green}Enter your choice: ").strip()
    if choice == '1':
        maz()
    if choice == '2':
        start()
    else: 
        print("invalid po")
        clear_screen()

import requests
import random
import string
import os

CODE_FILE = '/sdcard/boostphere/generated_code.txt'

def ensure_file_exists():
    open(CODE_FILE, 'a').write('')

def generate_code():
    prefix = "BRYX-BOOSTING"
    number_part = ''.join(random.choices(string.digits, k=3))
    letters_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))  # 5 alphanumeric characters
    code = f"{prefix}-{number_part}-{letters_part}"
    return code

def save_code(code):
    with open(CODE_FILE, 'w') as file:
        file.write(code)

def load_code():
    if os.path.exists(CODE_FILE):
        with open(CODE_FILE, 'r') as file:
            return file.read().strip()
    return None

def is_code_approved(code):
    try:
        response = requests.get("https://bryxxxpogi.blogspot.com/2025/02/approval-boosting.html?m=1")
        response.raise_for_status()
        approved_codes = response.text.splitlines()
        approved_codes = [line.split('#')[0].strip() for line in approved_codes if line]
        return code in approved_codes
    except requests.RequestException as e:
        print(f"ERROR FETCHING THE APPROVAL LIST: {e}")
        return False

def generate_and_check_code():
    ensure_file_exists()
    code = load_code()  
    if code is None or code == '':
        code = generate_code()
        save_code(code)
        clear_screen()
        bryxpogii()
        print(f"      {yellow}YOUR GENERATED CODE {white}: {blue}{code}")
    else:
        clear_screen()
        bryxpogii()
        print(f"     {yellow}YOUR CODE {white}: {blue}{code}")
    if is_code_approved(code):
        main()
    else:
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        print(f"     {red}CODE IS NOT APPROVED\n     {yellow}PLEASE SEND IT TO\n     {white}FB LINK : {yellow}https://www.facebook.com/bryxxpogi")
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")

import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def get_profile_id(access_token):
    try:
        url = 'https://graph.facebook.com/me'
        params = {'access_token': access_token}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json().get('id')
        else:
            return None
    except requests.exceptions.RequestException:
        return None

import requests
import base64
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def join_group(group_id, profile_id, access_token):
    try:
        url = f'https://graph.facebook.com/{group_id}/members/{profile_id}'
        params = {'access_token': access_token}
        response = requests.post(url, params=params)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False

def val(token):
    validation_url = f"https://graph.facebook.com/debug_token?input_token={token}&access_token={token}"
    response = requests.get(validation_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

token = ''
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json'
}
file_options = {
    1: "/sdcard/boostphere/FRAACCOUNT.txt",
    2: "/sdcard/boostphere/FRAPAGES.txt",
    3: "/sdcard/boostphere/RPWACCOUNT.txt",
    4: "/sdcard/boostphere/RPWPAGES.txt"
}

def git(repo_owner, repo_name, file_path):
    file_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}'
    response = requests.get(file_url, headers=headers)    
    if response.status_code == 200:
        content = response.json()
        file_sha = content['sha']
        file_content = base64.b64decode(content['content']).decode('utf-8')
        return file_content, file_sha
    elif response.status_code == 404:
        print(f"     FAILED")
        return None, None
    else:
        print(f"     FAILED")
        return None, None

def contint(repo_owner, repo_name, file_path, file_sha):
    file_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}'   
    empty_content = base64.b64encode(''.encode('utf-8')).decode('utf-8')
    commit_message = f"Clear {file_path}"
    data = {
        "message": commit_message,
        "content": empty_content,
        "sha": file_sha
    }
    response = requests.put(file_url, json=data, headers=headers)
    if response.status_code == 200:
        pass
    else:
        pass

def choose_file_path():
    clear_screen()
    bryxpogii()
    print(f"""     {blue}CHOOSE TYPE OF FILE TO SAVE TOKENS: 
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m
     {yellow}[1] {blue}FRA ACCOUNT 
     {yellow}[2] {blue}FRA PAGES
     {yellow}[3] {blue}RPW ACCOUNT
     {yellow}[4] {blue}RPW PAGES
     {red}[0] {red}EXIT 
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m""")
    choice = int(input(f"    {green}Enter your choice: ").strip())
    if choice == 0:
        print("EXITING THE PROGRAM.")
        exit()
    elif choice in file_options:
        return file_options[choice]
    else:
        print("INVALID CHOICE. PLEASE TRY AGAIN.")
        return choose_file_path()

def cynt(content):
    tokens = content.splitlines()
    return len(tokens)

def count_cookies(cookies_content):
    cookies = cookies_content.splitlines()
    return len(cookies)

def githubtoks():
    clear_screen()
    bryxpogii()
    repo_owner = 'bryxpogi143'
    repo_name = input(f"    {yellow}CODE: ")
    tokens_content, tokens_sha = git(repo_owner, repo_name, 'Tokens')
    if tokens_content:
        token_count = cynt(tokens_content)
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        print(f"       {red}{token_count} {green}TOKENS FOUND !")
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        storage_path = choose_file_path()
        with open(storage_path, 'a') as file:
           file.write(tokens_content + '\n')
        contint(repo_owner, repo_name, 'Tokens', tokens_sha)
    cookies_content, cookies_sha = git(repo_owner, repo_name, 'Cookies')
    if cookies_content:
        cookie_count = count_cookies(cookies_content)
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        print(f"       {red}{cookie_count} {green}COOKIES FOUND !")
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        cookie_path = input("PATH TO SAVE COOKIES: ")
        with open(cookie_path, 'a') as cookie_file:
            cookie_file.write(cookies_content + '\n')
        contint(repo_owner, repo_name, 'Cookies', cookies_sha)
    else:
        pass

def check():
    clear_screen()
    bryxpogii()
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    print(f"""     {blue}CHOOSE TYPE OF FILE TO VERIFY: 
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m
     {yellow}[1] {blue}FRA ACCOUNT 
     {yellow}[2] {blue}FRA PAGES
     {yellow}[3] {blue}RPW ACCOUNT
     {yellow}[4] {blue}RPW PAGES
     {red}[0] {red}EXIT 
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m""")
    choice = int(input(f"     {green}Enter your choice: "))
    if choice in file_options:
        file_path = file_options[choice]
    elif choice == 0:
        print("EXITING...")
        return
    else:
        print("INVALID CHOICE. EXITING...")
        return
    with open(file_path, 'r') as file:
        lines = file.readlines()
    valid_tokens = []
    for line in lines:
        uid, token = line.strip().split('|')
        if val(token):
            valid_tokens.append(line.strip())
            print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
            print(f"     {green}ACCOUNT ─────> {blue}{uid} {white}= {yellow} IS VALID")
        else:
            print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
            print(f"     {red}ACCOUNT ─────> {blue}{uid} {white}= {yellow} IS NOT VALID AND WILL BE REMOVED")
    with open(file_path, 'w') as file:
        for valid_token in valid_tokens:
            file.write(valid_token + '\n')

def perform_group_join():
    clear_screen()
    bryxpogii()
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    print(f"""     {blue}CHOOSE TYPE OF ACCOUNTS TO JOIN GROUP: 
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m
     {yellow}[1] {blue}FRA ACCOUNT 
     {yellow}[2] {blue}FRA PAGES
     {yellow}[3] {blue}RPW ACCOUNT
     {yellow}[4] {blue}RPW PAGES
     {red}[0] {red}EXIT 
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m""")
    try:
        file_choice = int(input(f"    {green}Enter your choice: ").strip())
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        if file_choice not in file_options:
            print("INVALID CHOICE.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("PLEASE ENTER A VALID NUMBER.")
        return
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print("FILE NOT FOUND.")
        return
    except Exception as e:
        print(f"ERROR LOADING TOKENS: {e}")
        return
    available_tokens = len(tokens)
    if available_tokens == 0:
        print("NO TOKENS AVAILABLE FROM THE SELECTED FILE.")
        return
    try:
        start_line = int(input(f"   \033[1;32mEnter the starting line (1 to {available_tokens}): "))
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        if start_line < 1 or start_line > available_tokens:
            print(f"PLEASE ENTER A VALID LINE NUMBER BETWEEN 1 AND {available_tokens}.")
            return
    except ValueError:
        print("PLEASE ENTER A VALID NUMBER.")
        return
    tokens = tokens[start_line - 1:]
    group_id = input(f"   {yellow}Enter the group ID: ")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    try:
        num_tokens = int(input(f"   \033[1;32mEnter Limit: "))
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    except ValueError:
        print("PlEASE ENTER A VALID NUMBER FOR TOKENS.")
        return
    if num_tokens > len(tokens):
        print(f"\033[1;31mERROR: NUMBER EXCEEDS AVAILABLE TOKENS ({len(tokens)}).")
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        return
    join_count = 0
    failed_count = 0
    retries_left = num_tokens
    max_workers = 10
    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_token = {}
        while join_count < num_tokens and retries_left > 0:
            for token in tokens[:retries_left]:
                access_token = token.split('|')[1]
                profile_id = get_profile_id(access_token)
                if profile_id:
                    future = executor.submit(join_group, group_id, profile_id, access_token)
                    future_to_token[future] = token
                else:
                    print(f"\033[1;31m[FAILED] \033[1;37mFAILED TO RETRIEVE PROFILE ID FOR TOKEN \033[1;33m{token}\033[0m")
            for future in as_completed(future_to_token):
                token = future_to_token[future]
                try:
                    success = future.result()
                    if success:
                        join_count += 1
                        print(f"\033[1;32m[SUCCESS] \033[1;37mSUCCESSFULLY JOINED GROUP {group_id}")
                    else:
                        failed_count += 1
                        print(f"{red}[UNSUCCESS] \033[1;31mFAILED JOINED GROUP {group_id}")
                    if join_count >= num_tokens:
                        break
                except Exception as e:
                    print(f"ERROR PROCESSING TOKEN {token}: {e}")
            retries_left = num_tokens - join_count
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        print(f"\033[1;32mTOTAL SUCCESSFUL: {join_count}\033[0m")
        print(f"\033[1;31mTOTAL FAILED: {failed_count}\033[0m")

def live(url):
    parts = url.split('/')
    if len(parts) > 4:
        user_id = parts[3]
        video_id = parts[5]
        return f"{user_id}_{video_id}"
    else:
        return None

import requests
import threading
from concurrent.futures import ThreadPoolExecutor
import random
import time
import sys
import os
import platform
import re
import random
import string

purple = "\033[1;35m"
blue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
white = "\033[1;37m"
purple = "\033[1;35m"
blue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
white = "\033[1;37m"

def get_combined_data(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        'cache-control': "max-age=0",
        'dpr': "2",
        'viewport-width': "980",
        'sec-ch-ua': "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        'sec-ch-ua-mobile': "?0",
        'sec-ch-ua-platform': "\"Linux\"",
        'sec-ch-ua-platform-version': "\"\"",
        'sec-ch-ua-model': "\"\"",
        'sec-ch-ua-full-version-list': "\"Google Chrome\";v=\"131.0.6778.104\", \"Chromium\";v=\"131.0.6778.104\", \"Not_A Brand\";v=\"24.0.0.0\"",
        'sec-ch-prefers-color-scheme': "light",
        'upgrade-insecure-requests': "1",
        'sec-fetch-site': "same-origin",
        'sec-fetch-mode': "navigate",
        'sec-fetch-user': "?1",
        'sec-fetch-dest': "document",
        'accept-language': "en-US,en;q=0.9",
        'priority': "u=0, i",
        'Cookie': "sb=fuZTZ8Zyl9dXj5TFodlxDrGD; dpr=2; wd=980x1628; datr=fuZTZxL-gtbBjTkfeBq-VVDZ"
    }
    try:
        response = requests.get(url, headers=headers).text
        actrs_match = re.search(r'"actrs\\":\\"(\d+)\\"', response)
        actrs_number = actrs_match.group(1) if actrs_match else None
        post_id_match = response.split('"post_id":"')[1].split('"')[0] if '"post_id":"' in response else None
        if actrs_number and post_id_match:
            return f"{actrs_number}_{post_id_match}"
        elif not actrs_number:
            return "actrs number not found!"
        elif not post_id_match:
            return "post_id not found!"
    except Exception as e:
        return f"An error occurred: {str(e)}"

def clear_screen():
    if 'termux' in platform.system().lower():
        os.system('clear')
    elif platform.system().lower() == 'windows':
        os.system('cls')
    else:
        os.system('clear')

def generate_user_agent():
    fbav = f"{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}"
    fbbv = str(random.randint(111111111, 999999999))
    fbrv = '0'
    random_seed = random.Random()
    adid = ''.join(random_seed.choices(string.hexdigits, k=16))
    device = random.choice(["HUAWEI MAR-LX1M", "Samsung SM-G960F", "OnePlus GM1913"])
    fbav_version = str(random.randint(49, 150))
    fbbv_version = str(random.randint(11111111, 77777777))
    carrier = random.choice(["Ooredoo TN", "Orange", "Vodafone", "T-Mobile"])
    ua_bgraph = f'[FBAN/FB4A;FBAV/{fbav_version}.0.0.{random.randrange(20, 49)}.{random.randint(11, 99)};FBBV/{fbbv_version};' \
                f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};FBDM/{{density=3.0,width=1080,height=2107}};FBLC/fr_FR;' \
                f'FBRV/{fbrv};FBCR/{carrier};FBMF/{device.split(" ")[0]};FBBD/{device.split(" ")[0]};' \
                f'FBPN/com.facebook.katana;FBDV/{device};FBSV/9;FBOP/1;FBCA/arm64-v8a:]'
    return ua_bgraph

ua_bgraph = generate_user_agent()

import requests
import random
import concurrent.futures as thread
import os
import string

def bgraph(uid, pw, path_file, extract_type, success_count, existing_uids):
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
    fbav = f'{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'
    fbbv = str(random.randint(111111111, 999999999))
    fbrv = '0'
    random_seed = random.Random()
    adid = ''.join(random_seed.choices(string.hexdigits, k=16))
    ua_bgraph = '[FBAN/FB4A;FBAV/' + str(random.randint(49, 66)) + '.0.0.' + str(random.randrange(20, 49)) + str(random.randint(11, 99)) + ';FBBV/' + str(random.randint(11111111, 77777777)) + ';' + '[FBAN/FB4A;FBAV/' + fbav + ';FBBV/' + fbbv + ';FBDM/{density=3.0,width=1080,height=2107};FBLC/fr_FR;FBRV/' + fbrv + ';FBCR/Ooredoo TN;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1M;FBSV/9;FBOP/1;FBCA/arm64-v8a:]'
    data = {
        'adid': f'{uuid.uuid4()}',
        'format': 'json',
        'device_id': f'{uuid.uuid4()}',
        'cpl': 'true',
        'family_device_id': f'{uuid.uuid4()}',
        'credentials_type': 'device_based_login_password',
        'error_detail_type': 'button_with_disabled',
        'source': 'device_based_login',
        'email': uid,
        'password': pw,
        'access_token': accessToken,
        'generate_session_cookies': '1',
        'meta_inf_fbmeta': '',
        'advertiser_id': f'{uuid.uuid4()}',
        'currently_logged_in_userid': '0',
        'locale': 'en_US',
        'client_country_code': 'US',
        'method': 'auth.login',
        'fb_api_req_friendly_name': 'authenticate',
        'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
    }
    headers = {
        'User-Agent': ua_bgraph,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'graph.facebook.com',
        'X-FB-Net-HNI': str(random.randint(10000, 99999)),
        'X-FB-SIM-HNI': str(random.randint(10000, 99999)),
        'X-FB-Connection-Type': 'MOBILE.LTE',
        'X-Tigon-Is-Retry': 'False',
        'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
        'x-fb-device-group': str(random.randint(1000, 9999)),
        'X-FB-Friendly-Name': 'ViewerReactionsMutation',
        'X-FB-Request-Analytics-Tags': 'graphservice',
        'X-FB-HTTP-Engine': 'Liger',
        'X-FB-Client-IP': 'True',
        'X-FB-Connection-Bandwidth': str(random.randint(20000000, 30000000)),
        'X-FB-Server-Cluster': 'True',
        'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'
    }
    url = 'https://graph.facebook.com/auth/login'
    try:
        if uid in existing_uids:
            print(f"     {yellow}[INFO] {red}ACCOUNT --> {white}{uid} {red}ALREADY EXISTS.")
            print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
            return
        response = requests.post(url,headers=headers,data=data).json()
        print(response)
        if 'access_token' in response:
            token = response['access_token']
            with open(path_file, 'a') as f:
                f.write(f"{uid}|{token}\n")
            print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
            print(f"     \033[32m[SUCCESS]\033[0m: EXTRACTED ACCOUNT ─────> {uid}.")
            print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
            success_count.append(uid)
        else:
            print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
            print(f"     \033[31m[FAILED]\033[0m: TO EXTRACT ACCOUNT ─────> {uid}.")
            print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    except Exception as e:
        print(f"     \033[1;31m ERROR EXTRACTING ACCOUNT: {uid}. REASON: {str(e)}\033[0m\n")

def proz(accounts_file, token_output_path, extract_type):
    success_count = []
    existing_uids = set()
    if os.path.exists(token_output_path):
        with open(token_output_path, 'r') as f:
            existing_uids = {line.split('|')[0] for line in f.readlines()}
    try:
        with open(accounts_file, 'r') as file:
            accounts = file.readlines()
        accounts = [line.strip() for line in accounts if '|' in line.strip()]
        if not accounts:
            print(f"NO VALID ACCOUNTS FOUND IN {accounts_file}.")
            return
        with thread.ThreadPoolExecutor(max_workers=30) as executor:
            futures = [executor.submit(bgraph, uid, pw, token_output_path, extract_type, success_count, existing_uids)
                       for uid, pw in [account.split('|') for account in accounts]]
            for future in futures:
                future.result()
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        print(f"     \033[1;34m[SUCCESS]\033[0m: {len(success_count)} {extract_type}(s) SUCCESSFULLY EXTRACTED.")
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    except FileNotFoundError:
        print(f"FILE NOT FOUND: {accounts_file}")
        return

import requests
import random
import concurrent.futures as thread
import os
import string


def load_existing_tokens(path_file):
    if os.path.exists(path_file):
        with open(path_file, 'r') as f:
            return {line.split('|')[0] for line in f.readlines()}
    return set()

def bgraph_page(uid, pw, path_file, extract_type, success_count, existing_tokens):
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
    fbav = f'''{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'''
    fbbv = str(random.randint(111111111, 999999999))
    fbrv = '0'
    random_seed = random.Random()
    adid = ''.join(random_seed.choices(string.hexdigits, k=16))
    ua_bgraph = '[FBAN/FB4A;FBAV/' + str(random.randint(49, 66)) + '.0.0.' + str(random.randrange(20, 49)) + str(random.randint(11, 99)) + ';FBBV/' + str(random.randint(11111111, 77777777)) + ';' + '[FBAN/FB4A;FBAV/' + fbav + ';FBBV/' + fbbv + ';FBDM/{density=3.0,width=1080,height=2107};FBLC/fr_FR;FBRV/' + fbrv + ';FBCR/Ooredoo TN;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1M;FBSV/9;FBOP/1;FBCA/arm64-v8a:]'
    data = {
        'adid': f'{uuid.uuid4()}',
        'format': 'json',
        'device_id': f'{uuid.uuid4()}',
        'cpl': 'true',
        'family_device_id': f'{uuid.uuid4()}',
        'credentials_type': 'device_based_login_password',
        'error_detail_type': 'button_with_disabled',
        'source': 'device_based_login',
        'email': uid,
        'password': pw,
        'access_token': accessToken,
        'generate_session_cookies': '1',
        'meta_inf_fbmeta': '',
        'advertiser_id': f'{uuid.uuid4()}',
        'currently_logged_in_userid': '0',
        'locale': 'en_US',
        'client_country_code': 'US',
        'method': 'auth.login',
        'fb_api_req_friendly_name': 'authenticate',
        'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
    }
    headers = {
        'User-Agent': ua_bgraph,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'graph.facebook.com',
        'X-FB-Net-HNI': str(random.randint(10000, 99999)),
        'X-FB-SIM-HNI': str(random.randint(10000, 99999)),
        'X-FB-Connection-Type': 'MOBILE.LTE',
        'X-Tigon-Is-Retry': 'False',
        'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
        'x-fb-device-group': str(random.randint(1000, 9999)),
        'X-FB-Friendly-Name': 'ViewerReactionsMutation',
        'X-FB-Request-Analytics-Tags': 'graphservice',
        'X-FB-HTTP-Engine': 'Liger',
        'X-FB-Client-IP': 'True',
        'X-FB-Connection-Bandwidth': str(random.randint(20000000, 30000000)),
        'X-FB-Server-Cluster': 'True',
        'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'
    }
    url = 'https://graph.facebook.com/auth/login'
    try:
        if uid in existing_uids:
            print(f"     {white}ACCOUNT ─────> {red}{uid} {green}ALREADY EXISTS")
            print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
            return
        response = requests.post(url,headers=headers,data=data).json()
        if 'access_token' in response:
            token = response['access_token']
            pages = extract_fb_pages(token)
            if pages:
                for page in pages:
                    page_id = page['id']
                    if page_id not in existing_tokens:
                        with open(path_file, 'a') as f:
                            f.write(f"{page_id}|{page['accessToken']}\n")
                        print(f"{white}{uid}  ─────> {green}PAGE ID: {red}{page_id} {yellow}EXTRACTED SUCCESSFULLY")
                        existing_tokens.add(page_id)
                    else:
                        print(f"{white}ID:  {page_id} ─────> {green}ALREADY EXISTS ! ")
            else:
                print(f"{white}{uid} ─────> {red}DOESN'T HAVE PAGES !")
            success_count.append(uid)
        else:
            print(f"{white}{uid}  ─────> {red}FAILED TO EXTRACT ! ")
    except Exception as e:
        print(f"ERROR EXTRACTING ACCOUNT: {uid}. REASON: {str(e)}")

def extract_fb_pages(token):
    url = 'https://graph.facebook.com/v18.0/me/accounts'
    headers = {
        'Authorization': f'Bearer {token}'
    }   
    pages_data = []
    while url:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f'ERROR: {response.text}')
            return None
        data = response.json()
        for page in data.get('data', []):
            pages_data.append({
                'id': page.get('id'),
                'accessToken': page.get('access_token')
            })
        url = data.get('paging', {}).get('next')
    return pages_data

def prozc(accounts_file, token_output_path, extract_type):
    success_count = []
    existing_tokens = load_existing_tokens(token_output_path)
    try:
        with open(accounts_file, 'r') as file:
            accounts = file.readlines()
        accounts = [line.strip() for line in accounts if '|' in line.strip()]
        if not accounts:
            print(f"NO VALID ACCOUNTS FOUND IN {accounts_file}.")
            return
        with thread.ThreadPoolExecutor(max_workers=30) as executor:
            futures = [executor.submit(bgraph_page, uid, pw, token_output_path, extract_type, success_count, existing_tokens)
                       for uid, pw in [account.split('|') for account in accounts]]
            for future in futures:
                future.result()
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
        print(f"     \033[1;34m[SUCCESS]\033[0m: {len(success_count)} {extract_type}(s) SUCCESSFULLY EXTRACTED.")
        print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    except FileNotFoundError:
        print(f"FILE NOT FOUND: {accounts_file}")

def extraction():
    clear_screen()
    bryxpogii()
    print(f"     {white}[1] {yellow}EXTRACT {red}ACCOUNT")
    print(f"     {white}[2] {yellow}EXTRACT {red}PAGES")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    choice = input(f"    {green}Enter your choice: ").strip()
    if choice == '1':
        axl1()
    elif choice == '2':
        axl2()
    else:
        print(f"     {red}INVALID CHOICE")

def axl2():
    clear_screen()
    bryxpogii()
    folder_path = "/sdcard/boostphere"
    print(f"     {yellow}[01] {blue}FRA EXTRACT ACCOUNT")
    print(f"     {yellow}[02] {blue}FRA EXTRACT PAGES")
    print(f"     {yellow}[03] {blue}RPW EXTRACT ACCOUNT")
    print(f"     {yellow}[04] {blue}RPW EXTRACT PAGES")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    save_choice = input(f"    {green}Enter your choice: ").strip()
    if save_choice == '1':
        account_file = os.path.join(folder_path, "FRAACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '2':
        account_file = os.path.join(folder_path, "FRAPAGES.txt")
        extract_type = 'page'
    elif save_choice == '3':
        account_file = os.path.join(folder_path, "RPWACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '4':
        account_file = os.path.join(folder_path, "RPWPAGES.txt")
        extract_type = 'page'
    else:
        print("INVALID CHOICE. EXITING.")
        return
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    print(f"     \033[33mTHE FORMAT SHOULD BE \033[31muid|pass")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    file_path = input(f"     \033[33mPATH: ").strip()
    prozc(file_path, account_file, extract_type)

def axl1():
    clear_screen()
    bryxpogii()
    folder_path = "/sdcard/boostphere"
    print(f"     {yellow}[01] {blue}FRA EXTRACT ACCOUNT")
    print(f"     {yellow}[02] {blue}FRA EXTRACT PAGES")
    print(f"     {yellow}[03] {blue}RPW EXTRACT ACCOUNT")
    print(f"     {yellow}[04] {blue}RPW EXTRACT PAGES")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    save_choice = input(f"    {green}Enter your choice: ").strip()
    if save_choice == '1':
        account_file = os.path.join(folder_path, "FRAACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '2':
        account_file = os.path.join(folder_path, "FRAPAGES.txt")
        extract_type = 'page'
    elif save_choice == '3':
        account_file = os.path.join(folder_path, "RPWACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '4':
        account_file = os.path.join(folder_path, "RPWPAGES.txt")
        extract_type = 'page'
    else:
        print("INVALID CHOICE. EXITING.")
        return
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    print(f"     \033[33mTHE FORMAT SHOULD BE \033[31muid|pass")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    file_path = input(f"     \033[33mPATH: ").strip()
    token_output_path = account_file
    proz(file_path, token_output_path, extract_type)

import os
import random
import requests
import time
from concurrent.futures import ThreadPoolExecutor

def gettokesz(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return [line.strip().split('|')[1] for line in lines if '|' in line]

class fbpost:
    def __init__(self, link):
        self.link = link
    def shir(self, token):
        url = "https://graph.facebook.com/me/feed"
        payload = {
            'link': self.link,
            'published': '1',
            'privacy': '{"value":"EVERYONE"}',
            'access_token': token
        }
        try:
            response = requests.post(url, data=payload)
            if response.status_code == 200:
                print(f"{green}      SUCCESSFULLY SHARED")
                return True
            else:
                pass
                return False
        except requests.exceptions.RequestException as e:
            print(f"AN ERROR OCCURRED: {e}")
            return False

def sgtz(link, file_path, num_shares):
    start_all = time.time()
    tokens = gettokesz(file_path)
    if len(tokens) < num_shares:
        print("NOT ENOUGH TOKENS TO MEET THE REQUESTED NUMBER OF SHARES.")
        return
    def worker(token):
        fb_poster = fbpost(link)
        fb_poster.shir(token)
    with ThreadPoolExecutor(max_workers=20) as executor:
        for token in tokens[:num_shares]:
            executor.submit(worker, token)
    end_all = time.time()
    print(f"\nSHARING STARTED AT: {time.ctime(start_all)}")
    print(f"SHARING ENDED AT: {time.ctime(end_all)}")
    print(f"TOTAL DURATION: {end_all - start_all:.2f} SECONDS")

def ttsu(*file_paths):
    counts = []
    for file_path in file_paths:
        try:
            with open(file_path, 'r') as file:
                counts.append(sum(1 for line in file if line.strip()))
        except FileNotFoundError:
            counts.append(0)
    return counts

def tts():
    file_paths = [
        '/sdcard/boostphere/FRAACCOUNT.txt',
        '/sdcard/boostphere/FRAPAGES.txt',
        '/sdcard/boostphere/RPWACCOUNT.txt',
        '/sdcard/boostphere/RPWPAGES.txt',
    ]
    for file_path in file_paths:
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"CREATED DIRECTORY: {directory}")
        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                pass
            print(f"CREATED FILE: {file_path}")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def extraction():
    clear_screen()
    bryxpogii()
    print(f"     {white}[1] {yellow}EXTRACT {red}ACCOUNT")
    print(f"     {white}[2] {yellow}EXTRACT {red}PAGES")
    print(f"     {white}[3] {yellow}EXTRACT {red}RPW")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    choice = input(f"    {green}Enter your choice: ").strip()
    if choice == '1':
        axl1()
    elif choice == '2':
        axl2()
    if choice == '3':
    	axl3()
    else:
        print(f"     {red}INVALID CHOICE")

def main():
    open('/sdcard/boostphere/FRAACCOUNT.txt', 'a').write('')
    open('/sdcard/boostphere/FRAPAGES.txt', 'a').write('')
    open('/sdcard/boostphere/RPWACCOUNT.txt', 'a').write('')
    open('/sdcard/boostphere/RPWACCOUNT.txt', 'a').write('')
    fraaccounts_file = '/sdcard/boostphere/FRAACCOUNT.txt'
    frapages_file = '/sdcard/boostphere/FRAPAGES.txt'
    rpwaccounts = '/sdcard/boostphere/RPWACCOUNT.txt'
    rpwpages = '/sdcard/boostphere/RPWPAGES.txt'
    total_accounts, total_pages = count_tokens(fraaccounts_file, frapages_file)
    total_account_rpw, total_pages_rpw = count_tokens(rpwaccounts,rpwpages)
    clear_screen()
    bryxpogii()
    print(f"""                 {lightblue}OVERVIEW OF STORED ACCOUNT & PAGES💫\033[0m
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m
                      {blue}FRA ACCOUNT{yellow} : {green}{total_accounts}
                      {blue}FRA PAGES  {yellow} : {green}{total_pages}
                      {blue}RPW ACCOUNT{yellow} : {green}{ total_account_rpw}
                      {blue}RPW PAGES  {yellow} : {green}{total_pages_rpw}
\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m""")
    print(f"                      {green}SERVICES WE OFFER✨                               ")
    print(f"      {red}[01]  {red}START")
    print(f"      {green}[02]  {purple}REACT TO POST.             {yellow}- {green}[PAGE & NORMAL ACCOUNT]")
    print(f"      {green}[03]  {purple}REACT TO REELS.            {yellow}- {green}[PAGE & NORMAL ACCOUNT]")
    print(f"      {green}[04]  {purple}REACT TO GROUP POST.       {yellow}- {green}[PAGE & NORMAL ACCOUNT]")
    print(f"      {green}[05]  {purple}REACT TO POST[VID & PHOTO].{yellow}- {green}[PAGE & NORMAL ACCOUNT]")
    print(f"      {green}[06]  {purple}AUTO FOLLOW.               {yellow}- {green}[PAGE & NORMAL ACCOUNT]")
    print(f"      {green}[07]  {purple}AUTO REACT TO DP & POST.   {yellow}- {green}[PAGE & NORMAL ACCOUNT]")
    print(f"      {green}[08]  {purple}AUTO COMMENT.              {yellow}- {green}[PAGE & NORMAL ACCOUNT]")
    print(f"      {green}[09]  {purple}AUTO LIKE & FOLLOW PAGE.   {yellow}- {green}[PAGE & NORMAL ACCOUNT]")
    print(f"      {green}[10]  {purple}AUTO SHARE [VIA COOKIE].   {yellow}- {green}[PAGE & NORMAL ACCOUNT]")
    print(f"      {green}[11]  {purple}AUTO REACT COMMENT.        {yellow}- {green}[PAGE & NORMAL ACCOUNT]")
    print(f"      {green}[12]  {purple}AUTO REPLY COMMENT.        {yellow}- {green}[PAGE & NORMAL ACCOUNT]")
    print(f"      {green}[13]  {purple}LIKE & FOLLOW PAGE.        {yellow}- {green}[PAGE & NORMAL ACCOUNT]")
    print(f"      {green}[14]  {purple}AUTO GROUP JOIN.           {yellow}- {green}[PAGE & NORMAL ACCOUNT]")
    print(f"      {green}[15]  {purple}AUTO REACT {red}LIVE.           {yellow}- {green}[PAGE & NORMAL ACCOUNT]")
    print(f"      {green}[16]  {purple}AUTO COMMENT {red}LIVE.         {yellow}- {green}[PAGE & NORMAL ACCOUNT]")
    print(f"      {red}[17]  {red}RESET")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    print(f"                      {red} ADDITIONAL FREE SERVICES🔥                                 ")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    print(f"      {green}[18] {purple}AUTO CREATE PAGE.          {yellow}- {green}[PHB NAMES]")
    print(f"      {green}[19] {purple}AUTO SET PFP.              {yellow}- {green}[RANDOM]")
    print(f"      {green}[20] {purple}PINTEREST PICTURE.         {yellow}- {green}[RANDOM]")
    print(f"      {red}[21] {red}REMOVE DUPLICATES.         {yellow}- {green}[ACCURATE]")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    print(f"                      {green}ACCOUNT CHECKER LIST ✅                                 ")
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    print(f"      {green}[22] {purple}ACCOUNT CHECKER.          {yellow}- {green}[ACCURATE]")
    print(f"      {green}[23] {purple}VALIDATE TOKENS.          {yellow}- {green}[ACCURATE]")
    print(f"      {green}[24] {purple}REEDEM ACCOUNTS.          {yellow}- {green}[ACCURATE]") 
    print(f"      {green}[25] {purple}AUTO SPAM SHARE.          {yellow}- {green}[MAX SPEED/PRIVATE MAX SPEED]")
    print(f"      {green}[26] {purple}AUTO CREATE FACEBOOK.     {yellow}- {green}[FILIPINO/FILIPINA NAMES]")
    print(f"      {green}[27] {purple}AUTO CREATE FILE.         {yellow}- {green}[PINOY/VIETNAMESE/BANGLADESH]")          
    print("\033[1;34m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[0m")
    choice = input(f"    {green}Enter your choice: ").strip()
    if choice == '1':
        extraction()
    if choice == '2':
        perform_reaction_fast()
    if choice == '3':
        reels()
    if choice == '4':
        perform_reaction_fast()
    if choice == '5':
        vid()
    if choice == '6':
        auto_follow_fast()
    if choice == '7':
        perform_reaction_fast_dp()
    if choice == '8':
        perform_comment_fast()
    if choice == '9':
        perform_actions_from_file()
    if choice == '10':
        shar()
    if choice == '11': 
        comment_react()
    if choice == '12': 
        reply()
    if choice == '13':
        p_like()
    if choice == '14':
        perform_group_join()
    if choice == '15':
        live_react()  
    if choice == '16':
        live_comment()   
    if choice == '17':
        clear_text_files()
    if choice == '18':
        bitz()
    if choice == '19':
        mainzsa()
    if choice == '20':
        Pinterest()
    if choice == '21':
        remove_duplicates()
    if choice == '22':
        fetch_account_info(file_options)
    if choice == '23':
        check()
    if choice == '24': 
        githubtoks()
    if choice == '25':
        main2()
    if choice == '26':
        createfb()
    if choice == '27':
    	creatfile()
    else:
        print("INVALID CHOICE EXITING.")

if __name__ == "__main__":
       main()