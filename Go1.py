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
vua = "\033[1;31m\033[1m\033[1m[\033[1;37m\033[1m=.=\033[1;31m\033[1m\033[1m] \033[1;37m\033[1m=> \033[1;32m\033[1m"

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
    
    
#import lại sau khi cài đặt
from faker import Faker
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import requests

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
vua = "\033[1;31m\033[1m\033[1m[\033[1;37m\033[1m=.=\033[1;31m\033[1m\033[1m] \033[1;37m\033[1m=> \033[1;32m\033[1m"


import os, sys, time, math, random, colorsys
from colorama import init

init(autoreset=True)

# ─────────── CLEAR MÀN HÌNH ───────────
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# ─────────── HỆ MÀU CẦU VỒNG ───────────
def hsv2rgb(h, s, v):
    return colorsys.hsv_to_rgb(h, s, v)

def rgb_to_ansi(r, g, b):
    return 16 + (36 * round(r * 5)) + (6 * round(g * 5)) + round(b * 5)

def smooth_rainbow(length, offset=0, brightness=1.0, saturation=0.9, phase_offset=0):
    return [rgb_to_ansi(*hsv2rgb(((i + offset) / (length * 1.2) + phase_offset) % 1.0, saturation, brightness)) for i in range(length)]

# ─────────── ÁNH SÁNG QUÉT DÒNG LOGO ───────────
def gradient_line(text, colors, light_sweep_pos=None, glow_strength=1.0):
    result = ""
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        distance = abs(i - light_sweep_pos) if light_sweep_pos is not None else 1000
        if distance < 3:
            result += f"\033[1m\033[38;5;{color}m{char}\033[0m"
        else:
            result += f"\033[38;5;{color}m{char}"
    return result + "\033[0m"

# ─────────── HIỆU ỨNG NHỊP THỞ ───────────
def render_logo_wave(frame, intensity=1):
    output = ""
    pulse = 0.5 + 0.5 * math.sin(frame * 0.06)
    brightness = 0.85 + 0.15 * pulse
    saturation = 0.88 + 0.1 * pulse
    sweep_pos = int((math.sin(frame * 0.1) + 1) * (max_logo_length // 2))
    phase_offset = math.sin(frame * 0.03) * 0.2
    for i, line in enumerate(logo_lines):
        shift = frame + i * intensity
        colors = smooth_rainbow(len(line), shift, brightness, saturation, phase_offset)
        output += gradient_line(line, colors, light_sweep_pos=sweep_pos, glow_strength=1.2) + "\n"
    return output

# ─────────── HIỆN BANNER ANIMATION ───────────
def animated_banner(frames=40, delay=0.045):
    start_offset = random.randint(0, 100)
    for f in range(frames):
        clear()
        print(render_logo_wave(f + start_offset))
        time.sleep(delay)

# ─────────── LOGO TOOL ───────────

logo_lines = [
    "╔═══════════════════════════════════════════════════════════════╗",
    "║   ████████╗███╗   ███╗  ██╗  ███╗  ██╗██████╗ ██╗  ██╗  ██╗   ║",
    "║   ╚══██╔══╝████╗ ████║  ╚═╝  ████╗ ██║██╔══██╗██║ ██╔╝  ██║   ║",
    "║      ██║   ██╔████╔██║       ██╔██╗██║██║  ██║█████═╝   ██║   ║",
    "║      ██║   ██║╚██╔╝██║       ██║╚████║██║  ██║██╔═██╗   ╚═╝   ║",
    "║      ██║   ██║ ╚═╝ ██║  ██╗  ██║ ╚███║██████╔╝██║ ╚██╗  ██╗   ║",
    "║      ╚═╝   ╚═╝     ╚═╝  ╚═╝  ╚═╝  ╚══╝╚═════╝ ╚═╝  ╚═╝  ╚═╝   ║",
    "╚═══════════════════════════════════════════════════════════════╝"
]


# ─────────── KHỞI CHẠY ───────────
max_logo_length = max(len(line) for line in logo_lines)
animated_banner()


def reverse_string(s):
    return s[::-1]

def xePwjMDG(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))

def tLx6cpsx():
    url = 'https://api.mail.tm/domains'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['hydra:member']
        else:
            pass
            return None
    except Exception as e:
        print(f'{vua}{do}[×] Error: {e}')
        return None

def f9kSLNSXl():
    fake = Faker()
    mail_domains = tLx6cpsx()
    if mail_domains:
        domain = random.choice(mail_domains)['domain']
        username = xePwjMDG(10)
        password = fake.password()
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=45)
        first_name = fake.first_name()
        last_name = fake.last_name()
        url = 'https://api.mail.tm/accounts'
        headers = {'Content-Type': 'application/json'}
        data = {'address': f'{username}@{domain}', 'password': password}
        try:
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 201:
                print(f'{vua}{xanh_la}[NGUYENDANGKHOA] Email Created: {username}@{domain}')
                return (f'{username}@{domain}', password, first_name, last_name, birthday)
            else:
                pass
                return None, None, None, None, None
        except Exception as e:
            print(f'{vua}{do}[×] Error: {e}')
            return None, None, None, None, None
    return None, None, None, None, None

