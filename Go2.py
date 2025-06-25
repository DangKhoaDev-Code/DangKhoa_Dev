#Coded by Traodoisub.com
import os
import datetime
from datetime import datetime
import requests,json
import uuid
from time import sleep

today = datetime.today()
ngay = today.day
thang = today.day
os.environ['TZ'] = 'Asia/Ho_Chi_Minh'

try:
	import requests
except:
	os.system("pip3 install requests")
	import requests

try:
	from pystyle import Colors, Colorate, Write, Center, Add, Box
except:
	os.system("pip3 install pystyle")
	from pystyle import Colors, Colorate, Write, Center, Add, Box

headers = {
	'authority': 'traodoisub.com',
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
	'user-agent': 'traodoisub tiktok tool',
}
class ApiPro5:
	
    def __init__(self, cookies,fb_dtsg,jazoet,id_page) -> None:
        self.headers = {
                'authority': 'www.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-language': 'vi',
                'cookie': cookies,
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
        url_profile = requests.get('https://www.facebook.com/me', headers=self.headers).url
        profile = requests.get(url_profile, headers=self.headers).text
        self.fb_dtsg = fb_dtsg
        self.jazoet = jazoet
        self.user_id = id_page
    def join(self, group_id):
        data = {
            'fb_dtsg': self.fb_dtsg,
            'jazoest': self.jazoet,
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'GroupCometJoinForumMutation',
            'variables': '{"feedType":"DISCUSSION","groupID":"'+group_id+'","imageMediaType":"image/x-auto","input":{"action_source":"GROUPS_ENGAGE_TAB","attribution_id_v2":"GroupsCometCrossGroupFeedRoot.react,comet.groups.feed,tap_tabbar,1667116100089,433821,2361831622,","group_id":"'+group_id+'","group_share_tracking_params":null,"actor_id":"'+self.user_id+'","client_mutation_id":"2"},"inviteShortLinkKey":null,"isChainingRecommendationUnit":false,"isEntityMenu":false,"scale":1,"source":"GROUPS_ENGAGE_TAB","renderLocation":"group_mall","__relay_internal__pv__GlobalPanelEnabledrelayprovider":false,"__relay_internal__pv__GroupsCometEntityMenuEmbeddedrelayprovider":true}',
            'server_timestamps': 'true',
            'doc_id': '5915153095183264',
        }

        response = requests.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data).text
        return response 
    def subscribe(self, uid):
        data = {
            'fb_dtsg': self.fb_dtsg,
            'jazoest': self.jazoet,
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'CometUserFollowMutation',
            'variables': '{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1667114418950,431532,190055527696468,","subscribe_location":"PROFILE","subscribee_id":"'+uid+'","actor_id":"'+self.user_id+'","client_mutation_id":"1"},"scale":1}',
            'server_timestamps': 'true',
            'doc_id': '5032256523527306',
        }
        subscribe = requests.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data).text
        return subscribe
    def reaction(self, id_post, reaction):
        try:
            url = requests.get('https://www.facebook.com/'+id_post, headers=self.headers).url
            home = requests.get(url, headers=self.headers).text
            feedback_id = home.split('{"__typename":"CommentComposerLiveTypingBroadcastPlugin","feedback_id":"')[1].split('","')[0]
            data = {
                'fb_dtsg': self.fb_dtsg,
                'jazoest': self.jazoet,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'CometUFIFeedbackReactMutation',
                'variables': '{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1667106623951,429237,190055527696468,","feedback_id":"'+feedback_id+'","feedback_reaction_id":"'+reaction+'","feedback_source":"PROFILE","is_tracking_encrypted":true,"tracking":["AZXg8_yM_zhwrTY7oSTw1K93G-sycXrSreRnRk66aBJ9mWkbSuyIgNqL0zHEY_XgxepV1XWYkuv2C5PuM14WXUB9NGsSO8pPe8qDZbqCw5FLQlsGTnh5w9IyC_JmDiRKOVh4gWEJKaTdTOYlGT7k5vUcSrvUk7lJ-DXs3YZsw994NV2tRrv_zq1SuYfVKqDboaAFSD0a9FKPiFbJLSfhJbi6ti2CaCYLBWc_UgRsK1iRcLTZQhV3QLYfYOLxcKw4s2b1GeSr-JWpxu1acVX_G8d_lGbvkYimd3_kdh1waZzVW333356_JAEiUMU_nmg7gd7RxDv72EkiAxPM6BA-ClqDcJ_krJ_Cg-qdhGiPa_oFTkGMzSh8VnMaeMPmLh6lULnJwvpJL_4E3PBTHk3tIcMXbSPo05m4q_Xn9ijOuB5-KB5_9ftPLc3RS3C24_7Z2bg4DfhaM4fHYC1sg3oFFsRfPVf-0k27EDJM0HZ5tszMHQ"],"session_id":"'+str(uuid.uuid4())+'","actor_id":"'+self.user_id+'","client_mutation_id":"1"},"useDefaultActor":false,"scale":1}',
                'server_timestamps': 'true',
                'doc_id': '5703418209680126',
            }

            reaction = requests.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data).text
            return {'status': True, 'url': url}
        except:
            return {'status': False, 'url': url}
    
