from flask import Flask
from app.routes import login_bp

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'  # Replace with AWS Secrets Manager
    app.register_blueprint(login_bp)
    return app
