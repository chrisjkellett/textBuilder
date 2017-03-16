from flask import Flask, render_template
from forms import User_form
app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    form = User_form()
    return render_template('items/index.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)