def QuanHau(email, password, first_name, last_name, birthday):
    api_key = '882a8490361da98702bf97a021ddc14d'
    secret = '62f8ce9f74b12f84c123cc23437a4a32'
    gender = random.choice(['M', 'F'])

    req = {
        'api_key': api_key,
        'attempt_login': True,
        'birthday': birthday.strftime('%Y-%m-%d'),
        'client_country_code': 'EN',
        'fb_api_caller_class': 'com.facebook.registration.protocol.RegisterAccountMethod',
        'fb_api_req_friendly_name': 'registerAccount',
        'firstname': first_name,
        'format': 'json',
        'gender': gender,
        'lastname': last_name,
        'email': email,
        'locale': 'en_US',
        'method': 'user.register',
        'password': password,
        'reg_instance': xePwjMDG(32),
        'return_multiple_errors': True
    }

    sorted_req = sorted(req.items(), key=lambda x: x[0])
    sig = ''.join(f'{k}={v}' for k, v in sorted_req)
    ensig = hashlib.md5((sig + secret).encode()).hexdigest()
    req['sig'] = ensig

    api_url = 'https://b-api.facebook.com/method/user.register'
    response = requests.post(api_url, data=req)

    if response.status_code == 200:
        reg = response.json()
        id = reg.get('new_user_id')
        token = reg.get('session_info', {}).get('access_token')
        print(
            f"""{vua}{xanh_la}[NGUYENDANGKHOA] Email: {email}
{vua}{xanh_la}[NGUYENDANGKHOA] Password: {password}
{vua}{xanh_la}[NGUYENDANGKHOA] Name: {first_name} {last_name}
{vua}{xanh_la}[NGUYENDANGKHOA] BirthDay: {birthday}
{vua}{xanh_la}[NGUYENDANGKHOA] Gender: {gender}
==================================="""
        )
    else:
        print(f'{vua}{do}[×] Registration Error: {response.text}')

def WcfriFTc(url, params, post=True):
    headers = {
        'User-Agent': '[FBAN/FB4A;FBAV/35.0.0.48.273;FBDM/{density=1.33125,width=800,height=1205};FBLC/en_US;FBCR/;FBPN/com.facebook.katana;FBDV/Nexus 7;FBSV/4.1.1;FBBK/0;]'
    }
    if post:
        response = requests.post(url, data=params, headers=headers)
    else:
        response = requests.get(url, params=params, headers=headers)
    return response.json()

def create_accounts(num_accounts):
    for i in range(num_accounts):
        email, password, first_name, last_name, birthday = f9kSLNSXl()
        if email and password and first_name and last_name and birthday:
            QuanHau(email, password, first_name, last_name, birthday)

# Sử dụng: gọi hàm create_accounts với số lượng tài khoản cần tạo
num_accounts = int(input(f'{vua}[NGUYENDANGKHOA] Muốn bao nhiêu tài khoản: {vang}'))
create_accounts(num_accounts)