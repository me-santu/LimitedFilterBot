# Powered by ZISHAN KHAN & SANTU GHOSH 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests
from info import (
    VERIFY_01, VERIFY_02, VERIFY_03,
    SHORTENER_API, SHORTENER_WEBSITE,
    SHORTENER_API2, SHORTENER_WEBSITE2,
    SHORTENER_API3, SHORTENER_WEBSITE3
)

# === Shortener Functions ===
def shortener_1(url):
    if not SHORTENER_API or not SHORTENER_WEBSITE:
        return url
    try:
        res = requests.get(
            f"https://{SHORTENER_WEBSITE}/api",
            params={"api": SHORTENER_API, "url": url},
            timeout=10
        ).json()
        return res.get("shortenedUrl", url)
    except:
        return url

def shortener_2(url):
    if not SHORTENER_API2 or not SHORTENER_WEBSITE2:
        return url
    try:
        res = requests.get(
            f"https://{SHORTENER_WEBSITE2}/api",
            params={"api": SHORTENER_API2, "url": url},
            timeout=10
        ).json()
        return res.get("shortenedUrl", url)
    except:
        return url

def shortener_3(url):
    if not SHORTENER_API3 or not SHORTENER_WEBSITE3:
        return url
    try:
        res = requests.get(
            f"https://{SHORTENER_WEBSITE3}/api",
            params={"api": SHORTENER_API3, "url": url},
            timeout=10
        ).json()
        return res.get("shortenedUrl", url)
    except:
        return url

# === Apply Shorteners Based on ON/OFF ===
def apply_shorteners(file_url):
    final_link = file_url
    if VERIFY_01:
        final_link = shortener_1(final_link)
    if VERIFY_02:
        final_link = shortener_2(final_link)
    if VERIFY_03:
        final_link = shortener_3(final_link)
    return final_link


@Client.on_message(filters.command("link"))
async def generate_link(client, message):
    command_text = message.text.split(maxsplit=1)
    if len(command_text) < 2:
        await message.reply(
            "Please provide the name for the movie! Example: `/link game of thrones`"
        )
        return
    movie_name = command_text[1].replace(" ", "-")
    file_url = f"https://telegram.me/NehaTestBot?start=getfile-{movie_name}"

    # ✅ Apply shorteners dynamically based on ON/OFF
    link = apply_shorteners(file_url)

    await message.reply(
        text=f"Here is your link: {link}",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Share Link",
                        url=f"https://telegram.me/share/url?url={link}",
                    )
                ]
            ]
        ),
    )
