"""
Main module for console version of picker
"""
from write_slots import load, write
from slots_tools import weight_and_things
from day_file import create_day_file

# load slots
slots = load()

# iterate over slots
result = [slot for slot in slots]

# append special values
special_values = weight_and_things(slots)
special_values.update({"days_at_all": slots.days_at_all})
result.append(special_values)

# create day-file and re-write slots
create_day_file(result)
write(slots)
