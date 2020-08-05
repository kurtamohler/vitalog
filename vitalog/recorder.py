import datetime

import blood_pressure

timestamp_format = '%Y-%m-%d-%H:%M:%S.%f'

def record(args):
    timestamp = datetime.datetime.today().strftime(timestamp_format)
    if args.blood_pressure is not None:
        blood_pressure.record(timestamp, args.blood_pressure)
