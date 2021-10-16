from flask import Flask, request
import serverdaten
app = Flask(__name__)

# @app.route('/', methods=['POST'])
# def result():
#     print(request.form['foo'])
#     return 'Received !'

@app.route('/', methods=['POST'])
def ergebnis():
    menge = int(request.form['menge'])
    wert = int(request.form['werte'])
    endwert = wert / menge
    return str(endwert)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=serverdaten.port)
    