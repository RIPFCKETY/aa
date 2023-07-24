# Import Libs
from pyrogram import Client
from pyrogram.types import Message , InlineKeyboardButton , InlineKeyboardMarkup , CallbackQuery
import pyromod , requests , socket , re , asyncio
from socket import error
from Resources.Get_Proxy import get

admin = [5580664758 , 6153993859 , 5254020295] # User ID Allow Use Bot

# Keyboards
KeyboardStart=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="𝐕𝐏𝐃 📟" , callback_data="VPD")
                ]
            ]
        )
KeyboardVPD=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="𝐒𝐭𝐚𝐫𝐭 𝐀𝐭𝐭𝐚𝐜𝐤 🔰" , callback_data="StartVPD"),
                    InlineKeyboardButton(text="𝐃𝐞𝐥𝐞𝐭𝐞 𝐏𝐫𝐨𝐱𝐲 𝐀𝐧𝐝 𝐕𝐥𝐞𝐬𝐬 🌐" , callback_data="Delete")
                ]
            ]
        )
 
print("DDoS Management Bot Is Online!") # Status Online

@Client.on_message() # Get Messages
async def OnMessage(client : Client , message : Message): 

    if message.from_user.id in admin: # Check User ID In admin list
        await message.reply_text("𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 𝐃𝐃𝐨𝐒 𝐌𝐚𝐧𝐚𝐠𝐞𝐦𝐞𝐧𝐭 𝐁𝐨𝐭" , reply_markup=KeyboardStart) # Answer Message
        if message.text == "/off":
            print("ok")
            exit()
        

@Client.on_callback_query()
async def OnCallBackQuery(client : Client , call : CallbackQuery):
    if call.data == "VPD":
        await client.edit_message_text(message_id=call.message.id , chat_id=call.message.chat.id , reply_markup=KeyboardVPD , text="𝐕𝐏𝐃 𝐌𝐚𝐧𝐚𝐠𝐞𝐦𝐞𝐧𝐭 🔰")
    
    elif call.data == "StartVPD":
        await client.edit_message_text(message_id=call.message.id , chat_id=call.message.chat.id , text="𝐆𝐞𝐭𝐭𝐢𝐧𝐠 𝐚 𝐩𝐫𝐨𝐱𝐲 ...")
        try:
           get()
           try:
               with open("VPD/proxy/proxy.txt", "r") as file:
                 ProxyList = file.readlines()
               await client.edit_message_text(message_id=call.message.id , chat_id=call.message.chat.id , text="𝐂𝐡𝐞𝐜𝐤 𝐩𝐫𝐨𝐱𝐲...")
               await asyncio.sleep(2)
               for ip in ProxyList:
                    ip_address, port = ip.split(':')
                    try:
                       client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                       client_socket.connect((ip_address, int(port)))
                       client_socket.close()
                       with open ("proxy.txt" , "a") as proxy:
                         await client.edit_message_text(message_id=call.message.id , chat_id=call.message.chat.id , text=f"𝐂𝐨𝐧𝐧𝐞𝐜𝐭𝐢𝐨𝐧 {ip_address}:{port} 𝐈𝐬 𝐎𝐤 ✅") 
                         proxy.write(ip_address+":"+port+"\n")
                    except Exception as i :
                         await client.edit_message_text(message_id=call.message.id , chat_id=call.message.chat.id , text=f"𝐂𝐨𝐧𝐧𝐞𝐜𝐭𝐢𝐨𝐧 {ip_address}:{port} 𝐈𝐬 𝐍𝐨𝐭 𝐎𝐤 ❌")
                         pass
               await client.edit_message_text(message_id=call.message.id , chat_id=call.message.chat.id , text=f"𝐂𝐡𝐞𝐜𝐤 𝐩𝐫𝐨𝐱𝐲 𝐅𝐢𝐧𝐢𝐬𝐡𝐞𝐝 ✅")
               await asyncio.sleep(2)
               

               
           except Exception as error:
                  await call.message.reply_text(error)
                  pass
        except Exception as error:
                  await call.message.reply_text(error)
                  pass
    
    
       