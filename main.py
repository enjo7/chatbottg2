import commands as c
import apikey as key
from telegram.ext import Updater

def main():
   
    updater = Updater(key.API_KEY, use_context=True)
    dispatcher = updater.dispatcher

    
    dispatcher.add_handler(c.helpFunc)
    dispatcher.add_handler(c.startFunc)
    dispatcher.add_handler(c.stopFunc)
    dispatcher.add_handler(c.persistFunc)
    dispatcher.add_handler(c.IOFunc)

   
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
