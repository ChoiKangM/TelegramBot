## 1교시
`Telegram`
`@botfather`: `/newbot`, `token`

`available methods`
  - `getMe`
  - `sendMessage`
  - `getUpdates`
    - `id`
  
## 2교시
API를 활용해 봇에 메시지 날리기
  1. `python`
    `requests`, `input`
  2. `flask`

## 3교시
대답하는 봇?
`return body, status_code`  
`POST`


[ngrok](https://ngrok.com/) : 인터넷과 내 로걸 서버를 연결

`ngrok.exe` 파일은 사용자 폴더로 옮겨 실행한다

## 4교시
win 10에서 ngrok이 잘 안되는 경우  
[equinox](https://dl.equinox.io/ngrok/ngrok/stable/archive)에서 `2.2.8` 버전으로 진행해보자  

`available methods`
  - `setWebhook`

## 5교시
`메아리치는 봇`
  - `request.args` # GET
  - `request.forms` # POST
  - `request.get_json()` 

## 6교시
`로또 외치면 로또 번호`

`is` vs `==`
```python
1000 is 10**3 # FALSE

# 띄어쓰기 없는 짧은 문자의 경우는 다를 수 있다
a = 'lotto lotto'
b = 'lotto lotto'
id(a) # 4437766384
id(b) # 4437766448

a is b # FALSE

-5 ~ 255 # 자주 쓰는 숫자는 메모리에 이미 넣어둠
```

[네이버 개발자센터`Papago`](https://developers.naver.com/products/translator/)

## 7교시
`JSON`에서 번역할 문자열 찾기
  - `get('message').get('result').get('translatedText')`
`명령어 추가`
  - `text[0:4] == '/번역 '`

[`pythonanywhere`](https://www.pythonanywhere.com/)


