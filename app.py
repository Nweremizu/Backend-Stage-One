from flask import Flask, request, jsonify
from datetime import datetime


app = Flask(__name__)




@app.route('/', methods=['GET'])
def stage_one_request():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track').lower()

    data = {
        'slack_name': slack_name,
        'current_day': datetime.now().strftime("%A"),
        'track': track,
        'utc_time': datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        'status_response': 200,
    }

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)