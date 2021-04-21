from typing import Iterator, Tuple

import pendulum
import requests
from bs4 import BeautifulSoup, element

from .entities.exchange_rate import ExchangeRate

__all__ = ["ExchangeRate", "extract_exchange_rates"]

BASE_URL = "http://cbr.ru/scripts/XML_daily.asp?date_req={date}"


def _get_exchange_rates_markup(base_url: str, date: str) -> bytes:
    response = requests.get(url=base_url.format(date=date))
    response.raise_for_status()
    return response.content


def _get_exchange_rates_soup(markup: bytes) -> BeautifulSoup:
    return BeautifulSoup(markup=markup, features="xml")


def _parse_exchange_rate_tag(tag: element.Tag) -> Tuple[str, float]:
    char_code = tag.find("CharCode").string
    value = tag.find("Value").string.replace(",", ".")
    return char_code, float(value)


def extract_exchange_rates(period: pendulum.period) -> Iterator[ExchangeRate]:
    for date in period:
        date = date.strftime("%d/%m/%Y")
        markup = _get_exchange_rates_markup(base_url=BASE_URL, date=date)
        soup = _get_exchange_rates_soup(markup=markup)
        for tag in soup.find_all(name="Valute"):
            currency_code, rate = _parse_exchange_rate_tag(tag=tag)
            yield ExchangeRate(date=date, currency_code=currency_code, rate=rate)
