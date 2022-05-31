from flask import Flask
from flask import render_template, redirect, url_for
from flask import request
from block import *

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        login_input = request.form['login_input']
        password_input = request.form['password_input']
        password_check_input = request.form['password_check_input']

        write_block(login=login_input, password=password_input, password_check=password_check_input)
        return redirect(url_for('index'))

    return render_template('index.html')


@app.route('/checking', methods=['GET'])
def check():
    results = check_integrity()
    return render_template('index.html', results=results)


if __name__ == '__main__':
    app.run(debug=True)
