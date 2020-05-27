import os
import pytest

from scripts import data_processor, data_aggregator


@pytest.fixture(scope="module")
def city_list_location():
    return 'tests/resources/cities/'


@pytest.fixture(scope="module")
def process_data(city_list_location):
    files = os.listdir(city_list_location)

    def _specify_type(filename):
        for f in files:
            if filename == f:
                if filename.endswith('.json'):
                    data = data_processor.json_reader(city_list_location + f)
                elif filename.endswith('.csv'):
                    data = data_processor.csv_reader(city_list_location + f)
                return data

    yield _specify_type


@pytest.mark.parametrize("country,stat,expected", [
    ('Andorra', 'Mean', 1641.42),
    ('Andorra', 'Median', 1538.02),
    ('Argentina', 'Median', 125.0),
    ])
def test_altitude_stat_per_country(process_data, country, stat, expected):
    data = process_data(file_name_or_type="clean_map.csv")
    stat_result = data_aggregator.altitude_stat_per_country(data, country, stat)

    assert stat_result == {'Country': country, stat: expected}