def get_page(cookie):
    headers = {
        'authority': 'mbasic.facebook.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'vi,en;q=0.9,vi-VN;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5',
        'cache-control': 'max-age=0',
        'cookie': cookie,
        'origin': 'https://www.facebook.com',
        'referer': 'https://www.facebook.com',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }
    response = requests.get('https://mbasic.facebook.com/',headers=headers).text
    fb_dtsg = response.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
    jazoest = response.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
    idpef = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data={'fb_dtsg': fb_dtsg,'jazoest': jazoest,'variables': '{"showUpdatedLaunchpointRedesign":true,"useAdminedPagesForActingAccount":false,"useNewPagesYouManage":true}','doc_id': '5300338636681652'}).json()
    a = idpef['data']['viewer']['actor']['profile_switcher_eligible_profiles']['nodes']
    sl = 0
    for b in a:
        sl +=1
        uid = b['profile']['id']
        name = b['profile']['name']
        delegate_page_id = b['profile']['delegate_page_id']
        print (f"\033[1;37mPAGE : {sl} | ID : {uid} | Name : {name} ")
        print ('\033[1;31m────────────────────────────────────────────────────────────')
    return a
def get_data(cookie):
    headers = {
        'authority': 'mbasic.facebook.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': cookie,
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }

    response = requests.get('https://mbasic.facebook.com/',headers=headers).text
    fb_dtsg = response.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
    jazoet = response.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
    return json.dumps({'fb_dtsg':fb_dtsg,'jazoet':jazoet})

def login_tds(token):
	try:
		r = requests.get('https://traodoisub.com/api/?fields=profile&access_token='+token, headers=headers, timeout=5).json()
		if 'success' in r:
			return r
		else:
			print(" \033[1;31m Token TDS không hợp lệ, hãy kiểm tra lại!\n")
			return 'error_token'
	except:
		return 'error'

def load_job(type, TDS_token):
		r = requests.get(f'https://traodoisub.com/api/?fields={type}&access_token={TDS_token}')


def type_cx(type_1) :
	if type_1 == "LOVE" :
		type_2 = '1678524932434102'
	elif type_1 == "CARE" :
		type_2 = '613557422527858'
	elif type_1 == "WOW" :
		type_2 = '478547315650144'
	elif type_1 == "HAHA" :
		type_2 = '115940658764963'
	elif type_1 == "SAD" :
		type_2 = '908563459236466'
	elif type_1 == "ANGRY" :
		type_2 = '444813342392137'
		
	return type_2
def cau_hinh(id, TDS_token, name):
	urlch = f"https://traodoisub.com/api/?fields=run&id={id}&access_token={TDS_token}'"
	ch = requests.get( url=urlch)
	try: 
		checkch = ch.json()["data"]["msg"]
		print(f" \033[1;32mCấu Hình \033[1;37m| \033[1;33mID : \033[1;32m{id} \033[1;37m| \033[1;32mName : \033[1;33m{name} ")
	except:
		print(f" \033[1;31m Cấu Hình Thất Bại {id} ")
		exit ()

