# URL Shortener (Python + Flask)

This project allows you to shorten URLs and get local short links like:

http://localhost:5000/abc123

Anyone who clones this repo can run it locally without buying a domain.

---

## 🚀 How to Run

### 1. Install dependencies

pip install -r requirements.txt

### 2. Start the redirect server

python server.py

(This listens on `http://localhost:5000`)

### 3. Run the URL shortener CLI

python main.py

You will get short URLs like:

http://localhost:5000/Xkd93j

### 4. Open the short URL in browser

It will redirect to the original long URL.

---

## 📌 Notes

- Uses your local database (configure in `db.py`)
- No domain needed
- Fully local
