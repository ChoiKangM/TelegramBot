from flask import Flask, render_template
app = Flask(__name__)

token = '815705291:AAE8jYAR3hS2A8V6s2XZgbDfOhbru7VwAnA'


@app.route(f'/{token}', methods=["POST"])
def telegram():
  return '', 200 # body, status_code

@app.route('/')
def index():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)