from urllib import response
from flask import Flask
from flask import render_template
from flask import request, send_from_directory, jsonify
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

	return (jsonify(loadImgFunction()))

DOWNLOAD_DIRECTORY = "./IO"

@app.route('/get-file/<path:path>',methods = ['GET','POST'])
def get_files(path):
    try:
        return send_from_directory(DOWNLOAD_DIRECTORY, path, as_attachment=True)
    except FileNotFoundError:
        os.abort(404)

if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0")