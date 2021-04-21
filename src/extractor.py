from dataclasses import dataclass
from typing import List

import pendulum
import requests

__all__ = ["ExchangeRate", "extract_exchange_rates"]


@dataclass
class ExchangeRate:
    date: str
    currency_code: str
    rate: float


def extract_exchange_rates(period: pendulum.period) -> List[ExchangeRate]:
    for date in period:
        date = date.strftime("%d.%m.%Y")
        print(date)
