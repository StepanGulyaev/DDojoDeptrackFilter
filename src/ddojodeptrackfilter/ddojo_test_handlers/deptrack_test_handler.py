from typing import List, Any
import json

from ddojodeptrackfilter.models.api.test import Test
from ddojodeptrackfilter.models.api.finding import Finding

from ddojodeptrackfilter.ddojo_test_handlers.base import DDojoTestHandler, ddojo_test_register_handler
from ddojodeptrackfilter.client import DefectDojoClient
from ddojodeptrackfilter.settings import settings
from ddojodeptrackfilter.ai.ai_client import OpenRouterAIClient
from ddojodeptrackfilter.models.app.deptrack_description_extract import FunctionExtractModel
from ddojodeptrackfilter.models.app.deptrack_description_extract import PackageExtractModel

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

        # TODO: I don't know if it's the best design for ai client. Maybe there is a better one. Need to think of it.
       
        ai_client_extract_functions = OpenRouterAIClient(
                system_prompt = settings.deptrack_description_extract_func_sys_prompt,
                human_prompt = settings.deptrack_description_extract_func_human_prompt,
                response_format = FunctionExtractModel,
                model_name = settings.openrouter_model_name,
                headers = {"HTTP-Referer" : settings.http_referer, "X-Title" : settings.app_name},
                temperature = 0,
                api_base = settings.openrouter_api_base_url,
                api_key = settings.openrouter_api_key
            )

        ai_client_extract_packages = OpenRouterAIClient(
                system_prompt = settings.deptrack_description_extract_package_sys_prompt,
                human_prompt = settings.deptrack_description_extract_package_human_prompt,
                response_format = PackageExtractModel,
                model_name = settings.openrouter_model_name,
                headers = {"HTTP-Referer" : settings.http_referer, "X-Title" : settings.app_name},
                temperature = 0,
                api_base = settings.openrouter_api_base_url,
                api_key = settings.openrouter_api_key
            )

        for finding in findings:
            if finding.id == 21:
                extracted_functions = ai_client_extract_functions.get_functions_deptrack_description(finding.description)
                extracted_packages = ai_client_extract_packages.get_packages_deptrack_description(finding.file_path,finding.component_name,finding.description)
                print(finding.id,extracted_functions.functions,extracted_packages.packages)
 
                        

