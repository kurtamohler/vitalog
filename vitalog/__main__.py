import arguments
import recorder

def main():
    args = arguments.parse_args()

    recorder.record(args)


if __name__ == '__main__':
    main()