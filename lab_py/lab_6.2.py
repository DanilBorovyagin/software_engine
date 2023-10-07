from pprint import *

dic = {"first": "easy"}


def dict(**kwargs):
    dic.update(**kwargs)


dict(имя="Данил", возраст=21, цвет_глаз="зелёные")
dict(x1=2, x3=44, y1=22, y2="лол")
pprint(dic)