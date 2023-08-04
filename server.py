from flask import Flask, request

app = Flask(__name__)

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello World'

@app.route("/calculator/add", methods=['POST'])
def add():
    a = int(request.form.get('a'))
    b = int(request.form.get('b'))
    return str(a + b)

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    a = int(request.form.get('a'))
    b = int(request.form.get('b'))
    return str(a - b)

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
