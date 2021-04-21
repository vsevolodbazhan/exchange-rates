import csv
from typing import Iterable

from .entities.exchange_rate import ExchangeRate


def write_exchange_rates(file_name: str, exchange_rates: Iterable[ExchangeRate]):
    with open(file_name, "w") as file:
        writer = csv.writer(file)
        writer.writerow(("date", "currency_code", "rate"))
        for exchange_rate in exchange_rates:
            writer.writerow(
                (
                    exchange_rate.date,
                    exchange_rate.currency_code,
                    exchange_rate.rate,
                )
            )
