from datetime import datetime

from flask import render_template, session, redirect, url_for, make_response, abort, flash, current_app

from . import main
from .forms import NameForm
from .. import db
from ..email import send_email
from ..models import User


@main.route("/", methods=['GET', 'POST'])
def index():
    # from flask import request
    # user_agent = request.headers.get('User-Agent')
    # return '<p>Your browser is {}</p>'.format(user_agent)
    form = NameForm()
    if form.validate_on_submit():
        db_user = User.query.filter_by(username=form.name.data).first()
        if db_user is None:
            flash('User created!')
            db_user = User(username=form.name.data)
            db.session.add(db_user)
            db.session.commit()
            session['known'] = False
            if current_app.config['FLASK_ADMIN']:
                send_email(current_app.config['FLASK_ADMIN'], 'New User', 'mail/new_user', user=db_user)
        else:
            flash('Welcome Back!')
            session['known'] = True
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get("name"),
                           current_time=datetime.utcnow(), known=session.get('known', False))


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
