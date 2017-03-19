from flask import (Flask,
                   render_template,
                   request,
                   flash,
                   Markup,
                   url_for,
                   redirect)
from forms import Login_form, Register_form
from models import User, db
import hashlib


app = Flask(__name__)
app.secret_key = 'secret'
app.debug = True


@app.route('/', methods=['GET', 'POST'])
def index():
    login_form = Login_form(request.form)
    regform = Register_form(request.form)
    if request.method == 'POST' and login_form.validate():
        email = login_form.email.data
        password = hashlib.md5(str(login_form.password.data).encode('utf-8')).hexdigest()
        my_user = User.query.filter_by(email=email, password=password).first()
        if my_user:
            logged_in_message = Markup(f'You are logged in as <b>{my_user.username}</b>.')
            flash(logged_in_message, 'success')
            my_user.session = True
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

    return render_template('items/index.html', form=login_form, regform=regform)


@app.route('/<username>', methods=['GET', 'POST'])
def logged_in(username):
    return render_template('items/index-logged.html')


@app.route('/logout')
def log_out():
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()