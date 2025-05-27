#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K | Modifieded By : @DC4_WARRIOR



import ntplib
import time
import os

# টাইমজোন UTC করে দাও
os.environ['TZ'] = 'UTC'
time.tzset()

try:
    ntp_client = ntplib.NTPClient()
    response = ntp_client.request('pool.ntp.org')
    ntp_time = response.tx_time
    local_time = time.time()
    time_diff = abs(local_time - ntp_time)

    if time_diff > 5:
        print(f"সার্ভারের সময় {time_diff:.2f} সেকেন্ড পিছিয়ে। Telegram কাজ করবে না।")
        exit("সময় সিঙ্ক করানো যায়নি।")

except Exception as e:
    print("NTP দিয়ে সময় আনা যায়নি:", e)
    exit("সমস্যা হয়েছে সময় সিঙ্ক করতে।")






import os
import logging
from config import Config
from pyrogram import Client as Clinton
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(root="plugins")
    Warrior = Clinton("@BOT_X_BOT",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    plugins=plugins)
    Warrior.run()
