from flask import Flask, request
import requests
app = Flask(__name__)

token = '815705291:AAE8jYAR3hS2A8V6s2XZgbDfOhbru7VwAnA'
api_url = f'https://api.telegram.org/bot{token}'

@app.route(f'/{token}', methods=["POST"])
def telegram():
  # request.args # GET
  # request.forms # POST
  # print(request.get_json())

  # lotto('key) # => value, 'key'가 없다면 예외 발생
  # lotto.get('key') # => value, 'key'가 없다면 none 반환
  message = request.get_json().get('message')
  print(message)

  # data 가져오기
  if message is not None:
    chat_id = message.get('from').get('id')
    text = message.get('text')
    send_url = f'{api_url}/sendMessage?chat_id={chat_id}&text={text}'
    
    # sendMessage 요청 보내기
    response = requests.get(send_url)
  

  return '', 200 # body, status_code

if __name__ == '__main__':
  app.run(debug=True)