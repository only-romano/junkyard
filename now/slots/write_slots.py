"""
Module to work with pickle
Loads file, if exist
If file not exist or period is over loads up a new slots instance with default value
"""
import pickle

FILE_NAME = "slots.pickle"

def load():
    try:
        with open(FILE_NAME, 'rb') as file:
            slots = pickle.load(file)
    except FileNotFoundError:
        from activity_slots import slots
    if slots.day == 15:
        from activity_slots import slots
    return slots

def write(slots):
    with open(FILE_NAME, 'wb') as file:
        pickle.dump(slots, file)
