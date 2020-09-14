from flask import Flask, session
from functools import wraps

app = Flask(__name__)
app.secret_key = 'YouWillNeverGuessMySecretKey'

def check_log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return func(*args, **kwargs)
        return 'You must log in to see this page'
    return wrapper

@app.route('/')
def hello() -> str:
    return 'Hello from the simple web app'

@app.route('/page<num>')
@check_log
def page(num) -> str:
    return f'This is page {num}'

@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in'

@app.route('/logout')
def do_logout() -> str:
    if 'logged_in' in session:
        session.pop('logged_in')
    return 'You are now logged out'

@app.route('/status')
def check_status() -> str:
    if 'logged_in' in session:
        return 'You are currently logged in'
    return 'You are NOT logged in'


if __name__ == '__main__':
    app.run(debug=True)
