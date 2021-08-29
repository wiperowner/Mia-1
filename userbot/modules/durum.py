# Copyright (C) 2020 Yusuf Usta.
#
# Licensed under the GPL-3.0 License;
# you may not use this file except in compliance with the License.
#

# SiriUserBot - ErdemBey - Midy

from userbot import CMD_HELP, ASYNC_POOL, tgbot, SPOTIFY_DC, G_DRIVE_CLIENT_ID, lastfm, YOUTUBE_API_KEY, OPEN_WEATHER_MAP_APPID, AUTO_PP, REM_BG_API_KEY, OCR_SPACE_API_KEY, PM_AUTO_BAN, ASISTAN, MYID, BOTLOG_CHATID, SIRI_VERSION
from userbot.events import register
from telethon import version
from platform import python_version
from userbot.cmdhelp import CmdHelp

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("durum")

# ████████████████████████████████ #

def durum(s):
    if s == None:
        return "❌"
    else:
        if s == False:
            return "❌"
        else:
            return "✅"

@register(outgoing=True, pattern="^.durum|^.status")
async def durums(event):

    await event.edit(f"""
**Python {LANG['VERSION']}:** `{python_version()}`
**TeleThon {LANG['VERSION']}:** `{version.__version__}` 
**Siri {LANG['VERSION']}:** `{SIRI_VERSION}`

**{LANG['PLUGIN_COUNT']}:** `{len(CMD_HELP)}`

**Inline Bot:** `{durum(tgbot)}`
**Spotify:** `{durum(SPOTIFY_DC)}`
**GDrive:** `{durum(G_DRIVE_CLIENT_ID)}`
**LastFm:** `{durum(lastfm)}`
**YouTube ApiKey:** `{durum(YOUTUBE_API_KEY)}`
**OpenWeather:** `{durum(OPEN_WEATHER_MAP_APPID)}`
**AutoPP:** `{durum(AUTO_PP)}`
**RemoveBG:** `{durum(REM_BG_API_KEY)}`
**OcrSpace:** `{durum(OCR_SPACE_API_KEY)}`
**Pm AutoBan:** `{durum(PM_AUTO_BAN)}`
**BotLog:** `{durum(BOTLOG_CHATID)}`
**Plugin:** `{LANG['PERMAMENT']}`

**{LANG['OK']} ✅**
    """)

@register(incoming=True, from_users=ASISTAN, pattern="^.durum$")
async def asistandurum(ups):
    """ .durum komutunu asistana söylerseniz sizin yerinize botun durumuna bakar. """
    if ups.is_reply:
        reply = await ups.get_reply_message()
        reply_user = await ups.client.get_entity(reply.from_id)
        ren = reply_user.id
        if ren == MYID:
            await ups.reply(f"""
**Python {LANG['VERSION']}:** `{python_version()}`
**TeleThon {LANG['VERSION']}:** `{version.__version__}` 
**Siri {LANG['VERSION']}:** `{SIRI_VERSION}`

**{LANG['PLUGIN_COUNT']}:** `{len(CMD_HELP)}`

**Inline Bot:** `{durum(tgbot)}`
**Spotify:** `{durum(SPOTIFY_DC)}`
**GDrive:** `{durum(G_DRIVE_CLIENT_ID)}`
**LastFm:** `{durum(lastfm)}`
**YouTube ApiKey:** `{durum(YOUTUBE_API_KEY)}`
**OpenWeather:** `{durum(OPEN_WEATHER_MAP_APPID)}`
**AutoPP:** `{durum(AUTO_PP)}`
**RemoveBG:** `{durum(REM_BG_API_KEY)}`
**OcrSpace:** `{durum(OCR_SPACE_API_KEY)}`
**Pm AutoBan:** `{durum(PM_AUTO_BAN)}`
**BotLog:** `{durum(BOTLOG_CHATID)}`
**Plugin:** `{LANG['PERMAMENT']}`

**{LANG['OK']} ✅**
            """)
        else:
            return



CmdHelp('durum').add_command(
    'durum', None, 'Eklenen Apiler ve sürümleri gösterir.'
).add()
