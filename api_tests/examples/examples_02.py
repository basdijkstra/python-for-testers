import pytest
import requests
import csv

test_data_zip = [
    ("us", "90210", "Beverly Hills"),
    ("us", "12345", "Schenectady"),
    ("ca", "B2A", "North Sydney South Central")
]


@pytest.mark.parametrize("country_code, zip_code, expected_place", test_data_zip)
def test_get_location_data_check_place_name(country_code, zip_code, expected_place):
    response = requests.get(f'http://api.zippopotam.us/{country_code}/{zip_code}')
    response_body = response.json()
    assert response_body["places"][0]["place name"] == expected_place


def write_data_to_csv():
    with open("api_tests/examples/testdata.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for row in test_data_zip:
            writer.writerow(row)


def read_data_from_csv():
    test_data_zip_from_csv = []
    with open("api_tests/examples/testdata.csv", newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        for row in data:
            test_data_zip_from_csv.append(row)
    return test_data_zip_from_csv


@pytest.mark.parametrize("country_code, zip_code, expected_place", read_data_from_csv())
def test_get_location_data_check_place_name_with_data_from_csv(country_code, zip_code, expected_place):
    response = requests.get(f'http://api.zippopotam.us/{country_code}/{zip_code}')
    response_body = response.json()
    assert response_body["places"][0]["place name"] == expected_place
