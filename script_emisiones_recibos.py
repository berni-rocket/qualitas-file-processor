from src.lib.layout.local import LocalLayoutMapper
from src.lib.parser.local import LocalParser

df = LocalParser(mapper=LocalLayoutMapper(layout_file='./layouts/PV.txt'), data_file='./files/pv/PV.txt').get_subparser().expand(indexes=[0,1,2],indexes_to_expand=[35])

print(df)