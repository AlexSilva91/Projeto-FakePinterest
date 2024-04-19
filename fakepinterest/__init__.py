import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
if os.getenv('DEBUG') == 0:
    link_banco = os.getenv("DATABASE_URL")
else:
    link_banco = "sqlite:///comunidade.db"

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SECRET_KEY"] = "4f52e669753727026e0c70c3d2433973"
app.config["UPLOAD_FOLDER"] = "static/fotos_post"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "homepage"


from fakepinterest import routes
