from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello World', 200

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.get_json()
    if 'first' in data and 'second' in data:
        first = data['first']
        second = data['second']
        result = first + second
        response = {'result': result}
        return jsonify(response), 200
    else:
        return jsonify({'error': 'Invalid request. Please provide both "first" and "second" numbers in the request body.'}), 400

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.get_json()
    if 'first' in data and 'second' in data:
        first = data['first']
        second = data['second']
        result = first - second
        response = {'result': result}
        return jsonify(response), 200
    else:
        return jsonify({'error': 'Invalid request. Please provide both "first" and "second" numbers in the request body.'}), 400

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
