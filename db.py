import pymysql.cursors
from dotenv import load_dotenv
import os

load_dotenv()

def get_connection():
  return pymysql.connect(
    host=os.getenv('DB_HOST','localhost'),
    user=os.getenv('DB_USER','root'),
    password=os.getenv('DB_PASS',''),
    database=os.getenv('DB_NAME','url_shortener'),
    cursorclass=pymysql.cursors.DictCursor
  )