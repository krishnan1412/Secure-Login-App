from flask import Blueprint, render_template, request, redirect, url_for
from app.auth import verify_user

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if verify_user(username, password):
            return "Login successful"
        return "Invalid credentials"
    return render_template('login.html')
