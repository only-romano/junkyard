# Map of americas
import pygal_maps_world.maps as pg

wm = pg.World()
wm.title = 'North, Central and South America, Russia, Kazakhstan'

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe',
                         'py', 'sr', 'uy', 've'])
wm.add('Russia', {'ru': 144300000})
wm.add('Kazakhstan', ['kz'])

wm.render_to_file('Russia_pop.svg')
