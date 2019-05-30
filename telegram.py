import requests
import random

token = '815705291:AAE8jYAR3hS2A8V6s2XZgbDfOhbru7VwAnA'
api_url = f'https://api.telegram.org/bot{token}'
chat_id = '852414454' # => 본인의 Telegram id
# text = input("메세지를 입력하세요: ")
text = random.sample(range(1,46), 6)
text.sort()

response = requests.get(f'{api_url}/sendMessage?chat_id={chat_id}&text={text}')