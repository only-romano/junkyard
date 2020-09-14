import mysql.connector
from vsearch import search4letters
from my_config import dbconfig


class ConnectionError(Exception):
    pass

class CredentialsError(Exception):
    pass

class SQLError(Exception):
    pass


class UseDB:

    def __init__(self, config:dict) -> None:
        self.configuration = config
        self.connection = None
        self.cursor = None

    def __enter__(self) -> 'DB':
        try:
            self.connection = mysql.connector.connect(**self.configuration)
            self.cursor = self.connection.cursor()
            return self
        except mysql.connector.errors.InterfaceError as err:
            raise ConnectionError(err)
        except mysql.connector.errors.ProgrammingError as err:
            raise CredentialsError(err)

    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
        if exc_type is mysql.connector.errors.ProgrammingError:
            raise SQLError(exc_value)
        elif exc_type:
            raise exc_type(exc_value)

    def query(self, sql:str, params:set=(), commit:bool=False, show:int=0) -> set:
        self.cursor.execute(sql, params)
        result = ()
        if show:
            result = self.cursor.fetchall()
            if show >= 2:
                print(result if show != 2 else [row for row in result])
        if commit:
            self.connection.commit()
        return result

    def insert(self, params, commit=False) -> None:
        _SQL = """INSERT INTO log
                  (phrase, letters, ip, browser_string, results)
                  VALUES
                  (%s, %s, %s, %s, %s)"""
        self.query(_SQL, params, commit)

    @staticmethod
    def operate_request(phrase:str="", letters:str="", req:'Flask request'=None) -> set:
        address, browser = '127.0.0.1', 'Firefox'
        if req:
            phrase = req.form['phrase']
            letters = req.form['letters']
            address = req.remote_addr
            browser = req.user_agent.browser
        result = str(search4letters(phrase, letters))
        return (phrase, letters, address, browser, result)


def try_db() -> None:
    with UseDB(dbconfig) as db:
        db.query("""show tables""", show=3)
        db.query("""describe log""", show=2)
        db.insert(db.operate_request('hitch-hiker', 'aeiou'))
        db.insert(db.operate_request('hitch-hiker', 'xyz'), commit=True)
        db.query("""SELECT * FROM log""", show=3)
        db.query("""SELECT count(*) FROM log""", show=3)
        db.query("""SELECT count(letters) AS 'count', letters
            FROM log
            GROUP BY letters
            ORDER BY count DESC
            LIMIT 1;""", show=3)
        db.query("""SELECT DISTINCT ip FROM log""", show=3)
        db.query("""SELECT browser_string, count(browser_string) AS 'count'
            FROM log
            GROUP BY browser_string
            ORDER BY count DESC
            LIMIT 1;""", show=3)



if __name__ == '__main__':
    try_db()
