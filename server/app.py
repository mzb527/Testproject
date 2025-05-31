from flask import Flask
from models import db
from auth import auth_bp
from routes import resource_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SECRET_KEY'] = 'your_secret_key'

db.init_app(app)

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(resource_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)