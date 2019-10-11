from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics import renderPDF
from data_scraper import DataScraper

"""
    Data section
"""
# Parser Rules
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

# Data scraper
scraper = DataScraper('\t', regex, replaces, rules)
scraper('src/data.txt')
data = scraper.data

"""
    RUB to USD PDF
"""
drawing = Drawing(900, 800)

def get_graph(i):
    return [int(float(row[i])) for row in data]

def get_zip(t_graph, v_graph):
    return list(zip(t_graph, v_graph))

time_graph = [2000 + int(row[0]) + int(row[1])/12 for row in data]
graphs = []
for i in range(2, 7):
    graphs.append(get_zip(time_graph, get_graph(i)))

# Plot
lp = LinePlot()
lp.x, lp.y = 50, 50
lp.height = 600
lp.width = 800
lp.data = []
lp_colors = [colors.gray, colors.blue, colors.green, colors.red, colors.black]

for i in range(5):
    lp.data.append(graphs[i]);
    lp.lines[i].strokeColor = lp_colors[i]

drawing.add(lp)
drawing.add(String(75, 600, 'Month\' start', fontSize=20, fillColor=colors.gray))
drawing.add(String(75, 550, 'End of month', fontSize=20, fillColor=colors.blue))
drawing.add(String(75, 500, 'Maximum', fontSize=20, fillColor=colors.green))
drawing.add(String(75, 450, 'Minimum', fontSize=20, fillColor=colors.red))
drawing.add(String(75, 200, 'Month\'s Change', fontSize=20, fillColor=colors.black))
renderPDF.drawToFile(drawing, 'src/rub2usd.pdf', 'RUB to USD plot')
