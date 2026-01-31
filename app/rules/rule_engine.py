from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path
from typing import Any, Dict

from jinja2 import Environment, FileSystemLoader

from .scoring import calculate_risk


def load_incident_json(path: str) -> Dict[str, Any]:
    p = Path(path)
    return json.loads(p.read_text(encoding="utf-8"))


def render_report(incident: Dict[str, Any], template_path: str = "app/templates/report.md.j2") -> str:
    env = Environment(loader=FileSystemLoader(searchpath="."), autoescape=False)
    template = env.get_template(template_path)

    result = calculate_risk(incident)
    payload = {
        "incident": incident,
        "result": asdict(result),
    }
    return template.render(**payload)


def save_text(path: str, content: str) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
