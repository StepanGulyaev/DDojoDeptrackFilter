from ddojodeptrackfilter.cli.cli import parse_DDojo_args
from ddojodeptrackfilter.defect_dojo_client.defect_dojo_client import DefectDojoClient
from ddojodeptrackfilter.models.test import TestModel
import json

def execute_main():
    args = parse_DDojo_args()
    client = DefectDojoClient(args.base_url,args.username,args.password,args.verify_ssl,args.timeout)
#    find_data = client.get_findings(args.engagement_id)
    raw_tests = client.get_tests(args.engagement_id)
    tests = [TestModel.model_validate(test) for test in raw_tests["results"]]
    print(tests[0])
#    print(json.dumps(tests,indent=2))
#    print(json.dumps(find_data,indent=2))

if __name__ == '__main__':
    execute_main()
