from dataclasses import dataclass

@dataclass
class VarResp:
    var: str
    pvar: str
    absoluteLoss: str
    percentile: str
    elements: []