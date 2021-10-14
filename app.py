from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker!'

if __name__ == '__main__':
  app.run(
    host="192.168.28.139",
    port=int("5000")
  )