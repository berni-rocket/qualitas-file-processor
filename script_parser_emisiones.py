from src.emisiones.parser import EmisionesParser
from src.emisiones.layout import EmisionesLayoutMapper

mapper = EmisionesLayoutMapper(layout_file='./layouts/PV.txt')
parser = EmisionesParser(mapper=mapper, data_file='./files/uv6190400001789715aa.txt')
parser.parse().to_csv('./data/emisiones.csv',index=False)
