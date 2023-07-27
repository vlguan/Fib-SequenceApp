from flask import Flask
import os
import sys
import click
from werkzeug.exceptions import HTTPException
import traceback


from dotenv import load_dotenv

load_dotenv()


def create_app():
    sys.path.append(".")  # to allow sub modules to access the parent module easily

    from db.db import db
    from api import api as api_blueprint

    app = Flask(__name__)
    # Unaltered sql Call, but I had to change to a specific path on my pc for some reason. 
    # Don't know if pulling it will also require change to direct path
    # Add extra / and type out direct path to the instanced database.db
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "DB_PATH", 'sqlite:///database.db'
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    
    app.register_blueprint(api_blueprint, url_prefix="/api")
    
    return app


app = create_app()
