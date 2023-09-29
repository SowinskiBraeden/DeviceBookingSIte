from src.main import main_blueprint
from flask import render_template

@main_blueprint.get("/")
def index():
  return render_template('index.html')
