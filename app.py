from flask import Flask, request, jsonify
from datetime import datetime


app = Flask(__name__)




@app.route('/api', methods=['GET'])
def stage_one_request():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track').lower()

    data = {
        'slack_name': slack_name,
        'current_day': datetime.now().strftime("%A"),
        'utc_time': datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        'track': track,
        'github_file_url': 'https://github.com/Nweremizu/Backend-Stage-One/blob/main/app.py',
        'github_repo_url': 'https://github.com/Nweremizu/Backend-Stage-One',
        'status_response': 200
    }

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)