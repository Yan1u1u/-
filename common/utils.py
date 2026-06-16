
import random
import time
import requests
from fake_useragent import UserAgent

def create_session(proxy=None):
    """创建统一配置的session"""
    session = requests.Session()
    session.headers.update({
        'User-Agent': UserAgent().random,
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
    })
    if proxy:
        session.proxies = {'http': proxy, 'https': proxy}
    return session

def random_sleep(min_sec=1, max_sec=3):
    """随机延时防反爬"""
    time.sleep(random.uniform(min_sec, max_sec))

def clean_html(raw_html: str) -> str:
    """去除HTML标签"""
    import re
    text = re.sub(r'<[^>]+>', '', raw_html)
    text = re.sub(r'https?://\S+', '', text)  # 去URL
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# 关键词列表（两人共用）
KEYWORDS=[
'考研',
'二战考研',
'考公',
'国考',
'省考',
'就业',
'秋招',
'春招',
'校招',
'实习',
'找工作',
'offer',
'失业',
'裁员',
'毕业即失业',
'应届生',
'研究生',
'985废物',
'考研还是就业',
'就业形势'
]
