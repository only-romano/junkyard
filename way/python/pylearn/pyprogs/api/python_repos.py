#! The Python repository API
import requests
import pygal
from pygal.style import LightColorizedStyle as Lcs, LightenStyle as Ls

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
req = requests.get(url)   # Using requests to make the call
print("Status code:", req.status_code)
# A status code of 200 indicates a successful response.

# Simple calls like this should return a complete set of results, so
# it’s pretty safe to ignore the value associated with
# 'incomplete_results'.  But when you’re making more complex API calls,
# your program should check this value.

# Store API response in a variable.
response_dict = req.json()

# Process results.
print("Total repositories:", response_dict['total_count'])

# Explore information about the repositories.
repo_dicts = response_dict['items']

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url'],
    }
    plot_dicts.append(plot_dict)

# Make visualization.
my_style = Ls('#333366', base_style=Lcs)
my_style.title_font_size = 24
my_style.label_font_size = 14
my_style.major_label_font_size = 18

# Refining Pygal Charts - manual config.
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos2.svg')
my_style = Ls('#333366', base_style=Lcs)
my_style.title_font_size = 24
my_style.label_font_size = 14
my_style.major_label_font_size = 18

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')
