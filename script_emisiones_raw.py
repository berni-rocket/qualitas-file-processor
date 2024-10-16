from src.emisiones.parser import EmisionesParser
from src.emisiones.layout import EmisionesLayoutMapper

data_file = './files/PV.txt'

mapper = EmisionesLayoutMapper(layout_file='./layouts/PV.txt')
parser = EmisionesParser(mapper=mapper, data_file=data_file)
df = parser.parse()

df.to_csv('./data/emisiones_raw.csv', index=False)