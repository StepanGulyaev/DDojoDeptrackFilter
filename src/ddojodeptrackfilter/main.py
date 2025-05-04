from ddojodeptrackfilter.cli.cli import parse_DDojo_args
from ddojodeptrackfilter.defect_dojo_client.defect_dojo_client import DefectDojoClient

def execute_main():
    args = parse_DDojo_args()
    client = DefectDojoClient(args.base_url,args.username,args.password,args.verify_ssl,args.timeout)
    print(client.base_url)

if __name__ == '__main__':
    execute_main()
