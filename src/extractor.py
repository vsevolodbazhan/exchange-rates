from dataclasses import dataclass
from typing import List

import pendulum
import requests

__all__ = ["ExchangeRate", "extract_exchange_rates"]

BASE_URL = "http://cbr.ru/scripts/XML_daily.asp?date_req={date}"


@dataclass
class ExchangeRate:
    date: str
    currency_code: str
    rate: float


def _get_exchange_rates_markup(base_url: str, date: str) -> str:
    response = requests.get(url=base_url.format(date=date))
    response.raise_for_status()
    return response.text


def extract_exchange_rates(period: pendulum.period) -> List[ExchangeRate]:
    for date in period:
        date = date.strftime("%d/%m/%Y")
        markup = _get_exchange_rates_markup(base_url=BASE_URL, date=date)
        print(markup)
