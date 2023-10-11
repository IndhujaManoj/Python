from flask import Flask
from my_app.auth import auth
from my_app.extensions import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:indhuja%4023@localhost:3306/mydatabase'

db.init_app(app)
app.register_blueprint(auth)

if __name__ == '__main__':
    app.run(debug=True)
