from typing import List, Dict, Optional, Type
from ddojodeptrackfilter.models.app.deptrack_description_extract import FunctionExtractModel
from ddojodeptrackfilter.models.app.deptrack_description_extract import PackageExtractModel

class DeptrackFindingReport:
    def __init__( 
        self,
        title : str,
        url: str,
        vulnerable_funcs: Type[FunctionExtractModel],
        vulnerable_packages: Type[PackageExtractModel],
        description : str
    ):
        self.title = title
        self.url = url
        self.vulnerable_funcs = vulnerable_funcs
        self.vulnerable_packages = vulnerable_packages
        self.description = description

    
    def gen_text_report(self) -> str:
        funcs_joined = "\n\t" + "\n\t".join(self.vulnerable_funcs.functions)
        #print(self.vulnerable_packages.packages)
        packages_joined = "\n\t" + "\n\t".join(f"{pkg.package}:{pkg.version}" if pkg.version is not None else pkg.package 
                            for pkg in self.vulnerable_packages.packages)
        report = f"""
-------------------------------------------------------------------
Title: {self.title}

Url: {self.url}

Vulnerable functions: {funcs_joined}

Vulnearble packages: {packages_joined}


Description:

{self.description}

-------------------------------------------------------------------
"""
        return report 

    def as_dict(self) -> dict:
        #funcs_joined = "".join(self.vulnerable_funcs.functions)
        #packages_joined = "".join(f"{pkg.package}:{pkg.version}" if pkg.version is not None else pkg.package 
                           # for pkg in self.vulnerable_packages.packages)
        
        return {
            "title": self.title,
            "url": self.url,
            "functions": self.vulnerable_funcs.functions,
            "packages": self.vulnerable_packages.packages,
            "description": self.description,
        }
