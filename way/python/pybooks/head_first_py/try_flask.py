from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'

@app.route('/cat/')
def cat() -> str:
    return '<h3>Best cat in the world</h3><hr><a href="#">Kitty</a>'

app.run()
