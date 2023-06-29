import requests
from flask import Flask, request, send_from_directory

# Replace "YOUR_API_KEY_HERE" with your actual API key.

BASE_URL = "https://live-traffic-images.p.rapidapi.com/get_image"
headers = {
  "X-RapidAPI-Key": "2753249664msh09d8b6c98ffcadbp1c36f6jsn01363be38920",
  "X-RapidAPI-Host": "live-traffic-images.p.rapidapi.com"
}
app = Flask(__name__)


@app.route("/")
def index():
  return "Hello world!  Your web application is working!"


@app.route('/get_image', methods=['GET'])
def get_traffic_data():
  region = request.args.get('region')

  querystring = {"country": "us", "region": region, "key": "4616618--17"}
  response = requests.get(BASE_URL, headers=headers, params=querystring)
  return response.json()


@app.route('/.well-known/ai-plugin.json')
def serve_ai_plugin():
  return send_from_directory('.',
                             'ai-plugin.json',
                             mimetype='application/json')


@app.route('/openapi.yaml')
def serve_openapi_yaml():
  return send_from_directory('.', 'openapi.yaml', mimetype='text/yaml')


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81)
