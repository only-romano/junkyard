"""Example of logging application"""
from datetime import datetime

class Logger:
    """ Logger class to create logs in files. Usage:
    create logger:
        log = Logger(path_to_file)
    write logs to file:
        log(*args)

    set logs time on/off globaly, for all logs (default=True):
        log.date(False)
    set logs time on/off for only log:
        log(*args, nodate=True)

    set separator globaly (default=" "):
        log.sep("_")
    set separator for only log:
        log(*args, sep="_")

    set new log file:
        log.file(path_to_file)
    """
    def __init__(self, file):
        self._file = file
        self._date = True
        self._sep = " "

    def __call__(self, *args, **kwargs):
        to_write = []
        date = ''

        is_nodate = "nodate" in kwargs
        nodate = is_nodate and kwargs["nodate"]
        if is_nodate and nodate == False or not is_nodate and self._date:
            date = str(datetime.now())[:-7] + "\t"
        for el in args:
            to_write.append(str(el))

        sep = "sep" in kwargs and str(kwargs["sep"]) or self._sep
        str_to_write = date + sep.join(to_write) + "\n"
        with open(self._file, 'a') as file:
            file.write(str_to_write)

    def date(self, flag):
        self._date = flag

    def sep(self, sep):
        self._sep = sep

    def file(self, file):
        self._file = file


# import
__all__ = ["Logger"]
