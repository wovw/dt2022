from urllib import response
from flask import Flask
from flask import render_template
from flask import request
import os
from load_image import loadImgFunction

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
	file = request.files['file']
	file.save(os.path.join('IO', file.filename))

	loadImgFunction()

if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0")