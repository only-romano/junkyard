"""Data Scraper class"""
import sys
from re import sub
from urllib.request import urlopen

class DataScraper:
    """
    Parse through text file and get legitiment data output with custom rules.

    Usage.

    scraper = DataScraper()
    scraper(filename:str)   parse file for data
    scraper()               get stored data
    """
    def __init__(self, sep='-', regex_rules={}, replace_dict={}, proc_rules=[]):
        self._sep = sep             # User's separator
        self._reg = regex_rules     # User's Regex rules
        self._dict = replace_dict   # User's Replacce rules
        self._rules = proc_rules    # User's Processing rules

        self._silence = False       # No exceptions mod
        self.data = []              # Stored data

    def __call__(self, filename=None):
        # default call with no parameters returns stored data, if there is a
        # given parameter - scraper trying to parse file from path in argument
        if filename:
            return self.from_file(filename)
        return self.data

    def from_file(self, filename):
        """
        Collecting data from file, parsing it from string to data list

        param filename: str     path to file
        returns: list           stored data
        """
        try:
            with open(filename, 'r') as file:
                for line in file.readlines():
                    formated_data = self.__format_line(line)
                    self.data.append(formated_data)
        except FileNotFoundError:
            err_msg = "File %s not found" % str(filename)
            if self._silence: return print(err_msg)
            raise FileNotFoundError(err_msg)
        finally:
            return self.data

    def from_url(self, url):
        """
        Collecting data from url, parsing it from string to data list

        param url: string       url
        returns: list           stored data
        """
        try:
            with urlopen(url) as file:
                for line in file.readlines():
                    formated_data = self.__format_line(line.decode('utf8'))
                    self.data.append(formated_data)
        except Exception:
            pass

    def format(self):
        pass

    def __format_line(self, line):
        # parsing and format manager
        # param line: str
        # returns: list
        valid_line = self.__sub_regex(line)
        raw_data = valid_line.split(self.separator)     # str to list
        processed_data = self.__process_data(raw_data)
        formated_data = self.__format_data(processed_data)
        return formated_data

    def __sub_regex(self, line):
        # substitute regex dict in line
        # param: line: str
        # returns: str
        for key in self._reg:
            line = sub(key, self._reg[key], line)
        return line
        
    def __process_data(self, raw_data):
        # processes given decorators over raw data
        # param: raw_data: list
        # returns: list
        for rule in self._rules:
            processed_data = rule(raw_data)
        return processed_data

    def __format_data(self, formated_data):
        # replaces list values
        # param: formated_data: list
        # returns: list
        for key in self._dict:
            if key in formated_data:
                index = formated_data.index(key)
                formated_data[index] = self._dict[key]
        return formated_data

    # separator property
    def _set_sep(self, u_sep):
        """Separator must be a string, you can use whatever you liked so far"""
        self._sep = str(u_sep)
    def _get_sep(self):
        """separator: str"""
        return self._sep
    separator = property(_get_sep, _set_sep)

    # regex property
    def _set_reg(self, u_regex):
        """User Regex Rules"""
        if not isinstance(u_regex, dict):
            err_msg = 'Regex rules must be a dictionary.'
            if self._silence: return print(err_msg)
            raise TypeError(err_msg)
        self._reg = u_regex
    def _get_reg(self):
        """regex: dict"""
        return self._reg
    regex = property(_get_reg, _set_reg)

    # rules property
    def _set_rules(self, u_rules):
        """User Processing Rules"""
        if not isinstance(u_rules, (list, tuple)):
            err_msg = 'Processing rules must be a list of callables.'
            if self._silence: return print(err_msg)
            raise TypeError(err_msg)
        for rule in u_rules:
            if not callable(rule):
                err_msg = 'Processing rule must be a callable.'
                if self._silence: return print(err_msg)
                raise TypeError(err_msg)
        self._rules = u_rules
    def _get_rules(self):
        """rules: list of callables"""
        return self._rules
    rules = property(_get_rules, _set_rules)

    # replaces property
    def _set_dict(self, u_dict):
        """User Replacing Rules"""
        if not isinstance(u_dict, dict):
            err_msg = 'Replacing rules must be a dictionary.'
            if self._silence: return print(err_msg)
            raise TypeError(err_msg)
        self._dict = u_dict
    def _get_dict(self):
        """replaces: dict"""
        return self._dict
    replaces = property(_get_dict, _set_dict)

    # silent property
    def _set_silence(self, u_silence):
        """Silent mode converts all raised errors to console printed log"""
        self._silence = bool(u_silence)
    def _get_silence(self):
        """silent: bool"""
        return self._silence
    silent = property(_get_silence, _set_silence)


def main():
    regex  = { "%\n|'": "", "(S*)\\.": "\\1", "(d*),(d*)": "\\1.\\2" }

    replaces = { 'Янв': '1', 'Февр': '2', 'Март': '3', 'Апр': '4',
        'Май': '5', 'Июнь': '6', 'Июль': '7', 'Авг': '8',
        'Сент': '9', 'Окт': '10', 'Нояб': '11', 'Дек': '12'}

    def parseMY(data):
        if data[0]:
            month, year = data[0].split(' ')
            data[0] = year.strip()
            data.insert(1, month.strip())
        return data


    rules = [ parseMY ]

    scraper = DataScraper('\t', regex, replaces, rules)
    scraper.from_url("https://raw.githubusercontent.com/only-romano/junkyar"\
            + "d/master/python/pylearn/pyprogs/pretty_data_pdf/src/data.txt")
    print(scraper.data)


if __name__ == '__main__':
    main()
