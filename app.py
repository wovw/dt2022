from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

#loads the file passed in
def loadFile():
    pass

if __name__ == '__main__':
	app.run(debug=True)
	# test()