from bottle import route, run, static_file

@route('/')
def home():
    return static_file('try_bottle_index.html', root='.')
    #return "<h2>It isn't fancy, but it's my home page</h2>"

@route('/echo/<thing>')
def echo(thing):
    return f"Say hello to my little friend: {thing}!"


if __name__ == '__main__':
    run(host='localhost', port=9999)
