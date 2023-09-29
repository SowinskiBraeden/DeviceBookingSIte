from flask import Blueprint

main_blueprint: Blueprint = Blueprint('main', __name__)

from src.main import routes
