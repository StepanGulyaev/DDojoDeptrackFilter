from ddojodeptrackfilter.cli import parse_DDojo_args
from ddojodeptrackfilter.client import DefectDojoClient
from ddojodeptrackfilter.models.api.test import Test
from ddojodeptrackfilter.models.api.finding import Finding

import ddojodeptrackfilter.ddojo_test_handlers
from ddojodeptrackfilter.ddojo_test_handlers.base import DDojoTestHandlerRegistry

import json

def execute_main():
    args = parse_DDojo_args()
    client = DefectDojoClient(args.base_url,args.username,args.password,args.verify_ssl,args.timeout)
    raw_tests = client.get_tests(args.engagement_id)
    tests = [Test.model_validate(test) for test in raw_tests["results"]]
    test_handler = DDojoTestHandlerRegistry.get_for(tests[0])
    if test_handler:
        raw_findings = test_handler.handle(tests[0],client)
        findings = [Finding.model_validate(finding) for finding in raw_findings["results"]]
        #print(json.dumps(findings,indent=2))

if __name__ == '__main__':
    execute_main()
