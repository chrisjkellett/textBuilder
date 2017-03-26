from flask import (Flask,
                   render_template,
                   request,
                   flash,
                   Markup,
                   url_for,
                   redirect,
                   session)
from flask_mail import Mail, Message
from forms import LoginForm, RegisterForm
from models import User, db
import hashlib
import configparser

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('.env')

app.debug = config['DEFAULT']['DEBUG']
app.secret_key = config['DEFAULT']['SECRET_KEY']

app.config['MAIL_SERVER'] = config['MAIL']['MAIL_SERVER']
app.config['MAIL_PORT'] = config['MAIL']['MAIL_PORT']
app.config['MAIL_USE_SSL'] = config['MAIL']['MAIL_USE_SSL']
app.config['MAIL_USERNAME'] = config['MAIL']['MAIL_USERNAME']
app.config['MAIL_PASSWORD'] = config['MAIL']['MAIL_PASSWORD']
app.config['MAIL_DEBUG'] = False
mail = Mail(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    login_form = LoginForm(request.form)
    reg_form = RegisterForm(request.form)
    if request.method == 'POST' and reg_form.register.data:
        if reg_form.validate():
            email = login_form.email.data
            password = hashlib.md5(str(login_form.password.data).encode('utf-8')).hexdigest()
            make_username = email.split('@')
            username_stripped = make_username[0]
            username_check = User.query.filter(User.email.startswith(username_stripped)).count()
            if username_check == 0:
                username = username_stripped
            else:
                username = username_stripped + str(username_check + 1)
            my_new_user = User(email, password, username)
            db.session.add(my_new_user)
            try:
                db.session.commit()
                message = Markup(f'User <strong>{username}</strong> now requires email confirmation.')
                flash(message, 'success')
                msg = Message("Activate your account",
                              sender=('TextBuilder', 'no-reply@textbuilder.com'),
                              recipients=[email]
                              )
                link = 'http://' + config['DEFAULT']['HOST'] + url_for('confirm', token=my_new_user.token)
                msg.body = render_template('emails/confirm.txt', link=link)
                msg.html = render_template('emails/confirm.html', link=link)
                mail.send(msg)
            except:
                db.session.rollback()
                flash('An error has occured', 'danger')
            return redirect(url_for('index'))
        else:
            errors = reg_form.errors.items()
            for field, messages in errors:
                for message in messages:
                    flash(message, 'danger')
    elif request.method == 'POST' and login_form.login.data:
        if login_form.validate():
            email = login_form.email.data
            password = hashlib.md5(str(login_form.password.data).encode('utf-8')).hexdigest()
            my_user = User.query.filter_by(email=email, password=password).first()
            if my_user and login_form.validate() and my_user.active:
                logged_in_message = Markup(f'You are logged in as <b>{my_user.username}</b>.')
                flash(logged_in_message, 'success')
                session['user'] = my_user.id
                username = my_user.username
                db.session.commit()
                return redirect(url_for('logged_in', username=username))
            elif my_user and login_form.validate():
                confirm_message = Markup(f'User <b>{my_user.username}</b> requires confirmation.')
                flash(confirm_message, 'success')
            else:
                flash_message = Markup('<strong>Email</strong> or <strong>password</strong> incorrect.')
                flash(flash_message, 'danger')
            return redirect(url_for('index'))
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


@app.route("/confirm/<token>")
def confirm(token):
    my_user = User.query.filter_by(token=token).first()
    my_user.active = True
    try:
        db.session.commit()
        message = Markup(f'User <strong>{my_user.username}</strong> is confirmed')
        flash(message, 'success')
    except:
        db.session.rollback()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()