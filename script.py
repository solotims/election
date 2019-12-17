#!/usr/bin/python3

import numpy 
import pandas 
import matplotlib.pyplot 

def parcer(src):
    table = pandas.read_html(src, encoding='CP1251')
    header = table[6].drop(12).T
    header = header.iloc[1]
    header[0] = 'Number of UIK'
    data = table[7].drop(12).T
    data.columns = header
    data.reset_index()
    return data

def numeric(inp):
    inp.iloc[:, 0]=[int(i.split()[1][1:]) for i in inp.iloc[:, 0]]
    for i in range(1, 12):
        inp.iloc[:, i] = pandas.to_numeric(inp.iloc[:, i])
    for i in range(12, 15):
        name = []
        percent = []
        for j in inp.iloc[:, i]:
            j = j.split()
            name.append(int(j[0]))
            percent.append(float(j[1][:-2]))
        inp.iloc[:, i] = name
        inp['percent for '+str(inp.columns.values[i])] = percent
    return inp

def answ_plot(x, y, label, n):
    matplotlib.pyplot.subplot(1, 3, n)
    x = numpy.array(x).reshape(-1, 1)
    y = numpy.array(y).reshape(-1, 1)
    matplotlib.pyplot.scatter(x, y, linewidth = 1)
    matplotlib.pyplot.title('Votes for ' + label)
    matplotlib.pyplot.xlabel('Turnout')
    matplotlib.pyplot.ylabel('Votes')


source = 'http://www.st-petersburg.vybory.izbirkom.ru/region/region/st-petersburg?action=show&tvd=27820001217417&vrn=27820001217413&region=78&global=&sub_region=78&prver=0&pronetvd=null&vibid=27820001217430&type=222'
data = parcer(source)
data = numeric(data)

answ_plot(data.iloc[:, 1], data.iloc[:, 12], 'Amosov', 1)
answ_plot(data.iloc[:, 1], data.iloc[:, 13], 'Beglov', 2)
answ_plot(data.iloc[:, 1], data.iloc[:, 14], 'Tikhonova', 3)
matplotlib.pyplot.show()



