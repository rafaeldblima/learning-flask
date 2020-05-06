from flask import render_template, url_for, make_response, abort

from . import main


@main.route("/")
def index():
    return render_template('index.html')


@main.route("/user/<name>")
def user(name):
    return render_template('user.html', name=name)


@main.route("/abort/<user_id>")
def abort_test(user_id):
    if int(user_id) == 1:
        abort(404)
    return "<h1>User XXX</h1>"


@main.route("/response")
def response():
    resp = make_response()
    resp.set_cookie("cookie", "monster")
    resp.set_data('<h1>Test response</h1>' + url_for("user", name="Rafael", _external=True))
    return resp
