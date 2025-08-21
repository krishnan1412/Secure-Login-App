import boto3
import json
from flask import Flask
from app.routes import login_bp

def get_secret():
    client = boto3.client('secretsmanager', region_name='ap-northeast-2')
    response = client.get_secret_value(SecretId='login-app-secrets')
    secret_dict = json.loads(response['SecretString'])
    return secret_dict['SECRET_KEY']

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = get_secret()
    app.register_blueprint(login_bp)
    return app
