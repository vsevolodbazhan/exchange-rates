import pendulum

from src.extractor import extract_exchange_rates
from src.writer import write_exchange_rates


if __name__ == "__main__":
    exchange_rates = extract_exchange_rates(
        period=pendulum.period(
            start=pendulum.datetime(year=2019, month=12, day=1),
            end=pendulum.datetime(year=2020, month=8, day=1),
        )
    )
    write_exchange_rates(file_name="exchange_rates.csv", exchange_rates=exchange_rates)
