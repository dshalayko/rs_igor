import json
import requests
import telebot

TOKEN = "5651594004:AAHGmicPOInrM3FbhtKqMBhDvoAwNKbtMCo"
CHAT_ID_USERBOT = 379085521
URL = 'https://cityexpert.rs/api/Search?req=%7B%22ptId%22%3A%5B1%5D%2C%22cityId%22%3A1%2C%22rentOrSale%22%3A%22r%22%2C%22currentPage%22%3A1%2C%22resultsPerPage%22%3A30%2C%22floor%22%3A%5B%5D%2C%22avFrom%22%3Afalse%2C%22underConstruction%22%3Afalse%2C%22furnished%22%3A%5B%5D%2C%22furnishingArray%22%3A%5B%5D%2C%22heatingArray%22%3A%5B%5D%2C%22parkingArray%22%3A%5B%5D%2C%22petsArray%22%3A%5B%5D%2C%22minPrice%22%3Anull%2C%22maxPrice%22%3A650%2C%22minSize%22%3Anull%2C%22maxSize%22%3Anull%2C%22polygonsArray%22%3A%5B%22Vra%C4%8Dar%22%2C%22Zemun%22%2C%22Stari%20grad%22%2C%22Palilula%22%2C%22Novi%20Beograd%22%5D%2C%22searchSource%22%3A%22regular%22%2C%22sort%22%3A%22datedsc%22%2C%22structure%22%3A%5B%222.0%22%2C%222.5%22%2C%223.0%22%5D%2C%22propIds%22%3A%5B%5D%2C%22filed%22%3A%5B%5D%2C%22ceiling%22%3A%5B%5D%2C%22bldgOptsArray%22%3A%5B%5D%2C%22joineryArray%22%3A%5B%5D%2C%22yearOfConstruction%22%3A%5B%5D%2C%22otherArray%22%3A%5B%5D%7D'
FILE = 'db.txt'
bot = telebot.TeleBot(TOKEN)

req = requests.get(URL)
request_data = json.loads(req.text)

db = open(FILE)
tmp_arr_int = []
tmp_arr_str = []
for line in db:
    if line not in '\n':
        tmp_arr_str.append(line)
        tmp_arr_int.append(int(line))
db.close()
db = open(FILE, 'w')

for i in request_data['result']:
    if i['propId'] not in tmp_arr_int:
        db.write(str(i['propId']) + '\n')
        bot.send_message(CHAT_ID_USERBOT,
                         'https://cityexpert.rs/en/properties-for-rent/belgrade/' + str(i['propId']) + '/igooooor')


for t in tmp_arr_str:
    db.write(t)
db.close()

# bot.send_message(CHAT_ID_USERBOT, req.status_code)
