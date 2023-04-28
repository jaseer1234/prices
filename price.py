from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)
@app.route('/price', methods=['GET'])
def get_price():
    url = 'https://www.metal.com/Lithium-ion-Battery/202303240001'  # Replace with the URL of the website you want to scrape
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    price = soup.find('span', {'class': 'price'}).text  # Replace with the CSS selector for the price element on the website
    return jsonify({'price': price})
if __name__ == '__main__':
    app.run()