from re import sub

class Athlete:
    def __init__(self, name):
        self.filename = 'coach/' + name + '.txt'
        self.name = None
        self.birth = None
        self.results = None
        self.best_results = None
        self.load_file()

    def top3(self):
        name = self.name
        if name:
            best = sorted({i for i in self.results})[:3]
            print("%s's fastest times are: %s, %s, %s" % (name, *best))
        else:
            print("There is no such Athlete.")

    def load_file(self):
        try:
            with open(self.filename, 'r') as file:
                info = file.read().split(',')
                self.update_values(info)
        except Exception:
            pass

    def update_values(self, info):
        self.name = info[0]
        self.birth = info[1]
        self.results = [sub('-|\.', ':', i).strip() for i in info[2:]]

    def add_time(self, *times):
        for time in times:
            self.results.append(sub('-|\.',':',time))



[Athlete(name).top3() for name in ('james','julie','mikey','sarah', 'bummy')]
jamie = Athlete('james')
jamie.add_time('1:21')
jamie.top3()
jamie.add_time('1:22', '2:15')
jamie.top3()



# DEPRECATED
def process_line(line):
    return create_dict(line.split(','))

def create_dict(arr):
    return { 'N': arr[0], 'B': arr[1], 'R': get_results(arr[2:]) }

def get_results(arr):
    return sorted({sub('-|\.', ':', i) for i in arr})[:3]

def load_file(file):
    # returns set of values 'm:ss' from propertly structured files
    try:
        with open(file, 'r') as file:
            return process_line(file.readline())
    except Exception as e:
        return e

def print_best_time(name):
    man = load_file('coach/' + name + '.txt')
    if isinstance(man, dict):
        print("%s's fastest times are: %s, %s, %s" %(man['N'], *man['R']))
    else:
        print(man)

# too ugly to be true
#[print_best_time(name) for name in ('james','julie','mikey','sarah', 'bummy')]
