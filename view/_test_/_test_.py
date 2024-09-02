import _config as c
from flask import Flask, render_template, redirect, render_template_string, Blueprint
from modules.brorn import Brorn



app = Blueprint("_test_",__name__,template_folder="pages")
_app = Brorn(app)


@app.route("/")
def index():
	_app.include_function("sample",sample_in_func)
	return _app.render_template("index.html", content="test", contents="test 2")
	# return _app.render_template("app.brn", content="test", contents="test 2")


def sample_in_func():
	return {"sample":"args"}