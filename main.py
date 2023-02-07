from pyrogram import Client, filters
from pyrogram.types import *
from pymongo import MongoClient
import requests
import random
import os
import re


API_ID = os.environ.get("API_ID", "10644386") 
API_HASH = os.environ.get("API_HASH", "b370b28d4ca22e28186e3e12a2a39431") 
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5680467811:AAEdwm1WnKn7MLbrNZm1TATlfGGRz8") 
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://karthika:karthika@cluster0.6jms6m3.mongodb.net/?retryWrites=true&w=majority")


bot = Client(
    "KarthikaBot" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)




@bot.on_message(filters.command("start"))
async def start(client, message):
        await message.reply_text("𝐻𝑒𝑙𝑙𝑜 𝐶ℎ𝑙𝑚 🙈\n  𝑁𝑎𝑛 𝑇ℎ𝑎𝑛 𝑄𝑢𝑒𝑒𝑛 𝑂𝑟𝑒𝑜 𝐵𝑜𝑡\n  ⋆─፝─᪵།͢❤️꯭𝛀꯭꯭𖽪𖽞𖽞𖽡꯭꯭꯭ 𝐎꯭꯭𖽷𖽞᪲᪳𖽙꯭🐾༉͙⋆\n  𝑈𝑛𝑜𝑜𝑑𝑎 𝐺𝑟𝑜𝑢𝑝 𝐶ℎ𝑎𝑡 𝐼𝑛𝑐𝑟𝑒𝑎𝑠𝑒 𝑁𝑎𝑛 𝐺𝑟𝑎𝑛𝑡𝑦\n  ➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n  👑 𝑀𝑦 𝑂𝑤𝑛𝑒𝑟 : @king_of_izzyy 👑\n  ➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n  😻 𝑀𝑦 𝑃𝑎𝑟𝑡𝑛𝑒𝑟: 𝑂𝑛𝑒 𝐿𝑜𝑣𝑒 𝑀𝑢𝑠𝑖𝑐 𝐵𝑜𝑡 😻\n  ➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n  𝐼 𝑑  :  @One_love_music_melting_bot\n  ➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n  𝐴𝑑𝑑 𝑌𝑜𝑢𝑟 𝑆𝑢𝑝𝑒𝑟 𝐺𝑟𝑜𝑢𝑝 𝑇𝑜 𝑈𝑛𝑙𝑖𝑚𝑖𝑡𝑒𝑑 𝐹𝑢𝑛\n  ▰▰▰▰▰▰▰▰▰▰▰▰▰\n         ⋆─፝─᪵།͢❤️꯭𝛀꯭꯭𖽪𖽞𖽞𖽡꯭꯭꯭ 𝐎꯭꯭𖽷𖽞᪲᪳𖽙꯭🐾༉͙⋆       \n  ▰▰▰▰▰▰▰▰▰▰▰▰▰\n   /chatbot - [on|off]")


