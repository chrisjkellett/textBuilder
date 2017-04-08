from flask import (Flask,
                   render_template,
                   request,
                   flash,
                   Markup,
                   url_for,
                   redirect,
                   session)
from flask_mail import Mail, Message
from forms import LoginForm, RegisterForm, GetTextForm
from models import User, Savetext, db
from functools import wraps
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


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            session.clear()
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/', methods=['GET', 'POST'])
def index():
    login_form = LoginForm(request.form)
    reg_form = RegisterForm(request.form)
    if request.method == 'POST' and reg_form.register.data:
        if reg_form.validate():
            email = login_form.email.data
            my_new_user = User.query.filter_by(email=email).first()
            password = hashlib.md5(str(login_form.password.data).encode('utf-8')).hexdigest()
            make_username = email.split('@')
            username_stripped = make_username[0]
            username_check = User.query.filter(User.email.startswith(username_stripped)).count()
            if username_check == 0:
                username = username_stripped
            else:
                username = username_stripped + str(username_check + 1)
            if not my_new_user:
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
                    msg.body = render_template('emails/confirm.txt', link=link, username=username)
                    msg.html = render_template('emails/confirm.html', link=link, username=username)
                    mail.send(msg)
                except:
                    db.session.rollback()
                    flash('An error has occured', 'danger')
            else:
                message = Markup(f'User at <strong>{email}</strong> already exists')
                flash(message, 'danger')
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
@login_required
def logged_in(username):
    text_form = GetTextForm(request.form)
    user_texts = Savetext.query.filter_by(id_user=session['user']).all()
    if request.method == 'POST':
        if text_form.validate():
            title = text_form.title.data
            user_text = text_form.user_text.data
            my_text = Savetext(title, user_text, session['user'])
            db.session.add(my_text)
            try:
                db.session.commit()
                message = Markup(f'Saved <strong>{title}</strong>.')
                flash(message, 'success')
            except:
                db.session.rollback()
                flash('Error: Not saved', 'danger')
            return redirect(url_for('logged_in', username=username))
        else:
            errors = text_form.errors.items()
            for field, messages in errors:
                for message in messages:
                    flash(message, 'danger')
        return redirect(url_for('logged_in', username=username))
    return render_template('items/index-logged.html', user_texts=user_texts, text_form=text_form, username=username)


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
        flash('Error: Not confirmed', 'danger')
    return redirect(url_for('index'))


@app.route('/<int:id>', methods=['GET', 'POST'])
def save_text(id):
    my_text = Savetext.query.filter_by(id=id).first()
    return render_template('items/builder.html', text=my_text)


@app.route('/delete/<int:id>')
def delete_text(id):
    text_delete = Savetext.query.filter_by(id=id).first()
    my_user = User.query.filter_by(id=text_delete.id_user).first()
    db.session.delete(text_delete)
    try:
        db.session.commit()
        message = Markup(f'Deleted <strong>{text_delete.title}</strong>.')
        flash(message, 'success')
    except:
        db.session.rollback()
        flash('Error: Not confirmed', 'danger')
    return redirect(url_for('logged_in', username=my_user.username  ))


if __name__ == "__main__":
    app.run()