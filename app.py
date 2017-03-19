from flask import (Flask,
                   render_template,
                   request,
                   flash,
                   redirect,
                   url_for)
from forms import Login_form, Register_form
from models import User
import hashlib


app = Flask(__name__)
app.secret_key = 'secret'
app.debug = True


@app.route('/', methods=['GET', 'POST'])
def index():
    loginform = Login_form(request.form)
    regform = Register_form(request.form)
    if request.method == 'POST' and loginform.validate():
        email = loginform.email.data
        password = loginform.password.data
        my_user = User.query.filter_by(email=email, password=password).first()
        if my_user:
            return 'user verified'
        else:
            flash('El usuario o contraseña no existe', 'danger')
    else:
        errores = loginform.errors.items()
        for campo, mensajes in errores:
            for mensaje in mensajes:
                flash(mensaje, 'danger')

    return render_template('items/index.html', form=loginform, regform=regform)



if __name__ == "__main__":
    app.run()