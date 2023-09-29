import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()

class Config:
  SECRET: str = os.environ.get("SECRET")
  API_URL: str = os.environ.get("API_URL")
