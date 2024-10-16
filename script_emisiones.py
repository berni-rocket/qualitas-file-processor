from src.emisiones.parser import EmisionesParser
from src.emisiones.layout import EmisionesLayoutMapper

data_file = './files/PV.txt'

mapper = EmisionesLayoutMapper(layout_file='./layouts/PV.txt')
parser = EmisionesParser(mapper=mapper, data_file=data_file)
df = parser.parse()

indices_to_chose = [0,1,2,3,4,5,6,7,8,9,10,11,12,14,15,22,24,25,26,29,30,31,32,52,56,57,62,64,66,67,68,69,78,79,80,95,97,98,99,100,101,102,103,104,105,106,107,122,147,163,164,165,166,179,190,197,290,293,294,385]
columns_to_chose = [df.columns[i] for i in indices_to_chose]
df = df[columns_to_chose]

df.to_csv('./data/emisiones.csv', index=False)