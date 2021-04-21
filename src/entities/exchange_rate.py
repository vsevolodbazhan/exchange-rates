from dataclasses import dataclass


@dataclass
class ExchangeRate:
    date: str
    currency_code: str
    rate: float