import requests
import random
import string
import hashlib,os

trang = "\033[1;37m\033[1m"
xanh_la = "\033[1;32m\033[1m"
xanh_duong = "\033[1;34m\033[1m"
xanhnhat = '\033[1m\033[38;5;51m'
do = "\033[1;31m\033[1m\033[1m"
xam = '\033[1;30m\033[1m'
vang = "\033[1;33m\033[1m"
tim = "\033[1;35m\033[1m"
hongnhat = "#FFC0CB"
kt_code = "</>"
dac_biet = "\033[32;5;245m\033[1m\033[38;5;39m"
vua = "\033[1;37m[>_<]\033[1;37m \033[1;37mNGUYENDANGKHOA\033[1;37m \033[1;37m=> \033[1;34m\033[1m"

import os
try:
    from faker import Faker
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad
    import requests
except ImportError:
    os.system('pip install Faker')
    os.system('pip install requests')
    os.system('pip install pycryptodome')

trang = "\033[1;37m\033[1m"
xanh_la = "\033[1;32m\033[1m"
xanh_duong = "\033[1;34m\033[1m"
xanhnhat = '\033[1m\033[38;5;51m'
do = "\033[1;31m\033[1m\033[1m"
xam='\033[1;30m\033[1m'
vang = "\033[1;33m\033[1m"
tim = "\033[1;35m\033[1m"
hongnhat = "#FFC0CB"
kt_code = "</>"
dac_biet = "\033[32;5;245m\033[1m\033[38;5;39m"
vua = "\033[1;37m[>_<]\033[1;37m \033[1;37mNGUYENDANGKHOA\033[1;37m \033[1;37m=> \033[1;34m\033[1m"


import os, json, sys, requests 
from sys import platform
from time import sleep
from datetime import datetime
from random import randint
from pystyle import Colors, Colorate
import uuid, re
from bs4 import BeautifulSoup
import os, sys, time, math, random, colorsys

# ────────── KÍCH HOẠT ANSI (Windows) ──────────
if os.name == "nt":
    import ctypes
    kernel32 = ctypes.windll.kernel32
    ENABLE_VT = 0x0004
    handle = kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE = -11
    mode = ctypes.c_ulong()
    if kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
        kernel32.SetConsoleMode(handle, mode.value | ENABLE_VT)

# ────────── HÀM TIỆN ÍCH ──────────
def hsv2rgb(h, s, v): return colorsys.hsv_to_rgb(h, s, v)

def rgb_to_ansi(r, g, b):
    return 16 + (36 * round(r * 5)) + (6 * round(g * 5)) + round(b * 5)

def pastel_rainbow(length, offset=0, bright=0.95, sat=0.42, phase=0):
    return [
        rgb_to_ansi(*hsv2rgb(((i + offset) / (length * 1.2) + phase) % 1, sat, bright))
        for i in range(length)
    ]

def gradient_line(text, colors, sweep=None):
    out = []
    for i, ch in enumerate(text):
        c = colors[i % len(colors)]
        if sweep is not None and abs(i - sweep) < 3:
            out.append(f"\033[1m\033[38;5;{c}m{ch}\033[0m")
        else:
            out.append(f"\033[38;5;{c}m{ch}")
    return "".join(out) + "\033[0m"

