TOKEN = '1856711707:AAFH3BirZu3v7_m2l5OUWnAhDJKMJmAF4MQ'

URL = 'https://api.telegram.org/bot{token}/{method}'

UPDATE_METH = 'getUpdates'
SEND_METH = 'sendMessage'

MY_ID = 602925558

UPDATE_ID_FILE_PATH = 'update_id'

with open(UPDATE_ID_FILE_PATH) as file:
    data = file.readline()
    if data:
        data = int(data)
    UPDATE_ID = data

WEATHER_TOKEN = 'a3cf06415e6a17d1b39450e3aaadb2e9'

WEATHER_URL = 'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}'