@bot.on_message(
    filters.command("chatbot off", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbotofd(client, message):
    Karthikadb = MongoClient(MONGO_URL)    
    Karthika = Karthikadb["KarthikaDb"]["Karthika"]     
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
           await is_admins(chat_id)
        ):
           return await message.reply_text(
                "You are not admin"
            )
    is_Karthika = Karthika.find_one({"chat_id": message.chat.id})
    if not is_Karthika:
        Karthika.insert_one({"chat_id": message.chat.id})
        await message.reply_text(f"Chatbot Disabled!")
    if is_Karthika:
        await message.reply_text(f"ChatBot Is Already Disabled")
    

@bot.on_message(
    filters.command("chatbot on", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatboton(client, message):
    Karthikadb = MongoClient(MONGO_URL)    
    Karthika = Karthikadb["KarthikaDb"]["Karthika"]     
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
            await is_admins(chat_id)
        ):
            return await message.reply_text(
                "You are not admin"
            )
    is_Karthika = Karthika.find_one({"chat_id": message.chat.id})
    if not is_Karthika:           
        await message.reply_text(f"Chatbot Is Already Enabled")
    if is_Karthika:
        Karthika.delete_one({"chat_id": message.chat.id})
        await message.reply_text(f"ChatBot Is Enable!")
    

@bot.on_message(
    filters.command("chatbot", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbot(client, message):
    await message.reply_text(f"**Usage:**\n/chatbot [on|off] only group")


@bot.on_message(
 (
        filters.text
        | filters.sticker
    )
    & ~filters.private
    & ~filters.bot,
)
async def Karthikaai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       Karthikadb = MongoClient(MONGO_URL)
       Karthika = Karthikadb["KarthikaDb"]["Karthika"] 
       is_Karthika = Karthika.find_one({"chat_id": message.chat.id})
       if not is_Karthika:
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})  
           k = chatai.find_one({"word": message.text})      
           if k:               
               for x in is_chat:
                   K.append(x['text'])          
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "sticker":
                   await message.reply_sticker(f"{hey}")
               if not Yo == "sticker":
                   await message.reply_text(f"{hey}")
   
   if message.reply_to_message:  
       Karthikadb = MongoClient(MONGO_URL)
       Karthika = Karthikadb["KarthikaDb"]["Karthika"] 
       is_Karthika = Karthika.find_one({"chat_id": message.chat.id})    
       getme = await bot.get_me()
       bot_id = getme.id                             
       if message.reply_to_message.from_user.id == bot_id: 
           if not is_Karthika:                   
               await bot.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:       
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "sticker":
                       await message.reply_sticker(f"{hey}")
                   if not Yo == "sticker":
                       await message.reply_text(f"{hey}")
       if not message.reply_to_message.from_user.id == bot_id:          
           if message.sticker:
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "id": message.sticker.file_unique_id})
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.sticker.file_id, "check": "sticker", "id": message.sticker.file_unique_id})
           if message.text:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "text": message.text})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.text, "check": "none"})    
               

@bot.on_message(
 (
        filters.sticker
        | filters.text
    )
    & ~filters.private
    & ~filters.bot,
)
async def Karthikastickerai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       Karthikadb = MongoClient(MONGO_URL)
       Karthika = Karthikadb["KarthikaDb"]["Karthika"] 
       is_Karthika = Karthika.find_one({"chat_id": message.chat.id})
       if not is_Karthika:
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})      
           k = chatai.find_one({"word": message.text})      
           if k:           
               for x in is_chat:
                   K.append(x['text'])
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "text":
                   await message.reply_text(f"{hey}")
               if not Yo == "text":
                   await message.reply_sticker(f"{hey}")
   
   if message.reply_to_message:
       Karthikadb = MongoClient(MONGO_URL)
       Karthika = Karthikadb["KarthikaDb"]["Karthika"] 
       is_Karthika = Karthika.find_one({"chat_id": message.chat.id})
       getme = await bot.get_me()
       bot_id = getme.id
       if message.reply_to_message.from_user.id == bot_id: 
           if not is_Karthika:                    
               await bot.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:           
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "text":
                       await message.reply_text(f"{hey}")
                   if not Yo == "text":
                       await message.reply_sticker(f"{hey}")
       if not message.reply_to_message.from_user.id == bot_id:          
           if message.text:
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text})
               if not is_chat:
                   toggle.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text, "check": "text"})
           if message.sticker:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id, "check": "none"})    
               


@bot.on_message(
    (
        filters.text
        | filters.sticker
    )
    & filters.private
    & ~filters.bot,
)
async def Karthikaprivate(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]
   if not message.reply_to_message: 
       await bot.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.text})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "sticker":
           await message.reply_sticker(f"{hey}")
       if not Yo == "sticker":
           await message.reply_text(f"{hey}")
   if message.reply_to_message:            
       getme = await bot.get_me()
       bot_id = getme.id       
       if message.reply_to_message.from_user.id == bot_id:                    
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "sticker":
               await message.reply_sticker(f"{hey}")
           if not Yo == "sticker":
               await message.reply_text(f"{hey}")
       

@bot.on_message(
 (
        filters.sticker
        | filters.text
    )
    & filters.private
    & ~filters.bot,
)
async def Karthikaprivatesticker(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"] 
   if not message.reply_to_message:
       await bot.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "text":
           await message.reply_text(f"{hey}")
       if not Yo == "text":
           await message.reply_sticker(f"{hey}")
   if message.reply_to_message:            
       getme = await bot.get_me()
       bot_id = getme.id       
       if message.reply_to_message.from_user.id == bot_id:                    
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "text":
               await message.reply_text(f"{hey}")
           if not Yo == "text":
               await message.reply_sticker(f"{hey}")
       
bot.run()
