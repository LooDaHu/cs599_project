import random

from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import HeatMap
from file_reader import file_reader

counties = ['BEL', 'BRA', 'CHI', 'CUB', 'EGY', 'FRA', 'IND', 'ISR', 'USA', 'USS', 'YUG', 'ZAI']


def heatmap_base() -> HeatMap:
    # value = [[i, j, random.randint(0, 50)] for i in range(24) for j in range(7)]
    # for i in range(len(value)):
    #     for j in range(len(value[i])):
    #         print(value[i][j])
    value = file_reader('data_set.txt')
    # print(value)
    c = (
        HeatMap()
        .add_xaxis(counties)
        .add_yaxis("dissimilarity", counties, value)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="HeatMap-基本示例"),
            visualmap_opts=opts.VisualMapOpts(),
        )
    )
    return c


def make_figure1():
    heatmap_base().render(path='figure1.html')


make_figure1()
