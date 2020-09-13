from flask import Flask, render_template, request, escape
from vsearch import search4letters

app = Flask(__name__)

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
        </form>
    </div>
    """)

@app.route('/search', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    log_request(request, results)
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
def view_the_log() -> 'html':
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote Address', 'User Agent', 'Result')
    return render_template('viewlog.html',
                            the_title='View Log',
                            the_row_titles=titles,
                            the_data=contents,)

def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')

if __name__ == '__main__':
    app.run(debug=True)
