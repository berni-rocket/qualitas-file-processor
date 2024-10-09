
from src.emisiones.layout import EmisionesLayoutMapper

mapper = EmisionesLayoutMapper(layout_file='./layouts/PV.txt')
df = mapper.get_layout().get_df()
df.to_csv('./data/layout.csv',index=False)