from flask import Flask, render_template, redirect, render_template_string
from modules.brorn import Brorn
from flask_minify import Minify

app = Flask(__name__)

_app = Brorn(__name__)

@app.route("/")
def index():
	_app.include_function("sample",sample_in_func)
	# return _app.render_template("index.html", content="test", contents="test 2")
	return _app.render_template("_test_/app.brn", content="test", contents="test 2")


def sample_in_func():
	return {"sample":"args"}

if __name__ == '__main__':
	app.run(debug=True)