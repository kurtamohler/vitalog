import blood_pressure

def record(args):
    if args.blood_pressure is not None:
        blood_pressure.record(args.blood_pressure)
