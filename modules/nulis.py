# Ayra - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Ayra/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Ayra/blob/main/LICENSE/>.
"""
✘ **Bantuan Untuk Nulis**

๏ **Perintah:** `nulis` <berikan pesan/balas pesan>
◉ **Keterangan:** Buat kamu yg males nulis.
"""

from telethon.errors import ChatSendMediaForbiddenError
import requests
from . import *

@ayra_cmd(pattern=r"(N|n)ulis( (.*)|$)")
async def handwrite(event):
    message = event.message
    text = message.reply_to_message.text if message.reply_to_message else event.pattern_match.group(1)
    m = await message.reply("`Processing...`")
    req = requests.get(f"https://api.sdbots.tk/write?text={text}").url
    try:
        await event.send_file(message.chat_id, req, caption=f"Ditulis Oleh: {OWNER_NAME}")
    except ChatSendMediaForbiddenError:
        await m.edit("Dilarang mengirim media digrup ini 😥!")
        return
    await m.delete()
