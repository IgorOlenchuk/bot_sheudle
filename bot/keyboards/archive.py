
if m.animation != None: 
    await post_data(url=url, json={
        "messages_id": m.id,
        "chat": m.chat.username,
        "userbot": tg_name,
        "user_id": m.from_user.id,
        "text": m.caption,
        "animation": m.animation.file_id,
        "user_fullname": m.from_user.username,
        "date": str(m.date)}
        )
    await app.send_message(chat_id, mes.notification_user.format(user=m.from_user.username))
    await app.send_animation(chat_id, animation=m.animation.file_id, caption=m.caption)
    await app.send_message(chat_id, mes.notification_chat.format(chat=m.chat.username))

if m.sticker != None:                                  
    await post_data(url=url, json={
        "messages_id": m.id,
        "chat": m.chat.username,
        "userbot": tg_name,
        "user_id": m.from_user.id,
        "sticker": m.sticker.file_id,
        "user_fullname": m.from_user.username,
        "date": str(m.date)}
        )
    await app.send_message(chat_id, mes.notification_user.format(user=m.from_user.username))
    await app.send_sticker(chat_id, sticker=m.sticker.file_id)
    await app.send_message(chat_id, mes.notification_chat.format(chat=m.chat.username))

if m.photo != None:    
    await post_data(url=url, json={
        "messages_id": m.id,
        "chat": m.chat.username,
        "userbot": tg_name,
        "user_id": m.from_user.id,
        "text": m.caption,
        "photo": m.photo.file_id,
        "user_fullname": m.from_user.username,
        "date": str(m.date)}
        )
    await app.send_message(chat_id, mes.notification_user.format(user=m.from_user.username))
    await app.send_photo(chat_id, photo=m.photo.file_id, caption=m.caption)
    await app.send_message(chat_id, mes.notification_chat.format(chat=m.chat.username))

if m.audio != None: 
    await post_data(url=url, json={
        "messages_id": m.id,
        "chat": m.chat.username,
        "userbot": tg_name,
        "user_id": m.from_user.id,
        "text": m.caption,
        "audio": m.audio.file_id,
        "user_fullname": m.from_user.username,
        "date": str(m.date)}
        )
    await app.send_message(chat_id, mes.notification_user.format(user=m.from_user.username))
    await app.send_audio(chat_id, audio=m.audio.file_id, caption=m.caption)
    await app.send_message(chat_id, mes.notification_chat.format(chat=m.chat.username))

if m.document != None: 
    await post_data(url=url, json={
        "messages_id": m.id,
        "chat": m.chat.username,
        "userbot": tg_name,
        "user_id": m.from_user.id,
        "text": m.caption,
        "document": m.document.file_id,
        "user_fullname": m.from_user.username,
        "date": str(m.date)}
        )
    await app.send_message(chat_id, mes.notification_user.format(user=m.from_user.username))
    await app.send_document(chat_id, document=m.document.file_id, caption=m.caption)
    await app.send_message(chat_id, mes.notification_chat.format(chat=m.chat.username))

if m.video != None: 
    await post_data(url=url, json={
        "messages_id": m.id,
        "chat": m.chat.username,
        "userbot": tg_name,
        "user_id": m.from_user.id,
        "text": m.caption,
        "video": m.video.file_id,
        "user_fullname": m.from_user.username,
        "date": str(m.date)}
        )
    await app.send_message(chat_id, mes.notification_user.format(user=m.from_user.username))
    await app.send_video(chat_id, video=m.video.file_id, caption=m.caption)
    await app.send_message(chat_id, mes.notification_chat.format(chat=m.chat.username))

if m.voice != None: 
    await post_data(url=url, json={
        "messages_id": m.id,
        "chat": m.chat.username,
        "userbot": tg_name,
        "user_id": m.from_user.id,
        "text": m.caption,
        "voice": m.voice.file_id,
        "user_fullname": m.from_user.username,
        "date": str(m.date)}
        )
    await app.send_message(chat_id, mes.notification_user.format(user=m.from_user.username))
    await app.send_voice(chat_id, voice=m.voice.file_id, caption=m.caption)
    await app.send_message(chat_id, mes.notification_chat.format(chat=m.chat.username))
