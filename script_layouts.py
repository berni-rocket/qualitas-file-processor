
from src.lib.layout.local import LocalLayoutMapper

LocalLayoutMapper(layout_file='./layouts/PV.txt').get_layout().get_df().to_csv('./data/layouts/pv_layout.csv',index=False)
LocalLayoutMapper(layout_file='./layouts/DI.txt').get_layout().get_df().to_csv('./data/layouts/di_layout.csv',index=False)
LocalLayoutMapper(layout_file='./layouts/REC-PAGO.txt').get_layout().get_df().to_csv('./data/layouts/rec_pago_layout.csv',index=False)
LocalLayoutMapper(layout_file='./layouts/COB.txt').get_layout().get_df().to_csv('./data/layouts/cob_layout.csv',index=False)