from flask import Flask, request, jsonify
import google.oauth2.credentials
import google.auth.transport.requests
import google.auth
import requests
import json
import os
import config

app = Flask(__name__)

if not os.path.exists(config.UPLOAD_FOLDER):
    os.makedirs(config.UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])
def upload():
    token = request.headers.get('Authorization')
    if not verify_token(token):
        return jsonify({'status': 'error', 'message': 'Invalid token.'}), 401
    user_info = get_user_info(token)
    if not is_authorized(user_info['email']):
        return jsonify({'status': 'error', 'message': 'Not authorized user.'}), 403
    if 'image' not in request.files:
        return jsonify({'status': 'error', 'message': 'Image file not found.'}), 400
    file = request.files['image']
    file.save(os.path.join(config.UPLOAD_FOLDER, file.filename))
    return jsonify({'status': 'success', 'message': 'Image sent successfully.'}), 200

# function to verify token
def verify_token(token):
    url = 'https://www.googleapis.com/oauth2/v1/tokeninfo'
    headers = {'Authorization':token}
    response = requests.get(url, headers=headers)
    return response.status_code == 200

# function to get user information from token
def get_user_info(token):
    url = 'http://www.googleapis.com/oauth2/v1/userinfo?alt=json'
    headers = {'Authorization': token}
    response = requests.get(url, headers=headers)
    return json.loads(response.content.decode('utf-8'))

# function to verify if the user is in allowed users
def is_authorized(email):
    return email in config.AUTHORIZED_ACCOUNTS

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
