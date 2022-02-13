from dataclasses import dataclass

@dataclass
class ForecastResp:
    profitTraditional: str
    profitPrng: str
    profitQrng: str
    qrng: []
    prng: []