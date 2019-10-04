#! Json practice
import json
import pygal_maps_world.maps as pm
from countries import get_country_code
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS

# Load the data into a list.
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# Buold a dictionary of population data.
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

# Group the countries into 3 population levels.
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 500000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# See how many countries are in each level.
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

# Styling
wm_style = RS('#336699', base_style=LCS)
wm = pm.World(style=wm_style)

wm.title = 'World Population in 2010, by Country'
wm.add('Up to 10 mil', cc_pops_1)
wm.add('10 to 500 mil', cc_pops_2)
wm.add('500+ mil', cc_pops_3)

wm.render_to_file('world_population2.svg')