def render_frame(f):
    pulse = 0.5 + 0.5 * math.sin(f * 0.03)
    bright = 0.9 + 0.1 * pulse
    sat    = 0.38 + 0.08 * pulse
    sweep  = int((math.sin(f * 0.05) + 1) * max_len // 2)
    phase  = math.sin(f * 0.025) * .25

    lines = []
    for idx, raw in enumerate(logo):
        shift = f + idx * .6
        colors = pastel_rainbow(len(raw), shift, bright, sat, phase)
        lines.append(gradient_line(raw, colors, sweep))
    return lines

def center_text(text, width):
    return text.center(width)

# ────────── LOGO ASCII ──────────
logo = [
    "╔═══════════════════════════════════════════════════════════════╗",
    "║   ████████╗███╗   ███╗  ██╗  ███╗  ██╗██████╗ ██╗  ██╗  ██╗   ║",
    "║   ╚══██╔══╝████╗ ████║  ╚═╝  ████╗ ██║██╔══██╗██║ ██╔╝  ██║   ║",
    "║      ██║   ██╔████╔██║       ██╔██╗██║██║  ██║█████═╝   ██║   ║",
    "║      ██║   ██║╚██╔╝██║       ██║╚████║██║  ██║██╔═██╗   ╚═╝   ║",
    "║      ██║   ██║ ╚═╝ ██║  ██╗  ██║ ╚███║██████╔╝██║ ╚██╗  ██╗   ║",
    "║      ╚═╝   ╚═╝     ╚═╝  ╚═╝  ╚═╝  ╚══╝╚═════╝ ╚═╝  ╚═╝  ╚═╝   ║",
    "╚═══════════════════════════════════════════════════════════════╝"
]
max_len   = max(len(l) for l in logo)
logo_h    = len(logo)
duration  = 3          # giây chạy
delay     = 0.06
frames    = int(duration / delay)
offset    = random.randint(0, 3)

# ────────── BANNER SETUP ──────────
banner_width = max_len + 4
title = "[>_<] NGUYENDANGKHOA /// DANGKHOA_DEV"
footer = "YOUTOBE SHARE TOOL :  https://www.youtube.com/channel/UCGJmaIZ_JbAwoOrHeBZru6A"
start_message = "NHÓM ZALO : https://zalo.me/g/wyboil196"
end_message = """ 
[>_<] NGUYENDANGKHOA                          source by DangKhoa_Dev
______________________________________________________________________
NHÓM ZALO : https://zalo.me/g/wyboil196 
______________________________________________________________________
SHARE TOOL :  https://www.youtube.com/channel/UCGJmaIZ_JbAwoOrHeBZru6A
______________________________________________________________________
"""
# ────────── IN BANNER ──────────
# Clear screen
print("\033[2J\033[H", end="")

# Print title
title_colors = pastel_rainbow(len(title), offset)
print(center_text(gradient_line(title, title_colors), banner_width))

# Print top border
border = "═" * (banner_width - 2)
print(f"╔{border}╗")

# Print initial logo
first = render_frame(offset)
for line in first:
    print(f"║ {line.ljust(max_len)} ║")

# Print bottom border
print(f"╚{border}╝")

# Print start message
start_colors = pastel_rainbow(len(start_message), offset)
print(center_text(gradient_line(start_message, start_colors), banner_width), flush=True)

# ────────── VÒNG LẶP ANIMATION ──────────
for f in range(1, frames):
    time.sleep(delay)
    # Move cursor to start of logo
    sys.stdout.write(f"\033[{logo_h + 2}F")
    # Print top border
    sys.stdout.write(f"╔{border}╗\n")
    # Print animated logo
    for line in render_frame(f + offset):
        sys.stdout.write(f"║ {line.ljust(max_len)} ║\n")
    # Print bottom border
    sys.stdout.write(f"╚{border}╝\n")
    sys.stdout.flush()

# ────────── KẾT THÚC BANNER & CHUYỂN SANG API ──────────
time.sleep(delay)
# Clear below logo
sys.stdout.write(f"\033[{logo_h + 2}F\033[J")
# Reprint title
print(center_text(gradient_line(title, title_colors), banner_width))
# Reprint top border
print(f"╔{border}╗")
# Print final frame
for line in render_frame(frames + offset):
    print(f"║ {line.ljust(max_len)} ║")
# Reprint bottom border
print(f"╚{border}╝")
# Print transition message
end_colors = pastel_rainbow(len(end_message), offset)
print(center_text(gradient_line(end_message, end_colors), banner_width))
import sys
from time import sleep
def banner():
    top_banner = "\033[1;37m[>_<] NGUYENDANGKHOA /// DANGKHOA_DEV...\033[0m\n"
    bottom_banner = (
        "\033[1;33m╔═══════════════════════════════════════════════════════════════════╗\033[0m\n"
        "\033[1;33m║                           TOOL TDS PRO5                           ║\033[0m\n"
        "\033[1;33m╚═══════════════════════════════════════════════════════════════════╝\033[0m\n"
    )
    for char in top_banner + bottom_banner:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.001)

