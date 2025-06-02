import requests
from bs4 import BeautifulSoup
import sqlite3

# Create database
def create_db():
    conn = sqlite3.connect('quotes.db')
    c = conn.cursor()
    c.execute('''
      CREATE TABLE IF NOT EXISTS quotes (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        quote TEXT NOT NULL, 
        author TEXT NOT NULL
      )
    ''')
    conn.commit()
    conn.close()

# Insert quote into database
def insert_quote(quote, author):
    conn = sqlite3.connect('quotes.db')
    c = conn.cursor()
    c.execute('INSERT INTO quotes (quote, author) VALUES (?, ?)', (quote, author))
    conn.commit()
    conn.close()


def scrape_and_store():
    url="https://quotes.toscrape.com/"
    response = requests.get(url)
    # check for request errors
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    quotes = []

    # Each quote is inside a <div class="quote">
    quote_divs = soup.find_all('div', class_='quote')

    for div in quote_divs:
        # The text of the quote is in a <span class="text">
        text = div.find('span', class_='text').get_text()

        # The author is in a small tag with class "author"
        author = div.find('small', class_='author').get_text()

        insert_quote(text, author)
        print(f"Stored quote: {text[:50]} ... by {author}")

    #     quotes.append({
    #         'quote': text, 
    #         'author': author
    #     })

    # return quotes

if __name__ == "__main__":
    create_db()
    scrape_and_store()