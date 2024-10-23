import _config as c
from flask import Flask, render_template, redirect, render_template_string, Blueprint
from modules.brorn import Brorn



app = Blueprint("_test_",__name__,template_folder="pages")
_app = Brorn(app,"view\\_test_\\pages\\")


@app.route("/")
def index():
	_app.include_function("sample",sample_in_func)
	return _app.render_template("index.html", content="test", contents="test 2")
	# return _app.render_template("app.brn", content="test", contents="test 2")


@app.route("/openAiTest")
def openAiTest():
	return {"test":"openAiTest"}
	from openai import OpenAI
	client = OpenAI()

	completion = client.chat.completions.create(
		model="gpt-4o-mini",
		messages=[
			{"role": "system", "content": "You are a helpful assistant."},
			{
				"role": "user",
				"content": "Write a haiku about recursion in programming."
			}
		]
	)

	print(completion.choices[0].message)
	return "openAiTest"
	# return _app.render_template("app.brn", content="test", contents="test 2")


def sample_in_func():
	return {"sample":"args"}