from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
import requests
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)
@app.route('/')
def shiba_inu():
    # return 'hello'
    url = 'https://api.coinpaprika.com/v1/tickers/shib-shiba-inu'
    shiba = requests.get(url).json()
    return render_template('index.html', crypto = shiba)
    # return 'El valor de Shiba-Inu es ' + str(shiba_price_CPL) + ' Pesos chilenos.'

@socketio.on('start')
def handle_start():
    """Update html every 1 second."""
    while True:
        url = 'https://api.coinpaprika.com/v1/tickers/shib-shiba-inu'
        shiba = requests.get(url).json()
        print("Updating...")
        print(shiba['last_updated'])
        print(shiba['quotes']['USD']['price'])
        emit('update', shiba)
        time.sleep(1)

if __name__ == '__main__':
    socketio.run(app)