def chon_job(so,chon):
	if chon == 1 :
		if so == 4 :
			so -= 4 
		else :
			type = ['like','likegiare','likesieure','reaction']
			job = type[so]
	elif chon == 2 :
		job = "group"
	elif chon == 3 :
		job = "follow"
	elif chon == 4:
		if so == 5 :
			so -= 5 
		else :
			type = ['like','likegiare','likesieure','reaction','group']
			job = type[so]
	else :
		if so == 6 :
			so -= 6 
		else :
			type = ['like','likegiare','likesieure','reaction','group','follow']
			
			job = type[so]
	return job


so = 0
token = input('\033[1;37m \033[1;37m[>_<]\033[1;37m \033[1;37mNGUYENDANGKHOA\033[1;37m \033[1;37m=> \033[1;32mNhập Token TDS :\033[1;33m ')
check_xu = login_tds(token)
print ('\033[1;31m────────────────────────────────────────────────────────────')
cookie = input('\033[1;37m \033[1;37m[>_<]\033[1;37m \033[1;37mNGUYENDANGKHOA\033[1;37m \033[1;37m=> \033[1;32mNhập Cookie Facebook :\033[1;33m ')
print ('\033[1;31m────────────────────────────────────────────────────────────')
#### vào việc
get_tt_page = get_page(cookie)
a = int(input('\033[1;37m \033[1;37m[>_<]\033[1;37m \033[1;37mNGUYENDANGKHOA\033[1;37m \033[1;37m=> \033[1;32mBạn Muốn Chạy Page Thứ Mấy : \033[1;33m'))
chon = a-1
print ('\033[1;31m────────────────────────────────────────────────────────────')
print ("\033[1;37m[>_<]\033[1;37m \033[1;37mNGUYENDANGKHOA\033[1;37m \033[1;37m=> \033[1;32mNhập 1 \033[1;37mJob Like + Cảm Xúc")
print ("\033[1;37m[>_<]\033[1;37m \033[1;37mNGUYENDANGKHOA\033[1;37m \033[1;37m=> \033[1;32mNhập 2 \033[1;37mJob Group")
print ("\033[1;37m[>_<]\033[1;37m \033[1;37mNGUYENDANGKHOA\033[1;37m \033[1;37m=> \033[1;32mNhập 3 \033[1;37mJob Follow ")
print ("\033[1;37m[>_<]\033[1;37m \033[1;37mNGUYENDANGKHOA\033[1;37m \033[1;37m=> \033[1;32mNhập 4 \033[1;37mJob Group + Like + Cảm Xúc")
print ("\033[1;37m[>_<]\033[1;37m \033[1;37mNGUYENDANGKHOA\033[1;37m \033[1;37m=> \033[1;32mNhập 5 \033[1;37mJob Group + Like + Cảm Xúc + Follow ")
chon_1 = int(input('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập : \033[1;33m '))
print ('\033[1;31m────────────────────────────────────────────────────────────')
dl = int(input('\033[1;37m \033[1;37m[>_<]\033[1;37m \033[1;37mNGUYENDANGKHOA\033[1;37m \033[1;37m=> \033[1;32mNhập Delay : \033[1;33m '))

