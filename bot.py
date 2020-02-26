from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import ephem
import datetime

PROXY = {"proxy_url": "socks5://t1.learn.python.ru:1080","urllib3_proxy_kwargs": {"username": "learn", "password": "python"}}


def greet_user(bot,update):
    text = "Вызван/start"
    print(text)
    update.messege.reply_text(text)

def ephem_planet_name(planet_name:str):
    _planet_name = _planet_name. lower()
    if _planet_name in ("Mercury", "меркурий","vthrehbq"):
        return ephem.Mercury() 
    elif _planet_name in ("Venus","dtythf","венера" ):
        return ephem.Venus() 
    elif planet_name in ("Earth","ptvkz","земля"):
        return ephem.Earth()
    elif planet_name in ("Mars","vfhc","марс"):
        return ephem.Mars()
    elif planet_name in ("Jupiter",".gbnth","юпитер"):
        return ephem.Jupiter()  
    elif planet_name in ("Saturn","cfnehy","сатурн"):
        return ephem.Saturn() 
    elif planet_name in ("Uranus","ehfy","уран"):
        return ephem.Uranus()    
    elif planet_name in ("Neptune","ytgney","нептун"):
        return ephem.Neptune()
    elif planet_name in ("Pluto","gkenjy","плутон"):
        return ephem.Pluto()

def planet_constellation_by_planet(bot,update):
    message_words = [] 
    for word in update.message.text.split(""):
        if word:
            message_words.append(word) 
    if len(message_words) < 2:
        update.message.reply_text("Введите название планеты=")
        return

    ephem_planet = ephem_planet_name(message_words[1])
    if epfem_planet is None:
        update.message.reply_text(
            "Введите назвагие планеты а не {planet_candidate}".format(
                planet_candidate = message_words[1],
            )
        )
        return

    message_dt: datetime = update.message.data 
    ephem_planet.compute(message_dt.strftime"%Y/%m/%d"))

    c_str = str(planet_constellation(ephem_planet))
     update.message.reply_text(c_str) 

def talk_to_me(bot,update)
    user_text = update.message.text
    print (user_text)
    update.message.reply_text(user_text)      


logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s",
                    level=logging.INFO,
                    filename="bot.log"
                    )
def main(): 
    mybot = Updater("1052174164:AAGOcpUtTeTAXjPba3Av12dAfkd524RndQw", request_kwargs=PROXY)
    
    logging.info("Бот запускается")
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user ))
    dp.add_handler(CommandHandler("planet", planet_tudei_ephem ))
    dp.add_error_handler(MessageHandler, Filters, talk_to_me)

    mybot.start_polling
    mybot.idle()          

if__name__=="main":
    main()



 
