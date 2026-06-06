import requests
import telebot

TOKEN = "8914885457:AAHrUT3P5g8P-fj2Pphm1Lu-LEhMKPoJgNY"

bot = telebot.TeleBot(TOKEN)

cached_coins = None


def load_coins():
    global cached_coins
    if cached_coins is None:
        url = "https://api.coingecko.com/api/v3/coins/list"
        cached_coins = requests.get(url).json()


def get_coin_id(user_input):
    load_coins()
    user_input = user_input.lower()
    ids = ''
    for coin in cached_coins:
        if coin["name"].lower() == user_input or coin["symbol"].lower() == user_input:
            if ids == '':
                ids = coin["id"]
            else:
                ids += ',' + coin["id"]

    return ids


def get_coin_price(user_input):
    coin_id = get_coin_id(user_input)

    if coin_id is None:
        return None

    url = "https://api.coingecko.com/api/v3/simple/price"

    params = {
        "ids": coin_id,
        "include_24hr_change":True,
        "vs_currencies": "usd"
    }

    headers = {
        "x_cg_demo_api_key": "CG-gofCBvDWQi9v27cxgr5CsaTC"
    }

    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    print(data)
    return data


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "سلام 👋\nنام یا نماد ارز را ارسال کنید.")


@bot.message_handler(func=lambda message: True)
def get_price(message):
    output_str = ''
    price = get_coin_price(message.text)

    if price is None:
        bot.reply_to(message, "کوین پیدا نشد ❌")
    else:
        for key,value in dict(price).items():
            if 'usd' in value:
                output_str += key + ' : ' + str(value['usd']) + ' $ ' + '\n'


        bot.reply_to(message, f"{output_str}")


bot.infinity_polling()
