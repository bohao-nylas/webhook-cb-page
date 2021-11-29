from flask import Flask, request
import pprint

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def print_test():

    if request.method == 'POST':
        request_data = request.get_json()
        print('=================Webhook Payload=================')
        pprint.pprint(request_data)
        print('=================================================')
        return 'OK'

    query_parameters = request.args
    if request.method == 'GET':
        challenge = query_parameters.get('challenge')
        if challenge != None:
            return challenge
        else:
            return "I'm a page"

if __name__ == '__main__':
    app.run(debug=True, port=3000)
