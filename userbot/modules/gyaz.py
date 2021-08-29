# SİRİUSERBOT - BERCESTE

import re
import os
from telethon import events
from userbot import bot
from userbot.events import register
from userbot.cmdhelp import CmdHelp

@register(pattern="^.gyaz ?(.*)")
async def gyazz(event):
 
    p = event.pattern_match.group(1)
    m = p.split(" ")

    chat_id = m[0]
    try:  
        chat_id = int(chat_id)
    except BaseException:
        pass
  
    msg = ""
    mssg = await event.get_reply_message() 
    if event.reply_to_msg_id:
        await event.client.send_message(chat_id, mssg)
        await event.edit("@SiriOT `Mesajınızı gönderdi ✅`")
    for i in m[1:]:
        msg += i + " "
    if msg == "":
        return
    try:
        await event.client.send_message(chat_id, msg)
        await event.edit("@SiriOT `Mesajınızı gönderdi ✅`")
    except BaseException:
        await event.edit("**@SiriOT Mesajınızı Gönderemedi Belirttiğin Grupta Olduğuna Eminmisin Sahip ? **")
        
CmdHelp('gyaz').add_command(
    'gyaz', ' <gruplinki> <mesajınız>', 'İstediğiniz Gruba Uzaktan Mesaj Göndermeye Yarar. '
).add()
