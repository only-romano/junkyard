"""
Module to work with pickle file.
"""
import pickle
import print_patterns as PP
from datetime import date
try:
    from my_values import PATH_TO_FOLDER
except ImportError:
    try:
        from my_values_placeholder import PATH_TO_FOLDER
    except ImportError:
        PATH_TO_FOLDER = "day_files/"


FILE_NAME = "slots.pickle"


def load():
    # Loads file, if exist.
    # If doesn't or period is over - loads up a new slots instance with default values.
    try:
        with open(PATH_TO_FOLDER + FILE_NAME, 'rb') as file:
            slots = pickle.load(file)
    except FileNotFoundError:
        from activity_slots import slots
    day_fix = 15 if date.today().toordinal() > 737394 else 9    # temporal fix
    if slots.day == day_fix:
        days_at_all, smoke = slots.days_at_all, slots.smoke
        weight, muscle, fat, water = slots.weight, slots.muscle, slots.fat, slots.water
        good_things, new_things = slots.good_things, slots.new_things
        diet_day, diet, diet_done = slots.diet_day, slots.diet, slots.diet_done
        from activity_slots import slots
        slots.days_at_all, slots.smoke = days_at_all, smoke
        slots.weight, slots.muscle, slots.fat, slots.water = weight, muscle, fat, water
        slots.good_things, slots.new_things = good_things, new_things
        slots.diet_day, slots.diet, slots.diet_done = diet_day, diet, diet_done
    return slots


def write(slots):
    slots.day += 1
    slots.days_at_all += 1
    slots.diet_day += 1
    if slots.diet_day == 30:
        slots.diet_day = 0
    with open(PATH_TO_FOLDER + FILE_NAME, 'wb') as file:
        pickle.dump(slots, file)
