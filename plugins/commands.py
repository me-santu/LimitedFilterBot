import os
import requests
import logging
import random
import asyncio
import string
import pytz
from datetime import datetime as dt
from Script import script
from pyrogram import Client, filters, enums
from pyrogram.errors import ChatAdminRequired
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
)
from database.ia_filterdb import (
    Media,
    get_file_details,
    get_bad_files,
    unpack_new_file_id,
)
from database.users_chats_db import db
from database.config_db import mdb
from database.topdb import JsTopDB
from database.jsreferdb import referdb
from plugins.pm_filter import auto_filter
from utils import (
    formate_file_name,
    get_settings,
    save_group_settings,
    is_req_subscribed,
    is_subscribed,
    get_size,
    get_shortlink,
    is_check_admin,
    get_status,
    temp,
    get_readable_time,
    save_default_settings,
)
import re
import base64
from info import *

logger = logging.getLogger(__name__)
movie_series_db = JsTopDB(DATABASE_URI)
verification_ids = {}


@Client.on_message(filters.command("start") & filters.incoming)
async def start(client: Client, message):
    await message.react(emoji=random.choice(REACTIONS))
    m = message
    user_id = m.from_user.id
    # [start command full original code ... unchanged]
    # Keep your existing logic here
    # ---------------
    # no change above this line


# ====== 3 Shortener Verification ON/OFF Commands ======
from pyrogram import Client, filters
from info import VERIFY_01, VERIFY_02, VERIFY_03, ADMINS

@Client.on_message(filters.command("verify_on_01") & filters.user(ADMINS))
async def verify_on_01(_, message):
    global VERIFY_01
    VERIFY_01 = True
    await message.reply("✅ Shortener 01 Enabled")

@Client.on_message(filters.command("verify_off_01") & filters.user(ADMINS))
async def verify_off_01(_, message):
    global VERIFY_01
    VERIFY_01 = False
    await message.reply("❌ Shortener 01 Disabled")

@Client.on_message(filters.command("verify_on_02") & filters.user(ADMINS))
async def verify_on_02(_, message):
    global VERIFY_02
    VERIFY_02 = True
    await message.reply("✅ Shortener 02 Enabled")

@Client.on_message(filters.command("verify_off_02") & filters.user(ADMINS))
async def verify_off_02(_, message):
    global VERIFY_02
    VERIFY_02 = False
    await message.reply("❌ Shortener 02 Disabled")

@Client.on_message(filters.command("verify_on_03") & filters.user(ADMINS))
async def verify_on_03(_, message):
    global VERIFY_03
    VERIFY_03 = True
    await message.reply("✅ Shortener 03 Enabled")

@Client.on_message(filters.command("verify_off_03") & filters.user(ADMINS))
async def verify_off_03(_, message):
    global VERIFY_03
    VERIFY_03 = False
    await message.reply("❌ Shortener 03 Disabled")
