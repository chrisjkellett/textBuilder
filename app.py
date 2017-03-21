from flask import (Flask,
                   render_template,
                   request,
                   flash,
                   Markup,
                   url_for,
                   redirect,
                   session)
from forms import LoginForm, RegisterForm
from models import User, db
import hashlib


app = Flask(__name__)
app.secret_key = 'secret'
app.debug = True


@app.route('/', methods=['GET', 'POST'])
def index():
    login_form = LoginForm(request.form)
    reg_form = RegisterForm(request.form)

    if request.method == 'POST' and reg_form.validate():
        email = login_form.email.data
        password = hashlib.md5(str(login_form.password.data).encode('utf-8')).hexdigest()
        make_username = email.split('@')
        username_stripped = make_username[0]
        username_check = User.query.filter_by(username=username_stripped).count()
        if username_check == 0:
            username = username_stripped
        else:
            username = username_stripped + str(username_check+ 1)
        my_new_user = User(email, password, username)
        db.session.add(my_new_user)
        try:
            db.session.commit()
            message = Markup(f'User <strong>{username}</strong> created. Please confirm registration by email.')
            flash(message, 'success')
        except:
            db.session.rollback()
            flash('An error has occured', 'danger')

    elif request.method == 'POST' and login_form.validate():
        email = login_form.email.data
        password = hashlib.md5(str(login_form.password.data).encode('utf-8')).hexdigest()
        my_user = User.query.filter_by(email=email, password=password).first()
        if my_user:
            logged_in_message = Markup(f'You are logged in as <b>{my_user.username}</b>.')
            flash(logged_in_message, 'success')
            session['user'] = my_user.id
            username = my_user.username
            db.session.commit()
            return redirect(url_for('logged_in', username=username))
        else:
            flash('Not a registered user', 'danger')

    else:
        errors = login_form.errors.items()
        for field, messages in errors:
            for message in messages:
                flash(message, 'danger')

    return render_template('items/index.html', form=login_form, regform=reg_form)


@app.route('/<username>', methods=['GET', 'POST'])
def logged_in(username):
    return render_template('items/index-logged.html')


@app.route('/logout')
def log_out():
    session.clear()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()