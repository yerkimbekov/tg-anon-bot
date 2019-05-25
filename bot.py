# -*- coding: utf-8 -*-
import telebot

TOKEN = 'TOKEN of your bot'

testb=telebot.TeleBot(token = TOKEN)
to_chat_id_1 = 'username of group where is your bot'

#{"ok":true,"result":[{
#   "update_id":628510725, "message":{
#       "message_id":108,"from":{
#           "id":222091424,"is_bot":false,"first_name":"Treo","last_name":"Roygbiv","username":"treo_a","language_code":"en"
#       }
#       ,"chat":{
#           "id":222091424,"first_name":"Treo","last_name":"Roygbiv","username":"treo_a","type":"private"
#       }
#       ,"date":1558549183,"photo":[{
#           "file_id":"AgADAgADt6oxGxT3KUvL8KDW8w-yH5pDXw8ABDG7Wq1-A6bhiiEFAAEC","file_size":1262,"width":51,"height":90
#       }
#       ,{
#           "file_id":"AgADAgADt6oxGxT3KUvL8KDW8w-yH5pDXw8ABJ9wVqml_A21iyEFAAEC","file_size":16489,"width":180,"height":320
#       },
#       {
#           "file_id":"AgADAgADt6oxGxT3KUvL8KDW8w-yH5pDXw8ABA30-v0xXDobjSEFAAEC","file_size":65623,"width":450,"height":800
#       },
#       {
#           "file_id":"AgADAgADt6oxGxT3KUvL8KDW8w-yH5pDXw8ABM55wlpvVIrzjCEFAAEC","file_size":128180,"width":720,"height":1280
#       }
#       ],"caption":"asdf"}}]}

@testb.message_handler(commands=['start', 'help'])
def send_welcome(message):
	testb.reply_to(message, "Привет. Твоё сообщение будет анонимно отправлено в чат (your group username). Я пока умею отправлять только текстовые сообщения, \
фото и документы. Я только учусь\n \n Пожалуйста, без оскорблений и матов. За это админ оставляет полное право удалить твоё сообщение")

#@testb.message_handler(content_types=['text', 'audio', 'document', 'photo', 'sticker', 'video', 'video_note', 'voice', 'contact'])
#def forwarding_the_message(message):
#    testb.forward_message(to_chat_id_1, message.chat.id, message.message_id)

@testb.message_handler(content_types=['text'])
def send_anon_text(message):
    if not message.content_type == 'text':
        return
    if not message.chat.type == 'private':
        return
    testb.send_message(to_chat_id_1, message.text)
    testb.send_message(message.chat.id, "Отправил твоё обращение :)")


@testb.message_handler(content_types = ['photo'])
def send_anon_photo (message):
    if not message.content_type == 'photo':
        return
    if not message.chat.type == 'private':
        return
    testb.send_photo(to_chat_id_1, message.photo[-1].file_id)
    if not message.caption == None:
        testb.send_message(to_chat_id_1, message.caption)
    testb.send_message(message.chat.id, "Отправил твоё обращение :)")


@testb.message_handler(content_types = ['document'])
def send_anon_document (message):
    if not message.content_type == 'photo':
        return
    if message.chat.id == to_chat_id_1:
        return
    testb.send_document(to_chat_id_1, message.document.file_id)
    if not message.caption == None:
        testb.send_message(to_chat_id_1, message.caption)
    testb.send_message(message.chat.id, "Отправил твоё обращение :)")


testb.polling()