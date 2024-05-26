import json
import socket
from flask import Flask,request, jsonify

host = socket.gethostname()
app = Flask(__name__)

@app.route('/postmethod', methods=['POST'])
def get_post_javascript_data():
    data = request.form
    data = jsonify(data)
    data.headers.add('Access-Control-Allow-Origin','*')
    with open('user_settings.json','w') as f:
        json.dump(request.form,f,indent=4,ensure_ascii=False)
    return data

if __name__ == "__main__":
    app.run(host=host,ssl_context=('root_ca.crt','root_ca.key'))
