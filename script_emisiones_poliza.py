from src.emisiones.parser import EmisionesParser
from src.lib.layout import LayoutMapper

mapper = LayoutMapper(layout_file='./layouts/PV.txt')

parser = EmisionesParser(mapper=mapper, data_file='./files/uv6190400001789715aa.txt')

parser.parse()
