from ddojodeptrackfilter.cli.cli import parse_DDojo_args


def execute_main():
    args = parse_DDojo_args()
    print(args)

if __name__ == '__main__':
    execute_main()
