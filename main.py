import requests
from flask import Flask, redirect, url_for, render_template

url = 'https://www.scorebat.com/video-api/v1/'

response = requests.get(url)
if response.status_code == 200:
    payload = response.json()
    if payload:
        for title in payload:
            name = title['title']
            #print(name)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("codigo.html", content=payload)

if __name__ == "__main__":
    app.run()

