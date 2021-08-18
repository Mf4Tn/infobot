import telebot , requests , json
from telebot.types import Message
from user_agent import generate_user_agent
token = "1961840045:AAHBzCAsj9qpXI37Wm5dg604Ppxr8sx9spQ"
def ex_id(id):
    result = False
    file = open("id.txt",'r')
    for lina in file:
        if lina.strip()==id:
            result = True
    file.close
    return result
sudo = 906630665
text = f"*Sorry This Bot Work Only In Groups\nAdd Me In Your Chat And Enjoy\n\nDév: @ffq_q\nIG : instagram.com/mf4.py*"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def star(message):
    idu = message.from_user.id
    f = open("id.txt",'a')
    if (not ex_id(str(idu))):
        f.write(str(idu)+"\n")
        f.close
    if message.chat.type == "group" or message.chat.type == "supergroup":
        if message.from_user.id == sudo:
            bot.reply_to(message,f"*Hey MF4 How Are You ?*",parse_mode="markdown")
        else:
            bot.reply_to(message,f"*Hey {message.chat.first_name}\n/igcmd To Check Commands 😁*",parse_mode="markdown")
    else:
        bot.send_message(message.chat.id,f"*Welcome {message.chat.first_name}*{message.chat.type}",parse_mode="markdown")
        bot.send_message(message.chat.id,f"*Sorry This Bot Work Only In Groups\nAdd Me In Your Chat And Enjoy\n\nDév: @ffq_q\nIG : instagram.com/mf4.py*",parse_mode="markdown")
@bot.message_handler(commands=["igcmd"])
def cmds(message):
    link = "https://raw.githubusercontent.com/mf4TN/gif/main/team.mp4"
    if message.chat.type == "group" or message.chat.type == "supergroup" or message.chat.type == "supergroup":
        bot.reply_to(message,"*Préparing ...*",parse_mode="markdown")
        bot.send_video(message.chat.id,link,caption="*/iginfo\n/igvalid\n/igrest\nIf You Need More Help\n/help \nEnjoy :)*",parse_mode="markdown")
    else:
        bot.send_message(message.chat.id,text=text,parse_mode="markdown")
@bot.message_handler(commands=["ighelp"])
def help(message):
    if message.chat.type == "group" or message.chat.type == "supergroup" or message.chat.type == "supergroup":
        bot.reply_to(message,"*/iginfo ( To Get Account Détails Like Picture , Followers Count , Following , Posts , Bio , Name , Création Date ) To Use It Send Exp /iginfo instagram\n/igvalid ( To Check If User Valid In Instagram Or No exp /igvalid instagram)\n/igrest ( To Send Rest Email To Your Mail exp /igrest instagram)\nNeed Another Help xD ?\nDm Dév : @ffq_q*",parse_mode="markdown")
    else:
        bot.send_message(message.chat.id,text,parse_mode="markdown")
@bot.message_handler(commands=["iginfo"])
def info(message):
    if message.chat.type == "group" or message.chat.type == "supergroup":
        try:
            user = message.text.split("/iginfo ")[1]
            bot.reply_to(message,"*Getting Information ... *",parse_mode="markdown")
            url = f"https://givt.ga/api/v1/instagram-info.php?user={user}"
            url2 = f"https://echoar.ml/Apimedia/infon.php?user={user}"
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36",
                "Pragma": "no-cache",
                "Accept": "*/*"
            }
            r2 = requests.get(url2)
            r = requests.get(url,headers=headers)
            if "User Not Found" != r.text:
                for data in r.json():
                    created = data["username_created_data"]
                    name = data["name"]
                    userid = data["username_ID"]
                    follwing = data["Following"]
                    followers = data["Followers"]
                    Posts = data["Posts"]
                    bio = data["bio"]
                pic = r2.json()["Info"]["image"]
                bot.send_photo(message.chat.id,pic,caption=f"*Account Created At : *`{created}`\n*Account Name : *`{name}`\n*User ID : *`{userid}`\n*Following : *`{follwing}`\n*Followers : *`{followers}`\n*Posts : *`{Posts}`\n*Bio : *`{bio}`",parse_mode="markdown")
            else:
                bot.reply_to(message,"*User Not Found\nOr Another Probléme DM @ffq_q*",parse_mode="markdown")
        except Exception as x:
            bot.reply_to(message,f"*Error:\n*`{x}`",parse_mode="markdown")
    else:
        bot.send_message(message.chat.id,text,parse_mode="markdown")
@bot.message_handler(commands=["igvalid"])
def val(message):
    if message.chat.type == "group" or message.chat.type == "supergroup":
        try:
            uservalid = message.text.split("/igvalid ")[1]
            urlvalid = f"https://givt.ga/api/v1/instagram-check.php?username={uservalid}"
            ridk = requests.get(urlvalid)
            if "Taken" in ridk.text:
                bot.reply_to(message,f"*User Taken :( => {uservalid}*",parse_mode="markdown")
            elif "Available" in ridk.text:
                bot.reply_to(message,f"*User Available Or Banned :) => {uservalid}*",parse_mode = "markdown")
            else:
                bot.reply_to(message,"*Error :(*",parse_mode="markdown")
        except Exception as mf4idk:
            bot.reply_to(message,f"*Error:\n*`{mf4idk}`",parse_mode="markdown")
    else:
        bot.send_message(message.chat.id,text,parse_mode="markdown")
            
@bot.message_handler(commands=["igrest"])
def rest(message):
    if message.chat.type == "group" or message.chat.type == "supergroup":
        try:
            mail  = message.text.split("/igrest ")[1]
            bot.reply_to(message,f"*Sending Rest Mail To {mail} ...*",parse_mode="markdown")
            urlh = 'https://www.instagram.com/accounts/account_recovery_send_ajax/' 
 
            headh = { 
                'accept':'*/*', 
                'accept-encoding':'gzip,deflate,br', 
                'accept-language':'en-US,en;q=0.9,ar;q=0.8', 
                'content-length':'269', 
                'content-type':'application/x-www-form-urlencoded', 
                'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-', 
                'origin':'https://www.instagram.com', 
                'referer':'https://www.instagram.com/', 
                'sec-fetch-dest':'empty', 
                'sec-fetch-mode':'cors', 
                'sec-fetch-site':'same-origin', 
                'user-agent': generate_user_agent(), 
                'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8', 
                'x-ig-app-id':'936619743392459', 
                'x-ig-www-claim':'0', 
                'x-instagram-ajax':'8a8118fa7d40', 
                'x-requested-with':'XMLHttpRequest', 
            } 
            
            datah = { 
                'email_or_username': mail, 
                'recaptcha_challenge_field': '', 
                'flow': '', 
                'app_id': '', 
                'source_account_id': '', 
            } 

            r = requests.post(urlh,headers=headh,data=datah)
            if "Email Sent" in r.text:
                email = r.json()["contact_point"]
                bot.reply_to(message,f"*Done Sent Email To *`{email}`\n*User Or Mail : *`{mail}`",parse_mode="markdown")
            elif "message" in r.text:
                bot.reply_to(message,"*"+r.json()["message"]+"*",parse_mode="markdown")
            else:
                bot.reply_to(message,"*"+r.text+"*")
            
        
        except Exception as m:
            bot.reply_to(message,f"*Error :\n*`{m}`",parse_mode="markdown")
    else:
        bot.send_message(message.chat.id,text,parse_mode="markdown")

bot.polling()
