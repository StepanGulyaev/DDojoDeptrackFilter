from typing import List, Any

from ddojodeptrackfilter.models.api.test import Test
from ddojodeptrackfilter.models.api.finding import Finding

from ddojodeptrackfilter.ddojo_test_handlers.base import DDojoTestHandler, ddojo_test_register_handler
from ddojodeptrackfilter.client import DefectDojoClient
from ddojodeptrackfilter.settings import settings

@ddojo_test_register_handler
class DeptrackTestHandler(DDojoTestHandler):

    @classmethod
    def supports(cls, test: Test) -> bool:
        name = (test.test_type_name or "").lower()
        for alias in settings.deptrack_aliases:
            if alias in name:
                return True
        return False

    def handle(self, test: Test, client: DefectDojoClient): # Later specify what it returns, probably findings
        raw_findings = client.get_findings(test.id)
        findings = [Finding.model_validate(finding) for finding in raw_findings["results"]] 
        for finding in findings:
            print('----------------------------------')
            print(finding.description)
        

