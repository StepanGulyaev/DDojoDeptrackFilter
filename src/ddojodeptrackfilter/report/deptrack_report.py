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

        funcs_joined = "\n\t" + "\n\t".join(vulnerable_funcs.functions)
        packages_joined = "\n\t" + "\n\t".join(f"{pkg.package}:{pkg.version}" if pkg.version is not None else pkg.package 
                            for pkg in vulnerable_packages.packages)
        self.report = f"""
-------------------------------------------------------------------
Title: {title}

Url: {url}

Vulnerable functions: {funcs_joined}

Vulnearble packages: {packages_joined}


Description:

{description}

-------------------------------------------------------------------
"""