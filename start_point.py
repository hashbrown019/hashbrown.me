from flask import Flask, render_template, redirect, render_template_string, Blueprint
app = Flask(__name__)


from view._test_ import _test_
app.register_blueprint(_test_.app);


