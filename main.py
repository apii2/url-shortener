from db import get_connection
from dotenv import load_dotenv
import re, random, string, os

load_dotenv()

URL_PATTERN = re.compile(r'^https://(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(?:/[^\s]*)?$')

def generateRandomString():
  return ''.join(random.choices((string.ascii_letters+string.digits),k=6))

def generateUniqueRandomString(cursor):
  while True:
    code = generateRandomString()
    shortUrl = f'{os.getenv('BASE_URL')}/{code}'
    cursor.execute('SELECT * FROM Links WHERE short_url=%s',(shortUrl,))
    if not cursor.fetchone():
      return shortUrl

def main():
  while True:
    originalUrl = input('Enter the url u want to shorten:  ')

    try:
      if not originalUrl:
        raise ValueError('Please enter url')

      if 'localhost' in originalUrl or '127.0.0.1' in originalUrl:                                                                     
        raise ValueError('Local URLs are not allowed')

      if not URL_PATTERN.match(originalUrl):
        raise ValueError('Invalid URL format or Domain. Must start with "https://"')

      conn = get_connection()
      with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM Links WHERE original_url=%s",(originalUrl,))
        urlData = cursor.fetchone()
        if urlData:
          print('This url has already been shorten.')
          getUrl = input('Do u want the short url for this url?Y/N:  ')
          if getUrl.lower()=='y':
            print(urlData['short_url'])
          return
        
        shortUrl = generateUniqueRandomString(cursor)

        cursor.execute("INSERT INTO Links (original_url, short_url) VALUES (%s, %s)", (originalUrl, shortUrl))
        conn.commit()

        print(f"Your url has been shortened successfully!\nThe short url is: {shortUrl}")

        # cursor.execute("SELECT * FROM Links")
        # print('ID\tOriginal Url\t\t\t\t\t\t\t\t\t\tShort Url')
        # for url in cursor.fetchall():
        #   print(f"{url['id']}\t{url['original_url']}\t{url['short_url']}")
      conn.close()

      break
    except Exception as e:
      print('Error:',e)

if __name__ == '__main__':
  main()
