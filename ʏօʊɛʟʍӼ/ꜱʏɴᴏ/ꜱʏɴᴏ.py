from Cula import *

async def send_file(c, q, med, item_id):
    print(med)
    try:
        await q.edit_message_reply_markup(InlineKeyboardMarkup([[InlineKeyboardButton("Sending Item📤",callback_data="down")]]))
        await c.send_chat_action(chat_id=q.message.chat.id, action="record_video")
        await q.edit_message_media(media=med)
    except Exception as e:
        print(e)
        await q.edit_message_text(e)
    finally:
        try:
            os.remove(item_id)
            os.remove(jpeg_fetched)
        except:
            print("ASK @HypeVoidSoul to fix this error")
            pass
