from jinja2 import Environment, PackageLoader, select_autoescape
from pydantic import BaseModel
from typing import List

class HTMLReportGenerator:
    def __init__(
        self,
        reports: List[BaseModel],
        package_name: str = "reports",
        templates_dir: str = "templates"
    ):

        self.env = Environment(
            loader=PackageLoader(package_name, templates_dir),
            autoescape=select_autoescape(enabled_extensions=("html", "xml"))
        )
        self.reports = reports

    def _generate_deptrack(self) -> str:
        template = self.env.get_template("deptrack_report.html")
        context = {
            "reports": [r.as_dict() for r in self.reports]
        }
        return template.render(context)

    def write(self, path: str):
        html = self._generate_deptrack()
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
