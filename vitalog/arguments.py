import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p',
        '--blood-pressure',
        type=float,
        nargs=2,
        metavar=('S', 'D'),
        help=(
            'Record a blood pressure measurement, in mmHg. '
            'S is sistolic (higher), D is diastolic (lower).'))
    args = parser.parse_args()

    return args
