import sched
import requests

token = "5665995939:AAFP4Ralnwt27upHfbdRAb6"

scheduler = sched.scheduler()

# mostra o id do último grupo adicionado
def last_chat_id(token):
    try:
        url = "https://api.telegram.org/bot{5665995939:AAFP4Ralnwt27upHfbdRAb6}/getUpdates".format(token)
        print(url)
        response = requests.get(url)
        if response.status_code == 200:
            json_msg = response.json()
            for json_result in reversed(json_msg['result']):
                message_keys = json_result['message'].keys()
                if ('new_chat_member' in message_keys) or ('group_chat_created' in message_keys):
                    return json_result['message']['chat']['id']
            print('Nenhum grupo encontrado')
        else:
            print('A resposta falhou, código de status: {}'.format(response.status_code))
    except Exception as e:
        print("Erro no getUpdates:", e)


def printa():
    print("Estou rodando")
    URL = "http://localhost:5154/WeatherForecast"
    location = "Computador de teste da SIM"
    PARAMS = {'address':location} 
    r = requests.get(url = URL, params = PARAMS) 
    print(r)
    scheduler.enter(delay=5, priority=0, action=printa)

last_chat_id(token)


def send_message(token, chat_id, message):
    try:
        data = {"chat_id": chat_id, "text": message}
        url = "https://api.telegram.org/bot{token}/sendMessage".format(token)
        requests.post(url, data)
    except Exception as e:
        print("Erro no sendMessage:", e)

printa()
last_chat_id(token)


scheduler.run(blocking=True)