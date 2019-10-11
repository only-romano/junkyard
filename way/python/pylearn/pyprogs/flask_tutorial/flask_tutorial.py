from flask import Flask

app = Flask(__name__)


@app.route('/hello')
# app.route(rule [represents URL binding with the function],
#           options [list of parameters to be forwarded to the
#           underlying Rule object])
def hello_world():
    return 'Hello World!'
# == app.add_url_rule(‘/’, ‘hello’, hello_world)


if __name__ == '__main__':
    app.run(debug=True)
# app.run( host [Hostname to listen on. Defaults to 127.0.0.1
#          Set to ‘0.0.0.0’ to have server available externally],
#          port [Defaults to 5000], debug [Defaults to false],
#          options [To be forwarded to underlying Werkzeug server]) )