id_page = get_tt_page[chon]['profile']['id']
name = get_tt_page[chon]['profile']['name']
ck_pro5 = 'sb={}; datr={}; c_user={}; wd={}; xs={}; fr={}; i_user={};'.format(cookie.split('sb=')[1].split(';')[0], cookie.split('datr=')[1].split(';')[0], cookie.split('c_user=')[1].split(';')[0],cookie.split('wd=')[1].split(';')[0], cookie.split('xs=')[1].split(';')[0],cookie.split('fr=')[1].split(';')[0],id_page)
data = get_data(cookie)
fb_dtsg = json.loads(data)['fb_dtsg']
jazoet = json.loads(data)['jazoet']
fb = ApiPro5(cookies=ck_pro5, fb_dtsg=fb_dtsg, jazoet=jazoet,id_page=id_page)
tt = 0

os.system('clear')
print(banner)
tdstk = check_xu['data']['user']
xu_5 = check_xu['data']['xu']
print (f"\033[1;37m \033[1;37m[>_<]\033[1;37m \033[1;37mNGUYENDANGKHOA\033[1;37m \033[1;37m=> \033[1;32mTài Khoản: \033[1;33m{tdstk} \n\033[1;37m[>_<]\033[1;37m \033[1;37mNGUYENDANGKHOA\033[1;37m \033[1;37m=>  \033[1;32mXu Hiện Tại : \033[1;33m{xu_5} ")

print ('\033[1;31m────────────────────────────────────────────────────────────')
cau_hinh(id_page, token, name)
print ('\033[1;31m────────────────────────────────────────────────────────────')
while True :
	print(" Đang Tìm Job ",end="\r")
	if so == 5 :
		so -= 5
	else :
		
		job = chon_job(so,chon_1)
		print(f" \033[1;37mĐang Tìm Job ☞ (⁠>{job}<⁠)       ",end="\r")
		job_1 = requests.get(f'https://traodoisub.com/api/?fields={job}&access_token={token}')
		so += 1
		
		a = job_1.json()
		try :
			b = a["error"] 
			
			if chon_1 == 1 :
				if so == 4 :
					for i in range(20,-1,-1):
						print(f'\033[1;37m[TÌM JOB SAU] => {i} GIÂY   ',end='\r')
						sleep(1)
			elif chon_1 == 2 :
				for i in range(50,-1,-1):
					print(f'\033[1;37m[TÌM JOB SAU] => {i} GIÂY    ',end='\r')
					sleep(1)
			else :
				if so == 5 :
					for i in range(20,-1,-1):
						print(f'\033[1;37m[TÌM JOB SAU] => {i} GIÂY    ',end='\r')
						sleep(1)
		except :
			for job_2 in a:
				id_job = job_2["id"]
				if job == "like" :
					type_1 = "LIKE"
					type_2 = '1635855486666999'
					lam = fb.reaction(id_job, type_2)
				elif job == "likegiare" :
					type_1 = "LIKEGIARE"
					type_2 = '1635855486666999'
					lam = fb.reaction(id_job, type_2)
				elif job == "likesieure" :
					type_1 = "LIKESIEURE"
					type_2 = '1635855486666999'
					lam = fb.reaction(id_job, type_2)
				elif job == "reaction" :
					type_1 = job_2["type"]
					type_2 = type_cx(type_1) 
					lam = fb.reaction(id_job, type_2)
				elif job == "group" :
					type_1 = "GROUP"
					lam = fb.join(id_job)
				elif job == "follow" :
					type_1 = "FOLLOW"
					lam = fb.subscribe(id_job)
					
				nhan = requests.get(f'https://traodoisub.com/api/coin/?type={type_1}&id={id_job}&access_token={token}')
				
				try :
					nhan_1 = nhan.json()["error"] 
					print (f' \033[1;31m ERROR => {id_job} ',end='\r')
					sleep(1)
				except :
					tt += 1
					gio = datetime.now().strftime("%H:%M:%S")
					xu_1 = nhan.json()["data"]["msg"]
					xu_2 = nhan.json()["data"]["xu"]
					print (f"\033[1;37m| {tt} | {type_1} | {id_job} | {xu_1} | {xu_2} Xu")
					
				
				for i in range(dl,-1,-1):
					print(f'\033[1;37m[ ĐANG DELAY CHẠY LẠI SAU ] => \033[1;36m {i} GIÂY',end='\r')
					sleep(1)
					
					
					
