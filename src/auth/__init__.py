from flask import Blueprint

authentication_blueprint: Blueprint = Blueprint('auth', __name__)

from src.auth import handlers