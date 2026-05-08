from dotenv import load_dotenv
import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR/ ".env")

BASE_URL = os.getenv("BASE_URL", "http://54.255.195.111:5171")
USERNAME = os.getenv("API_USERNAME")
PASSWORD = os.getenv("API_PASSWORD")