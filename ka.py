from flask import Flask,render_template
from threading import Thread

app = Flask(__name__)

@app.route('/')
def index():
    return "Alive"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():  
    t = Thread(target=run)
    t.start()

# keep always on by t.me/vano_ganzzz
# add the url on uptimerobot that allow bot run 24/7
