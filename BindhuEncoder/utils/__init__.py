from pyrogram import Client, filters
from .. import LOGGER
from . import (direct_link_generator, display_progress, ffmpeg, helper,
               settings, tasks)

LOGGER.info('Imported Utils!')

sauce = '''<b>BindhuEncoder - a telegram bot for compressing/encoding videos in h264 format.</b>
Copyright (c) 2024<a href='https://github.com/MAHESH-KADALI/compressor-bot-with-all-features'>MAHESH-KADALI/compressor-bot-with-all-features</a>
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.
You should have received a copy of the GNU Affero General Public License
along with this program. If not, see .'''


@Client.on_message(filters.command('so' 'ur' 'ce'))
async def g_s(_, message):
    try:
        await message.reply(text=sauce, reply_markup=helper.output, disable_web_page_preview=True)
    except RPCError:
        pass
