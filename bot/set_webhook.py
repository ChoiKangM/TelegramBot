import requests
 
token = '815705291:AAE8jYAR3hS2A8V6s2XZgbDfOhbru7VwAnA'
api_url = f'https://api.telegram.org/bot{token}'
flask_url = f'https://b109ae8c.ngrok.io/{token}'
set_url = f'{api_url}/setWebhook?url={flask_url}'

response = requests.get(set_url)
print(response.text)
