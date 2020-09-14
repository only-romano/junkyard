from threading import Thread
from flask import Flask, render_template, request, escape, session, copy_current_request_context
from db_tools import UseDB, ConnectionError, CredentialsError, SQLError
from checker import check_log_in
from vsearch import search4letters
from my_config import dbconfig, secret_key


app = Flask(__name__)
app.config['dbconfig'] = dbconfig
app.secret_key = secret_key


@app.route('/')
def index() -> str:
    return ("""
    <div align="center" style="width: 500px; margin: 10% 25%; color: #004f00">
        <h2>Welcome to search4letters on the Web!</h2>
        <form method="POST">
            <div style="border: 1px solid black; margin: 25px; padding: 10px">
                Use this form to submit a search request:
                <p>Phrase:\t<input type="text"/></p>
                <p>Letters:\t<input type="text"/></p>
                When you're ready click this button:
            </div>
            <button style="font-size: 1.33em; padding: 10px">Do it!</button>
            <a href='/entry'>New Search Engine</a>
        </form>
    </div>
    """)


@app.route('/search', methods=['POST'])
def do_search() -> 'html':

    @copy_current_request_context
    def log_request(req: 'flask_request') -> None:
        with UseDB(app.config['dbconfig']) as db:
            data = db.operate_request(req=req)
            db.insert(data)
        # with open('vsearch.log', 'a') as log:
        #    print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')

    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    try:
        t = Thread(target=log_request, args=(request))
        t.start()
    except Exception as err:
        print(f"****** Logging failed with this error: {err}")
    return render_template('results.html',
                            the_phrase=phrase,
                            the_letters=letters,
                            the_title=title,
                            the_results=results,)


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                            the_title='Welcome to search4letters on the web')


@app.route('/viewlog')
@check_log_in
def view_the_log() -> 'html':
    _SQL = """SELECT phrase, letters, ip, browser_string, results FROM log"""
    try:
        with UseDB(app.config['dbconfig']) as db:
            contents = db.query(_SQL, show=1)
        titles = ('Phrase', 'Letters', 'Remote Address', 'Browser', 'Result')
        return render_template('viewlog.html',
                                the_title='View Log',
                                the_row_titles=titles,
                                the_data=contents,)
    except ConnectionError as err:
        print(f'Is your database switched on? Error: {err}')
    except CredentialsError as err:
        print(f'User-id/Password issues. Error: {err}')
    except SQLError as err:
        print(f'Is your query correct? Error: {err}')
    except Exception as err:
        print(f'Something went wrong: {err}')
    return "<h3>Error</h3>"


if __name__ == '__main__':
    app.run(debug=True)
