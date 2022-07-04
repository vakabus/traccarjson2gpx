from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Json
from pydantic.dataclasses import dataclass
from jinja2 import Template

class Point(BaseModel):
    id: int
    attributes: Any
    deviceId: int
    type: Any
    protocol: str
    serverTime: str
    deviceTime: str
    fixTime: str
    outdated: bool
    valid: bool
    latitude: float
    longitude: float
    altitude: float
    speed: float
    course: float
    address: Optional[str]
    accuracy: float
    network: Any

class Trace(BaseModel):
    __root__: List[Point]


def main():
    with open("input.json", "r") as f:
        data: Trace = Trace.parse_raw(f.read())
    
    with open('template.gpx.j2') as f:
        template = Template(f.read())
    
    with open("output.gpx", "w") as f:
        f.write(template.render(pts=data.__root__))


if __name__ == "__main__":
    main()



