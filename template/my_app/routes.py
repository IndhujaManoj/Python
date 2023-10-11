from flask import render_template, request, redirect, url_for
from my_app.extensions import db
from my_app.models import User
from . import auth

@register.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data=request.get_json()
        username = data['username']
        password = data['password']
        
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return "Username already exists. Please choose a different one."

        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        return "Registration successful. You can now log in."

    # return render_template('register.html')
