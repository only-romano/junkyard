from flask import Flask, render_template

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def home():
    return app.send_static_file("try_flask_index.html")

@app.route('/echo/<thing>')
def echo(thing):
    return render_template('flask2.html', thing=thing)

@app.route('/hoho/<thing>/<place>')
def hoho(**kwargs):
    return render_template('flask3.html', **kwargs)

if __name__ == '__main__':
    app.run(debug=True)
