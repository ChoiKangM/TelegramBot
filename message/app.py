from flask import Flask, render_template, request
import requests
from decouple import config
app = Flask(__name__)

@app.route('/write')
def write():
  return render_template('write.html')

@app.route('/send')
def send():
  token = config('TELE_TOKEN')
  api_url = f'https://api.telegram.org/bot{token}'
  chat_id = config('CHAT_ID') # => 본인의 Telegram id
  # text = input("메세지를 입력하세요: ")
  # text = random.sample(range(1,46), 6)
  # text.sort()
  text = request.args.get('message')
  response = requests.get(f'{api_url}/sendMessage?chat_id={chat_id}&text={text}')
  return '전송완료'

if __name__ == '__main__':
  app.run(debug=True)