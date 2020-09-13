import pickle
from athlete import AthleteList

def put_to_store(files_list):
    all_athletes = {}
    for each_file in files_list:
        ath = AthleteList(each_file)
        all_athletes[ath.name] = ath
    try:
        with open('athletes.pickle', 'wb') as athf:
            pickle.dump(all_athletes, athf)
    except IOError as ioerr:
        print(f'File error (put and store): {ioerr}')
    return all_athletes

def get_from_store():
    all_athletes = {}
    try:
        with open('athletes.pickle', 'rb') as athf:
            all_athletes = pickle.load(athf)
    except IOError as ioerr:
        print(f'File error (get from store): {ioerr}')
    return all_athletes

#print(get_coach_data('sarah'))
