from dataclasses import dataclass

@dataclass
class SimulationResp:
    mean: str
    median: str
    percentile: str
    qrng: []
    prng: []