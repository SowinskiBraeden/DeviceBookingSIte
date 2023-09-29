from flask import Blueprint

errors_blueprint = Blueprint('errors', __name__)

from src.errors import handlers
