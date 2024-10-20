from src.lib.layout.local import LocalLayoutMapper
from src.lib.parser.local import LocalParser

LocalParser(mapper=LocalLayoutMapper(layout_file='./layouts/PV.txt'), data_file='./files/pv/PV.txt').get_subparser().all().to_csv('./data/pv/pv.csv', index=False)
LocalParser(mapper=LocalLayoutMapper(layout_file='./layouts/DI.txt'), data_file='./files/di/DI.txt').get_subparser().all().to_csv('./data/di/di.csv', index=False)
LocalParser(mapper=LocalLayoutMapper(layout_file='./layouts/COB.txt'), data_file='./files/cob/COB.txt').get_subparser().all().to_csv('./data/cob/cob.csv', index=False)
LocalParser(mapper=LocalLayoutMapper(layout_file='./layouts/REC-PAGO.txt'), data_file='./files/rec_pago/REC-PAGO.txt').get_subparser().all().to_csv('./data/rec_pago/rec_pago.csv', index=False)

