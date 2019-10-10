from re import sub

class DataScrapper:
    def __init__(self, sep='\t', reg_rules=[], own_rules=[], replace_dict={}):
        self.data = []
        self.separator = sep
        self.rules_reg = reg_rules
        self.rules_own = own_rules
        self.replace_dict = replace_dict

    def __call__(self, filename=None):
        if filename:
            return self.get_data(filename)
        else:
            return self.data

    def get_data(filename):
        with open(filename, 'r') as file:
            for line in file.readline():
                formated_data = __format_dataline(line)
                self.data.append(formated_data)
        return self.data

    def _format_dataline(self, line):
        legal_line = self.__replace_regex(line)
        raw_data = legal_line.split(self.separator)
        processed_data = self.__process_data(raw_data)
        formated_data = self.__format_data(processed_data)
        return formated_data

    def __replace_regex(self, line):
        for rule in self.reg_rules:
            re.sub(rule[0], rule[1], self.line)
        return line
        
    def __process_data(self, raw_data):
        # test length in-out lists
        for rule in self.own_rules:
            processed_data = rule(raw_data)
        return processed_data

    def __format_data(self, formated_data):
        for key in self.replace_dict:
            if key in formated_data:
                index = formated_data.index(key)
                formated_data[index] = self.replace_dict[key]
        return formated_data

        #if data_line[0]:
         #   month_name, year = data_line[0].split(' ')
          #  data_line[0] = year
           # month_num = __replace_month(month_name)
            #data_line.insert(1, month_num)

        #re.sub('%|\'', '', self.line)
        #re.sub(',', '.', self.line)


    def __replace_month(self, month_name):
        months = ['Янв.', 'Февр.', 'Март', 'Апр.', 'Май', 'Июнь', 'Июль',
            'Авг.', 'Сент.', 'Окт.', 'Нояб.', 'Дек.']
