from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def process_data():
    data = request.get_json()
    # Process the data received from the client
    # Perform actions based on the data
    result = {'message': 'Data processed successfully'}
    return jsonify(result)

if __name__ == '__main__':
    app.run()