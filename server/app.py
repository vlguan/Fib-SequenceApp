from flask import Flask
import os
import sys
import click
from werkzeug.exceptions import HTTPException
import traceback
from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv

load_dotenv()

# db = SQLAlchemy()
def create_app():
    sys.path.append(".")  # to allow sub modules to access the parent module easily

    from db.db import db
    from api import api as api_blueprint
    

    
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DB_PATH','sqlite:///server/instance/database.db')
    # breakpoint()
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    # with app.app_context():
    # db.create_all()
    #     db.session.commit()
    db.init_app(app)
    app.register_blueprint(api_blueprint, url_prefix="/api")
    
    return app


app = create_app()
