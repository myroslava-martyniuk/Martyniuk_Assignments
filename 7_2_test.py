from flask import Flask

app = Flask(__name__)

request_count = 0

@app.route('/count-requests', methods=['GET'])
def get_request_count():
  global request_count 
  request_count += 1
  return ({'request_count': request_count})

@app.route('/reset-counter', methods=['POST'])
def reset_requests():
  global request_count
  request_count = 0
  return ({'message': 'Request counter reset!'})



if __name__ == '__main__':
  app.run(debug=True)