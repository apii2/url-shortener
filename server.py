from flask import Flask, redirect
from db import get_connection

app = Flask(__name__)

@app.route('/<code>')
def redirect_short_url(code):
  short_url = f"https://localhost:5000/{code}"
  print('code',code)

  conn = get_connection()
  with conn.cursor() as cursor:
    cursor.execute("SELECT original_url FROM Links WHERE short_url=%s", (short_url,))
    data = cursor.fetchone()

    if data:
      return redirect(data['original_url'])
    return "Short URL not found", 404


if __name__ == '__main__':
  app.run(port=5000, debug=True)
